"""Three playable science games."""
from __future__ import annotations
import sys
from pathlib import Path
_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path: sys.path.insert(0, str(_ROOT))
from science_utils import run_game

def run_will_the_tower_fall() -> None:
    run_game({'id': 'make_test_beginner_will_the_tower_fall', 'title': 'Will the Tower Fall?', 'tagline': 'Which tower will stay up?', 'question': 'Which tower will stay up?', 'choices': ['Wide bottom', 'Tiny bottom'], 'answer': 'Wide bottom', 'picture': '🗼', 'tip': 'A wide base helps a tower stay steady.'})

def run_ramp_or_wall() -> None:
    run_game({'id': 'make_test_beginner_ramp_or_wall', 'title': 'Ramp or Wall?', 'tagline': 'Which helps the car roll down?', 'question': 'Which helps the car roll down?', 'choices': ['Ramp', 'Wall'], 'answer': 'Ramp', 'picture': '🛝', 'tip': 'A ramp gives the car a sloping path.'})

def run_fit_the_hole() -> None:
    run_game({'id': 'make_test_beginner_fit_the_hole', 'title': 'Fit the Hole', 'tagline': 'Which shape fits the round hole?', 'question': 'Which shape fits the round hole?', 'choices': ['Circle', 'Square'], 'answer': 'Circle', 'picture': '⭕', 'tip': 'The circle matches the round hole.'})
