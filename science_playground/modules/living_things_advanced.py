"""Three playable science games."""
from __future__ import annotations
import sys
from pathlib import Path
_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path: sys.path.insert(0, str(_ROOT))
from science_utils import run_game

def run_life_cycle_order() -> None:
    run_game({'id': 'living_things_advanced_life_cycle_order', 'title': 'Life Cycle Order', 'tagline': 'What comes after an egg?', 'question': 'What comes after an egg?', 'choices': ['Chick', 'Adult chicken'], 'answer': 'Chick', 'picture': '🐣', 'tip': 'A chick hatches before becoming an adult.'})

def run_day_and_night_animals() -> None:
    run_game({'id': 'living_things_advanced_day_and_night_animals', 'title': 'Day and Night Animals', 'tagline': 'Which animal is awake at night?', 'question': 'Which animal is awake at night?', 'choices': ['Owl', 'Butterfly'], 'answer': 'Owl', 'picture': '🦉', 'tip': 'Many owls are active at night.'})

def run_help_it_grow() -> None:
    run_game({'id': 'living_things_advanced_help_it_grow', 'title': 'Help It Grow', 'tagline': 'Plant is pale. What should change?', 'question': 'Plant is pale. What should change?', 'choices': ['Give light', 'Hide in dark'], 'answer': 'Give light', 'picture': '🪴', 'tip': 'Plants use light to help make food.'})
