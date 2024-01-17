import pytest

import card_generator.base as base
import card_generator.abilities as abilities

test_data = [
    pytest.param([], [], {}, id="No abilities generates no results."),
    pytest.param(
        [
            abilities.AbilityConfiguration(
                name="do_thing",
                text_template="Do the thing.",
                base_cost=1,
            )
        ],
        [],
        {
            1: [
                abilities.Ability(
                    text="Do the thing.",
                    cost=1,
                )
            ]
        },
        id="A single ability returns a single result"
    ),
    pytest.param(
        [
            abilities.AbilityConfiguration(
                name="do_thing",
                text_template="Do the thing",
                base_cost=1
            ),
            abilities.AbilityConfiguration(
                name="do_damage",
                text_template="Do {damage_value} damage.",
                base_cost=1,
                scalars=(
                    abilities.Scalar(
                        cost_schedule=(base.CostStep(0, 1), base.CostStep(2, 2), base.CostStep(4, 1)),
                        max_value=5,
                        name="damage_value"
                    ),
                )
            )
        ],
        [],
        {
            1: [abilities.Ability(text="Do the thing", cost=1)],
            2: [abilities.Ability(
                text="Do 1 damage.",
                cost=2
            )
            ],
            3: [
                abilities.Ability(
                    text="Do 2 damage.",
                    cost=3
                )
            ],
            5: [abilities.Ability(
                text="Do 3 damage.",
                cost=5
            )],
            7: [abilities.Ability(
                text="Do 4 damage.",
                cost=7
            )],
            8: [abilities.Ability(
                text="Do 5 damage.",
                cost=8
            )]
        },
        id="Scalars and cost schedules generate multiple abilities."
    )
]


@pytest.mark.parametrize(
    "abilities_configuration,modifiers_configuration,expected_output",
    test_data
)
def test_generate_abilities(abilities_configuration, modifiers_configuration, expected_output):
    # Goal, go over all the abilities and modifiers and emit card effects with
    # costs that can then be cycled over at each cost target to generate various
    # cards.
    results = abilities.generate(abilities_configuration, modifiers_configuration)

    assert results == expected_output
