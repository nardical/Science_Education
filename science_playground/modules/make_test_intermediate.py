"""Make & Test — Intermediate: 10 picture pairs per game."""
from __future__ import annotations
import sys
from pathlib import Path
_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))
from pair_trials import compare_game

BRIDGE = (
    {"a": "Add toy cars", "b": "Paint it", "a_pic": "🚗", "b_pic": "🎨", "a_move": "bob", "b_move": "still",
     "kid_tip": "Toy cars test if the bridge holds. Paint only changes the look.",
     "tip": "A load test checks if it holds weight."},
    {"a": "Stack blocks", "b": "Draw a star", "a_pic": "🧱", "b_pic": "⭐", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "Stacking blocks tests the bridge. A star is just a picture.",
     "tip": "A test asks: does it work?"},
    {"a": "Roll a marble", "b": "Stick a sticker", "a_pic": "🟠", "b_pic": "🏷️", "a_move": "bob", "b_move": "still",
     "kid_tip": "A marble tests the path. A sticker does not.",
     "tip": "Try the job the bridge is for."},
    {"a": "Set a book on it", "b": "Sing a song", "a_pic": "📘", "b_pic": "🎤", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "A book is a load test. A song is not.",
     "tip": "A test uses a real load."},
    {"a": "Walk a toy truck", "b": "Change the color", "a_pic": "🚚", "b_pic": "🖍️", "a_move": "bob", "b_move": "still",
     "kid_tip": "A truck tests holding. Color does not.",
     "tip": "Looks are not the strength test."},
    {"a": "Add coins", "b": "Add glitter", "a_pic": "🪙", "b_pic": "✨", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "Coins test weight. Glitter does not.",
     "tip": "Weight is the test."},
    {"a": "Press gently", "b": "Take a photo only", "a_pic": "👆", "b_pic": "📷", "a_move": "wiggle", "b_move": "still",
     "kid_tip": "A gentle press is a test. A photo is not.",
     "tip": "You have to try it."},
    {"a": "Send two cars", "b": "Write its name", "a_pic": "🚙", "b_pic": "✏️", "a_move": "bob", "b_move": "still",
     "kid_tip": "Two cars test it. A name does not.",
     "tip": "A test checks if it holds."},
    {"a": "Hang a bag", "b": "Tie a bow", "a_pic": "👜", "b_pic": "🎀", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "A hanging bag is a load. A bow is decoration.",
     "tip": "Load tests the bridge."},
    {"a": "Count how many cars", "b": "Count the stickers", "a_pic": "🔢", "b_pic": "🌟", "a_move": "bob", "b_move": "still",
     "kid_tip": "Counting cars is the test result.",
     "tip": "The number of cars tells you how it did."},
)

RAMP = (
    {"a": "Steep ramp", "b": "Flat ramp", "a_pic": "🛝", "b_pic": "➖", "a_move": "slide", "b_move": "still",
     "kid_tip": "A steeper ramp can help the car go. A flat ramp can stop it early.",
     "tip": "A steeper ramp can give more speed."},
    {"a": "Tilt the book more", "b": "Lay the book flat", "a_pic": "📗", "b_pic": "📘", "a_move": "slide", "b_move": "still",
     "kid_tip": "Tilt more to fix a slow ramp.", "tip": "If it does not work, change one thing."},
    {"a": "Add a wedge", "b": "Take the slope away", "a_pic": "📐", "b_pic": "🧱", "a_move": "slide", "b_move": "still",
     "kid_tip": "A wedge makes a slope. No slope stops the roll.",
     "tip": "A slope helps the car go."},
    {"a": "Raise one end", "b": "Push both ends down", "a_pic": "📦", "b_pic": "⬇️", "a_move": "slide", "b_move": "still",
     "kid_tip": "Raising one end makes it steeper.", "tip": "Steeper can mean more speed."},
    {"a": "Use a slide", "b": "Use a wall", "a_pic": "🛝", "b_pic": "🧱", "a_move": "slide", "b_move": "still",
     "kid_tip": "A slide helps. A wall stops it.", "tip": "Pick the sloping path."},
    {"a": "Steeper board", "b": "Level board", "a_pic": "🪵", "b_pic": "🪵", "a_move": "slide", "b_move": "still",
     "kid_tip": "A steeper board helps the car.", "tip": "Change the slope and try again."},
    {"a": "Hill path", "b": "Flat floor", "a_pic": "⛰️", "b_pic": "⬜", "a_move": "slide", "b_move": "still",
     "kid_tip": "A hill path helps. A flat floor may stop it early.",
     "tip": "A slope gives the car a path down."},
    {"a": "Cardboard tilt", "b": "Cardboard flat", "a_pic": "📦", "b_pic": "📄", "a_move": "slide", "b_move": "still",
     "kid_tip": "Tilt the cardboard to fix it.", "tip": "Change one thing: the tilt."},
    {"a": "Driveway slope", "b": "Closed door", "a_pic": "🚗", "b_pic": "🚪", "a_move": "slide", "b_move": "still",
     "kid_tip": "A slope helps. A closed door stops it.", "tip": "A ramp is a sloping path."},
    {"a": "Make it steeper", "b": "Make it flatter", "a_pic": "📐", "b_pic": "➖", "a_move": "slide", "b_move": "still",
     "kid_tip": "If the car stops early, make it steeper.",
     "tip": "A steeper ramp can give more speed."},
)

