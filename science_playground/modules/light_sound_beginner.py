"""Three playable science games."""
from __future__ import annotations
import sys
from pathlib import Path
_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path: sys.path.insert(0, str(_ROOT))
from science_utils import run_game

def run_light_or_dark() -> None:
    run_game({'id': 'light_sound_beginner_light_or_dark', 'title': 'Light or Dark', 'tagline': 'Which place is light?', 'question': 'Which place is light?', 'choices': ['Sunny yard', 'Closed closet'], 'answer': 'Sunny yard', 'picture': '☀️', 'tip': 'Sunlight makes the yard bright.'})

def run_loud_or_quiet() -> None:
    run_game({'id': 'light_sound_beginner_loud_or_quiet', 'title': 'Loud or Quiet', 'tagline': 'Which sound is loud?', 'question': 'Which sound is loud?', 'choices': ['Whisper', 'Drum'], 'answer': 'Drum', 'picture': '🥁', 'tip': 'A drum makes a loud sound.'})

def run_high_or_low() -> None:
    run_game({'id': 'light_sound_beginner_high_or_low', 'title': 'High or Low', 'tagline': 'Which makes a high sound?', 'question': 'Which makes a high sound?', 'choices': ['Tiny bell', 'Big drum'], 'answer': 'Tiny bell', 'picture': '🔔', 'tip': 'A tiny bell often has high pitch.'})
