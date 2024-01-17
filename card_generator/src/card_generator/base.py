from dataclasses import dataclass
from itertools import zip_longest
from math import inf
from typing import Sequence

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


def calculate_cost(cost_schedule: Sequence[CostStep], value):
    accumulator = 0
    current: CostStep
    next: CostStep | None
    for current, next in zip_longest(cost_schedule, cost_schedule[1:]):
        modified_value = value - current.value
        if modified_value < 0:
            break
        value_range = next.value - current.value if next else inf
        accumulator += min(value_range, modified_value) * current.cost
    return accumulator
