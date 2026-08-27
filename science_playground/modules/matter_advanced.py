"""Three playable science games."""
from __future__ import annotations
import sys
from pathlib import Path
_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path: sys.path.insert(0, str(_ROOT))
from science_utils import run_game

def run_water_cycle_pictures() -> None:
    run_game({'id': 'matter_advanced_water_cycle_pictures', 'title': 'Water Cycle Pictures', 'tagline': 'What comes after a rain puddle warms?', 'question': 'What comes after a rain puddle warms?', 'choices': ['Water vapor rises', 'Ice forms'], 'answer': 'Water vapor rises', 'picture': '🌦️', 'tip': 'Warm water can become vapor and rise.'})

def run_soft_to_hard() -> None:
    run_game({'id': 'matter_advanced_soft_to_hard', 'title': 'Soft to Hard', 'tagline': 'Clay is baked. What happens?', 'question': 'Clay is baked. What happens?', 'choices': ['Gets harder', 'Gets wetter'], 'answer': 'Gets harder', 'picture': '🏺', 'tip': 'Heating can make clay hard.'})

def run_what_holds_shape() -> None:
    run_game({'id': 'matter_advanced_what_holds_shape', 'title': 'What Holds Shape?', 'tagline': 'Which keeps its own shape?', 'question': 'Which keeps its own shape?', 'choices': ['Juice', 'Wood block'], 'answer': 'Wood block', 'picture': '🧱', 'tip': 'A solid holds its own shape.'})
