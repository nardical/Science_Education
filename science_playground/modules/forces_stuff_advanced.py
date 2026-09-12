"""Forces & Stuff — Advanced: 10 picture pairs per game."""
from __future__ import annotations
import sys
from pathlib import Path
_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))
from pair_trials import compare_game

FAIR = (
    {"a": "Equal weights", "b": "One heavy side", "a_pic": "⚖️", "b_pic": "🏋️", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "Equal weights can balance. One heavy side tips.",
     "tip": "Equal weights at equal distances balance."},
    {"a": "Two same books", "b": "Book vs brick", "a_pic": "📕📕", "b_pic": "📕🧱", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "Two same books can balance.", "tip": "Same weight, same place, it balances."},
    {"a": "Two same kids", "b": "Kid vs grown-up", "a_pic": "🧒🧒", "b_pic": "🧒🧑", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "Two same kids can sit even.", "tip": "Matching sides stay even."},
    {"a": "Two cups of water", "b": "Cup vs jug", "a_pic": "🥛🥛", "b_pic": "🥛🫗", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "Two same cups can balance.", "tip": "Equal amounts stay even."},
    {"a": "Two apples", "b": "Apple vs pumpkin", "a_pic": "🍎🍎", "b_pic": "🍎🎃", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "Two apples can balance.", "tip": "A pumpkin tips the other side."},
    {"a": "Two shoes", "b": "Shoe vs boot", "a_pic": "👟👟", "b_pic": "👟🥾", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "Two same shoes stay even.", "tip": "A heavier boot tips it."},
    {"a": "Two toys", "b": "Toy vs box", "a_pic": "🧸🧸", "b_pic": "🧸📦", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "Two same toys can balance.", "tip": "A heavier box tips it."},
    {"a": "Two bags", "b": "Bag vs backpack", "a_pic": "👜👜", "b_pic": "👜🎒", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "Two same bags stay even.", "tip": "A heavier pack tips it."},
    {"a": "Two blocks", "b": "Block vs pile", "a_pic": "🧱🧱", "b_pic": "🧱📦", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "Two same blocks stay even.", "tip": "A pile is heavier."},
    {"a": "Two spoons", "b": "Spoon vs pot", "a_pic": "🥄🥄", "b_pic": "🥄🍲", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "Two spoons can balance.", "tip": "A pot is heavier."},
)

ROUGH = (
    {"a": "Smooth ramp", "b": "Rough ramp", "a_pic": "🪵", "b_pic": "🧻", "a_move": "slide", "b_move": "still",
     "kid_tip": "The smooth ramp lets the car go farther.",
     "tip": "Less friction lets the car travel farther."},
    {"a": "Ice board", "b": "Sandpaper board", "a_pic": "🧊", "b_pic": "📄", "a_move": "slide", "b_move": "still",
     "kid_tip": "Ice is smoother, so the car goes farther.", "tip": "Less grip can mean a longer roll."},
    {"a": "Tile ramp", "b": "Carpet ramp", "a_pic": "⬜", "b_pic": "🧶", "a_move": "slide", "b_move": "still",
     "kid_tip": "Tile is smoother.", "tip": "Smooth has less grip."},
    {"a": "Waxed board", "b": "Towel board", "a_pic": "✨", "b_pic": "🧻", "a_move": "slide", "b_move": "still",
     "kid_tip": "Wax is smoother.", "tip": "A towel grabs the wheels."},
    {"a": "Glass ramp", "b": "Dirt ramp", "a_pic": "🪟", "b_pic": "🟤", "a_move": "slide", "b_move": "still",
     "kid_tip": "Glass is smoother.", "tip": "Dirt has more grip."},
    {"a": "Soap ramp", "b": "Grass ramp", "a_pic": "🧼", "b_pic": "🌱", "a_move": "slide", "b_move": "still",
     "kid_tip": "Soap is slippy, so farther.", "tip": "Grass holds the car."},
    {"a": "Marble ramp", "b": "Rubber ramp", "a_pic": "⚪", "b_pic": "🛞", "a_move": "slide", "b_move": "still",
     "kid_tip": "Marble is smoother.", "tip": "Rubber has more grip."},
    {"a": "Wet tile", "b": "Doormat", "a_pic": "💧", "b_pic": "🚪", "a_move": "slide", "b_move": "still",
     "kid_tip": "Wet tile is slippy.", "tip": "A mat grabs."},
    {"a": "Sled track", "b": "Velcro track", "a_pic": "🛷", "b_pic": "🧷", "a_move": "slide", "b_move": "still",
     "kid_tip": "A sled track is smoother.", "tip": "Velcro holds."},
    {"a": "Polished wood", "b": "Bark path", "a_pic": "🪵", "b_pic": "🌳", "a_move": "slide", "b_move": "still",
     "kid_tip": "Polished wood is smoother.", "tip": "Bark is rough."},
)

