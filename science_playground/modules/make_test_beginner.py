"""Three playable science games."""
from __future__ import annotations
import sys
from pathlib import Path
_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))
from pair_trials import named_trials
from science_utils import run_game

TOWERS = (
    {"a": "Wide bottom", "b": "Tiny bottom", "wide": "Wide bottom", "tiny": "Tiny bottom",
     "kid_tip": "The wide tower stays up. The tiny-bottom tower tips.",
     "tip": "A wide base helps a tower stay steady."},
    {"a": "Fat base", "b": "Skinny base", "wide": "Fat base", "tiny": "Skinny base",
     "kid_tip": "A fat base stays. A skinny base tips.",
     "tip": "A wider base is steadier."},
    {"a": "Big bottom blocks", "b": "Little bottom block", "wide": "Big bottom blocks", "tiny": "Little bottom block",
     "kid_tip": "Big bottom blocks hold. A little bottom block tips.",
     "tip": "More bottom support keeps a stack up."},
    {"a": "Wide cup tower", "b": "Pointy cup tower", "wide": "Wide cup tower", "tiny": "Pointy cup tower",
     "kid_tip": "The wide cups stay. The pointy stack tips.",
     "tip": "A wide stack of cups is steadier."},
    {"a": "Book stack, big book down", "b": "Book stack, tiny book down", "wide": "Big book down", "tiny": "Tiny book down",
     "kid_tip": "A big book on the bottom stays. A tiny book tips.",
     "tip": "Put the wide piece on the bottom."},
    {"a": "Wide box tower", "b": "Thin box tower", "wide": "Wide box tower", "tiny": "Thin box tower",
     "kid_tip": "Wide boxes stay. Thin boxes tip.",
     "tip": "Wide boxes make a steady tower."},
    {"a": "Pyramid stack", "b": "Upside-down pyramid", "wide": "Pyramid stack", "tiny": "Upside-down pyramid",
     "kid_tip": "A pyramid stays. Upside-down tips.",
     "tip": "A pyramid is wide at the bottom."},
    {"a": "Stool tower", "b": "Pencil tower", "wide": "Stool tower", "tiny": "Pencil tower",
     "kid_tip": "A stool is wide and stays. Pencils tip.",
     "tip": "A wide stool is steadier than pencils."},
    {"a": "Can stack, fat can down", "b": "Can stack, skinny can down", "wide": "Fat can down", "tiny": "Skinny can down",
     "kid_tip": "A fat can on the bottom stays.",
     "tip": "The biggest can belongs at the bottom."},
    {"a": "Sandcastle, wide walls", "b": "Sandcastle, skinny walls", "wide": "Wide walls", "tiny": "Skinny walls",
     "kid_tip": "Wide sand walls stay. Skinny walls fall.",
     "tip": "Wide walls help a sandcastle stay up."},
)

RAMPS = (
    {"a": "Ramp", "b": "Wall", "path": "Ramp", "block": "Wall",
     "kid_tip": "The ramp lets the car roll. The wall stops it.",
     "tip": "A ramp gives the car a sloping path."},
    {"a": "Slide", "b": "Fence", "path": "Slide", "block": "Fence",
     "kid_tip": "A slide lets it go down. A fence blocks it.",
     "tip": "A slide is a ramp. A fence is a wall."},
    {"a": "Hill path", "b": "Cliff wall", "path": "Hill path", "block": "Cliff wall",
     "kid_tip": "The hill path lets it roll. The cliff wall stops it.",
     "tip": "A sloping path helps. A wall blocks."},
    {"a": "Board ramp", "b": "Closed door", "path": "Board ramp", "block": "Closed door",
     "kid_tip": "A board ramp works. A closed door blocks.",
     "tip": "A board can be a ramp. A door can be a wall."},
    {"a": "Playground slide", "b": "Brick wall", "path": "Playground slide", "block": "Brick wall",
     "kid_tip": "The slide helps. The brick wall stops.",
     "tip": "Slides are ramps. Brick walls block."},
    {"a": "Driveway slope", "b": "Garage door", "path": "Driveway slope", "block": "Garage door",
     "kid_tip": "The slope lets a car roll. A closed garage door stops it.",
     "tip": "A slope is a ramp."},
    {"a": "Book ramp", "b": "Book wall", "path": "Book ramp", "block": "Book wall",
     "kid_tip": "A tilted book is a ramp. A standing book is a wall.",
     "tip": "Tilt a book to make a ramp."},
    {"a": "Cardboard ramp", "b": "Cardboard wall", "path": "Cardboard ramp", "block": "Cardboard wall",
     "kid_tip": "Tilted cardboard helps. Upright cardboard blocks.",
     "tip": "The same cardboard can be a ramp or a wall."},
    {"a": "Wedge", "b": "Block", "path": "Wedge", "block": "Block",
     "kid_tip": "A wedge is a little ramp. A block stands like a wall.",
     "tip": "A wedge slopes. A block does not."},
    {"a": "Downstairs", "b": "Closed gate", "path": "Downstairs", "block": "Closed gate",
     "kid_tip": "Stairs go down. A closed gate stops you.",
     "tip": "Stairs are a stepped ramp. A gate can block."},
)

