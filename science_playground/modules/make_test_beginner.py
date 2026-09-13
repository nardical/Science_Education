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
     "tower_kind": "blocks",
     "kid_tip": "The wide tower stays up. The tiny-bottom tower tips.",
     "tip": "A wide base helps a tower stay steady."},
    {"a": "Wide cups", "b": "Pointy cups", "wide": "Wide cups", "tiny": "Pointy cups",
     "tower_kind": "cups",
     "kid_tip": "The wide cups stay. The pointy stack tips.",
     "tip": "A wide stack of cups is steadier."},
    {"a": "Big book down", "b": "Tiny book down", "wide": "Big book down", "tiny": "Tiny book down",
     "tower_kind": "books",
     "kid_tip": "A big book on the bottom stays. A tiny book tips.",
     "tip": "Put the wide book on the bottom."},
    {"a": "Wide boxes", "b": "Thin boxes", "wide": "Wide boxes", "tiny": "Thin boxes",
     "tower_kind": "boxes",
     "kid_tip": "Wide boxes stay. Thin boxes tip.",
     "tip": "Wide boxes make a steady tower."},
    {"a": "Pyramid stack", "b": "Upside-down pyramid", "wide": "Pyramid stack", "tiny": "Upside-down pyramid",
     "tower_kind": "pyramid",
     "kid_tip": "A pyramid stays. Upside-down tips.",
     "tip": "A pyramid is wide at the bottom."},
    {"a": "Fat can down", "b": "Skinny can down", "wide": "Fat can down", "tiny": "Skinny can down",
     "tower_kind": "cans",
     "kid_tip": "A fat can on the bottom stays.",
     "tip": "The biggest can belongs at the bottom."},
    {"a": "Wide sandcastle", "b": "Skinny sandcastle", "wide": "Wide sandcastle", "tiny": "Skinny sandcastle",
     "tower_kind": "sand",
     "kid_tip": "Wide sand walls stay. Skinny walls fall.",
     "tip": "Wide walls help a sandcastle stay up."},
    {"a": "Stool tower", "b": "Pencil tower", "wide": "Stool tower", "tiny": "Pencil tower",
     "tower_kind": "stool",
     "kid_tip": "A stool is wide and stays. Pencils tip.",
     "tip": "A wide stool is steadier than pencils."},
    {"a": "Fat pillows", "b": "Skinny pillows", "wide": "Fat pillows", "tiny": "Skinny pillows",
     "tower_kind": "pillows",
     "kid_tip": "Fat pillows make a steady stack. Skinny pillows tip.",
     "tip": "A wide soft stack stays up better."},
    {"a": "Wide rock pile", "b": "Skinny rock pile", "wide": "Wide rock pile", "tiny": "Skinny rock pile",
     "tower_kind": "stones",
     "kid_tip": "A wide rock pile stays. A skinny pile tips.",
     "tip": "A wide pile of rocks is steadier."},
)

RAMPS = (
    {"a": "Ramp", "b": "Wall", "path": "Ramp", "block": "Wall",
     "ramp_kind": "board",
     "kid_tip": "The ramp lets the car roll. The wall stops it.",
     "tip": "A ramp gives the car a sloping path."},
    {"a": "Slide", "b": "Fence", "path": "Slide", "block": "Fence",
     "ramp_kind": "slide",
     "kid_tip": "A slide lets it go down. A fence blocks it.",
     "tip": "A slide is a ramp. A fence is a wall."},
    {"a": "Hill path", "b": "Cliff wall", "path": "Hill path", "block": "Cliff wall",
     "ramp_kind": "hill",
     "kid_tip": "The hill path lets it roll. The cliff wall stops it.",
     "tip": "A sloping path helps. A wall blocks."},
    {"a": "Board ramp", "b": "Closed door", "path": "Board ramp", "block": "Closed door",
     "ramp_kind": "door",
     "kid_tip": "A board ramp works. A closed door blocks.",
     "tip": "A board can be a ramp. A door can be a wall."},
    {"a": "Playground slide", "b": "Brick wall", "path": "Playground slide", "block": "Brick wall",
     "ramp_kind": "playground",
     "kid_tip": "The slide helps. The brick wall stops.",
     "tip": "Slides are ramps. Brick walls block."},
    {"a": "Driveway slope", "b": "Garage door", "path": "Driveway slope", "block": "Garage door",
     "ramp_kind": "driveway",
     "kid_tip": "The slope lets a car roll. A closed garage door stops it.",
     "tip": "A slope is a ramp."},
    {"a": "Book ramp", "b": "Book wall", "path": "Book ramp", "block": "Book wall",
     "ramp_kind": "book",
     "kid_tip": "A tilted book is a ramp. A standing book is a wall.",
     "tip": "Tilt a book to make a ramp."},
    {"a": "Cardboard ramp", "b": "Cardboard wall", "path": "Cardboard ramp", "block": "Cardboard wall",
     "ramp_kind": "cardboard",
     "kid_tip": "Tilted cardboard helps. Upright cardboard blocks.",
     "tip": "The same cardboard can be a ramp or a wall."},
    {"a": "Wedge", "b": "Block", "path": "Wedge", "block": "Block",
     "ramp_kind": "wedge",
     "kid_tip": "A wedge is a little ramp. A block stands like a wall.",
     "tip": "A wedge slopes. A block does not."},
    {"a": "Downstairs", "b": "Closed gate", "path": "Downstairs", "block": "Closed gate",
     "ramp_kind": "stairs",
     "kid_tip": "Stairs go down. A closed gate stops you.",
     "tip": "Stairs are a stepped ramp. A gate can block."},
)

