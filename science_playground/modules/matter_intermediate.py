"""Matter — Intermediate: 10 picture pairs per game."""
from __future__ import annotations
import sys
from pathlib import Path
_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))
from pair_trials import compare_game

ICE = (
    {"a": "Ice in sun", "b": "Ice in freezer", "a_pic": "🧊", "b_pic": "❄️", "a_move": "splash", "b_move": "still",
     "kid_tip": "Sun-warmed ice turns to water. Freezer ice stays ice.",
     "tip": "Heating can turn ice into water."},
    {"a": "Popsicle outside", "b": "Popsicle in freezer", "a_pic": "🍭", "b_pic": "❄️", "a_move": "splash", "b_move": "still",
     "kid_tip": "A popsicle outside melts. A freezer popsicle stays frozen.",
     "tip": "Heat changes ice to water."},
    {"a": "Snowman in sun", "b": "Snowman in snow", "a_pic": "⛄", "b_pic": "❄️", "a_move": "splash", "b_move": "still",
     "kid_tip": "Sun can melt the snowman.", "tip": "Warmth melts snow."},
    {"a": "Butter on toast", "b": "Butter in fridge", "a_pic": "🍞", "b_pic": "🧈", "a_move": "splash", "b_move": "still",
     "kid_tip": "Warm toast melts butter. Fridge butter stays firm.",
     "tip": "Heat can melt butter."},
    {"a": "Chocolate in pocket", "b": "Chocolate in fridge", "a_pic": "🍫", "b_pic": "❄️", "a_move": "splash", "b_move": "still",
     "kid_tip": "A warm pocket melts chocolate.", "tip": "Heat can melt chocolate."},
    {"a": "Ice on sidewalk", "b": "Ice in shade", "a_pic": "☀️", "b_pic": "🌳", "a_move": "splash", "b_move": "still",
     "kid_tip": "Sunny sidewalk ice melts. Shade ice lasts longer.",
     "tip": "Sun can heat ice until it melts."},
    {"a": "Ice by heater", "b": "Ice in cooler", "a_pic": "🌡️", "b_pic": "🧊", "a_move": "splash", "b_move": "still",
     "kid_tip": "A heater melts ice. A cooler keeps it.", "tip": "Heating changes ice to water."},
    {"a": "Pond at noon", "b": "Pond at night", "a_pic": "🌞", "b_pic": "🌙", "a_move": "splash", "b_move": "still",
     "kid_tip": "Noon sun can melt pond ice. Night can keep it frozen.",
     "tip": "Warmth melts. Cold keeps ice."},
    {"a": "Ice cube on plate", "b": "Ice cube in freezer", "a_pic": "🍽️", "b_pic": "🧊", "a_move": "splash", "b_move": "still",
     "kid_tip": "A plate in a warm room melts the cube.", "tip": "Heating turns ice into water."},
    {"a": "Candle wax drip", "b": "Wax in drawer", "a_pic": "🕯️", "b_pic": "📦", "a_move": "splash", "b_move": "still",
     "kid_tip": "Warm wax drips. Cool wax stays firm.", "tip": "Heat can melt wax."},
)

SAME = (
    {"a": "Ice and water", "b": "Ice and juice", "a_pic": "🧊", "b_pic": "🧃", "a_move": "splash", "b_move": "still",
     "kid_tip": "Ice and water are the same stuff. Ice and juice are not.",
     "tip": "Melting changes the look, not the stuff."},
    {"a": "Chocolate puddle", "b": "Chocolate and cookie", "a_pic": "🍫", "b_pic": "🍪", "a_move": "splash", "b_move": "still",
     "kid_tip": "Melted chocolate is still chocolate.", "tip": "Melting changes form, not the stuff."},
    {"a": "Snow and water", "b": "Snow and sand", "a_pic": "❄️", "b_pic": "🏖️", "a_move": "splash", "b_move": "still",
     "kid_tip": "Snow and water are the same stuff.", "tip": "Snow is frozen water."},
    {"a": "Steam and water", "b": "Steam and soup", "a_pic": "♨️", "b_pic": "🍲", "a_move": "steam", "b_move": "steam",
     "kid_tip": "Steam from a kettle is still water.", "tip": "Warm water can become vapor."},
    {"a": "Ice cube and puddle", "b": "Ice cube and rock", "a_pic": "🧊", "b_pic": "🪨", "a_move": "splash", "b_move": "still",
     "kid_tip": "A puddle from ice is still water.", "tip": "Melted ice is still water."},
    {"a": "Wax and drip", "b": "Wax and honey", "a_pic": "🕯️", "b_pic": "🍯", "a_move": "splash", "b_move": "still",
     "kid_tip": "Dripped wax is still wax.", "tip": "Melted wax is the same stuff."},
    {"a": "Frozen juice and juice", "b": "Frozen juice and soda", "a_pic": "🧃", "b_pic": "🥤", "a_move": "splash", "b_move": "still",
     "kid_tip": "Frozen juice is still juice.", "tip": "Freezing changes the look, not the stuff."},
    {"a": "Butter puddle", "b": "Butter and milk", "a_pic": "🧈", "b_pic": "🥛", "a_move": "splash", "b_move": "still",
     "kid_tip": "Melted butter is still butter.", "tip": "Melting does not make new stuff."},
    {"a": "Cloud and rain", "b": "Cloud and smoke", "a_pic": "☁️", "b_pic": "💨", "a_move": "steam", "b_move": "steam",
     "kid_tip": "Rain and many clouds are water. Smoke is different.",
     "tip": "Rain is water falling from clouds."},
    {"a": "Ice pop and juice", "b": "Ice pop and stone", "a_pic": "🍭", "b_pic": "🪨", "a_move": "splash", "b_move": "still",
     "kid_tip": "A melted ice pop is still the juice.", "tip": "The look changes. The stuff stays."},
)

