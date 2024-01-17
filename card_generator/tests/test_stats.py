import pytest

from card_generator import stats, base


stat_distribution_test_data = [
    pytest.param(  # 0 budget with no free points returns 0 dicts.
        (
            stats.Stat(name="attack", cost_schedule=(base.CostStep(0, 1),)),
            stats.Stat(name="defense", cost_schedule=(base.CostStep(0, 1),)),
        ),
        0,
        [],
        0,
        id="0 budget should result in 0 results.",
    ),
    pytest.param(  # 1 budget with equal costs and two stats should return 1, 0 and 0, 1
        (
            stats.Stat(name="attack", cost_schedule=(base.CostStep(0, 1),)),
            stats.Stat(name="defense", cost_schedule=(base.CostStep(0, 1),)),
        ),
        1,
        [(0, 1), (1, 0)],
        1,
        id="Two stats worth 1 each should result in two cards.",
    ),
    pytest.param(
        (
            stats.Stat(name="attack", cost_schedule=(base.CostStep(0, 1),)),
            stats.Stat(name="defense", cost_schedule=(base.CostStep(0, 1),)),
            stats.Stat(name="focus", cost_schedule=(base.CostStep(0, 1),)),
        ),
        2,
        [(0, 0, 2), (0, 1, 1), (0, 2, 0), (1, 0, 1), (1, 1, 0), (2, 0, 0)],
        2,
        id="Three stats should emit all six card variants.",
    ),
]


@pytest.mark.parametrize(
    "stat_configuration,remaining_budget,expected_values,expected_spend",
    stat_distribution_test_data,
)
def test_stat_distribution_generation(
    stat_configuration: tuple[stats.Stat], remaining_budget: float | int, expected_values: list[tuple], expected_spend: int
):
    expected_output = [
        {k: values[i] for i, k in enumerate(stat.name for stat in stat_configuration)}
        for values in expected_values
    ]

    results = list(
        stats.generate_stat_distribution(stat_configuration, remaining_budget)
    )
    assert len(results) == len(expected_output)
    for result in results:
        assert result.values in expected_output
        assert expected_spend == result.spent_budget
