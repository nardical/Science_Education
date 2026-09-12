"""Matter — Advanced: 10 picture pairs per game."""
from __future__ import annotations
import sys
from pathlib import Path
_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))
from pair_trials import compare_game

CYCLE = (
    {"a": "Water vapor rises", "b": "Ice forms", "a_pic": "♨️", "b_pic": "🧊", "a_move": "steam", "b_move": "still",
     "kid_tip": "A warm puddle can become vapor and rise. Ice needs cold.",
     "tip": "Warm water can become vapor and rise."},
    {"a": "Steam from a kettle", "b": "Snow from a freezer", "a_pic": "♨️", "b_pic": "❄️", "a_move": "steam", "b_move": "shiver",
     "kid_tip": "A warm kettle makes vapor. A freezer makes ice.",
     "tip": "Warm puddles can become vapor and rise."},
    {"a": "Wet sidewalk in sun", "b": "Wet sidewalk in freeze", "a_pic": "☀️", "b_pic": "❄️", "a_move": "steam", "b_move": "still",
     "kid_tip": "Sun dries a sidewalk as vapor. Freeze would make ice.",
     "tip": "Warm water can become vapor."},
    {"a": "Puddle on a warm plate", "b": "Puddle in a snowbank", "a_pic": "🍽️", "b_pic": "⛄", "a_move": "steam", "b_move": "shiver",
     "kid_tip": "A warm plate lets the puddle rise as vapor.",
     "tip": "Heat can turn water into vapor."},
    {"a": "Rain cloud forming", "b": "Ice cube tray", "a_pic": "☁️", "b_pic": "🧊", "a_move": "steam", "b_move": "still",
     "kid_tip": "Warm vapor can make a cloud. A tray makes ice.",
     "tip": "Vapor can rise and make clouds."},
    {"a": "Wet spoon in sun", "b": "Wet spoon in snow", "a_pic": "🥄", "b_pic": "❄️", "a_move": "steam", "b_move": "shiver",
     "kid_tip": "Sun dries the spoon. Snow keeps it icy.",
     "tip": "Warmth can dry water as vapor."},
    {"a": "Tea steam", "b": "Frozen tea pop", "a_pic": "🍵", "b_pic": "🍭", "a_move": "steam", "b_move": "still",
     "kid_tip": "Hot tea makes vapor. A freezer makes a pop.",
     "tip": "Warm water can become vapor."},
    {"a": "Bath steam", "b": "Ice bath", "a_pic": "🛁", "b_pic": "🧊", "a_move": "steam", "b_move": "shiver",
     "kid_tip": "A warm bath makes vapor.", "tip": "Warm water rises as vapor."},
    {"a": "Drying shirt", "b": "Frozen shirt", "a_pic": "👕", "b_pic": "❄️", "a_move": "steam", "b_move": "still",
     "kid_tip": "A warm day dries a shirt as vapor.", "tip": "Water can leave as vapor."},
    {"a": "Lake in summer sun", "b": "Lake in deep freeze", "a_pic": "🏞️", "b_pic": "🧊", "a_move": "steam", "b_move": "still",
     "kid_tip": "Summer sun can lift vapor. Deep freeze makes ice.",
     "tip": "Warm puddles can become vapor and rise."},
)

HARD = (
    {"a": "Baked clay", "b": "Wet clay", "a_pic": "🏺", "b_pic": "🥣", "a_move": "still", "b_move": "splash",
     "kid_tip": "Baked clay gets harder. Wet clay stays soft.",
     "tip": "Heating can make clay hard."},
    {"a": "Cookie from oven", "b": "Cookie dough", "a_pic": "🍪", "b_pic": "🥣", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "Oven heat makes the cookie firmer.", "tip": "Heating can make some stuff harder."},
    {"a": "Toast", "b": "Soft bread", "a_pic": "🍞", "b_pic": "🥖", "a_move": "steam", "b_move": "still",
     "kid_tip": "Toast is firmer after heat.", "tip": "Heat can change how food feels."},
    {"a": "Dried mud brick", "b": "Mud puddle", "a_pic": "🧱", "b_pic": "🟤", "a_move": "still", "b_move": "splash",
     "kid_tip": "Dried mud is harder.", "tip": "Drying and heat can harden mud."},
    {"a": "Hard pretzel", "b": "Soft dough", "a_pic": "🥨", "b_pic": "🫓", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "A baked pretzel is harder.", "tip": "Baking can harden dough."},
    {"a": "Crisp bacon", "b": "Raw strip", "a_pic": "🥓", "b_pic": "🥩", "a_move": "steam", "b_move": "still",
     "kid_tip": "Heat makes it crisp.", "tip": "Heating can make some food firmer."},
    {"a": "Baked pizza crust", "b": "Raw dough ball", "a_pic": "🍕", "b_pic": "⚪", "a_move": "steam", "b_move": "wiggle",
     "kid_tip": "The baked crust is harder.", "tip": "Heat can harden dough."},
    {"a": "Dry sponge left out", "b": "Soaking sponge", "a_pic": "🧽", "b_pic": "💧", "a_move": "still", "b_move": "splash",
     "kid_tip": "A dry sponge is firmer.", "tip": "Water can make it softer."},
    {"a": "Hard candy after cool", "b": "Warm candy goo", "a_pic": "🍬", "b_pic": "🍯", "a_move": "still", "b_move": "splash",
     "kid_tip": "Cool candy is hard. Warm goo is soft.", "tip": "Heat and cool can change how it feels."},
    {"a": "Kiln pot", "b": "Play-dough pot", "a_pic": "🏺", "b_pic": "🧸", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "A kiln pot is hard. Play-dough stays soft.",
     "tip": "Heating can make clay hard."},
)

