"""Forces & Stuff — Intermediate: 10 picture pairs per game."""
from __future__ import annotations
import sys
from pathlib import Path
_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))
from pair_trials import compare_game

BALANCE = (
    {"a": "Heavy bear", "b": "Light bunny", "a_pic": "🐻", "b_pic": "🐰", "a_move": "still", "b_move": "bob",
     "kid_tip": "The heavy bear sits near the middle. The light bunny sits far out.",
     "tip": "A heavy object balances closer to the middle."},
    {"a": "Big bag", "b": "Tiny bag", "a_pic": "👜", "b_pic": "👛", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "The big bag sits near the middle.", "tip": "Heavier sits closer to the middle."},
    {"a": "Pumpkin", "b": "Apple", "a_pic": "🎃", "b_pic": "🍎", "a_move": "still", "b_move": "bob",
     "kid_tip": "The pumpkin sits near the middle. The apple can sit far out.",
     "tip": "A heavier pumpkin sits closer in."},
    {"a": "Stack of books", "b": "One book", "a_pic": "📚", "b_pic": "📕", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "The stack sits near the middle.", "tip": "More books sit closer to the middle."},
    {"a": "Bowling ball", "b": "Beach ball", "a_pic": "🎳", "b_pic": "🏐", "a_move": "still", "b_move": "bob",
     "kid_tip": "The bowling ball sits near the middle.", "tip": "The heavier ball sits closer in."},
    {"a": "Grown-up", "b": "Toddler", "a_pic": "🧑", "b_pic": "🧒", "a_move": "still", "b_move": "hop",
     "kid_tip": "The grown-up sits near the middle.", "tip": "A heavier person sits closer in."},
    {"a": "Full backpack", "b": "Empty backpack", "a_pic": "🎒", "b_pic": "👜", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "The full backpack sits near the middle.", "tip": "A fuller pack sits closer in."},
    {"a": "Watermelon", "b": "Grape", "a_pic": "🍉", "b_pic": "🍇", "a_move": "still", "b_move": "bob",
     "kid_tip": "The watermelon sits near the middle.", "tip": "The heavier fruit sits closer in."},
    {"a": "Brick", "b": "Sponge", "a_pic": "🧱", "b_pic": "🧽", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "The brick sits near the middle.", "tip": "A brick is heavier, so it sits closer in."},
    {"a": "Rock", "b": "Feather", "a_pic": "🪨", "b_pic": "🪶", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "The rock sits near the middle. The feather sits far out.",
     "tip": "Heavy sits closer. Light sits farther out."},
)

SLIDE = (
    {"a": "Smooth tile", "b": "Sandpaper", "a_pic": "⬜", "b_pic": "🧻", "a_move": "slide", "b_move": "still",
     "kid_tip": "The box slides on tile. Sandpaper holds it.", "tip": "Smooth tile has less grip."},
    {"a": "Ice", "b": "Rug", "a_pic": "🧊", "b_pic": "🧶", "a_move": "slide", "b_move": "still",
     "kid_tip": "Ice lets the box slide. A rug holds it.", "tip": "Ice is slippy. A rug has grip."},
    {"a": "Soap board", "b": "Grass", "a_pic": "🧼", "b_pic": "🌱", "a_move": "slide", "b_move": "still",
     "kid_tip": "Soap is slippy. Grass holds the box.", "tip": "Slippy surfaces let things slide."},
    {"a": "Wax paper", "b": "Carpet", "a_pic": "📄", "b_pic": "🟫", "a_move": "slide", "b_move": "still",
     "kid_tip": "Wax paper is slippy. Carpet holds.", "tip": "Smooth wax has less grip."},
    {"a": "Wet tile", "b": "Towel", "a_pic": "💧", "b_pic": "🧻", "a_move": "slide", "b_move": "still",
     "kid_tip": "Wet tile is slippy. A towel holds.", "tip": "Water can make a floor slippy."},
    {"a": "Marble floor", "b": "Dirt path", "a_pic": "⚪", "b_pic": "🟤", "a_move": "slide", "b_move": "still",
     "kid_tip": "Marble is slippy. Dirt holds.", "tip": "A smooth floor has less grip."},
    {"a": "Sled hill", "b": "Velcro mat", "a_pic": "🛷", "b_pic": "🧷", "a_move": "slide", "b_move": "still",
     "kid_tip": "A sled hill is slippy. Velcro holds.", "tip": "Grip stops the slide."},
    {"a": "Glass table", "b": "Rubber mat", "a_pic": "🪟", "b_pic": "🛞", "a_move": "slide", "b_move": "still",
     "kid_tip": "Glass is slippy. Rubber holds.", "tip": "Rubber has more grip."},
    {"a": "Oil tray", "b": "Sand box", "a_pic": "🛢️", "b_pic": "🏖️", "a_move": "slide", "b_move": "still",
     "kid_tip": "Oil is slippy. Sand holds.", "tip": "Oil makes less grip."},
    {"a": "Banana peel", "b": "Doormat", "a_pic": "🍌", "b_pic": "🚪", "a_move": "slide", "b_move": "still",
     "kid_tip": "A banana peel is slippy. A doormat holds.", "tip": "A mat has grip."},
)

