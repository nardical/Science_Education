"""Motion — Advanced: 10 picture pairs per game."""
from __future__ import annotations
import sys
from pathlib import Path
_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))
from pair_trials import compare_game

STEEP = (
    {"a": "Steep ramp", "b": "Flat ramp", "a_pic": "🛝", "b_pic": "➖", "a_move": "slide", "b_move": "still",
     "kid_tip": "The steep ramp makes more speed.", "tip": "A steeper ramp makes it speed up more."},
    {"a": "Tall book ramp", "b": "Low book ramp", "a_pic": "📗", "b_pic": "📘", "a_move": "slide", "b_move": "wiggle",
     "kid_tip": "The tall book ramp is steeper, so faster.", "tip": "Steeper can mean more speed at the bottom."},
    {"a": "Slide", "b": "Gentle slope", "a_pic": "🛝", "b_pic": "🛣️", "a_move": "slide", "b_move": "still",
     "kid_tip": "The slide is steeper.", "tip": "A steeper path speeds you up more."},
    {"a": "Hill", "b": "Almost flat path", "a_pic": "⛰️", "b_pic": "⬜", "a_move": "slide", "b_move": "still",
     "kid_tip": "The hill is steeper.", "tip": "A hill can add more speed."},
    {"a": "Wedge on end", "b": "Wedge almost flat", "a_pic": "📐", "b_pic": "➖", "a_move": "slide", "b_move": "still",
     "kid_tip": "A standing wedge is steeper.", "tip": "More tilt, more speed."},
    {"a": "Driveway hill", "b": "Sidewalk", "a_pic": "🚗", "b_pic": "🚶", "a_move": "slide", "b_move": "still",
     "kid_tip": "The driveway hill is steeper.", "tip": "A steeper driveway speeds a roll."},
    {"a": "Playground slide", "b": "Wide stairs", "a_pic": "🛝", "b_pic": "🪜", "a_move": "slide", "b_move": "still",
     "kid_tip": "The slide is the steeper path.", "tip": "A slide is steeper than wide stairs."},
    {"a": "Roof slope", "b": "Table top", "a_pic": "🏠", "b_pic": "🪵", "a_move": "slide", "b_move": "still",
     "kid_tip": "A roof slope is steeper than a table.", "tip": "A table is almost flat."},
    {"a": "Ski jump", "b": "Soft bump", "a_pic": "🎿", "b_pic": "🟤", "a_move": "slide", "b_move": "wiggle",
     "kid_tip": "The ski jump is steeper.", "tip": "Steeper means more speed."},
    {"a": "Cardboard tilt high", "b": "Cardboard tilt tiny", "a_pic": "📦", "b_pic": "📄", "a_move": "slide", "b_move": "still",
     "kid_tip": "The high tilt is steeper.", "tip": "Raise one end more to go faster."},
)

PUSHES = (
    {"a": "Two right pushes", "b": "One left push", "a_pic": "➡️➡️", "b_pic": "⬅️", "a_move": "slide", "b_move": "still",
     "kid_tip": "Two pushes to the right add up. The box goes right.",
     "tip": "Pushes in one direction add together."},
    {"a": "Both hands right", "b": "One hand left", "a_pic": "🙌", "b_pic": "👈", "a_move": "slide", "b_move": "wiggle",
     "kid_tip": "Both hands to the right move it right.", "tip": "Pushes the same way add up."},
    {"a": "Two kicks right", "b": "A tap left", "a_pic": "🦵", "b_pic": "👆", "a_move": "slide", "b_move": "still",
     "kid_tip": "Two right kicks add up.", "tip": "Same-way pushes add."},
    {"a": "Wind and push right", "b": "Tiny left poke", "a_pic": "💨", "b_pic": "👈", "a_move": "slide", "b_move": "still",
     "kid_tip": "Wind and a push both right add up.", "tip": "Two right pushes win."},
    {"a": "Two kids right", "b": "One kid left", "a_pic": "🧒🧒", "b_pic": "🧒", "a_move": "slide", "b_move": "wiggle",
     "kid_tip": "Two kids pushing right add up.", "tip": "More same-way push wins."},
    {"a": "Magnet and hand right", "b": "A left finger", "a_pic": "🧲", "b_pic": "👆", "a_move": "slide", "b_move": "still",
     "kid_tip": "Both right pulls add.", "tip": "Same direction adds."},
    {"a": "Two rolls right", "b": "One roll left", "a_pic": "🎳", "b_pic": "↩️", "a_move": "slide", "b_move": "still",
     "kid_tip": "Two right rolls add.", "tip": "Same-way motion adds."},
    {"a": "Fan and shove right", "b": "A left whisper", "a_pic": "🪭", "b_pic": "😮", "a_move": "slide", "b_move": "still",
     "kid_tip": "Fan and shove to the right add.", "tip": "Pushes the same way add up."},
    {"a": "Two wagons right", "b": "One wagon left", "a_pic": "🛒🛒", "b_pic": "🛒", "a_move": "slide", "b_move": "still",
     "kid_tip": "Two wagons pulling right add.", "tip": "Same-way pulls add."},
    {"a": "Double tap right", "b": "Single tap left", "a_pic": "👉👉", "b_pic": "👈", "a_move": "slide", "b_move": "wiggle",
     "kid_tip": "Two right taps add up.", "tip": "Pushes in one direction add together."},
)