MIX = (
    {"a": "Sand and water", "b": "Sugar and water", "a_pic": "🏖️", "b_pic": "🍬", "a_move": "still", "b_move": "splash",
     "kid_tip": "Sand settles. Sugar stays mixed.", "tip": "Sand does not disappear. It settles."},
    {"a": "Oil and water", "b": "Juice and water", "a_pic": "🛢️", "b_pic": "🧃", "a_move": "still", "b_move": "splash",
     "kid_tip": "Oil sits apart. Juice mixes.", "tip": "Some mixes stay mixed. Some settle."},
    {"a": "Mud and water", "b": "Salt and water", "a_pic": "🟤", "b_pic": "🧂", "a_move": "still", "b_move": "splash",
     "kid_tip": "Mud settles. Salt stays mixed.", "tip": "Salt can stay mixed in water."},
    {"a": "Leaves and water", "b": "Honey and tea", "a_pic": "🍃", "b_pic": "🍯", "a_move": "still", "b_move": "splash",
     "kid_tip": "Leaves float or settle. Honey mixes into tea.", "tip": "Leaves do not disappear."},
    {"a": "Rocks and water", "b": "Milk and cocoa", "a_pic": "🪨", "b_pic": "☕", "a_move": "still", "b_move": "splash",
     "kid_tip": "Rocks settle. Cocoa mixes.", "tip": "Heavy bits can settle."},
    {"a": "Pepper and water", "b": "Lemon and water", "a_pic": "🌶️", "b_pic": "🍋", "a_move": "still", "b_move": "splash",
     "kid_tip": "Pepper sits on top. Lemon mixes.", "tip": "Some bits stay apart."},
    {"a": "Wood chips and water", "b": "Soap and water", "a_pic": "🪵", "b_pic": "🧼", "a_move": "still", "b_move": "splash",
     "kid_tip": "Wood chips stay apart. Soap mixes.", "tip": "Soap can stay mixed."},
    {"a": "Gravel and water", "b": "Paint and water", "a_pic": "🪨", "b_pic": "🎨", "a_move": "still", "b_move": "splash",
     "kid_tip": "Gravel settles. Paint can mix.", "tip": "Heavy gravel sinks and sits."},
    {"a": "Corks and water", "b": "Syrup and water", "a_pic": "🪵", "b_pic": "🍯", "a_move": "still", "b_move": "splash",
     "kid_tip": "Corks stay apart. Syrup mixes.", "tip": "Corks do not disappear."},
    {"a": "Dirt and water", "b": "Kool-Aid and water", "a_pic": "🟤", "b_pic": "🥤", "a_move": "still", "b_move": "splash",
     "kid_tip": "Dirt settles. The drink mix stays mixed.", "tip": "Some mixes stay mixed. Sand and dirt settle."},
)

run_ice_to_water = compare_game(
    game_id="matter_intermediate_ice_to_water",
    title="Ice to Water",
    tagline="Which ice turns to water? Which ice stays ice?",
    picture="🧊",
    pairs=ICE,
    q_for_a="Which one turns to water?",
    q_for_b="Which one stays frozen?",
    tip="Heating can turn ice into water.",
)

run_same_stuff_new_look = compare_game(
    game_id="matter_intermediate_same_stuff_new_look",
    title="Same Stuff, New Look",
    tagline="Which pair is the same stuff? Which pair is different?",
    picture="🍫",
    pairs=SAME,
    q_for_a="Which pair is the same stuff?",
    q_for_b="Which pair is different stuff?",
    tip="Melting changes the look, not the stuff.",
)

run_mix_or_settle = compare_game(
    game_id="matter_intermediate_mix_or_settle",
    title="Mix or Settle",
    tagline="Which mix settles? Which mix stays mixed?",
    picture="🥛",
    pairs=MIX,
    q_for_a="Which mix settles apart?",
    q_for_b="Which mix stays mixed?",
    tip="Sand does not disappear. It settles.",
)
