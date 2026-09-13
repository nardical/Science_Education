"""Light & Sound — Intermediate: 10 picture pairs per game."""
from __future__ import annotations
import sys
from pathlib import Path
_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))
from pair_trials import compare_game

SHADOW = (
    {"a": "Toy", "b": "Empty air", "a_pic": "🧸", "b_pic": "✨", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "The toy blocks light and makes a shadow.", "tip": "An object blocks light and makes a shadow."},
    {"a": "Book", "b": "Clear window", "a_pic": "📘", "b_pic": "🪟", "a_move": "still", "b_move": "still",
     "kid_tip": "A book blocks light. A clear window lets light through.",
     "tip": "A shadow needs something that blocks light."},
    {"a": "Hand", "b": "More flashlight", "a_pic": "✋", "b_pic": "🔦", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "A hand can make a shadow. More light does not block light.",
     "tip": "A blocker makes a shadow, not more light."},
    {"a": "Ball", "b": "Open doorway", "a_pic": "⚽", "b_pic": "🚪", "a_move": "still", "b_move": "still",
     "kid_tip": "The ball blocks light. An open doorway does not.",
     "tip": "Something in the way makes a shadow."},
    {"a": "Cup", "b": "Glass jar", "a_pic": "🥤", "b_pic": "🫙", "a_move": "still", "b_move": "still",
     "kid_tip": "A solid cup makes a darker shadow.", "tip": "A blocker makes a shadow."},
    {"a": "Hat", "b": "Sunbeam", "a_pic": "🎩", "b_pic": "☀️", "a_move": "still", "b_move": "steam",
     "kid_tip": "A hat can make a shadow. A sunbeam is light, not a blocker.",
     "tip": "Light itself does not make a shadow."},
    {"a": "Tree", "b": "Open sky", "a_pic": "🌳", "b_pic": "🌤️", "a_move": "still", "b_move": "still",
     "kid_tip": "A tree blocks light and makes shade.", "tip": "A tree is a blocker."},
    {"a": "Box", "b": "Clear wrap", "a_pic": "📦", "b_pic": "📦", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "A box blocks light. Clear wrap lets a lot through.",
     "tip": "Solid things block more light."},
    {"a": "Kid", "b": "Empty hall", "a_pic": "🧒", "b_pic": "⬜", "a_move": "still", "b_move": "still",
     "kid_tip": "A kid in the light makes a shadow.", "tip": "A person can block light."},
    {"a": "Spoon", "b": "More lamps", "a_pic": "🥄", "b_pic": "💡", "a_move": "still", "b_move": "steam",
     "kid_tip": "A spoon can make a shadow. More lamps add light.",
     "tip": "An object blocks light. More light does not."},
)

LOUDER = (
    {"a": "Big wave", "b": "Tiny wave", "a_pic": "〰️", "b_pic": "·", "a_move": "wiggle", "b_move": "still",
     "kid_tip": "The big wave looks louder.", "tip": "A bigger sound wave means louder."},
    {"a": "Drum boom", "b": "Soft tap", "a_pic": "🥁", "b_pic": "👆", "a_move": "wiggle", "b_move": "still",
     "kid_tip": "The drum boom is the louder wave.", "tip": "A bigger wave picture means a louder sound."},
    {"a": "Thunder", "b": "Rain drip", "a_pic": "⛈️", "b_pic": "💧", "a_move": "wiggle", "b_move": "still",
     "kid_tip": "Thunder makes a bigger wave.", "tip": "Louder sounds make taller waves."},
    {"a": "Shout", "b": "Whisper", "a_pic": "📣", "b_pic": "🤫", "a_move": "wiggle", "b_move": "still",
     "kid_tip": "A shout is the louder wave.", "tip": "A shout is louder than a whisper."},
    {"a": "Siren", "b": "Bell ding", "a_pic": "🚨", "b_pic": "🔔", "a_move": "wiggle", "b_move": "still",
     "kid_tip": "The siren wave is bigger.", "tip": "A bigger wave is louder."},
    {"a": "Lion roar", "b": "Mouse squeak", "a_pic": "🦁", "b_pic": "🐭", "a_move": "wiggle", "b_move": "still",
     "kid_tip": "The roar is louder.", "tip": "A roar makes a bigger wave."},
    {"a": "Horn", "b": "Hum", "a_pic": "📯", "b_pic": "🎵", "a_move": "wiggle", "b_move": "still",
     "kid_tip": "The horn wave is bigger.", "tip": "A horn is louder than a hum."},
    {"a": "Crash", "b": "Leaf rustle", "a_pic": "💥", "b_pic": "🍃", "a_move": "wiggle", "b_move": "still",
     "kid_tip": "The crash is louder.", "tip": "A crash makes a bigger wave."},
    {"a": "Speaker", "b": "Phone", "a_pic": "🔊", "b_pic": "📱", "a_move": "wiggle", "b_move": "still",
     "kid_tip": "The big speaker is louder.", "tip": "A bigger speaker can make a bigger wave."},
    {"a": "Alarm", "b": "Clock tick", "a_pic": "⏰", "b_pic": "🕐", "a_move": "wiggle", "b_move": "still",
     "kid_tip": "The alarm is louder.", "tip": "An alarm wave is bigger than a tick."},
)

