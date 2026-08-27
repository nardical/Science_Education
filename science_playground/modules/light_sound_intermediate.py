"""Three playable science games."""
from __future__ import annotations
import sys
from pathlib import Path
_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path: sys.path.insert(0, str(_ROOT))
from science_utils import run_game

def run_make_a_shadow() -> None:
    run_game({'id': 'light_sound_intermediate_make_a_shadow', 'title': 'Make a Shadow', 'tagline': 'What must block the light?', 'question': 'What must block the light?', 'choices': ['An object', 'More light'], 'answer': 'An object', 'picture': '🔦', 'tip': 'An object blocks light and makes a shadow.'})

def run_which_is_louder() -> None:
    run_game({'id': 'light_sound_intermediate_which_is_louder', 'title': 'Which Is Louder?', 'tagline': 'Which wave looks louder?', 'question': 'Which wave looks louder?', 'choices': ['Small wave', 'Big wave'], 'answer': 'Big wave', 'picture': '〰️', 'tip': 'A bigger sound wave means louder.'})

def run_echo_or_no_echo() -> None:
    run_game({'id': 'light_sound_intermediate_echo_or_no_echo', 'title': 'Echo or No Echo', 'tagline': 'Where will you hear an echo?', 'question': 'Where will you hear an echo?', 'choices': ['Open pillow pile', 'Empty cave'], 'answer': 'Empty cave', 'picture': '🗣️', 'tip': 'Hard cave walls reflect sound.'})
