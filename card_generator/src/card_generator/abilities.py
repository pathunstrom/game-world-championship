from collections import defaultdict
from dataclasses import dataclass
from functools import partial

import card_generator.base as base


@dataclass(frozen=True)
class Scalar:
    name: str
    cost_schedule: tuple[base.CostStep, ...]
    max_value: int


@dataclass(frozen=True)
class AbilityConfiguration:
    name: str
    text_template: str
    base_cost: float | int
    scalars: tuple[Scalar] = tuple()


@dataclass(frozen=True)
class Ability:
    text: str
    cost: int


def generate(ability_configurations: tuple[AbilityConfiguration], modifier_configurations) -> dict[int, list[Ability]]:
    output: dict[int, list[Ability]] = defaultdict(list)
    for ability_configuration in ability_configurations:
        if ability_configuration.scalars:
            for cost, format_function in apply_scalars(ability_configuration.text_template.format, ability_configuration.scalars):
                ability = Ability(
                    text=format_function(),
                    cost=cost + ability_configuration.base_cost
                )
                output[ability.cost].append(ability)
        else:
            ability = Ability(
                text=ability_configuration.text_template,
                cost=ability_configuration.base_cost
            )
            output[ability.cost].append(ability)
    return output


def apply_scalars(text_format_function, scalars):
    scalar, *remaining_scalars = scalars
    if not remaining_scalars:
        for value in range(1, scalar.max_value + 1):
            cost = base.calculate_cost(scalar.cost_schedule, value)
            output_template_function = partial(text_format_function, **{scalar.name: value})
            yield cost, output_template_function
    else:
        for tallied_cost, format_function in apply_scalars(text_format_function, remaining_scalars):
            for value in range(1, scalar.max_value + 1):
                cost = tallied_cost + base.calculate_cost(scalar.cost_schedule, value)
                output_template_function = partial(format_function, **{scalar.name: value})
                yield cost, output_template_function
