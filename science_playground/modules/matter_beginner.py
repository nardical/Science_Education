"""Three playable science games."""
from __future__ import annotations
import sys
from pathlib import Path
_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))
from pair_trials import flip_two_choice
from science_utils import run_game

SOLID_SPLASH = (
    {"a": "Water", "b": "Wood block", "a_pic": "💦", "b_pic": "🧱", "a_move": "splash", "b_move": "still",
     "kid_tip": "Water can splash. The wood block keeps its shape.", "tip": "A liquid can splash. A solid holds shape."},
    {"a": "Juice", "b": "Rock", "a_pic": "🧃", "b_pic": "🪨", "a_move": "splash", "b_move": "still",
     "kid_tip": "Juice can splash. The rock does not.", "tip": "Juice is a liquid. A rock is a solid."},
    {"a": "Milk", "b": "Cup", "a_pic": "🥛", "b_pic": "🥤", "a_move": "splash", "b_move": "still",
     "kid_tip": "Milk can splash. The cup holds shape.", "tip": "Milk is a liquid. The cup is a solid."},
    {"a": "Rain", "b": "Brick", "a_pic": "🌧️", "b_pic": "🧱", "a_move": "splash", "b_move": "still",
     "kid_tip": "Rain can splash. A brick does not.", "tip": "Rain is liquid water. A brick is solid."},
    {"a": "Puddle", "b": "Stick", "a_pic": "💧", "b_pic": "🪵", "a_move": "splash", "b_move": "still",
     "kid_tip": "A puddle can splash. A stick keeps its shape.", "tip": "Puddles are liquid. Sticks are solid."},
    {"a": "Soap water", "b": "Soap bar", "a_pic": "🫧", "b_pic": "🧼", "a_move": "splash", "b_move": "still",
     "kid_tip": "Soapy water splashes. The bar holds shape.", "tip": "The water is liquid. The bar is solid."},
    {"a": "Paint", "b": "Crayon", "a_pic": "🎨", "b_pic": "🖍️", "a_move": "splash", "b_move": "still",
     "kid_tip": "Paint can splash. A crayon does not.", "tip": "Paint is a liquid. A crayon is a solid."},
    {"a": "Ocean", "b": "Shell", "a_pic": "🌊", "b_pic": "🐚", "a_move": "splash", "b_move": "still",
     "kid_tip": "Ocean water splashes. A shell holds shape.", "tip": "The ocean is liquid. A shell is solid."},
    {"a": "Tea", "b": "Spoon", "a_pic": "🍵", "b_pic": "🥄", "a_move": "splash", "b_move": "still",
     "kid_tip": "Tea can splash. A spoon does not.", "tip": "Tea is a liquid. A spoon is a solid."},
    {"a": "Honey", "b": "Jar", "a_pic": "🍯", "b_pic": "🫙", "a_move": "splash", "b_move": "still",
     "kid_tip": "Honey can drip and splash. The jar holds shape.", "tip": "Honey is a thick liquid. The jar is solid."},
)

HOT_COLD = (
    {"a": "Ice cube", "b": "Warm soup", "a_pic": "🧊", "b_pic": "🍲", "a_move": "shiver", "b_move": "steam",
     "kid_tip": "Ice feels cold. Soup feels hot.", "tip": "Ice is cold. Soup is hot."},
    {"a": "Snowball", "b": "Hot cocoa", "a_pic": "❄️", "b_pic": "☕", "a_move": "shiver", "b_move": "steam",
     "kid_tip": "Snow is cold. Cocoa is hot.", "tip": "Snow is cold. Cocoa is hot."},
    {"a": "Popsicle", "b": "Toast", "a_pic": "🍭", "b_pic": "🍞", "a_move": "shiver", "b_move": "steam",
     "kid_tip": "A popsicle is cold. Toast is warm.", "tip": "A popsicle is cold. Toast is hot from the toaster."},
    {"a": "Ice cream", "b": "Pizza", "a_pic": "🍦", "b_pic": "🍕", "a_move": "shiver", "b_move": "steam",
     "kid_tip": "Ice cream is cold. Pizza is hot.", "tip": "Ice cream is kept cold. Pizza comes out hot."},
    {"a": "Frozen peas", "b": "Baked potato", "a_pic": "🟢", "b_pic": "🥔", "a_move": "shiver", "b_move": "steam",
     "kid_tip": "Frozen peas are cold. A baked potato is hot.", "tip": "The freezer makes food cold. The oven makes it hot."},
    {"a": "Cold water", "b": "Hot tea", "a_pic": "🚰", "b_pic": "🍵", "a_move": "shiver", "b_move": "steam",
     "kid_tip": "This water is cold. Tea is hot.", "tip": "Cold water feels chilly. Tea is heated."},
    {"a": "Ice pack", "b": "Warm bath", "a_pic": "🧊", "b_pic": "🛁", "a_move": "shiver", "b_move": "steam",
     "kid_tip": "An ice pack is cold. A bath can be warm.", "tip": "Ice packs are cold on purpose. Baths are warmed."},
    {"a": "Winter wind", "b": "Campfire", "a_pic": "🌬️", "b_pic": "🔥", "a_move": "shiver", "b_move": "steam",
     "kid_tip": "Winter wind is cold. A campfire is hot.", "tip": "Wind in winter feels cold. Fire is hot."},
    {"a": "Fridge", "b": "Oven", "a_pic": "🧊", "b_pic": "🔥", "a_move": "shiver", "b_move": "steam",
     "kid_tip": "A fridge is cold inside. An oven is hot.", "tip": "Fridges keep food cold. Ovens heat food."},
    {"a": "Shade", "b": "Sunny sidewalk", "a_pic": "🌳", "b_pic": "☀️", "a_move": "still", "b_move": "steam",
     "kid_tip": "Shade feels cooler. A sunny sidewalk can feel hot.", "tip": "Sun can heat the ground. Shade is cooler."},
)


