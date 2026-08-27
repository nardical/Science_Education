"""Three playable science games."""
from __future__ import annotations
import sys
from pathlib import Path
_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path: sys.path.insert(0, str(_ROOT))
from science_utils import run_game

def run_solid_or_splash() -> None:
    run_game({'id': 'matter_beginner_solid_or_splash', 'title': 'Solid or Splash', 'tagline': 'Which one can splash?', 'question': 'Which one can splash?', 'choices': ['Wood block', 'Water'], 'answer': 'Water', 'picture': '💦', 'tip': 'Liquid water can splash.'})

def run_hot_or_cold() -> None:
    run_game({'id': 'matter_beginner_hot_or_cold', 'title': 'Hot or Cold', 'tagline': 'Which one feels cold?', 'question': 'Which one feels cold?', 'choices': ['Ice cube', 'Warm soup'], 'answer': 'Ice cube', 'picture': '🧊', 'tip': 'Ice is cold.'})

def run_melt_or_freeze() -> None:
    run_game({'id': 'matter_beginner_melt_or_freeze', 'title': 'Melt or Freeze', 'tagline': 'Ice warms. What happens?', 'question': 'Ice warms. What happens?', 'choices': ['Melt', 'Freeze'], 'answer': 'Melt', 'picture': '🌡️', 'tip': 'Warm ice melts into water.'})
