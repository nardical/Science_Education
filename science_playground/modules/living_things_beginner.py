"""Three playable science games."""
from __future__ import annotations
import sys
from pathlib import Path
_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path: sys.path.insert(0, str(_ROOT))
from science_utils import run_game

def run_living_or_not() -> None:
    run_game({'id': 'living_things_beginner_living_or_not', 'title': 'Living or Not', 'tagline': 'Which one is living?', 'question': 'Which one is living?', 'choices': ['Puppy', 'Toy car'], 'answer': 'Puppy', 'picture': '🐶', 'tip': 'A puppy grows and needs food.'})

def run_plant_or_animal() -> None:
    run_game({'id': 'living_things_beginner_plant_or_animal', 'title': 'Plant or Animal', 'tagline': 'Which one is a plant?', 'question': 'Which one is a plant?', 'choices': ['Sunflower', 'Rabbit'], 'answer': 'Sunflower', 'picture': '🌻', 'tip': 'A sunflower is a plant.'})

def run_hungry_or_full() -> None:
    run_game({'id': 'living_things_beginner_hungry_or_full', 'title': 'Hungry or Full', 'tagline': 'What does the hungry bird need?', 'question': 'What does the hungry bird need?', 'choices': ['Food', 'A toy'], 'answer': 'Food', 'picture': '🐦', 'tip': 'Living animals need food.'})
