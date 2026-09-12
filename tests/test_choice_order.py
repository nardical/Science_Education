"""Answer-button placement: stored shuffle, not rotate-by-round."""
from __future__ import annotations

import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "science_playground"))

from modules.forces_stuff_beginner import _heavy_trials, _sink_trials
from modules.motion_beginner import _fast_slow_trials
from science_utils import remember_choice_order


def _rotated(choices: list[str], round_no: int) -> list[str]:
    shift = round_no % len(choices)
    return choices[shift:] + choices[:shift]


def test_old_rotate_pinned_heavy_light_and_fast_slow() -> None:
    heavy_sides = [
        _rotated(list(trial["choices"]), i).index(trial["answer"])
        for i, trial in enumerate(_heavy_trials())
    ]
    fast_sides = [
        _rotated(list(trial["choices"]), i).index(trial["answer"])
        for i, trial in enumerate(_fast_slow_trials())
    ]
    sink_sides = [
        _rotated(list(trial["choices"]), i).index(trial["answer"])
        for i, trial in enumerate(_sink_trials())
    ]
    assert heavy_sides == [0] * 10
    assert fast_sides == [0] * 10
    assert sink_sides == [1] * 10


def test_remembered_shuffle_is_stable_and_uses_both_sides() -> None:
    store: dict[str, object] = {}
    first = remember_choice_order(store, "r0", ["Rock", "Feather"], rng=random.Random(1))
    again = remember_choice_order(store, "r0", ["Rock", "Feather"], rng=random.Random(99))
    assert first == again
    assert sorted(first) == ["Feather", "Rock"]

    left = right = 0
    for i, trial in enumerate(_heavy_trials()):
        order = remember_choice_order(
            {}, f"heavy-{i}", list(trial["choices"]), rng=random.Random(i + 17)
        )
        if order[0] == trial["answer"]:
            left += 1
        else:
            right += 1
    assert left > 0 and right > 0
