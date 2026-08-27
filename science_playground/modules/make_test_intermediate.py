"""Three playable science games."""
from __future__ import annotations
import sys
from pathlib import Path
_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path: sys.path.insert(0, str(_ROOT))
from science_utils import run_game

def run_test_the_bridge() -> None:
    run_game({'id': 'make_test_intermediate_test_the_bridge', 'title': 'Test the Bridge', 'tagline': 'Which test checks the bridge?', 'question': 'Which test checks the bridge?', 'choices': ['Add toy cars', 'Paint it'], 'answer': 'Add toy cars', 'picture': '🌉', 'tip': 'A load test checks if it holds weight.'})

def run_fix_the_ramp() -> None:
    run_game({'id': 'make_test_intermediate_fix_the_ramp', 'title': 'Fix the Ramp', 'tagline': 'Car stops early. What should change?', 'question': 'Car stops early. What should change?', 'choices': ['Make steeper', 'Make flatter'], 'answer': 'Make steeper', 'picture': '🏎️', 'tip': 'A steeper ramp can give more speed.'})

def run_predict_then_try() -> None:
    run_game({'id': 'make_test_intermediate_predict_then_try', 'title': 'Predict Then Try', 'tagline': 'What comes after predict?', 'question': 'What comes after predict?', 'choices': ['Test it', 'Forget it'], 'answer': 'Test it', 'picture': '🔬', 'tip': 'Engineers predict, test, and learn.'})
