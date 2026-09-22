"""Sticky or Slippy uses real floors, not the discovery beach/scale card."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "science_playground"))

from modules.forces_stuff_beginner import STICKY_SLIPPY_PAIRS, _sticky_trials
from science_utils import _BESPOKE_GAMES, _scene_sticky_slippy, _with_discovery_trials


def test_game_is_bespoke_and_has_ten_floors() -> None:
    assert "forces_stuff_beginner_sticky_or_slippy" in _BESPOKE_GAMES
    assert len(STICKY_SLIPPY_PAIRS) == 10
    trials = _sticky_trials()
    assert [t["question"] for t in trials[:2]] == [
        "Which floor is slippy?",
        "Which floor is sticky?",
    ]
    assert trials[0]["choices"] == ["Rough rug", "Smooth ice"]
    wrapped = _with_discovery_trials({
        "id": "forces_stuff_beginner_sticky_or_slippy",
        "scene": "sticky_slippy",
        "choices": ["Rough rug", "Smooth ice"],
        "answer": "Smooth ice",
        "question": "Which floor is slippy?",
        "trials": trials,
    })
    assert wrapped["trials"][3]["slippy"] == "Soapy tub"
    assert all(trial.get("context") != "Beach" for trial in wrapped["trials"])


def test_scene_shows_names_and_sliding_boxes() -> None:
    html = _scene_sticky_slippy(
        0,
        {
            "sticky": "Rough rug",
            "slippy": "Smooth ice",
            "sticky_kind": "rug",
            "slippy_kind": "ice",
            "sticky_left": True,
        },
        pose="play",
    )
    assert "Rough rug" in html
    assert "Smooth ice" in html
    assert "STICKY" not in html
    assert "SLIPPY" not in html
    assert "Beach" not in html
    assert "box-shadow" in html
    assert "stickMove" in html and "slipMove" in html
