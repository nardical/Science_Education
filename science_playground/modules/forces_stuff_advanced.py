"""Three playable science games."""
from __future__ import annotations
import sys
from pathlib import Path
_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path: sys.path.insert(0, str(_ROOT))
from science_utils import run_game

def run_fair_balance() -> None:
    run_game({'id': 'forces_stuff_advanced_fair_balance', 'title': 'Fair Balance', 'tagline': 'How can both sides balance?', 'question': 'How can both sides balance?', 'choices': ['Equal weights', 'One heavy side'], 'answer': 'Equal weights', 'picture': '⚖️', 'tip': 'Equal weights at equal distances balance.'})

def run_rough_vs_smooth_ramp() -> None:
    run_game({'id': 'forces_stuff_advanced_rough_vs_smooth_ramp', 'title': 'Rough vs Smooth Ramp', 'tagline': 'Which car travels farther?', 'question': 'Which car travels farther?', 'choices': ['Rough ramp', 'Smooth ramp'], 'answer': 'Smooth ramp', 'picture': '🏎️', 'tip': 'Less friction lets the car travel farther.'})

def run_lift_with_a_lever() -> None:
    run_game({'id': 'forces_stuff_advanced_lift_with_a_lever', 'title': 'Lift With a Lever', 'tagline': 'Where should the pivot go?', 'question': 'Where should the pivot go?', 'choices': ['Near the rock', 'Near your hand'], 'answer': 'Near the rock', 'picture': '🪵', 'tip': 'A nearby pivot makes lifting easier.'})
