"""Three playable science games."""
from __future__ import annotations
import sys
from pathlib import Path
_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path: sys.path.insert(0, str(_ROOT))
from science_utils import run_game

def run_first_then_next() -> None:
    run_game({'id': 'follow_the_steps_beginner_first_then_next', 'title': 'First Then Next', 'tagline': 'First socks. What comes next?', 'question': 'First socks. What comes next?', 'choices': ['Shoes', 'Hat'], 'answer': 'Shoes', 'picture': '🧦', 'tip': 'Socks come before shoes.'})

def run_which_step_is_missing() -> None:
    run_game({'id': 'follow_the_steps_beginner_which_step_is_missing', 'title': 'Which Step Is Missing?', 'tagline': 'Wash, dry, then what?', 'question': 'Wash, dry, then what?', 'choices': ['Put away', 'Make muddy'], 'answer': 'Put away', 'picture': '🧼', 'tip': 'Put it away after it is dry.'})

def run_do_it_again() -> None:
    run_game({'id': 'follow_the_steps_beginner_do_it_again', 'title': 'Do It Again', 'tagline': 'Repeat means what?', 'question': 'Repeat means what?', 'choices': ['Do it again', 'Stop forever'], 'answer': 'Do it again', 'picture': '🔁', 'tip': 'Repeat means do the step again.'})
