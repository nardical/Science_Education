"""Three playable science games."""
from __future__ import annotations
import sys
from pathlib import Path
_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))
from pair_trials import step_trials
from science_utils import run_game

FIRST_NEXT = (
    {
        "question": "First socks. What comes next?",
        "choices": ["Shoes", "Hat"], "answer": "Shoes",
        "first": "Socks", "next": "Shoes", "later": "Hat",
        "first_pic": "🧦", "next_pic": "👟", "later_pic": "🎩",
        "kid_tip": "Socks come before shoes.", "tip": "Socks come before shoes.",
        "picture": "🧦",
    },
    {
        "question": "First wash hands. What comes next?",
        "choices": ["Soap", "Boots"], "answer": "Soap",
        "first": "Wash", "next": "Soap", "later": "Boots",
        "first_pic": "🧼", "next_pic": "🧴", "later_pic": "👢",
        "kid_tip": "After you wash, use soap.", "tip": "Wash, then soap.",
        "picture": "🧼",
    },
    {
        "question": "First bread. What comes next?",
        "choices": ["Spread", "Pajamas"], "answer": "Spread",
        "first": "Bread", "next": "Spread", "later": "Pajamas",
        "first_pic": "🍞", "next_pic": "🧈", "later_pic": "👘",
        "kid_tip": "After bread comes the spread.", "tip": "Sandwich steps stay together.",
        "picture": "🍞",
    },
    {
        "question": "First toothpaste. What comes next?",
        "choices": ["Brush", "Drum"], "answer": "Brush",
        "first": "Paste", "next": "Brush", "later": "Drum",
        "first_pic": "🦷", "next_pic": "🪥", "later_pic": "🥁",
        "kid_tip": "After toothpaste, you brush.", "tip": "Paste then brush.",
        "picture": "🪥",
    },
    {
        "question": "First seeds. What comes next?",
        "choices": ["Water", "Balloon"], "answer": "Water",
        "first": "Seeds", "next": "Water", "later": "Balloon",
        "first_pic": "🌱", "next_pic": "💧", "later_pic": "🎈",
        "kid_tip": "Seeds need water next.", "tip": "Plant, then water.",
        "picture": "🌱",
    },
    {
        "question": "First coat. What comes next?",
        "choices": ["Zip", "Ice cream"], "answer": "Zip",
        "first": "Coat", "next": "Zip", "later": "Ice cream",
        "first_pic": "🧥", "next_pic": "🔐", "later_pic": "🍦",
        "kid_tip": "After the coat, zip it.", "tip": "Put on the coat, then zip.",
        "picture": "🧥",
    },
    {
        "question": "First bowl. What comes next?",
        "choices": ["Cereal", "Hammer"], "answer": "Cereal",
        "first": "Bowl", "next": "Cereal", "later": "Hammer",
        "first_pic": "🥣", "next_pic": "🥣", "later_pic": "🔨",
        "kid_tip": "After the bowl comes cereal.", "tip": "Bowl, then cereal.",
        "picture": "🥣",
    },
    {
        "question": "First sit in the car. What comes next?",
        "choices": ["Seatbelt", "Paint"], "answer": "Seatbelt",
        "first": "Sit", "next": "Seatbelt", "later": "Paint",
        "first_pic": "🚗", "next_pic": "🚗", "later_pic": "🎨",
        "first_art": "car-seat", "next_art": "seatbelt",
        "kid_tip": "After you sit in the car, put on the seatbelt.",
        "tip": "Sit, then click the seatbelt.",
        "picture": "🚗",
    },
    {
        "question": "First wet hair. What comes next?",
        "choices": ["Shampoo", "Skateboard"], "answer": "Shampoo",
        "first": "Wet hair", "next": "Shampoo", "later": "Skateboard",
        "first_pic": "🚿", "next_pic": "🧴", "later_pic": "🛹",
        "kid_tip": "After wet hair comes shampoo.", "tip": "Wet, then shampoo.",
        "picture": "🚿",
    },
    {
        "question": "First paper. What comes next?",
        "choices": ["Draw", "Sleep"], "answer": "Draw",
        "first": "Paper", "next": "Draw", "later": "Sleep",
        "first_pic": "📄", "next_pic": "✏️", "later_pic": "😴",
        "kid_tip": "After paper, you can draw.", "tip": "Paper, then draw.",
        "picture": "✏️",
    },
)

