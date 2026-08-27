"""Three playable science games."""
from __future__ import annotations
import sys
from pathlib import Path
_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path: sys.path.insert(0, str(_ROOT))
from science_utils import run_game

def run_ice_to_water() -> None:
    run_game({'id': 'matter_intermediate_ice_to_water', 'title': 'Ice to Water', 'tagline': 'What changed the ice?', 'question': 'What changed the ice?', 'choices': ['Heating', 'Cooling'], 'answer': 'Heating', 'picture': '🧊', 'tip': 'Heating changes solid ice to liquid water.'})

def run_same_stuff_new_look() -> None:
    run_game({'id': 'matter_intermediate_same_stuff_new_look', 'title': 'Same Stuff, New Look', 'tagline': 'Melted chocolate is still what?', 'question': 'Melted chocolate is still what?', 'choices': ['Chocolate', 'Stone'], 'answer': 'Chocolate', 'picture': '🍫', 'tip': 'Melting changes its form, not the stuff.'})

def run_mix_or_settle() -> None:
    run_game({'id': 'matter_intermediate_mix_or_settle', 'title': 'Mix or Settle', 'tagline': 'Sand in water will what?', 'question': 'Sand in water will what?', 'choices': ['Settle', 'Disappear'], 'answer': 'Settle', 'picture': '🥛', 'tip': 'Sand settles to the bottom.'})
