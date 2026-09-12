"""Beginner Light & Sound games use their own scenes, not the discovery card."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "science_playground"))

from kid_sounds import render_sound
from modules.light_sound_beginner import (
    _high_trials,
    _light_trials,
    _loud_trials,
)
from picture_scenes import EXTRA_SCENES
from science_utils import _BESPOKE_GAMES, _with_discovery_trials


def test_three_games_are_bespoke() -> None:
    for game_id in (
        "light_sound_beginner_light_or_dark",
        "light_sound_beginner_loud_or_quiet",
        "light_sound_beginner_high_or_low",
    ):
        assert game_id in _BESPOKE_GAMES
    wrapped = _with_discovery_trials({
        "id": "light_sound_beginner_loud_or_quiet",
        "scene": "loud_or_quiet",
        "choices": ["Drum", "Whisper"],
        "answer": "Drum",
        "question": "Which sound is loud?",
        "trials": _loud_trials(),
    })
    assert all(trial.get("context") != "Music room" for trial in wrapped["trials"])
    assert wrapped["trials"][0]["loud"] == "Drum"


def test_scenes_use_pair_names_not_giveaway_or_sun_card() -> None:
    light = EXTRA_SCENES["light_or_dark"](
        0,
        {"light": "Lit lamp", "dark": "Dark cave", "light_kind": "lamp", "dark_kind": "cave"},
        pose="play",
    )
    assert "Lit lamp" in light and "Dark cave" in light
    assert "Balance table" not in light

    loud = EXTRA_SCENES["loud_or_quiet"](
        1,
        {"loud": "Thunder", "quiet": "Soft rain", "loud_kind": "thunder", "quiet_kind": "rain"},
        pose="play",
    )
    assert "Thunder" in loud and "Soft rain" in loud
    assert "LOUD" not in loud
    assert "Sunny yard" not in loud

    high = EXTRA_SCENES["high_or_low"](
        0,
        {"high": "Bird", "low": "Frog", "high_pic": "🐦", "low_pic": "🐸"},
        pose="play",
    )
    assert "Bird" in high and "Frog" in high
    assert "HIGH" not in high


def test_loud_trials_carry_sounds_and_wav_is_real() -> None:
    trial = _loud_trials()[0]
    assert trial["answer_sound"] == "drum"
    assert trial["hear_left"] == "whisper"
    wav = render_sound("drum")
    assert wav[:4] == b"RIFF"
    assert _high_trials()[0]["answer_sound"] == "high"
    assert _light_trials()[1]["question"] == "Which place is dark?"
