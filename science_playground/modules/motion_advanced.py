"""Three playable science games."""
from __future__ import annotations
import sys
from pathlib import Path
_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path: sys.path.insert(0, str(_ROOT))
from science_utils import run_game

def run_steeper_goes_faster() -> None:
    run_game({'id': 'motion_advanced_steeper_goes_faster', 'title': 'Steeper Goes Faster', 'tagline': 'Which ramp makes more speed?', 'question': 'Which ramp makes more speed?', 'choices': ['Flat ramp', 'Steep ramp'], 'answer': 'Steep ramp', 'picture': '🛝', 'tip': 'A steeper ramp makes it speed up more.'})

def run_two_pushes_add_up() -> None:
    run_game({'id': 'motion_advanced_two_pushes_add_up', 'title': 'Two Pushes Add Up', 'tagline': 'Two pushes point right. Then what?', 'question': 'Two pushes point right. Then what?', 'choices': ['Moves left', 'Moves right'], 'answer': 'Moves right', 'picture': '➡️', 'tip': 'Pushes in one direction add together.'})

def run_race_the_clock() -> None:
    run_game({'id': 'motion_advanced_race_the_clock', 'title': 'Race the Clock', 'tagline': 'Same trip. Who is faster?', 'question': 'Same trip. Who is faster?', 'choices': ['3-second car', '6-second car'], 'answer': '3-second car', 'picture': '⏱️', 'tip': 'Less time for the same trip means faster.'})
