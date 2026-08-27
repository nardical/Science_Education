"""Three playable science games."""
from __future__ import annotations
import sys
from pathlib import Path
_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path: sys.path.insert(0, str(_ROOT))
from science_utils import run_game

def run_bigger_block_bigger_shadow() -> None:
    run_game({'id': 'light_sound_advanced_bigger_block_bigger_shadow', 'title': 'Bigger Block, Bigger Shadow', 'tagline': 'Which makes the bigger shadow?', 'question': 'Which makes the bigger shadow?', 'choices': ['Small block', 'Big block'], 'answer': 'Big block', 'picture': '⬛', 'tip': 'A bigger blocker can make a bigger shadow.'})

def run_pitch_ladder() -> None:
    run_game({'id': 'light_sound_advanced_pitch_ladder', 'title': 'Pitch Ladder', 'tagline': 'Which note has highest pitch?', 'question': 'Which note has highest pitch?', 'choices': ['Slow wiggles', 'Fast wiggles'], 'answer': 'Fast wiggles', 'picture': '🎵', 'tip': 'Faster vibrations make a higher pitch.'})

def run_light_path_blocked() -> None:
    run_game({'id': 'light_sound_advanced_light_path_blocked', 'title': 'Light Path Blocked', 'tagline': 'Can light go through the wall?', 'question': 'Can light go through the wall?', 'choices': ['Yes', 'No'], 'answer': 'No', 'picture': '🧱', 'tip': 'An opaque wall blocks the light path.'})