MISSING = (
    {"question": "Wash, dry, then what?", "choices": ["Put away", "Make muddy"], "answer": "Put away",
     "one": "Wash", "two": "Dry", "missing": "Put away", "one_pic": "🧼", "two_pic": "💨", "missing_pic": "🧺",
     "kid_tip": "Put it away after it is dry.", "tip": "Put it away after it is dry.", "picture": "🧼"},
    {"question": "Pour, sip, then what?", "choices": ["Wash cup", "Throw cup far"], "answer": "Wash cup",
     "one": "Pour", "two": "Sip", "missing": "Wash cup", "one_pic": "🥛", "two_pic": "😋", "missing_pic": "🧽",
     "kid_tip": "After a drink, wash the cup.", "tip": "Finish the job: wash the cup.", "picture": "🥛"},
    {"question": "Open, look, then what?", "choices": ["Close", "Hide book"], "answer": "Close",
     "one": "Open", "two": "Look", "missing": "Close", "one_pic": "📖", "two_pic": "👀", "missing_pic": "📕",
     "kid_tip": "After you look, close the book.", "tip": "Open, look, close.", "picture": "📖"},
    {"question": "Plant, water, then what?", "choices": ["Give light", "Stomp it"], "answer": "Give light",
     "one": "Plant", "two": "Water", "missing": "Light", "one_pic": "🌱", "two_pic": "💧", "missing_pic": "☀️",
     "kid_tip": "A plant also needs light.", "tip": "Plant, water, light.", "picture": "🌱"},
    {"question": "Soap, rinse, then what?", "choices": ["Dry hands", "Play in mud"], "answer": "Dry hands",
     "one": "Soap", "two": "Rinse", "missing": "Dry", "one_pic": "🧴", "two_pic": "💧", "missing_pic": "🧻",
     "kid_tip": "After rinse, dry your hands.", "tip": "Soap, rinse, dry.", "picture": "🧴"},
    {"question": "Mix, pour, then what?", "choices": ["Bake", "Freeze the oven"], "answer": "Bake",
     "one": "Mix", "two": "Pour", "missing": "Bake", "one_pic": "🥣", "two_pic": "🧁", "missing_pic": "🔥",
     "kid_tip": "After you pour, bake.", "tip": "Mix, pour, bake.", "picture": "🧁"},
    {"question": "Brush, rinse, then what?", "choices": ["Put brush away", "Eat the brush"], "answer": "Put brush away",
     "one": "Brush", "two": "Rinse", "missing": "Put away", "one_pic": "🪥", "two_pic": "💧", "missing_pic": "🧺",
     "kid_tip": "Put the brush away when you finish.", "tip": "Brush, rinse, put away.", "picture": "🪥"},
    {"question": "Build, test, then what?", "choices": ["Fix", "Give up"], "answer": "Fix",
     "one": "Build", "two": "Test", "missing": "Fix", "one_pic": "🧱", "two_pic": "🔬", "missing_pic": "🛠️",
     "kid_tip": "After a test, you can fix it.", "tip": "Build, test, fix.", "picture": "🛠️"},
    {"question": "On, ride, then what?", "choices": ["Helmet off last", "Helmet off first"], "answer": "Helmet off last",
     "one": "Helmet on", "two": "Ride", "missing": "Helmet off", "one_pic": "⛑️", "two_pic": "🚲", "missing_pic": "🏠",
     "kid_tip": "Take the helmet off after the ride.", "tip": "Helmet on, ride, then off.", "picture": "🚲"},
    {"question": "Night, sleep, then what?", "choices": ["Wake", "Stay asleep all day"], "answer": "Wake",
     "one": "Night", "two": "Sleep", "missing": "Wake", "one_pic": "🌙", "two_pic": "😴", "missing_pic": "☀️",
     "kid_tip": "After sleep comes waking up.", "tip": "Night, sleep, wake.", "picture": "😴"},
)

