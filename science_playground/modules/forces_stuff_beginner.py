"""Three playable science games."""
from __future__ import annotations
import sys
from pathlib import Path
_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path: sys.path.insert(0, str(_ROOT))
from science_utils import run_game

# Cycle in order, then wrap. Question alternates heavier / lighter by index.
HEAVY_PAIRS: tuple[dict[str, str], ...] = (
    {
        "heavy": "Rock",
        "light": "Feather",
        "heavy_pic": "🪨",
        "light_pic": "🪶",
        "kid_tip": "The rock is heavy. The feather is light.",
        "tip": "The rock is heavier than the feather.",
    },
    {
        "heavy": "Bowling ball",
        "light": "Balloon",
        "heavy_kind": "bowling",
        "light_pic": "🎈",
        "kid_tip": "The bowling ball is heavy. The balloon is light.",
        "tip": "A bowling ball is much heavier than a balloon.",
    },
    {
        "heavy": "Elephant",
        "light": "Mouse",
        "heavy_pic": "🐘",
        "light_pic": "🐭",
        "kid_tip": "The elephant is heavy. The mouse is light.",
        "tip": "An elephant is much heavier than a mouse.",
    },
    {
        "heavy": "Truck",
        "light": "Paper airplane",
        "heavy_pic": "🚚",
        "light_kind": "paper_plane",
        "kid_tip": "The truck is heavy. The paper airplane is light.",
        "tip": "A truck is much heavier than a paper airplane.",
    },
    {
        "heavy": "Watermelon",
        "light": "Marshmallow",
        "heavy_pic": "🍉",
        "light_kind": "marshmallow",
        "kid_tip": "The watermelon is heavy. The marshmallow is light.",
        "tip": "A watermelon is much heavier than a marshmallow.",
    },
    {
        "heavy": "Anvil",
        "light": "Leaf",
        "heavy_kind": "anvil",
        "light_pic": "🍃",
        "kid_tip": "The anvil is heavy. The leaf is light.",
        "tip": "An anvil is much heavier than a leaf.",
    },
    {
        "heavy": "Full backpack",
        "light": "Empty bag",
        "heavy_pic": "🎒",
        "light_pic": "👜",
        "kid_tip": "The full backpack is heavy. The empty bag is light.",
        "tip": "A full backpack is heavier than an empty bag.",
    },
    {
        "heavy": "Brick",
        "light": "Sponge",
        "heavy_pic": "🧱",
        "light_pic": "🧽",
        "kid_tip": "The brick is heavy. The sponge is light.",
        "tip": "A brick is heavier than a sponge.",
    },
    {
        "heavy": "Pumpkin",
        "light": "Bubble",
        "heavy_pic": "🎃",
        "light_kind": "bubble",
        "kid_tip": "The pumpkin is heavy. The bubble is light.",
        "tip": "A pumpkin is much heavier than a bubble.",
    },
    {
        "heavy": "Dumbbell",
        "light": "Cotton ball",
        "heavy_kind": "dumbbell",
        "light_kind": "cotton",
        "kid_tip": "The dumbbell is heavy. The cotton ball is light.",
        "tip": "A dumbbell is much heavier than a cotton ball.",
    },
)


def _heavy_trials() -> tuple[dict[str, str | list[str] | bool], ...]:
    trials: list[dict[str, str | list[str] | bool]] = []
    for i, pair in enumerate(HEAVY_PAIRS):
        ask_heavier = i % 2 == 0
        heavy = pair["heavy"]
        light = pair["light"]
        trial: dict[str, str | list[str] | bool] = dict(pair)
        trial["question"] = "Which one is heavier?" if ask_heavier else "Which one is lighter?"
        trial["choices"] = [heavy, light]
        trial["answer"] = heavy if ask_heavier else light
        trial["heavy_left"] = i % 2 == 0
        trials.append(trial)
    return tuple(trials)


def run_heavy_or_light() -> None:
    run_game({
        'id': 'forces_stuff_beginner_heavy_or_light',
        'title': 'Heavy or Light',
        'tagline': 'Which one is heavier? Which one is lighter?',
        'question': 'Which one is heavier?',
        'choices': ['Rock', 'Feather'],
        'answer': 'Rock',
        'picture': '🪨',
        'scene': 'heavy_light',
        'animate_mode': 'once',
        'trials': _heavy_trials(),
        'kid_tip': 'The rock is heavy. The feather is light.',
        'tip': 'The rock is heavier than the feather.',
    })

