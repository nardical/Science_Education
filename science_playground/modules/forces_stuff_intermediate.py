"""Three playable science games."""
from __future__ import annotations
import sys
from pathlib import Path
_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path: sys.path.insert(0, str(_ROOT))
from science_utils import run_game

def run_balance_the_seesaw() -> None:
    run_game({'id': 'forces_stuff_intermediate_balance_the_seesaw', 'title': 'Balance the Seesaw', 'tagline': 'Where should the heavy bear sit?', 'question': 'Where should the heavy bear sit?', 'choices': ['Near the middle', 'Far away'], 'answer': 'Near the middle', 'picture': '⚖️', 'tip': 'A heavy object balances closer to the middle.'})

def run_will_it_slide() -> None:
    run_game({'id': 'forces_stuff_intermediate_will_it_slide', 'title': 'Will It Slide?', 'tagline': 'Which surface has less friction?', 'question': 'Which surface has less friction?', 'choices': ['Sandpaper', 'Smooth tile'], 'answer': 'Smooth tile', 'picture': '📦', 'tip': 'Smooth tile has less friction.'})

def run_stronger_push_wins() -> None:
    run_game({'id': 'forces_stuff_intermediate_stronger_push_wins', 'title': 'Stronger Push Wins', 'tagline': 'Which way will the box move?', 'question': 'Which way will the box move?', 'choices': ['Toward big push', 'Toward small push'], 'answer': 'Toward big push', 'picture': '💪', 'tip': 'The stronger force wins.'})
