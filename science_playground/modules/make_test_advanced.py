"""Three playable science games."""
from __future__ import annotations
import sys
from pathlib import Path
_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path: sys.path.insert(0, str(_ROOT))
from science_utils import run_game

def run_stronger_shape() -> None:
    run_game({'id': 'make_test_advanced_stronger_shape', 'title': 'Stronger Shape', 'tagline': 'Which shape makes a strong frame?', 'question': 'Which shape makes a strong frame?', 'choices': ['Triangle', 'Wobbly curve'], 'answer': 'Triangle', 'picture': '🔺', 'tip': 'Triangles help frames keep their shape.'})

def run_two_tests_pick_better() -> None:
    run_game({'id': 'make_test_advanced_two_tests_pick_better', 'title': 'Two Tests, Pick Better', 'tagline': 'Bridge A holds more. Pick which?', 'question': 'Bridge A holds more. Pick which?', 'choices': ['Bridge A', 'Bridge B'], 'answer': 'Bridge A', 'picture': '🌉', 'tip': 'Test results show Bridge A is stronger.'})

def run_build_a_path() -> None:
    run_game({'id': 'make_test_advanced_build_a_path', 'title': 'Build a Path', 'tagline': 'Gap blocks the marble. Add what?', 'question': 'Gap blocks the marble. Add what?', 'choices': ['Short bridge', 'Soft pillow'], 'answer': 'Short bridge', 'picture': '🟠', 'tip': 'A firm bridge completes the path.'})
