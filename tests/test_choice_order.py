"""Answer buttons should not march left, right, left, right."""
from __future__ import annotations

import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "science_playground"))

from modules.forces_stuff_beginner import _heavy_trials, _sticky_trials
from modules.light_sound_beginner import _high_trials, _light_trials, _loud_trials
from modules.matter_beginner import MELT_FREEZE
from modules.motion_beginner import _fast_slow_trials
from pair_trials import flip_two_choice, pair_a_left
from science_utils import remember_choice_order, run_game

_STABLE = ["Melt", "Freeze"]
_OLD_CORRECT_FIRST = [
    ["Melt", "Freeze"],
    ["Freeze", "Melt"],
    ["Melt", "Freeze"],
    ["Freeze", "Melt"],
    ["Melt", "Freeze"],
    ["Freeze", "Melt"],
    ["Melt", "Freeze"],
    ["Freeze", "Melt"],
    ["Melt", "Freeze"],
    ["Freeze", "Melt"],
]


def _rotated(choices: list[str], round_no: int) -> list[str]:
    shift = round_no % len(choices)
    return choices[shift:] + choices[:shift]


def test_old_correct_first_plus_rotate_made_left_right() -> None:
    """Listing the right word first, then rotating, made L, R, L, R."""
    sides = [
        _rotated(list(choices), i).index(trial["answer"])
        for i, (trial, choices) in enumerate(zip(MELT_FREEZE, _OLD_CORRECT_FIRST))
    ]
    assert sides == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]


def test_melt_or_freeze_labels_stay_melt_then_freeze() -> None:
    for trial in MELT_FREEZE:
        assert list(trial["choices"]) == _STABLE


def test_locked_labels_without_shuffle_would_alternate() -> None:
    """Stable Melt/Freeze labels plus alternating answers is still L, R, L, R."""
    sides = [list(trial["choices"]).index(trial["answer"]) for trial in MELT_FREEZE]
    assert sides == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]


def test_melt_or_freeze_shuffle_uses_both_sides() -> None:
    left = right = 0
    shuffled_sides = []
    for i, trial in enumerate(MELT_FREEZE):
        order = remember_choice_order(
            {}, f"melt-{i}", list(trial["choices"]), rng=random.Random(i + 23)
        )
        assert sorted(order) == sorted(_STABLE)
        side = order.index(trial["answer"])
        shuffled_sides.append(side)
        if side == 0:
            left += 1
        else:
            right += 1
    assert left > 0 and right > 0
    assert shuffled_sides != [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]


def test_run_game_no_longer_rotates_by_round() -> None:
    import inspect
    source = inspect.getsource(run_game)
    assert "remember_choice_order" in source
    assert "shift = round_no % len(choices)" not in source


def test_remembered_shuffle_stays_put_on_rerun() -> None:
    store: dict[str, object] = {}
    first = remember_choice_order(store, "r0", ["Melt", "Freeze"], rng=random.Random(1))
    again = remember_choice_order(store, "r0", ["Melt", "Freeze"], rng=random.Random(99))
    assert first == again
    assert sorted(first) == ["Freeze", "Melt"]


def _scene_answer_left(trials, a_key: str, left_key: str) -> list[bool]:
    sides = []
    for trial in trials:
        a_on_left = bool(trial[left_key])
        answer_is_a = trial["answer"] == trial[a_key]
        sides.append(a_on_left if answer_is_a else not a_on_left)
    return sides


def test_scene_sides_no_longer_pin_the_correct_picture() -> None:
    light = _scene_answer_left(_light_trials(), "light", "light_left")
    loud = _scene_answer_left(_loud_trials(), "loud", "loud_left")
    high = _scene_answer_left(_high_trials(), "high", "high_left")
    heavy = _scene_answer_left(_heavy_trials(), "heavy", "heavy_left")
    sticky = _scene_answer_left(_sticky_trials(), "sticky", "sticky_left")
    for sides, name in (
        (light, "light"),
        (loud, "loud"),
        (high, "high"),
        (heavy, "heavy"),
        (sticky, "sticky"),
    ):
        assert True in sides and False in sides, name
        assert sides != [True] * 10, name
        assert sides != [False] * 10, name


def test_pair_a_left_is_independent_of_the_question() -> None:
    assert [pair_a_left(i) for i in range(10)] == [
        True, True, False, False, True, True, False, False, True, True,
    ]
    pairs = (
        {"a": "Yes", "b": "No", "a_pic": "🟢", "b_pic": "🔴"},
        {"a": "Up", "b": "Down", "a_pic": "⬆️", "b_pic": "⬇️"},
        {"a": "In", "b": "Out", "a_pic": "📥", "b_pic": "📤"},
        {"a": "Hot", "b": "Cold", "a_pic": "🔥", "b_pic": "❄️"},
    )
    trials = flip_two_choice(
        pairs, a="a", b="b", q_for_a="Which is A?", q_for_b="Which is B?", scene="compare",
    )
    answer_left = [trial["left_name"] == trial["answer"] for trial in trials]
    assert answer_left == [True, False, False, True]
    assert _fast_slow_trials()[0]["fast_top"] is True
