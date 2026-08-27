"""Three playable science games."""
from __future__ import annotations
import sys
from pathlib import Path
_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path: sys.path.insert(0, str(_ROOT))
from science_utils import run_game

def run_heavy_or_light() -> None:
    run_game({'id': 'forces_stuff_beginner_heavy_or_light', 'title': 'Heavy or Light', 'tagline': 'Which one is heavy?', 'question': 'Which one is heavy?', 'choices': ['Feather', 'Rock'], 'answer': 'Rock', 'picture': '🪨', 'tip': 'The rock is heavier than the feather.'})

def run_sink_or_float() -> None:
    run_game({'id': 'forces_stuff_beginner_sink_or_float', 'title': 'Sink or Float', 'tagline': 'What will the cork do?', 'question': 'What will the cork do?', 'choices': ['Sink', 'Float'], 'answer': 'Float', 'picture': '🟤', 'tip': 'Cork usually floats on water.'})

def run_sticky_or_slippy() -> None:
    run_game({'id': 'forces_stuff_beginner_sticky_or_slippy', 'title': 'Sticky or Slippy', 'tagline': 'Which floor is slippy?', 'question': 'Which floor is slippy?', 'choices': ['Rough rug', 'Smooth ice'], 'answer': 'Smooth ice', 'picture': '⛸️', 'tip': 'Smooth ice has little grip.'})