SHAPE = (
    {"a": "Wood block", "b": "Juice", "a_pic": "🧱", "b_pic": "🧃", "a_move": "still", "b_move": "splash",
     "kid_tip": "A wood block keeps its shape. Juice takes the cup’s shape.",
     "tip": "A solid holds its own shape."},
    {"a": "Rock", "b": "Milk", "a_pic": "🪨", "b_pic": "🥛", "a_move": "still", "b_move": "splash",
     "kid_tip": "A rock holds shape. Milk does not.", "tip": "A liquid takes the cup’s shape."},
    {"a": "Brick", "b": "Water", "a_pic": "🧱", "b_pic": "💧", "a_move": "still", "b_move": "splash",
     "kid_tip": "A brick holds shape.", "tip": "A solid holds its own shape."},
    {"a": "Spoon", "b": "Soup", "a_pic": "🥄", "b_pic": "🍲", "a_move": "still", "b_move": "steam",
     "kid_tip": "A spoon holds shape. Soup does not.", "tip": "Soup is a liquid."},
    {"a": "Crayon", "b": "Paint", "a_pic": "🖍️", "b_pic": "🎨", "a_move": "still", "b_move": "splash",
     "kid_tip": "A crayon holds shape. Paint can splash.", "tip": "A solid holds shape."},
    {"a": "Cup", "b": "Tea", "a_pic": "🥤", "b_pic": "🍵", "a_move": "still", "b_move": "steam",
     "kid_tip": "The cup holds shape. Tea does not.", "tip": "A solid cup holds the liquid."},
    {"a": "Shell", "b": "Ocean", "a_pic": "🐚", "b_pic": "🌊", "a_move": "still", "b_move": "splash",
     "kid_tip": "A shell holds shape. Ocean water does not.", "tip": "A solid holds its own shape."},
    {"a": "Ice cube (cold)", "b": "Puddle", "a_pic": "🧊", "b_pic": "💧", "a_move": "still", "b_move": "splash",
     "kid_tip": "Cold ice holds a cube shape. A puddle does not.",
     "tip": "A solid ice cube holds shape until it melts."},
    {"a": "Stick", "b": "Rain", "a_pic": "🪵", "b_pic": "🌧️", "a_move": "still", "b_move": "splash",
     "kid_tip": "A stick holds shape. Rain does not.", "tip": "A solid holds its own shape."},
    {"a": "Toy car", "b": "Soap water", "a_pic": "🚗", "b_pic": "🫧", "a_move": "still", "b_move": "splash",
     "kid_tip": "A toy car holds shape. Soapy water does not.",
     "tip": "A solid holds its own shape. A liquid takes the cup’s shape."},
)

run_water_cycle_pictures = compare_game(
    game_id="matter_advanced_water_cycle_pictures",
    title="Water Cycle Pictures",
    tagline="What comes after a puddle warms? What needs cold?",
    picture="🌦️",
    pairs=CYCLE,
    q_for_a="What comes after a rain puddle warms?",
    q_for_b="What needs cold instead?",
    tip="Warm water can become vapor and rise.",
)

run_soft_to_hard = compare_game(
    game_id="matter_advanced_soft_to_hard",
    title="Soft to Hard",
    tagline="Which gets harder? Which stays soft?",
    picture="🏺",
    pairs=HARD,
    q_for_a="Which one gets harder?",
    q_for_b="Which one stays soft?",
    tip="Heating can make clay hard.",
)

run_what_holds_shape = compare_game(
    game_id="matter_advanced_what_holds_shape",
    title="What Holds Shape?",
    tagline="Which keeps its shape? Which can splash?",
    picture="🧱",
    pairs=SHAPE,
    q_for_a="Which keeps its own shape?",
    q_for_b="Which can splash or spill?",
    tip="A solid holds its own shape.",
)