HOLES = (
    {"a": "Circle", "b": "Square", "hole": "circle",
     "round_art": "circle", "square_art": "square",
     "kid_tip": "The circle fits the round hole. The square does not.",
     "tip": "The circle matches the round hole."},
    {"a": "Round cookie", "b": "Square cracker", "hole": "square",
     "round_art": "cookie", "square_art": "cracker",
     "kid_tip": "A square cracker fits a square cutter. A round cookie does not.",
     "tip": "The cracker matches the square hole."},
    {"a": "Ball", "b": "Block", "hole": "square",
     "round_art": "ball", "square_art": "block",
     "kid_tip": "A block fits a square hole. A ball does not.",
     "tip": "The block matches the square hole."},
    {"a": "Coin", "b": "Ticket", "hole": "circle",
     "round_art": "coin", "square_art": "ticket",
     "kid_tip": "A coin fits a round slot. A ticket does not.",
     "tip": "The coin matches the round slot."},
    {"a": "Lid", "b": "Book", "hole": "square",
     "round_art": "lid", "square_art": "book",
     "kid_tip": "A book fits a square hole. A round lid does not.",
     "tip": "The book matches the square hole."},
    {"a": "Button", "b": "Stamp", "hole": "circle",
     "round_art": "button", "square_art": "stamp",
     "kid_tip": "A button fits a round hole. A stamp does not.",
     "tip": "The button is the matching shape."},
    {"a": "Orange", "b": "Box", "hole": "circle",
     "round_art": "orange", "square_art": "box",
     "kid_tip": "An orange is round like the hole.",
     "tip": "Round things fit round holes."},
    {"a": "Wheel", "b": "Crate", "hole": "square",
     "round_art": "wheel", "square_art": "crate",
     "kid_tip": "A crate fits a square hole. A wheel does not.",
     "tip": "The crate matches the square hole."},
    {"a": "Plate", "b": "Napkin", "hole": "square",
     "round_art": "plate", "square_art": "napkin",
     "kid_tip": "A folded napkin fits a square hole. A round plate does not.",
     "tip": "The napkin matches the square hole."},
    {"a": "Donut", "b": "Toast", "hole": "circle",
     "round_art": "donut", "square_art": "toast",
     "kid_tip": "A donut is round. Toast is square.",
     "tip": "The donut matches the round hole."},
)


def hole_trials() -> tuple:
    trials = []
    for i, row in enumerate(HOLES):
        hole = str(row.get("hole") or "circle")
        round_name, square_name = str(row["a"]), str(row["b"])
        if hole == "square":
            fits, misses = square_name, round_name
            q_fits = "Which shape fits the square hole?"
        else:
            fits, misses = round_name, square_name
            q_fits = "Which shape fits the round hole?"
        ask_fits = i % 2 == 0
        trial = dict(row)
        trial.update({
            "scene": "fit_the_hole",
            "fits": fits,
            "misses": misses,
            "question": q_fits if ask_fits else "Which shape does not fit?",
            "choices": [round_name, square_name],
            "answer": fits if ask_fits else misses,
            "picture": "⬜" if hole == "square" else "⭕",
        })
        trials.append(trial)
    return tuple(trials)


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
        "animate_mode": "on_answer",
        "anim_seconds": 1.6,
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
        "animate_mode": "on_answer",
        "anim_seconds": 1.7,
        "trials": named_trials(
            RAMPS, "ramp_or_wall",
            "Which helps it roll down?", "Which stops it?",
            picture="🛝",
        ),
        "kid_tip": "The ramp lets the car roll. The wall stops it.",
        "tip": "A ramp gives the car a sloping path.",
    })


def run_fit_the_hole() -> None:
    trials = hole_trials()
    first = trials[0]
    run_game({
        "id": "make_test_beginner_fit_the_hole",
        "title": "Fit the Hole",
        "tagline": "Which shape fits? Which shape does not?",
        "question": first["question"],
        "choices": list(first["choices"]),
        "answer": first["answer"],
        "picture": "⭕",
        "scene": "fit_the_hole",
        "animate_mode": "on_answer",
        "anim_seconds": 1.5,
        "trials": trials,
        "kid_tip": first["kid_tip"],
        "tip": first["tip"],
    })
