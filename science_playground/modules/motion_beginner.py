"""Three playable science games."""
from __future__ import annotations
import sys
from pathlib import Path
_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path: sys.path.insert(0, str(_ROOT))
from science_utils import run_game

# Cycle in order, then wrap. Some stories only make sense as push or pull.
PUSH_PULL_SCENES: tuple[dict[str, str], ...] = (
    {
        "kind": "wagon",
        "actor": "kid",
        "action": "Pull",
        "question": "Move the wagon toward the kid.",
        "kid_tip": "Pull brings the wagon toward the kid.",
        "tip": "A pull moves something toward you.",
    },
    {
        "kind": "ant_rock",
        "actor": "ant",
        "action": "Push",
        "question": "Move the rock away from the ant.",
        "kid_tip": "The ant pushes the rock away.",
        "tip": "A push moves something away from you.",
    },
    {
        "kind": "girl_car",
        "actor": "girl",
        "action": "Push",
        "question": "Move the toy car away from the girl.",
        "kid_tip": "The girl pushes the toy car away.",
        "tip": "A push moves something away from you.",
    },
    {
        "kind": "sled",
        "actor": "kid",
        "action": "Pull",
        "question": "Move the sled toward the kid.",
        "kid_tip": "The kid pulls the sled closer.",
        "tip": "A pull moves something toward you.",
    },
    {
        "kind": "dog_toy",
        "actor": "dog",
        "action": "Pull",
        "question": "Move the toy toward the dog.",
        "kid_tip": "The dog pulls the toy closer.",
        "tip": "A pull moves something toward you.",
    },
    {
        "kind": "stroller",
        "actor": "parent",
        "action": "Push",
        "question": "Move the stroller away from the parent.",
        "kid_tip": "The parent pushes the stroller away.",
        "tip": "A push moves something away from you.",
    },
    {
        "kind": "hero_bus",
        "actor": "hero",
        "action": "Push",
        "question": "Move the bus away from the superhero.",
        "kid_tip": "The superhero pushes the bus away.",
        "tip": "A push moves something away from you.",
    },
    {
        "kind": "teddy",
        "actor": "kid",
        "action": "Pull",
        "question": "Move the stuffed animal toward the kid.",
        "kid_tip": "The kid pulls the stuffed animal closer.",
        "tip": "A pull moves something toward you.",
    },
    {
        "kind": "crate",
        "actor": "robot",
        "action": "Push",
        "question": "Move the crate away from the robot.",
        "kid_tip": "The robot pushes the crate away.",
        "tip": "A push moves something away from you.",
    },
    {
        "kind": "hose",
        "actor": "firefighter",
        "action": "Pull",
        "question": "Move the hose toward the firefighter.",
        "kid_tip": "The firefighter pulls the hose closer.",
        "tip": "A pull moves something toward you.",
    },
)


def _push_pull_trials() -> tuple[dict[str, str | list[str]], ...]:
    trials: list[dict[str, str | list[str]]] = []
    for scene in PUSH_PULL_SCENES:
        trial: dict[str, str | list[str]] = dict(scene)
        trial["choices"] = ["Push", "Pull"]
        trial["answer"] = scene["action"]
        trials.append(trial)
    return tuple(trials)


def run_fast_or_slow() -> None:
    run_game({
        'id': 'motion_beginner_fast_or_slow',
        'title': 'Fast or Slow',
        'tagline': 'Which one moves fast?',
        'question': 'Which one moves fast?',
        'choices': ['Snail', 'Race car'],
        'answer': 'Race car',
        'picture': '🏎️',
        'scene': 'fast_slow',
        'kid_tip': 'The car zooms. The snail creeps.',
        'tip': 'The race car moves fast.',
    })

# Cycle green → yellow → red, then wrap.
STOP_GO_LIGHTS: tuple[dict[str, str], ...] = (
    {
        "light": "green",
        "answer": "Go",
        "kid_tip": "Green light means go!",
        "tip": "Green means go. Yellow means slow. Red means stop.",
    },
    {
        "light": "yellow",
        "answer": "Slow",
        "kid_tip": "Yellow light means slow down.",
        "tip": "Green means go. Yellow means slow. Red means stop.",
    },
    {
        "light": "red",
        "answer": "Stop",
        "kid_tip": "Red light means stop!",
        "tip": "Green means go. Yellow means slow. Red means stop.",
    },
)


def _stop_go_trials() -> tuple[dict[str, str | list[str]], ...]:
    trials: list[dict[str, str | list[str]]] = []
    for light in STOP_GO_LIGHTS:
        trial: dict[str, str | list[str]] = dict(light)
        trial["question"] = "What should the car do?"
        trial["choices"] = ["Go", "Slow", "Stop"]
        trials.append(trial)
    return tuple(trials)


def run_stop_or_go() -> None:
    run_game({
        'id': 'motion_beginner_stop_or_go',
        'title': 'Stop or Go',
        'tagline': 'Watch the light. What should the car do?',
        'question': 'What should the car do?',
        'choices': ['Go', 'Slow', 'Stop'],
        'answer': 'Go',
        'picture': '🚦',
        'scene': 'stop_go',
        'animate_mode': 'once',
        'trials': _stop_go_trials(),
        'kid_tip': 'Green light means go!',
        'tip': 'Green means go. Yellow means slow. Red means stop.',
    })

def run_push_or_pull() -> None:
    run_game({
        'id': 'motion_beginner_push_or_pull',
        'title': 'Push or Pull',
        'tagline': 'Toward the person, or away?',
        'question': 'Move the wagon toward the kid.',
        'choices': ['Push', 'Pull'],
        'answer': 'Pull',
        'picture': '🛒',
        'scene': 'push_pull',
        'animate_mode': 'on_answer',
        'anim_seconds': 2.0,
        'trials': _push_pull_trials(),
        'kid_tip': 'Pull brings the wagon toward the kid.',
        'tip': 'A pull moves something toward you. A push moves it away.',
    })