MELT_FREEZE = (
    {"stuff": "Ice", "stuff_pic": "🧊", "action": "melt", "question": "Ice warms. What happens?",
     "choices": ["Melt", "Freeze"], "answer": "Melt",
     "kid_tip": "Warm ice melts into water.", "tip": "Heating ice turns it into liquid water."},
    {"stuff": "Puddle", "stuff_pic": "💧", "action": "freeze", "question": "A puddle gets very cold. What happens?",
     "choices": ["Freeze", "Melt"], "answer": "Freeze",
     "kid_tip": "A very cold puddle can freeze.", "tip": "Cooling water can turn it into ice."},
    {"stuff": "Chocolate", "stuff_pic": "🍫", "action": "melt", "question": "Chocolate gets warm. What happens?",
     "choices": ["Melt", "Freeze"], "answer": "Melt",
     "kid_tip": "Warm chocolate gets soft and melts.", "tip": "Heat can melt chocolate."},
    {"stuff": "Juice", "stuff_pic": "🧃", "action": "freeze", "question": "Juice sits in a freezer. What happens?",
     "choices": ["Freeze", "Melt"], "answer": "Freeze",
     "kid_tip": "Freezer juice can freeze into a pop.", "tip": "A freezer can freeze juice."},
    {"stuff": "Butter", "stuff_pic": "🧈", "action": "melt", "question": "Butter sits in a warm pan. What happens?",
     "choices": ["Melt", "Freeze"], "answer": "Melt",
     "kid_tip": "Warm butter melts.", "tip": "Heat melts butter."},
    {"stuff": "Ice cube tray", "stuff_pic": "🧊", "action": "freeze", "question": "Water sits in the freezer. What happens?",
     "choices": ["Freeze", "Melt"], "answer": "Freeze",
     "kid_tip": "The water freezes into cubes.", "tip": "Cold turns water into ice."},
    {"stuff": "Snowman", "stuff_pic": "⛄", "action": "melt", "question": "The sun shines on a snowman. What happens?",
     "choices": ["Melt", "Freeze"], "answer": "Melt",
     "kid_tip": "Sun can melt the snowman.", "tip": "Warmth melts snow."},
    {"stuff": "Pond", "stuff_pic": "🏞️", "action": "freeze", "question": "A winter night gets very cold. What happens to the pond?",
     "choices": ["Freeze", "Melt"], "answer": "Freeze",
     "kid_tip": "A very cold pond can freeze.", "tip": "Cold can freeze pond water."},
    {"stuff": "Ice cream", "stuff_pic": "🍦", "action": "melt", "question": "Ice cream sits in the sun. What happens?",
     "choices": ["Melt", "Freeze"], "answer": "Melt",
     "kid_tip": "Sun-warmed ice cream melts.", "tip": "Heat melts ice cream."},
    {"stuff": "Wet gloves", "stuff_pic": "🧤", "action": "freeze", "question": "Wet gloves stay outside in the snow. What happens?",
     "choices": ["Freeze", "Melt"], "answer": "Freeze",
     "kid_tip": "The wet gloves can freeze stiff.", "tip": "Cold can freeze the water in the gloves."},
)


def run_solid_or_splash() -> None:
    run_game({
        "id": "matter_beginner_solid_or_splash",
        "title": "Solid or Splash",
        "tagline": "Which one can splash? Which one holds its shape?",
        "question": "Which one can splash?",
        "choices": ["Wood block", "Water"],
        "answer": "Water",
        "picture": "💦",
        "scene": "solid_or_splash",
        "animate_mode": "once",
        "trials": flip_two_choice(
            SOLID_SPLASH, a="a", b="b",
            q_for_a="Which one can splash?", q_for_b="Which one holds its shape?",
            scene="solid_or_splash",
        ),
        "kid_tip": "Water can splash. The wood block keeps its shape.",
        "tip": "A liquid can splash. A solid holds shape.",
    })


def run_hot_or_cold() -> None:
    run_game({
        "id": "matter_beginner_hot_or_cold",
        "title": "Hot or Cold",
        "tagline": "Which one feels cold? Which one feels hot?",
        "question": "Which one feels cold?",
        "choices": ["Ice cube", "Warm soup"],
        "answer": "Ice cube",
        "picture": "🧊",
        "scene": "hot_or_cold",
        "animate_mode": "once",
        "trials": flip_two_choice(
            HOT_COLD, a="a", b="b",
            q_for_a="Which one feels cold?", q_for_b="Which one feels hot?",
            scene="hot_or_cold",
        ),
        "kid_tip": "Ice feels cold. Soup feels hot.",
        "tip": "Ice is cold. Soup is hot.",
    })


def run_melt_or_freeze() -> None:
    trials = []
    for row in MELT_FREEZE:
        trial = dict(row)
        trial["scene"] = "melt_or_freeze"
        trial["picture"] = row["stuff_pic"]
        trials.append(trial)
    run_game({
        "id": "matter_beginner_melt_or_freeze",
        "title": "Melt or Freeze",
        "tagline": "Warm can melt. Cold can freeze.",
        "question": "Ice warms. What happens?",
        "choices": ["Melt", "Freeze"],
        "answer": "Melt",
        "picture": "🌡️",
        "scene": "melt_or_freeze",
        "animate_mode": "once",
        "trials": tuple(trials),
        "kid_tip": "Warm ice melts into water.",
        "tip": "Heating ice turns it into liquid water.",
    })
