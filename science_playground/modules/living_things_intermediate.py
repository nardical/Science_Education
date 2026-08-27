"""Three playable science games."""
from __future__ import annotations
import sys
from pathlib import Path
_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path: sys.path.insert(0, str(_ROOT))
from science_utils import run_game

def run_what_does_it_need() -> None:
    run_game({'id': 'living_things_intermediate_what_does_it_need', 'title': 'What Does It Need?', 'tagline': 'What helps this plant grow?', 'question': 'What helps this plant grow?', 'choices': ['Water', 'Plastic beads'], 'answer': 'Water', 'picture': '🌱', 'tip': 'Plants need water, light, and air.'})

def run_who_eats_what() -> None:
    run_game({'id': 'living_things_intermediate_who_eats_what', 'title': 'Who Eats What?', 'tagline': 'What should the rabbit eat?', 'question': 'What should the rabbit eat?', 'choices': ['Grass', 'Pebbles'], 'answer': 'Grass', 'picture': '🐇', 'tip': 'Rabbits eat plants such as grass.'})

def run_home_habitat() -> None:
    run_game({'id': 'living_things_intermediate_home_habitat', 'title': 'Home Habitat', 'tagline': 'Where does a fish belong?', 'question': 'Where does a fish belong?', 'choices': ['Pond', 'Dry sandbox'], 'answer': 'Pond', 'picture': '🐟', 'tip': 'A pond gives fish water and food.'})
