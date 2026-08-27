"""Three playable science games."""
from __future__ import annotations
import sys
from pathlib import Path
_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path: sys.path.insert(0, str(_ROOT))
from science_utils import run_game

def run_three_step_robot() -> None:
    run_game({'id': 'follow_the_steps_intermediate_three_step_robot', 'title': 'Three-Step Robot', 'tagline': 'Forward, turn, then what?', 'question': 'Forward, turn, then what?', 'choices': ['Forward', 'Sleep'], 'answer': 'Forward', 'picture': '🤖', 'tip': 'The robot follows each step in order.'})

def run_if_red_then_stop() -> None:
    run_game({'id': 'follow_the_steps_intermediate_if_red_then_stop', 'title': 'If Red, Then Stop', 'tagline': 'The light turns red. Do what?', 'question': 'The light turns red. Do what?', 'choices': ['Stop', 'Go'], 'answer': 'Stop', 'picture': '🚦', 'tip': 'The if-then rule says red means stop.'})

def run_repeat_3_times() -> None:
    run_game({'id': 'follow_the_steps_intermediate_repeat_3_times', 'title': 'Repeat 3 Times', 'tagline': 'Tap repeats three times. How many?', 'question': 'Tap repeats three times. How many?', 'choices': ['3', '1', '5'], 'answer': '3', 'picture': '🔁', 'tip': 'A loop repeats the action three times.'})
