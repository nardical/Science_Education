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

# Cycle in order, then wrap. Question alternates slippy / sticky by index.
STICKY_SLIPPY_PAIRS: tuple[dict[str, str], ...] = (
    {
        "sticky": "Rough rug",
        "slippy": "Smooth ice",
        "sticky_kind": "rug",
        "slippy_kind": "ice",
        "kid_tip": "The rug holds the box. The ice lets it slide.",
        "tip": "A rough rug has more grip. Smooth ice is slippy.",
    },
    {
        "sticky": "Sandpaper",
        "slippy": "Wet tile",
        "sticky_kind": "sandpaper",
        "slippy_kind": "tile",
        "kid_tip": "Sandpaper grabs. Wet tile is slippy.",
        "tip": "A rough surface has more grip than a wet smooth one.",
    },
    {
        "sticky": "Grass",
        "slippy": "Playground slide",
        "sticky_kind": "grass",
        "slippy_kind": "slide",
        "kid_tip": "Grass holds on. The slide lets the box zoom.",
        "tip": "A playground slide is smooth, so things slip down it.",
    },
    {
        "sticky": "Carpet",
        "slippy": "Soapy tub",
        "sticky_kind": "carpet",
        "slippy_kind": "soap",
        "kid_tip": "Carpet grabs the box. Soap makes the tub slippy.",
        "tip": "Soap and water cut grip, so the tub is slippy.",
    },
    {
        "sticky": "Dirt path",
        "slippy": "Frozen puddle",
        "sticky_kind": "dirt",
        "slippy_kind": "ice",
        "kid_tip": "Dirt holds the box. The frozen puddle is slippy.",
        "tip": "Ice is smoother than dirt, so it is slippy.",
    },
    {
        "sticky": "Rubber mat",
        "slippy": "Marble floor",
        "sticky_kind": "rubber",
        "slippy_kind": "marble",
        "kid_tip": "The rubber mat grabs. Marble is smooth and slippy.",
        "tip": "Rubber has grip. Polished marble does not.",
    },
    {
        "sticky": "Velcro",
        "slippy": "Banana peel",
        "sticky_kind": "velcro",
        "slippy_kind": "peel",
        "kid_tip": "Velcro sticks. A banana peel is slippy.",
        "tip": "Hooks grab. A smooth peel does not.",
    },
    {
        "sticky": "Gravel",
        "slippy": "Wet rock",
        "sticky_kind": "gravel",
        "slippy_kind": "wetrock",
        "kid_tip": "Gravel holds the box. A wet rock is slippy.",
        "tip": "Water on a smooth rock makes it slippy.",
    },
    {
        "sticky": "Towel",
        "slippy": "Ice rink",
        "sticky_kind": "towel",
        "slippy_kind": "ice",
        "kid_tip": "A towel grabs. The ice rink lets the box slide.",
        "tip": "A towel is rough and dry. Ice has little grip.",
    },
    {
        "sticky": "Fuzzy sock",
        "slippy": "Smooth glass",
        "sticky_kind": "sock",
        "slippy_kind": "glass",
        "kid_tip": "The fuzzy sock holds on. Glass is slippy.",
        "tip": "Fuzz adds grip. Smooth glass does not.",
    },
)


def _sticky_trials() -> tuple[dict[str, str | list[str] | bool], ...]:
    trials: list[dict[str, str | list[str] | bool]] = []
    for i, pair in enumerate(STICKY_SLIPPY_PAIRS):
        ask_slippy = i % 2 == 0
        sticky = pair["sticky"]
        slippy = pair["slippy"]
        trial: dict[str, str | list[str] | bool] = dict(pair)
        trial["question"] = "Which floor is slippy?" if ask_slippy else "Which floor is sticky?"
        trial["choices"] = [sticky, slippy]
        trial["answer"] = slippy if ask_slippy else sticky
        trial["sticky_left"] = i % 2 == 0
        trial["picture"] = "🧊" if ask_slippy else "🧶"
        trials.append(trial)
    return tuple(trials)


def run_sticky_or_slippy() -> None:
    run_game({
        'id': 'forces_stuff_beginner_sticky_or_slippy',
        'title': 'Sticky or Slippy',
        'tagline': 'Which floor is sticky? Which floor is slippy?',
        'question': 'Which floor is slippy?',
        'choices': ['Rough rug', 'Smooth ice'],
        'answer': 'Smooth ice',
        'picture': '⛸️',
        'scene': 'sticky_slippy',
        'animate_mode': 'once',
        'trials': _sticky_trials(),
        'kid_tip': 'The rug holds the box. The ice lets it slide.',
        'tip': 'A rough rug has more grip. Smooth ice is slippy.',
    })