CLOCK = (
    {"a": "3-second car", "b": "6-second car", "a_pic": "🚗", "b_pic": "🚙", "a_move": "slide", "b_move": "still",
     "kid_tip": "Same path, less time: the 3-second car is faster.",
     "tip": "Less time for the same trip means faster."},
    {"a": "Quick bike", "b": "Slow bike", "a_pic": "🚲", "b_pic": "🚲", "a_move": "slide", "b_move": "wiggle",
     "kid_tip": "The bike that finishes first is faster.", "tip": "Same path, less time, faster."},
    {"a": "Short-time runner", "b": "Long-time runner", "a_pic": "🏃", "b_pic": "🚶", "a_move": "hop", "b_move": "still",
     "kid_tip": "The runner who finishes sooner is faster.", "tip": "Less time means faster."},
    {"a": "Fast sled", "b": "Slow sled", "a_pic": "🛷", "b_pic": "🛷", "a_move": "slide", "b_move": "still",
     "kid_tip": "The sled that gets there first is faster.", "tip": "Same hill, less time, faster."},
    {"a": "2-clap finish", "b": "5-clap finish", "a_pic": "👏", "b_pic": "👏", "a_move": "wiggle", "b_move": "still",
     "kid_tip": "Fewer claps of waiting means faster.", "tip": "Less time on the same path is faster."},
    {"a": "Early marble", "b": "Late marble", "a_pic": "🟠", "b_pic": "⚪", "a_move": "slide", "b_move": "still",
     "kid_tip": "The early marble is faster.", "tip": "Same track, first one is faster."},
    {"a": "Quick boat", "b": "Slow boat", "a_pic": "🚤", "b_pic": "🛶", "a_move": "splash", "b_move": "still",
     "kid_tip": "The boat that arrives first is faster.", "tip": "Same trip, less time, faster."},
    {"a": "Short wait", "b": "Long wait", "a_pic": "⏱️", "b_pic": "⏳", "a_move": "wiggle", "b_move": "still",
     "kid_tip": "A shorter wait for the same trip means faster.", "tip": "Less time means faster."},
    {"a": "First skateboard", "b": "Last skateboard", "a_pic": "🛹", "b_pic": "🛹", "a_move": "slide", "b_move": "still",
     "kid_tip": "First to the end is faster.", "tip": "Same path, sooner is faster."},
    {"a": "Blink-and-done", "b": "Slow crawl", "a_pic": "✨", "b_pic": "🐢", "a_move": "wiggle", "b_move": "still",
     "kid_tip": "Done in a blink is faster than a crawl.", "tip": "Same trip, less time, faster."},
)

run_steeper_goes_faster = compare_game(
    game_id="motion_advanced_steeper_goes_faster",
    title="Steeper Goes Faster",
    tagline="Which ramp makes more speed? Which ramp stays slow?",
    picture="🛝",
    pairs=STEEP,
    q_for_a="Which ramp makes more speed?",
    q_for_b="Which ramp stays slow?",
    tip="A steeper ramp makes it speed up more.",
)

run_two_pushes_add_up = compare_game(
    game_id="motion_advanced_two_pushes_add_up",
    title="Two Pushes Add Up",
    tagline="Which way do the pushes add? Which way loses?",
    picture="➡️",
    pairs=PUSHES,
    q_for_a="Which way do the pushes add?",
    q_for_b="Which way loses?",
    tip="Pushes in one direction add together.",
)

run_race_the_clock = compare_game(
    game_id="motion_advanced_race_the_clock",
    title="Race the Clock",
    tagline="Same trip. Who is faster? Who is slower?",
    picture="⏱️",
    pairs=CLOCK,
    q_for_a="Same trip. Who is faster?",
    q_for_b="Same trip. Who is slower?",
    tip="Less time for the same trip means faster.",
)