ECHO = (
    {"a": "Empty cave", "b": "Pillow pile", "a_pic": "🕳️", "b_pic": "🛏️", "a_move": "wiggle", "b_move": "still",
     "kid_tip": "The cave sends sound back. Pillows swallow it.", "tip": "Hard cave walls reflect sound."},
    {"a": "Canyon", "b": "Open field", "a_pic": "🏔️", "b_pic": "🌾", "a_move": "wiggle", "b_move": "still",
     "kid_tip": "A canyon can echo. An open field does not.", "tip": "Hard walls send sound back."},
    {"a": "Tile hall", "b": "Carpet hall", "a_pic": "⬜", "b_pic": "🧶", "a_move": "wiggle", "b_move": "still",
     "kid_tip": "Tile can echo. Carpet swallows sound.", "tip": "Soft things soak up sound."},
    {"a": "Empty gym", "b": "Soft bedroom", "a_pic": "🏟️", "b_pic": "🛏️", "a_move": "wiggle", "b_move": "still",
     "kid_tip": "A gym can echo. A bedroom is soft.", "tip": "Empty hard rooms echo more."},
    {"a": "Well", "b": "Park", "a_pic": "🪣", "b_pic": "🌳", "a_move": "wiggle", "b_move": "still",
     "kid_tip": "A well can send sound back.", "tip": "Hard walls around you can echo."},
    {"a": "Bathroom", "b": "Coat closet", "a_pic": "🛁", "b_pic": "🧥", "a_move": "wiggle", "b_move": "still",
     "kid_tip": "A bathroom can echo. Coats swallow sound.", "tip": "Hard tile can send sound back."},
    {"a": "Tunnel", "b": "Meadow", "a_pic": "🚇", "b_pic": "🌼", "a_move": "wiggle", "b_move": "still",
     "kid_tip": "A tunnel can echo.", "tip": "A tunnel has hard walls around you."},
    {"a": "Brick alley", "b": "Curtain room", "a_pic": "🧱", "b_pic": "🪟", "a_move": "wiggle", "b_move": "still",
     "kid_tip": "Brick can echo. Curtains swallow sound.", "tip": "Hard brick reflects sound."},
    {"a": "Empty garage", "b": "Forest", "a_pic": "🚗", "b_pic": "🌲", "a_move": "wiggle", "b_move": "still",
     "kid_tip": "An empty garage can echo.", "tip": "Hard walls send sound back."},
    {"a": "Metal shed", "b": "Pillow fort", "a_pic": "🛖", "b_pic": "🛏️", "a_move": "wiggle", "b_move": "still",
     "kid_tip": "A metal shed can echo. A pillow fort does not.", "tip": "Hard metal reflects sound."},
)

run_make_a_shadow = compare_game(
    game_id="light_sound_intermediate_make_a_shadow",
    title="Make a Shadow",
    tagline="What makes a shadow? What does not?",
    picture="🔦",
    pairs=SHADOW,
    q_for_a="What makes a shadow?",
    q_for_b="What does not make a shadow?",
    tip="An object blocks light and makes a shadow.",
)

run_which_is_louder = compare_game(
    game_id="light_sound_intermediate_which_is_louder",
    title="Which Is Louder?",
    tagline="Which wave looks louder? Which wave looks quieter?",
    picture="〰️",
    pairs=LOUDER,
    q_for_a="Which wave looks louder?",
    q_for_b="Which wave looks quieter?",
    tip="A bigger sound wave means louder.",
)

run_echo_or_no_echo = compare_game(
    game_id="light_sound_intermediate_echo_or_no_echo",
    title="Echo or No Echo",
    tagline="Where will you hear an echo? Where will sound stay quiet?",
    picture="🗣️",
    pairs=ECHO,
    q_for_a="Where will you hear an echo?",
    q_for_b="Where will the sound stay quiet?",
    tip="Hard cave walls reflect sound.",
)
