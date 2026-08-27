"""Three playable science games."""
from __future__ import annotations
import sys
from pathlib import Path
_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path: sys.path.insert(0, str(_ROOT))
from science_utils import run_game

def run_debug_the_path() -> None:
    run_game({'id': 'follow_the_steps_advanced_debug_the_path', 'title': 'Debug the Path', 'tagline': 'Robot turns wrong. What should change?', 'question': 'Robot turns wrong. What should change?', 'choices': ['Turn step', 'Battery color'], 'answer': 'Turn step', 'picture': '🐞', 'tip': 'Debug the incorrect turn instruction.'})

def run_loop_the_square() -> None:
    run_game({'id': 'follow_the_steps_advanced_loop_the_square', 'title': 'Loop the Square', 'tagline': 'Which steps repeat four times?', 'question': 'Which steps repeat four times?', 'choices': ['Forward, turn', 'Jump, sleep'], 'answer': 'Forward, turn', 'picture': '⬜', 'tip': 'Forward then turn repeated makes a square.'})

def run_if_wet_then_boots() -> None:
    run_game({'id': 'follow_the_steps_advanced_if_wet_then_boots', 'title': 'If Wet, Then Boots', 'tagline': 'The ground is wet. Wear what?', 'question': 'The ground is wet. Wear what?', 'choices': ['Boots', 'Slippers'], 'answer': 'Boots', 'picture': '🌧️', 'tip': 'The condition is wet, so choose boots.'})
