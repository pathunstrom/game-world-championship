import math
from dataclasses import dataclass
from functools import lru_cache
from typing import Iterator, Sequence


@dataclass(frozen=True)
class CostStep:
    """
    A cost step is a starting value, and a cost per point.

    All sequences of CostSteps should start at (0, x) where x is the basic
    value of the stat.
    The value field should strictly increase as your progress through the
    sequence.
    """

    value: int
    cost: int


@dataclass(frozen=True)
class Stat:
    """
    A Stat definition.

    Consists of a string name and a tuple of cost schedules.
    """

    name: str
    cost_schedule: tuple[CostStep]


@dataclass
class GeneratedStats:
    """
    Output of state generation.
    """

    values: dict[str, int]
    spent_budget: float | int


@lru_cache()
def generate_stat_distribution(
    stat_configuration: Sequence[Stat], remaining_budget: float | int
) -> Iterator[GeneratedStats]:
    for generated_stat in _generate_stat_splits(stat_configuration, remaining_budget):
        if sum(generated_stat.values.values()):
            yield generated_stat


def _generate_stat_splits(
    stat_configuration: tuple[Stat], remaining_budget: float | int
) -> Iterator[GeneratedStats]:
    stat, *remaining_stats = stat_configuration
    if not remaining_stats:
        stat_value = remaining_budget // stat.cost_schedule[0].cost
        stat_cost = stat.cost_schedule[0].cost * stat_value
        yield GeneratedStats(values={stat.name: stat_value}, spent_budget=stat_cost)
    else:
        for value in range(0, remaining_budget // stat.cost_schedule[0].cost + 1):
            modified_budget = math.floor(
                remaining_budget - (value * stat.cost_schedule[0].cost)
            )
            for generated_stat in _generate_stat_splits(
                tuple(remaining_stats), modified_budget
            ):
                stat_dict = generated_stat.values | {stat.name: value}
                spent = generated_stat.spent_budget + (
                    value * stat.cost_schedule[0].cost
                )
                yield GeneratedStats(stat_dict, spent)