PUSH = (
    {"a": "Big push", "b": "Small push", "a_pic": "💪", "b_pic": "👆", "a_move": "slide", "b_move": "wiggle",
     "kid_tip": "The big push wins. The box goes that way.", "tip": "The stronger force wins."},
    {"a": "Grown-up push", "b": "Toddler push", "a_pic": "🧑", "b_pic": "🧒", "a_move": "slide", "b_move": "still",
     "kid_tip": "The grown-up push wins.", "tip": "A stronger push moves the box."},
    {"a": "Wind gust", "b": "Tiny breeze", "a_pic": "💨", "b_pic": "🍃", "a_move": "slide", "b_move": "wiggle",
     "kid_tip": "The gust wins.", "tip": "A bigger push of air wins."},
    {"a": "Both hands", "b": "One finger", "a_pic": "🙌", "b_pic": "👆", "a_move": "slide", "b_move": "still",
     "kid_tip": "Both hands win.", "tip": "More push wins."},
    {"a": "Hard kick", "b": "Soft tap", "a_pic": "🦵", "b_pic": "👟", "a_move": "slide", "b_move": "wiggle",
     "kid_tip": "The hard kick wins.", "tip": "A stronger kick moves it more."},
    {"a": "Elephant", "b": "Ant", "a_pic": "🐘", "b_pic": "🐜", "a_move": "slide", "b_move": "still",
     "kid_tip": "The elephant push wins.", "tip": "A stronger push wins."},
    {"a": "Truck bump", "b": "Toy bump", "a_pic": "🚛", "b_pic": "🚚", "a_move": "slide", "b_move": "wiggle",
     "kid_tip": "The truck bump wins.", "tip": "A bigger bump is a stronger push."},
    {"a": "Magnet close", "b": "Magnet far", "a_pic": "🧲", "b_pic": "✨", "a_move": "slide", "b_move": "still",
     "kid_tip": "The close magnet pulls more.", "tip": "A closer magnet is a stronger pull."},
    {"a": "Three kids", "b": "One kid", "a_pic": "🧒🧒🧒", "b_pic": "🧒", "a_move": "slide", "b_move": "wiggle",
     "kid_tip": "Three kids push more.", "tip": "More pushers make a stronger push."},
    {"a": "Balloon pop", "b": "Whisper blow", "a_pic": "💥", "b_pic": "😮", "a_move": "slide", "b_move": "still",
     "kid_tip": "The pop is a bigger push.", "tip": "A stronger burst wins."},
)

run_balance_the_seesaw = compare_game(
    game_id="forces_stuff_intermediate_balance_the_seesaw",
    title="Balance the Seesaw",
    tagline="Who sits near the middle? Who sits far away?",
    picture="⚖️",
    pairs=BALANCE,
    q_for_a="Who sits near the middle?",
    q_for_b="Who sits far away?",
    tip="A heavy object balances closer to the middle.",
)

run_will_it_slide = compare_game(
    game_id="forces_stuff_intermediate_will_it_slide",
    title="Will It Slide?",
    tagline="Which floor lets it slide? Which floor holds it?",
    picture="📦",
    pairs=SLIDE,
    q_for_a="Which floor lets the box slide?",
    q_for_b="Which floor holds the box?",
    tip="Smooth tile has less grip.",
)

run_stronger_push_wins = compare_game(
    game_id="forces_stuff_intermediate_stronger_push_wins",
    title="Stronger Push Wins",
    tagline="Which push wins? Which push loses?",
    picture="💪",
    pairs=PUSH,
    q_for_a="Which push wins?",
    q_for_b="Which push loses?",
    tip="The stronger force wins.",
)
