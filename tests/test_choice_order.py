"""Answer buttons should not march left, right, left, right."""
from __future__ import annotations

import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "science_playground"))

from modules.matter_beginner import MELT_FREEZE
from science_utils import remember_choice_order, run_game


def _rotated(choices: list[str], round_no: int) -> list[str]:
    shift = round_no % len(choices)
    return choices[shift:] + choices[:shift]


def test_old_rotate_made_melt_or_freeze_alternate_left_right() -> None:
    """Melt or Freeze lists the right word first, then rotate made L,R,L,R."""
    sides = [
        _rotated(list(trial["choices"]), i).index(trial["answer"])
        for i, trial in enumerate(MELT_FREEZE)
    ]
    assert sides == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]


def test_melt_or_freeze_shuffle_uses_both_sides() -> None:
    left = right = 0
    for i, trial in enumerate(MELT_FREEZE):
        order = remember_choice_order(
            {}, f"melt-{i}", list(trial["choices"]), rng=random.Random(i + 23)
        )
        if order[0] == trial["answer"]:
            left += 1
        else:
            right += 1
    assert left > 0 and right > 0
    shuffled_sides = [
        remember_choice_order(
            {}, f"melt-side-{i}", list(trial["choices"]), rng=random.Random(i + 23)
        ).index(trial["answer"])
        for i, trial in enumerate(MELT_FREEZE)
    ]
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
