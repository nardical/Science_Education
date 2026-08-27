"""Three playable science games."""
from __future__ import annotations
import sys
from pathlib import Path
_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path: sys.path.insert(0, str(_ROOT))
from science_utils import run_game

def run_who_went_farther() -> None:
    run_game({'id': 'motion_intermediate_who_went_farther', 'title': 'Who Went Farther?', 'tagline': 'Which car went farther?', 'question': 'Which car went farther?', 'choices': ['Blue car', 'Red car'], 'answer': 'Red car', 'picture': '🏁', 'tip': 'The red car ends farther from start.'})

def run_speeding_up() -> None:
    run_game({'id': 'motion_intermediate_speeding_up', 'title': 'Speeding Up?', 'tagline': 'The gaps grow. What happens?', 'question': 'The gaps grow. What happens?', 'choices': ['Slowing down', 'Speeding up'], 'answer': 'Speeding up', 'picture': '🚙', 'tip': 'Growing gaps show increasing speed.'})

def run_which_way_does_it_roll() -> None:
    run_game({'id': 'motion_intermediate_which_way_does_it_roll', 'title': 'Which Way Does It Roll?', 'tagline': 'Which way will the ball roll?', 'question': 'Which way will the ball roll?', 'choices': ['Downhill', 'Uphill'], 'answer': 'Downhill', 'picture': '⚽', 'tip': 'Gravity pulls the ball downhill.'})
