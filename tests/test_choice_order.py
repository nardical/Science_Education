"""Answer buttons should not march left, right, left, right."""
from __future__ import annotations

import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "science_playground"))

from modules.matter_beginner import MELT_FREEZE
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