AGAIN = (
    {"question": "Repeat means what?", "choices": ["Do it again", "Stop forever"], "answer": "Do it again",
     "action": "Clap", "action_pic": "👏", "kid_tip": "Repeat means do the step again.", "tip": "Repeat means do the step again.", "picture": "🔁"},
    {"question": "The song says again. What do you do?", "choices": ["Sing it again", "Leave the room"], "answer": "Sing it again",
     "action": "Sing", "action_pic": "🎤", "kid_tip": "Again means sing it once more.", "tip": "Again means one more time.", "picture": "🎤"},
    {"question": "The teacher says do it again. What happens?", "choices": ["Try the step once more", "Never try"], "answer": "Try the step once more",
     "action": "Jump", "action_pic": "🦘", "kid_tip": "Do the jump again.", "tip": "Again means another try.", "picture": "🦘"},
    {"question": "A loop in a game repeats. What does that mean?", "choices": ["The step happens more times", "The game deletes itself"], "answer": "The step happens more times",
     "action": "Tap", "action_pic": "👆", "kid_tip": "A loop does the tap again.", "tip": "A loop repeats a step.", "picture": "👆"},
    {"question": "Stir again means what?", "choices": ["Stir one more time", "Throw the spoon"], "answer": "Stir one more time",
     "action": "Stir", "action_pic": "🥄", "kid_tip": "Stir once more.", "tip": "Again adds one more stir.", "picture": "🥄"},
    {"question": "Hop again means what?", "choices": ["Hop once more", "Sit forever"], "answer": "Hop once more",
     "action": "Hop", "action_pic": "🐰", "kid_tip": "Hop one more time.", "tip": "Again means one more hop.", "picture": "🐰"},
    {"question": "Read it again means what?", "choices": ["Read the page once more", "Close the book forever"], "answer": "Read the page once more",
     "action": "Read", "action_pic": "📖", "kid_tip": "Read it one more time.", "tip": "Again means another read.", "picture": "📖"},
    {"question": "Push again means what?", "choices": ["Push one more time", "Walk away"], "answer": "Push one more time",
     "action": "Push", "action_pic": "🫷", "kid_tip": "Give one more push.", "tip": "Again means another push.", "picture": "🫷"},
    {"question": "The dance says repeat. What do you do?", "choices": ["Do the move again", "Freeze forever"], "answer": "Do the move again",
     "action": "Dance", "action_pic": "💃", "kid_tip": "Do the dance move again.", "tip": "Repeat the move.", "picture": "💃"},
    {"question": "Count again means what?", "choices": ["Count once more", "Forget numbers"], "answer": "Count once more",
     "action": "Count", "action_pic": "🔢", "kid_tip": "Count one more time.", "tip": "Again means another count.", "picture": "🔢"},
)


def run_first_then_next() -> None:
    run_game({
        "id": "follow_the_steps_beginner_first_then_next",
        "title": "First Then Next",
        "tagline": "First this. What comes next?",
        "question": "First socks. What comes next?",
        "choices": ["Shoes", "Hat"],
        "answer": "Shoes",
        "picture": "🧦",
        "scene": "first_then_next",
        "animate_mode": "once",
        "trials": step_trials(FIRST_NEXT, "first_then_next"),
        "kid_tip": "Socks come before shoes.",
        "tip": "Socks come before shoes.",
    })


def run_which_step_is_missing() -> None:
    run_game({
        "id": "follow_the_steps_beginner_which_step_is_missing",
        "title": "Which Step Is Missing?",
        "tagline": "What step finishes the job?",
        "question": "Wash, dry, then what?",
        "choices": ["Put away", "Make muddy"],
        "answer": "Put away",
        "picture": "🧼",
        "scene": "missing_step",
        "animate_mode": "once",
        "trials": step_trials(MISSING, "missing_step"),
        "kid_tip": "Put it away after it is dry.",
        "tip": "Put it away after it is dry.",
    })


def run_do_it_again() -> None:
    run_game({
        "id": "follow_the_steps_beginner_do_it_again",
        "title": "Do It Again",
        "tagline": "Repeat means do it again.",
        "question": "Repeat means what?",
        "choices": ["Do it again", "Stop forever"],
        "answer": "Do it again",
        "picture": "🔁",
        "scene": "do_it_again",
        "animate_mode": "once",
        "trials": step_trials(AGAIN, "do_it_again"),
        "kid_tip": "Repeat means do the step again.",
        "tip": "Repeat means do the step again.",
    })
