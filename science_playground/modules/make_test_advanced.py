"""Make & Test — Advanced: 10 picture pairs per game."""
from __future__ import annotations
import sys
from pathlib import Path
_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))
from pair_trials import compare_game

SHAPE = (
    {"a": "Triangle", "b": "Wobbly curve", "a_pic": "🔺", "b_pic": "〰️", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "A triangle keeps its shape. A wobbly curve does not.",
     "tip": "Triangles help frames keep their shape."},
    {"a": "Triangle frame", "b": "Floppy square", "a_pic": "🔺", "b_pic": "⬜", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "A triangle frame stays. A floppy square sags.",
     "tip": "Triangles help a frame keep its shape."},
    {"a": "Straw triangle", "b": "Straw loop", "a_pic": "📐", "b_pic": "⭕", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "Straw triangles stay strong.", "tip": "A loop can squash."},
    {"a": "Roof triangle", "b": "Sagging rope", "a_pic": "🏠", "b_pic": "🪢", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "A roof triangle is strong.", "tip": "A rope sags."},
    {"a": "Bridge brace", "b": "Loose string", "a_pic": "🌉", "b_pic": "🧵", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "A triangle brace helps a bridge.", "tip": "String is floppy."},
    {"a": "Paper triangle", "b": "Paper curl", "a_pic": "📄", "b_pic": "🌀", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "Folded into a triangle, paper is stronger.", "tip": "A curl is weak."},
    {"a": "Tent poles triangle", "b": "One floppy pole", "a_pic": "⛺", "b_pic": "🪵", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "Tent poles make triangles.", "tip": "One floppy pole falls."},
    {"a": "Bike frame", "b": "Wiggly hose", "a_pic": "🚲", "b_pic": "🚿", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "A bike frame uses triangles.", "tip": "A hose is floppy."},
    {"a": "Shelf brace", "b": "No brace", "a_pic": "📚", "b_pic": "➖", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "A triangle brace holds a shelf.", "tip": "No brace lets it sag."},
    {"a": "Kite sticks", "b": "Loose ribbon", "a_pic": "🪁", "b_pic": "🎀", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "Kite sticks make a strong shape.", "tip": "A ribbon is floppy."},
)

BETTER = (
    {"a": "Bridge A", "b": "Bridge B", "a_pic": "🌉", "b_pic": "🪵", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "Bridge A held more cars, so pick A.",
     "tip": "Test results show Bridge A is stronger."},
    {"a": "Ramp that finished", "b": "Ramp that stopped", "a_pic": "🛝", "b_pic": "🛑", "a_move": "slide", "b_move": "still",
     "kid_tip": "Pick the ramp that finished the test.", "tip": "We pick the one that did better."},
    {"a": "Tower that stayed", "b": "Tower that fell", "a_pic": "🗼", "b_pic": "💥", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "Pick the tower that stayed.", "tip": "The test shows which is better."},
    {"a": "Path that worked", "b": "Path with a gap", "a_pic": "🟠", "b_pic": "🕳️", "a_move": "bob", "b_move": "still",
     "kid_tip": "Pick the path that worked.", "tip": "Compare the two tests."},
    {"a": "Frame that held a push", "b": "Frame that folded", "a_pic": "🔺", "b_pic": "〰️", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "Pick the frame that held.", "tip": "Test results help us pick."},
    {"a": "Boat that floated", "b": "Boat that sank", "a_pic": "🚤", "b_pic": "⚓", "a_move": "bob", "b_move": "splash",
     "kid_tip": "Pick the boat that floated.", "tip": "The test tells you."},
    {"a": "Cup that held coins", "b": "Cup that tipped", "a_pic": "🥤", "b_pic": "💧", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "Pick the cup that held.", "tip": "We pick the one that did better."},
    {"a": "Car that went farther", "b": "Car that stopped short", "a_pic": "🚗", "b_pic": "🚙", "a_move": "slide", "b_move": "still",
     "kid_tip": "Pick the car that went farther.", "tip": "Compare the two results."},
    {"a": "Paper that held", "b": "Paper that tore", "a_pic": "📄", "b_pic": "✂️", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "Pick the paper that held.", "tip": "The test shows which is better."},
    {"a": "Glue that stuck", "b": "Tape that peeled", "a_pic": "🧴", "b_pic": "🏷️", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "Pick the glue that stuck.", "tip": "We pick the one that did better on the test."},
)

PATH = (
    {"a": "Short bridge", "b": "Soft pillow", "a_pic": "🌉", "b_pic": "🛏️", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "A firm bridge completes the path. A pillow is too soft.",
     "tip": "A firm bridge completes the path."},
    {"a": "Board across the gap", "b": "A sock in the gap", "a_pic": "🪵", "b_pic": "🧦", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "A board can finish the path.", "tip": "A sock is too floppy."},
    {"a": "Book as a bridge", "b": "Tissue pile", "a_pic": "📘", "b_pic": "🧻", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "A book can span the gap.", "tip": "Tissue is too soft."},
    {"a": "Cardboard strip", "b": "Feather", "a_pic": "📦", "b_pic": "🪶", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "Cardboard can finish the run.", "tip": "A feather cannot hold a marble."},
    {"a": "Ruler across", "b": "Yarn across", "a_pic": "📏", "b_pic": "🧶", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "A ruler is firm.", "tip": "Yarn sags."},
    {"a": "Block step", "b": "Open air", "a_pic": "🧱", "b_pic": "🌬️", "a_move": "still", "b_move": "still",
     "kid_tip": "A block fills the gap.", "tip": "Open air is still a gap."},
    {"a": "Lid as a path", "b": "Cotton ball", "a_pic": "🫙", "b_pic": "⚪", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "A lid can be a short bridge.", "tip": "Cotton is too soft."},
    {"a": "Tray across chairs", "b": "Blanket sag", "a_pic": "🍽️", "b_pic": "🛏️", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "A tray is firm.", "tip": "A blanket sags."},
    {"a": "Stick bridge", "b": "Leaf", "a_pic": "🪵", "b_pic": "🍃", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "A stick can span a small gap.", "tip": "A leaf is too weak."},
    {"a": "Folded card", "b": "Open hole", "a_pic": "🃏", "b_pic": "⭕", "a_move": "still", "b_move": "still",
     "kid_tip": "A folded card can finish the path.", "tip": "An open hole is still a gap."},
)

run_stronger_shape = compare_game(
    game_id="make_test_advanced_stronger_shape",
    title="Stronger Shape",
    tagline="Which shape is strong? Which shape is floppy?",
    picture="🔺",
    pairs=SHAPE,
    q_for_a="Which shape makes a strong frame?",
    q_for_b="Which shape is floppy?",
    tip="Triangles help frames keep their shape.",
)

run_two_tests_pick_better = compare_game(
    game_id="make_test_advanced_two_tests_pick_better",
    title="Two Tests, Pick Better",
    tagline="Which did better? Which did worse?",
    picture="🌉",
    pairs=BETTER,
    q_for_a="Which one did better on the test?",
    q_for_b="Which one did worse?",
    tip="Test results show Bridge A is stronger.",
)

run_build_a_path = compare_game(
    game_id="make_test_advanced_build_a_path",
    title="Build a Path",
    tagline="What finishes the path? What is too soft?",
    picture="🟠",
    pairs=PATH,
    q_for_a="Gap blocks the marble. Add what?",
    q_for_b="What is too soft for the gap?",
    tip="A firm bridge completes the path.",
)
