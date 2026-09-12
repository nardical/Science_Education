"""Three playable science games."""
from __future__ import annotations
import sys
from pathlib import Path
_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))
from pair_trials import flip_two_choice, step_trials
from science_utils import run_game

FARTHER = (
    {"a": "Red car", "b": "Blue car", "a_pic": "🚗", "b_pic": "🚙", "a_move": "bob", "b_move": "still",
     "kid_tip": "The red car stops farther from start.", "tip": "The red car ends farther from start."},
    {"a": "Orange bike", "b": "Green bike", "a_pic": "🚲", "b_pic": "🚲", "a_move": "bob", "b_move": "still",
     "kid_tip": "The orange bike went farther.", "tip": "Farther means it stopped more ahead."},
    {"a": "Yellow sled", "b": "Purple sled", "a_pic": "🛷", "b_pic": "🛷", "a_move": "bob", "b_move": "still",
     "kid_tip": "The yellow sled went farther.", "tip": "Compare where each sled stopped."},
    {"a": "Fast marble", "b": "Slow marble", "a_pic": "🟠", "b_pic": "⚪", "a_move": "bob", "b_move": "still",
     "kid_tip": "The fast marble rolled farther.", "tip": "More travel means farther."},
    {"a": "Long kick", "b": "Short kick", "a_pic": "⚽", "b_pic": "⚽", "a_move": "bob", "b_move": "still",
     "kid_tip": "The long kick sent the ball farther.", "tip": "A longer path is farther."},
    {"a": "Paper plane A", "b": "Paper plane B", "a_pic": "✈️", "b_pic": "✈️", "a_move": "wiggle", "b_move": "still",
     "kid_tip": "Plane A flew farther.", "tip": "Farther is the one that landed ahead."},
    {"a": "Wagon", "b": "Stroller", "a_pic": "🛒", "b_pic": "🍼", "a_move": "bob", "b_move": "still",
     "kid_tip": "The wagon rolled farther.", "tip": "See which one is farther from start."},
    {"a": "Skateboard", "b": "Scooter", "a_pic": "🛹", "b_pic": "🛴", "a_move": "bob", "b_move": "still",
     "kid_tip": "The skateboard went farther.", "tip": "Farther means more distance."},
    {"a": "Bowling ball", "b": "Soft ball", "a_pic": "🎳", "b_pic": "⚾", "a_move": "bob", "b_move": "still",
     "kid_tip": "The bowling ball rolled farther.", "tip": "Compare the stop marks."},
    {"a": "Toy train", "b": "Toy bus", "a_pic": "🚂", "b_pic": "🚌", "a_move": "bob", "b_move": "still",
     "kid_tip": "The toy train went farther.", "tip": "The train stopped farther ahead."},
)

SPEED = (
    {"vehicle": "Race car", "picture": "🏎️", "gaps": "grow", "question": "The gaps grow. What happens?",
     "choices": ["Speeding up", "Slowing down"], "answer": "Speeding up",
     "kid_tip": "Growing gaps mean the race car is speeding up.", "tip": "Growing gaps show increasing speed."},
    {"vehicle": "Turtle", "picture": "🐢", "gaps": "shrink", "question": "The gaps shrink. What happens?",
     "choices": ["Slowing down", "Speeding up"], "answer": "Slowing down",
     "kid_tip": "Shrinking gaps mean the turtle is slowing down.", "tip": "Closer marks mean less speed."},
    {"vehicle": "Bike", "picture": "🚴", "gaps": "grow", "question": "The gaps grow. What happens?",
     "choices": ["Speeding up", "Stopping"], "answer": "Speeding up",
     "kid_tip": "Wider spaces mean the bike is speeding up, not stopping.", "tip": "Growing gaps are not a stop."},
    {"vehicle": "Scooter", "picture": "🛵", "gaps": "shrink", "question": "The gaps shrink. What happens?",
     "choices": ["Slowing down", "Going backward"], "answer": "Slowing down",
     "kid_tip": "The scooter marks get closer. It is slowing down.", "tip": "Closer marks mean less speed."},
    {"vehicle": "Skier", "picture": "🎿", "gaps": "grow", "question": "The gaps grow. What happens?",
     "choices": ["Speeding up", "Slowing down"], "answer": "Speeding up",
     "kid_tip": "The skier’s marks spread out.", "tip": "Spreading marks mean more speed."},
    {"vehicle": "Boat", "picture": "🛶", "gaps": "shrink", "question": "The gaps shrink. What happens?",
     "choices": ["Slowing down", "Speeding up"], "answer": "Slowing down",
     "kid_tip": "The boat marks get closer together.", "tip": "Shrinking gaps mean slowing down."},
    {"vehicle": "Roller skate", "picture": "🛼", "gaps": "grow", "question": "The gaps grow. What happens?",
     "choices": ["Speeding up", "Slowing down"], "answer": "Speeding up",
     "kid_tip": "Roller marks get farther apart.", "tip": "Farther marks mean more speed."},
    {"vehicle": "Sled", "picture": "🛷", "gaps": "shrink", "question": "The gaps shrink. What happens?",
     "choices": ["Slowing down", "Speeding up"], "answer": "Slowing down",
     "kid_tip": "The sled marks bunch up. It is slowing down.", "tip": "Closer marks mean less speed."},
    {"vehicle": "Motorcycle", "picture": "🏍️", "gaps": "grow", "question": "The gaps grow. What happens?",
     "choices": ["Speeding up", "Slowing down"], "answer": "Speeding up",
     "kid_tip": "The motorcycle jumps get bigger.", "tip": "Bigger jumps in the path mean faster."},
    {"vehicle": "Balloon cart", "picture": "🎈", "gaps": "shrink", "question": "The gaps shrink. What happens?",
     "choices": ["Slowing down", "Speeding up"], "answer": "Slowing down",
     "kid_tip": "The cart ticks get closer.", "tip": "Closer ticks mean slowing down."},
)

