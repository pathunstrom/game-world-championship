import pytest

from card_generator import base


@pytest.mark.parametrize(
    "schedule, value, expected",
    [
        ((base.CostStep(0, 1), base.CostStep(2, 2), base.CostStep(4, 1)), 1, 1),
        ((base.CostStep(0, 1), base.CostStep(2, 2), base.CostStep(4, 1)), 2, 2),
        ((base.CostStep(0, 1), base.CostStep(2, 2), base.CostStep(4, 1)), 3, 4),
        ((base.CostStep(0, 1), base.CostStep(2, 2), base.CostStep(4, 1)), 4, 6),
        ((base.CostStep(0, 1), base.CostStep(2, 2), base.CostStep(4, 1)), 5, 7),
        ((base.CostStep(0, 1), base.CostStep(2, 2), base.CostStep(4, 1)), 6, 8),
        ((base.CostStep(0, 2),), 1, 2),
        ((base.CostStep(0, 2),), 4, 8),
    ]
)
def test_calculate_cost(schedule, value, expected):
    result = base.calculate_cost(schedule, value)
    assert result == expected