# Cycle in order, then wrap. Mix sink and float so the answer is not a pattern.
SINK_FLOAT_ITEMS: tuple[dict[str, str], ...] = (
    {
        "item": "Rubber duck",
        "kind": "duck",
        "answer": "Float",
        "kid_tip": "The rubber duck stays on top of the water.",
        "tip": "A rubber duck is light for its size, so it floats.",
    },
    {
        "item": "Rock",
        "kind": "rock",
        "answer": "Sink",
        "kid_tip": "The rock goes down to the bottom.",
        "tip": "A rock is heavy for its size, so it sinks.",
    },
    {
        "item": "Wood boat",
        "kind": "boat",
        "answer": "Float",
        "kid_tip": "The wood boat stays on top of the water.",
        "tip": "A wood boat holds air inside, so it floats.",
    },
    {
        "item": "Coin",
        "kind": "coin",
        "answer": "Sink",
        "kid_tip": "The coin goes down to the bottom.",
        "tip": "A metal coin is heavy for its size, so it sinks.",
    },
    {
        "item": "Beach ball",
        "kind": "beachball",
        "answer": "Float",
        "kid_tip": "The beach ball stays on top of the water.",
        "tip": "A beach ball is full of air, so it floats.",
    },
    {
        "item": "Metal spoon",
        "kind": "spoon",
        "answer": "Sink",
        "kid_tip": "The metal spoon goes down to the bottom.",
        "tip": "A metal spoon is heavy for its size, so it sinks.",
    },
    {
        "item": "Apple",
        "kind": "apple",
        "answer": "Float",
        "kid_tip": "The apple stays on top of the water.",
        "tip": "An apple has tiny air pockets, so it floats.",
    },
    {
        "item": "Key",
        "kind": "key",
        "answer": "Sink",
        "kid_tip": "The key goes down to the bottom.",
        "tip": "A metal key is heavy for its size, so it sinks.",
    },
    {
        "item": "Empty bottle",
        "kind": "bottle",
        "answer": "Float",
        "kid_tip": "The empty bottle stays on top of the water.",
        "tip": "An empty bottle is full of air, so it floats.",
    },
    {
        "item": "Toy car",
        "kind": "toy_car",
        "answer": "Sink",
        "kid_tip": "The toy car goes down to the bottom.",
        "tip": "A metal toy car is heavy for its size, so it sinks.",
    },
)


def _sink_trials() -> tuple[dict[str, str | list[str]], ...]:
    trials: list[dict[str, str | list[str]]] = []
    for item in SINK_FLOAT_ITEMS:
        trial: dict[str, str | list[str]] = dict(item)
        trial["question"] = "Will it sink or float?"
        trial["choices"] = ["Sink", "Float"]
        trials.append(trial)
    return tuple(trials)


def run_sink_or_float() -> None:
    run_game({
        'id': 'forces_stuff_beginner_sink_or_float',
        'title': 'Sink or Float',
        'tagline': 'Will it sink or float?',
        'question': 'Will it sink or float?',
        'choices': ['Sink', 'Float'],
        'answer': 'Float',
        'item': 'Rubber duck',
        'kind': 'duck',
        'picture': '🦆',
        'scene': 'sink_float',
        'animate_mode': 'once',
        'trials': _sink_trials(),
        'kid_tip': 'The rubber duck stays on top of the water.',
        'tip': 'A rubber duck is light for its size, so it floats.',
    })

def run_sticky_or_slippy() -> None:
    run_game({
        'id': 'forces_stuff_beginner_sticky_or_slippy',
        'title': 'Sticky or Slippy',
        'tagline': 'Which floor is slippy?',
        'question': 'Which floor is slippy?',
        'choices': ['Rough rug', 'Smooth ice'],
        'answer': 'Smooth ice',
        'picture': '⛸️',
        'scene': 'sticky_slippy',
        'kid_tip': 'Smooth ice is slippy!',
        'tip': 'Smooth ice has little grip.',
    })