ROLL = (
    {"ball": "Soccer ball", "ball_pic": "⚽", "picture": "⚽", "question": "Which way will it roll?",
     "choices": ["Downhill", "Uphill"], "answer": "Downhill",
     "kid_tip": "The soccer ball rolls downhill.", "tip": "Things roll downhill unless something stops them."},
    {"ball": "Marble", "ball_pic": "🟠", "picture": "🟠", "question": "Which way will it not roll by itself?",
     "choices": ["Uphill", "Downhill"], "answer": "Uphill",
     "kid_tip": "A marble will not roll uphill by itself.", "tip": "Uphill needs an extra push."},
    {"ball": "Sled", "ball_pic": "🛷", "picture": "🛷", "question": "Which way will it roll?",
     "choices": ["Downhill", "Uphill"], "answer": "Downhill",
     "kid_tip": "The sled slides downhill.", "tip": "Sleds go down the hill."},
    {"ball": "Bike", "ball_pic": "🚲", "picture": "🚲", "question": "Which way will it not roll by itself?",
     "choices": ["Uphill", "Downhill"], "answer": "Uphill",
     "kid_tip": "Without pedaling, a bike will not roll uphill.", "tip": "Downhill needs no extra push."},
    {"ball": "Skateboard", "ball_pic": "🛹", "picture": "🛹", "question": "Which way will it roll?",
     "choices": ["Downhill", "Uphill"], "answer": "Downhill",
     "kid_tip": "The skateboard rolls down the driveway.", "tip": "A driveway slope is downhill."},
    {"ball": "Bowling ball", "ball_pic": "🎳", "picture": "🎳", "question": "Which way will it not roll by itself?",
     "choices": ["Uphill", "Downhill"], "answer": "Uphill",
     "kid_tip": "The bowling ball will not roll up the ramp by itself.", "tip": "Ramps send balls downhill."},
    {"ball": "Apple", "ball_pic": "🍎", "picture": "🍎", "question": "Which way will it roll?",
     "choices": ["Downhill", "Uphill"], "answer": "Downhill",
     "kid_tip": "An apple rolls down the grass hill.", "tip": "Round things roll downhill."},
    {"ball": "Toy car", "ball_pic": "🚗", "picture": "🚗", "question": "Which way will it not roll by itself?",
     "choices": ["Uphill", "Downhill"], "answer": "Uphill",
     "kid_tip": "A free-rolling car will not go uphill by itself.", "tip": "Down the hill, not up."},
    {"ball": "Ice chunk", "ball_pic": "🧊", "picture": "🧊", "question": "Which way will it roll?",
     "choices": ["Downhill", "Uphill"], "answer": "Downhill",
     "kid_tip": "An ice chunk slides downhill.", "tip": "Slippy ice still follows the slope down."},
    {"ball": "Orange", "ball_pic": "🍊", "picture": "🍊", "question": "Which way will it not roll by itself?",
     "choices": ["Uphill", "Downhill"], "answer": "Uphill",
     "kid_tip": "An orange will not roll up the hill by itself.", "tip": "Uphill needs a push."},
)


def run_who_went_farther() -> None:
    run_game({
        "id": "motion_intermediate_who_went_farther",
        "title": "Who Went Farther?",
        "tagline": "Which one went farther? Which one stopped sooner?",
        "question": "Which car went farther?",
        "choices": ["Blue car", "Red car"],
        "answer": "Red car",
        "picture": "🏁",
        "scene": "compare",
        "animate_mode": "once",
        "trials": flip_two_choice(
            FARTHER, a="a", b="b",
            q_for_a="Which one went farther?", q_for_b="Which one stopped sooner?",
            scene="compare",
        ),
        "kid_tip": "The red car stops farther from start.",
        "tip": "The red car ends farther from start.",
    })


def run_speeding_up() -> None:
    run_game({
        "id": "motion_intermediate_speeding_up",
        "title": "Speeding Up?",
        "tagline": "Watch the gaps. Speeding up or slowing down?",
        "question": "The gaps grow. What happens?",
        "choices": ["Speeding up", "Slowing down"],
        "answer": "Speeding up",
        "picture": "🚙",
        "scene": "speeding_up",
        "animate_mode": "once",
        "trials": step_trials(SPEED, "speeding_up"),
        "kid_tip": "Growing gaps mean the race car is speeding up.",
        "tip": "Growing gaps show increasing speed.",
    })


def run_which_way_does_it_roll() -> None:
    run_game({
        "id": "motion_intermediate_which_way_does_it_roll",
        "title": "Which Way Does It Roll?",
        "tagline": "Which way will it roll? Which way will it not?",
        "question": "Which way will it roll?",
        "choices": ["Downhill", "Uphill"],
        "answer": "Downhill",
        "picture": "⚽",
        "scene": "roll_downhill",
        "animate_mode": "once",
        "trials": step_trials(ROLL, "roll_downhill"),
        "kid_tip": "The soccer ball rolls downhill.",
        "tip": "Things roll downhill unless something stops them.",
    })