HOLES = (
    {"a": "Circle", "b": "Square", "fits": "Circle", "misses": "Square",
     "kid_tip": "The circle fits the round hole. The square does not.",
     "tip": "The circle matches the round hole."},
    {"a": "Round cookie", "b": "Square cracker", "fits": "Round cookie", "misses": "Square cracker",
     "kid_tip": "A round cookie fits a round cutter.",
     "tip": "Matching shapes fit."},
    {"a": "Ball", "b": "Block", "fits": "Ball", "misses": "Block",
     "kid_tip": "A ball fits a round hole. A block does not.",
     "tip": "A ball is round like the hole."},
    {"a": "Coin", "b": "Ticket", "fits": "Coin", "misses": "Ticket",
     "kid_tip": "A coin fits a round slot. A ticket does not.",
     "tip": "The coin matches the round slot."},
    {"a": "Lid", "b": "Book", "fits": "Lid", "misses": "Book",
     "kid_tip": "A round lid fits a round jar.",
     "tip": "The lid matches the jar opening."},
    {"a": "Button", "b": "Stamp", "fits": "Button", "misses": "Stamp",
     "kid_tip": "A button fits a round hole. A stamp does not.",
     "tip": "The button is the matching shape."},
    {"a": "Orange", "b": "Box", "fits": "Orange", "misses": "Box",
     "kid_tip": "An orange is round like the hole.",
     "tip": "Round things fit round holes."},
    {"a": "Wheel", "b": "Crate", "fits": "Wheel", "misses": "Crate",
     "kid_tip": "A wheel is round. A crate is not.",
     "tip": "A wheel matches a round hole."},
    {"a": "Plate", "b": "Napkin", "fits": "Plate", "misses": "Napkin",
     "kid_tip": "A round plate matches a round sink hole cover.",
     "tip": "Matching shapes fit."},
    {"a": "Donut", "b": "Toast", "fits": "Donut", "misses": "Toast",
     "kid_tip": "A donut is round. Toast is square.",
     "tip": "The donut matches the round hole."},
)


def run_will_the_tower_fall() -> None:
    run_game({
        "id": "make_test_beginner_will_the_tower_fall",
        "title": "Will the Tower Fall?",
        "tagline": "Which tower will stay up? Which tower will fall?",
        "question": "Which tower will stay up?",
        "choices": ["Wide bottom", "Tiny bottom"],
        "answer": "Wide bottom",
        "picture": "🗼",
        "scene": "tower_fall",
        "animate_mode": "once",
        "trials": named_trials(
            TOWERS, "tower_fall",
            "Which tower will stay up?", "Which tower will fall?",
        ),
        "kid_tip": "The wide tower stays up. The tiny-bottom tower tips.",
        "tip": "A wide base helps a tower stay steady.",
    })


def run_ramp_or_wall() -> None:
    run_game({
        "id": "make_test_beginner_ramp_or_wall",
        "title": "Ramp or Wall?",
        "tagline": "Which helps the car roll down? Which stops it?",
        "question": "Which helps the car roll down?",
        "choices": ["Ramp", "Wall"],
        "answer": "Ramp",
        "picture": "🛝",
        "scene": "ramp_or_wall",
        "animate_mode": "once",
        "trials": named_trials(
            RAMPS, "ramp_or_wall",
            "Which helps it roll down?", "Which stops it?",
            picture="🛝",
        ),
        "kid_tip": "The ramp lets the car roll. The wall stops it.",
        "tip": "A ramp gives the car a sloping path.",
    })


def run_fit_the_hole() -> None:
    run_game({
        "id": "make_test_beginner_fit_the_hole",
        "title": "Fit the Hole",
        "tagline": "Which shape fits? Which shape does not?",
        "question": "Which shape fits the round hole?",
        "choices": ["Circle", "Square"],
        "answer": "Circle",
        "picture": "⭕",
        "scene": "fit_the_hole",
        "animate_mode": "once",
        "trials": named_trials(
            HOLES, "fit_the_hole",
            "Which shape fits the round hole?", "Which shape does not fit?",
            picture="⭕",
        ),
        "kid_tip": "The circle fits the round hole. The square does not.",
        "tip": "The circle matches the round hole.",
    })
