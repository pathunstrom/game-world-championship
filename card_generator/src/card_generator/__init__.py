import csv
from dataclasses import dataclass, asdict
from enum import StrEnum, auto

import tomlkit


DEFAULT_GENERATOR_META = {"version": "0.1.0"}
DEFAULT_BUDGET = {
    "attack_base": 2,
    "budget_per_energy": 2,
    "defense_base": 1,
    "max_cost": 5,
    "max_defense": 5,
    "max_attack": 12,
}
DEFAULT_COSTS = {
    "attack_additional": 1,
    "attack_removed": -1,
    "defense_additional": 1,
    "defense_removed": -1,
}


class CardType(StrEnum):
    ATTACK = auto()
    TACTIC = auto()
    CHARACTER = auto()
    DRILL = auto()


class AbilityKeyword(StrEnum):
    ACTION = auto()
    ATTACK = auto()
    DEFENSE = auto()
    REACTION = auto()


@dataclass
class Budget:
    attack_base: float | int
    defense_base: float | int
    budget_per_energy: float | int
    max_cost: int
    max_defense: int
    max_attack: int


@dataclass
class Card:
    name: str
    cost: int
    target_budget: float | int
    calculated_budget: float | int
    attack: int
    defense: int
    card_type: CardType
    ability_text: str = ""
    ability_keyword: AbilityKeyword | None = None


@dataclass
class Costs:
    attack_additional: float | int
    attack_removed: float | int
    defense_additional: float | int
    defense_removed: float | int


@dataclass
class Generator:
    version: str


@dataclass
class Ability:
    types = list[CardType]
    test = str
    cost = int
    keyword = AbilityKeyword


def generate_default_configuration(file):
    default_config = {
        "generator": DEFAULT_GENERATOR_META,
        "budget": DEFAULT_BUDGET,
        "costs": DEFAULT_COSTS,
    }
    document = tomlkit.dumps(default_config)
    tomlkit.dump(default_config, file)


def generate_stat_variances(stat_budget, card_template: Card, costs, budget):
    maximum_attack_for_budget = (
        stat_budget // costs.attack_additional
    ) + budget.attack_base
    for attack in range(budget.attack_base, maximum_attack_for_budget + 1):
        if attack > budget.max_attack:
            continue
        spent_on_attack = (attack - budget.attack_base) * costs.attack_additional
        defense = (
            (stat_budget - spent_on_attack) // costs.defense_additional
        ) + budget.defense_base
        spent_on_defense = (defense - budget.defense_base) * costs.defense_additional
        if defense > budget.max_defense:
            continue
        card = Card(
            name=f"{card_template.name} A{attack}D{defense}",
            card_type=card_template.card_type,
            cost=card_template.cost,
            target_budget=card_template.target_budget,
            calculated_budget=card_template.calculated_budget
            + spent_on_attack
            + spent_on_defense,
            attack=attack,
            defense=defense,
        )
        yield card


def generate_vanilla_cards(base_card_budget, base_card_cost, costs, budget):
    yield from generate_stat_variances(
        base_card_budget,
        Card(
            name="Simple",
            card_type=CardType.ATTACK,
            cost=base_card_cost,
            target_budget=base_card_budget,
            calculated_budget=0,
            attack=0,
            defense=0,
        ),
        costs,
        budget,
    )


def generate_attacks_with_abilities(
    attack_abilities,
    attack_ability_modifiers,
    base_card_cost,
    base_card_budget,
    costs,
    budget,
):
    pass


def main(output_path, configuration_path):
    try:
        file = configuration_path.open("r")
    except FileNotFoundError:
        with configuration_path.open("w") as file:
            generate_default_configuration(file)
        file = configuration_path.open("r")
    configuration = tomlkit.load(file)
    generator = Generator(**configuration.get("generator", DEFAULT_GENERATOR_META))
    budget = Budget(**configuration.get("budget", DEFAULT_BUDGET))
    costs = Costs(**configuration.get("costs", DEFAULT_COSTS))
    cards = []
    for base_card_cost in range(budget.max_cost + 1):
        base_card_budget = budget.budget_per_energy * base_card_cost
        cards.extend(
            generate_vanilla_cards(base_card_budget, base_card_cost, costs, budget)
        )

    with output_path.open("w", newline="") as file:
        writer = csv.DictWriter(file, asdict(cards[0]).keys())
        writer.writeheader()
        for card in cards:
            writer.writerow(asdict(card))