LEVER = (
    {"a": "Pivot near the rock", "b": "Pivot near your hand", "a_pic": "🪨", "b_pic": "✋", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "Put the pivot near the rock to lift easier.",
     "tip": "A nearby pivot makes lifting easier."},
    {"a": "Fulcrum by the load", "b": "Fulcrum by the handle", "a_pic": "📦", "b_pic": "🥄", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "The fulcrum belongs near the load.", "tip": "A lever helps you lift. Put the pivot near the heavy thing."},
    {"a": "Close to the brick", "b": "Close to your fingers", "a_pic": "🧱", "b_pic": "👆", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "Stay close to the brick.", "tip": "Pivot near the heavy thing."},
    {"a": "Near the bag", "b": "Near the long end", "a_pic": "👜", "b_pic": "🪵", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "Near the bag is easier.", "tip": "A long handle and a close pivot help."},
    {"a": "By the book", "b": "By the far tip", "a_pic": "📘", "b_pic": "✨", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "By the book is the helpful pivot.", "tip": "Pivot near the load."},
    {"a": "Next to the log", "b": "Next to your elbow", "a_pic": "🪵", "b_pic": "💪", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "Next to the log helps.", "tip": "Keep the pivot near the heavy log."},
    {"a": "Under the lid edge", "b": "Under the far handle", "a_pic": "🫙", "b_pic": "🥄", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "A spoon pivot near the lid lifts it.", "tip": "A spoon can be a lever."},
    {"a": "Near the paint can", "b": "Near the stick end", "a_pic": "🎨", "b_pic": "🪄", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "Near the can is easier.", "tip": "Pivot near the load."},
    {"a": "Close to the stone", "b": "Close to the tip", "a_pic": "🪨", "b_pic": "📍", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "Close to the stone.", "tip": "A nearby pivot makes lifting easier."},
    {"a": "By the heavy box", "b": "By the empty air", "a_pic": "📦", "b_pic": "🌬️", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "By the heavy box.", "tip": "Put the pivot near the heavy thing."},
)

run_fair_balance = compare_game(
    game_id="forces_stuff_advanced_fair_balance",
    title="Fair Balance",
    tagline="What keeps it even? What tips it?",
    picture="⚖️",
    pairs=FAIR,
    q_for_a="What keeps both sides even?",
    q_for_b="What tips the seesaw?",
    tip="Equal weights at equal distances balance.",
)

run_rough_vs_smooth_ramp = compare_game(
    game_id="forces_stuff_advanced_rough_vs_smooth_ramp",
    title="Rough vs Smooth Ramp",
    tagline="Which car goes farther? Which car stops sooner?",
    picture="🏎️",
    pairs=ROUGH,
    q_for_a="Which ramp lets the car go farther?",
    q_for_b="Which ramp stops the car sooner?",
    tip="Less friction lets the car travel farther.",
)

run_lift_with_a_lever = compare_game(
    game_id="forces_stuff_advanced_lift_with_a_lever",
    title="Lift With a Lever",
    tagline="Where should the pivot go? Where makes it harder?",
    picture="🪵",
    pairs=LEVER,
    q_for_a="Where should the pivot go?",
    q_for_b="Where makes lifting harder?",
    tip="A nearby pivot makes lifting easier.",
)
