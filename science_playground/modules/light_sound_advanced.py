"""Light & Sound — Advanced: 10 picture pairs per game."""
from __future__ import annotations
import sys
from pathlib import Path
_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))
from pair_trials import compare_game

BLOCK = (
    {"a": "Big block", "b": "Small block", "a_pic": "⬛", "b_pic": "▪️", "a_move": "grow", "b_move": "still",
     "kid_tip": "The big block makes the bigger shadow.", "tip": "A bigger blocker can make a bigger shadow."},
    {"a": "Book", "b": "Coin", "a_pic": "📘", "b_pic": "🪙", "a_move": "grow", "b_move": "still",
     "kid_tip": "A book makes a bigger shadow than a coin.", "tip": "A bigger blocker can make a bigger shadow."},
    {"a": "Grown-up", "b": "Toddler", "a_pic": "🧑", "b_pic": "🧒", "a_move": "grow", "b_move": "still",
     "kid_tip": "A grown-up can make a bigger shadow.", "tip": "A taller blocker can make a longer shadow."},
    {"a": "Tree", "b": "Twig", "a_pic": "🌳", "b_pic": "🪵", "a_move": "grow", "b_move": "still",
     "kid_tip": "A tree makes a bigger shadow.", "tip": "A bigger blocker, a bigger shadow."},
    {"a": "Box", "b": "Button", "a_pic": "📦", "b_pic": "🔘", "a_move": "grow", "b_move": "still",
     "kid_tip": "A box makes a bigger shadow.", "tip": "Size of the blocker matters."},
    {"a": "Hat", "b": "Bead", "a_pic": "🎩", "b_pic": "🔵", "a_move": "grow", "b_move": "still",
     "kid_tip": "A hat makes a bigger shadow.", "tip": "A bigger blocker can make a bigger shadow."},
    {"a": "Chair", "b": "Spoon", "a_pic": "🪑", "b_pic": "🥄", "a_move": "grow", "b_move": "still",
     "kid_tip": "A chair makes a bigger shadow.", "tip": "A bigger blocker, a bigger shadow."},
    {"a": "Ball", "b": "Pea", "a_pic": "⚽", "b_pic": "🟢", "a_move": "grow", "b_move": "still",
     "kid_tip": "A ball makes a bigger shadow.", "tip": "A bigger blocker can make a bigger shadow."},
    {"a": "Door", "b": "Key", "a_pic": "🚪", "b_pic": "🔑", "a_move": "grow", "b_move": "still",
     "kid_tip": "A door makes a bigger shadow.", "tip": "A bigger blocker, a bigger shadow."},
    {"a": "Backpack", "b": "Pencil", "a_pic": "🎒", "b_pic": "✏️", "a_move": "grow", "b_move": "still",
     "kid_tip": "A backpack makes a bigger shadow.", "tip": "A bigger blocker can make a bigger shadow."},
)

PITCH = (
    {"a": "Tiny bell", "b": "Floor drum", "a_pic": "🔔", "b_pic": "🥁", "a_move": "wiggle", "b_move": "still",
     "kid_tip": "A tiny bell wiggles fast and sounds high.",
     "tip": "Faster vibrations make a higher pitch."},
    {"a": "Whistle", "b": "Big drum", "a_pic": "😗", "b_pic": "🥁", "a_move": "wiggle", "b_move": "still",
     "kid_tip": "A whistle sounds high. A big drum sounds low.", "tip": "Fast wiggles sound high."},
    {"a": "Bird", "b": "Frog", "a_pic": "🐦", "b_pic": "🐸", "a_move": "wiggle", "b_move": "still",
     "kid_tip": "A bird song is higher. A frog is lower.", "tip": "High sounds wiggle faster."},
    {"a": "Whistle", "b": "Foghorn", "a_pic": "😗", "b_pic": "🚢", "a_move": "wiggle", "b_move": "still",
     "kid_tip": "A whistle is higher.", "tip": "A foghorn is a slow, low wiggle."},
    {"a": "Squeak", "b": "Rumble", "a_pic": "🐭", "b_pic": "🔉", "a_move": "wiggle", "b_move": "still",
     "kid_tip": "A squeak is high. A rumble is low.", "tip": "Fast wiggles sound high."},
    {"a": "Flute", "b": "Tuba", "a_pic": "🎶", "b_pic": "🎺", "a_move": "wiggle", "b_move": "still",
     "kid_tip": "A flute is higher. A tuba is lower.", "tip": "Slow wiggles sound low."},
    {"a": "Ping", "b": "Boom", "a_pic": "✨", "b_pic": "💥", "a_move": "wiggle", "b_move": "still",
     "kid_tip": "A ping is high. A boom is low.", "tip": "Fast wiggles sound high."},
    {"a": "Kitten", "b": "Lion", "a_pic": "🐱", "b_pic": "🦁", "a_move": "wiggle", "b_move": "still",
     "kid_tip": "A kitten is higher. A lion is lower.", "tip": "High and low are pitch."},
    {"a": "Triangle ding", "b": "Bass thump", "a_pic": "🔺", "b_pic": "🥁", "a_move": "wiggle", "b_move": "still",
     "kid_tip": "A ding is high. A thump is low.", "tip": "Faster vibrations make a higher pitch."},
    {"a": "Piccolo", "b": "Tuba slide", "a_pic": "🎶", "b_pic": "🎺", "a_move": "wiggle", "b_move": "still",
     "kid_tip": "A piccolo wiggles faster and sounds high.", "tip": "Fast wiggles sound high."},
)

