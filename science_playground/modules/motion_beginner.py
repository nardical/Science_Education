"""Three playable science games."""
from __future__ import annotations
import sys
from pathlib import Path
_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path: sys.path.insert(0, str(_ROOT))
from science_utils import run_game

def run_fast_or_slow() -> None:
    run_game({'id': 'motion_beginner_fast_or_slow', 'title': 'Fast or Slow', 'tagline': 'Which one moves fast?', 'question': 'Which one moves fast?', 'choices': ['Snail', 'Race car'], 'answer': 'Race car', 'picture': '🏎️', 'tip': 'The race car moves fast.'})

def run_stop_or_go() -> None:
    run_game({'id': 'motion_beginner_stop_or_go', 'title': 'Stop or Go', 'tagline': 'The light is green. What now?', 'question': 'The light is green. What now?', 'choices': ['Stop', 'Go'], 'answer': 'Go', 'picture': '🚦', 'tip': 'Green means go.'})

def run_push_or_pull() -> None:
    run_game({'id': 'motion_beginner_push_or_pull', 'title': 'Push or Pull', 'tagline': 'Move the wagon toward you.', 'question': 'Move the wagon toward you.', 'choices': ['Push', 'Pull'], 'answer': 'Pull', 'picture': '🛒', 'tip': 'A pull brings it toward you.'})