PREDICT = (
    {"a": "Test it", "b": "Forget it", "a_pic": "🔬", "b_pic": "🙈", "a_move": "bob", "b_move": "still",
     "kid_tip": "After you predict, you test.", "tip": "Engineers predict, test, and learn."},
    {"a": "Try the ramp", "b": "Only guess forever", "a_pic": "🛝", "b_pic": "🤔", "a_move": "slide", "b_move": "still",
     "kid_tip": "A guess needs a try.", "tip": "Predict means guess. Then we test."},
    {"a": "Roll the car", "b": "Put the car away", "a_pic": "🚗", "b_pic": "📦", "a_move": "bob", "b_move": "still",
     "kid_tip": "Roll it to check your guess.", "tip": "Trying is how we learn."},
    {"a": "Add a load", "b": "Hope without looking", "a_pic": "🧱", "b_pic": "✨", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "Add a load to test the guess.", "tip": "A test checks the guess."},
    {"a": "Watch what happens", "b": "Cover your eyes", "a_pic": "👀", "b_pic": "🙈", "a_move": "bob", "b_move": "still",
     "kid_tip": "Watch the test.", "tip": "We look at the result."},
    {"a": "Change one thing", "b": "Throw it out", "a_pic": "🛠️", "b_pic": "🗑️", "a_move": "wiggle", "b_move": "still",
     "kid_tip": "If it fails, change one thing and try again.",
     "tip": "Fix, then test again."},
    {"a": "Compare two ramps", "b": "Pick without a try", "a_pic": "🛝", "b_pic": "🎲", "a_move": "slide", "b_move": "still",
     "kid_tip": "Compare after you try both.", "tip": "Tests help us pick."},
    {"a": "Time the roll", "b": "Skip the roll", "a_pic": "⏱️", "b_pic": "⏭️", "a_move": "bob", "b_move": "still",
     "kid_tip": "A timed roll is a test.", "tip": "A test can be a simple try."},
    {"a": "Check the bridge", "b": "Only color it", "a_pic": "🌉", "b_pic": "🎨", "a_move": "still", "b_move": "wiggle",
     "kid_tip": "Check if it holds after you predict.", "tip": "Predict, then try."},
    {"a": "Try again", "b": "Stop after the guess", "a_pic": "🔁", "b_pic": "🛑", "a_move": "hop", "b_move": "still",
     "kid_tip": "The next step after predict is try.", "tip": "Trying is how we learn."},
)

run_test_the_bridge = compare_game(
    game_id="make_test_intermediate_test_the_bridge",
    title="Test the Bridge",
    tagline="Which test checks the bridge? Which does not?",
    picture="🌉",
    pairs=BRIDGE,
    q_for_a="Which test checks the bridge?",
    q_for_b="Which does not test the bridge?",
    tip="A load test checks if it holds weight.",
)

run_fix_the_ramp = compare_game(
    game_id="make_test_intermediate_fix_the_ramp",
    title="Fix the Ramp",
    tagline="What should change? What makes it worse?",
    picture="🏎️",
    pairs=RAMP,
    q_for_a="What should change to help the car?",
    q_for_b="What makes the car stop early?",
    tip="A steeper ramp can give more speed.",
)

run_predict_then_try = compare_game(
    game_id="make_test_intermediate_predict_then_try",
    title="Predict Then Try",
    tagline="What comes after predict? What skips the test?",
    picture="🔬",
    pairs=PREDICT,
    q_for_a="What comes after predict?",
    q_for_b="What skips the test?",
    tip="Engineers predict, test, and learn.",
)