PATH = (
    {"a": "Wall", "b": "Open door", "a_pic": "🧱", "b_pic": "🚪", "a_move": "still", "b_move": "steam",
     "kid_tip": "A wall blocks the light. An open door lets it through.",
     "tip": "An opaque wall blocks the light path."},
    {"a": "Notebook", "b": "Clear glass", "a_pic": "📓", "b_pic": "🪟", "a_move": "still", "b_move": "steam",
     "kid_tip": "A notebook blocks light. Clear glass lets a lot through.",
     "tip": "Some things block the path of light."},
    {"a": "Wood door", "b": "Window", "a_pic": "🚪", "b_pic": "🪟", "a_move": "still", "b_move": "steam",
     "kid_tip": "A wood door blocks light.", "tip": "Light does not go through an opaque door."},
    {"a": "Cardboard", "b": "Empty hoop", "a_pic": "📦", "b_pic": "⭕", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "Cardboard blocks. An empty hoop does not.",
     "tip": "A blocker stops the beam."},
    {"a": "Book", "b": "Air", "a_pic": "📘", "b_pic": "🌬️", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "A book blocks the flashlight.", "tip": "Air lets light keep going."},
    {"a": "Metal lid", "b": "Clear wrap", "a_pic": "🥘", "b_pic": "✨", "a_move": "still", "b_move": "steam",
     "kid_tip": "A metal lid blocks light.", "tip": "Clear wrap lets light through."},
    {"a": "Closet door", "b": "Open closet", "a_pic": "🚪", "b_pic": "👕", "a_move": "still", "b_move": "steam",
     "kid_tip": "A closed closet door blocks light.", "tip": "An open space lets light in."},
    {"a": "Hand", "b": "No hand", "a_pic": "✋", "b_pic": "⬜", "a_move": "still", "b_move": "steam",
     "kid_tip": "A hand in the way blocks the beam.", "tip": "A blocker stops the path."},
    {"a": "Box lid", "b": "Open box", "a_pic": "📦", "b_pic": "📤", "a_move": "still", "b_move": "steam",
     "kid_tip": "A lid blocks light. An open box lets it in.",
     "tip": "Some things block the path of light."},
    {"a": "Brick", "b": "Hole in the brick", "a_pic": "🧱", "b_pic": "🕳️", "a_move": "still", "b_move": "steam",
     "kid_tip": "A solid brick blocks. A hole lets light through.",
     "tip": "Light needs an opening."},
)

run_bigger_block_bigger_shadow = compare_game(
    game_id="light_sound_advanced_bigger_block_bigger_shadow",
    title="Bigger Block, Bigger Shadow",
    tagline="Which makes the bigger shadow? Which makes the smaller one?",
    picture="⬛",
    pairs=BLOCK,
    q_for_a="Which makes the bigger shadow?",
    q_for_b="Which makes the smaller shadow?",
    tip="A bigger blocker can make a bigger shadow.",
)

run_pitch_ladder = compare_game(
    game_id="light_sound_advanced_pitch_ladder",
    title="Pitch Ladder",
    tagline="Which note is high? Which note is low?",
    picture="🎵",
    pairs=PITCH,
    q_for_a="Which note has the highest pitch?",
    q_for_b="Which note has the lowest pitch?",
    tip="Faster vibrations make a higher pitch.",
)

run_light_path_blocked = compare_game(
    game_id="light_sound_advanced_light_path_blocked",
    title="Light Path Blocked",
    tagline="What blocks the light? What lets it through?",
    picture="🧱",
    pairs=PATH,
    q_for_a="What blocks the light?",
    q_for_b="What lets the light through?",
    tip="An opaque wall blocks the light path.",
)
