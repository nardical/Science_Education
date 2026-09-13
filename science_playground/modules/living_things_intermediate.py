"""Living Things — Intermediate: 10 picture pairs per game."""
from __future__ import annotations
import sys
from pathlib import Path
_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))
from pair_trials import compare_game

NEEDS = (
    {"a": "Water", "b": "Plastic beads", "a_pic": "💧", "b_pic": "🔵", "a_move": "splash", "b_move": "still",
     "kid_tip": "A plant needs water, not beads.", "tip": "Plants need water, light, and air."},
    {"a": "Sunlight", "b": "A closed box", "a_pic": "☀️", "b_pic": "📦", "a_move": "grow", "b_move": "still",
     "kid_tip": "A plant needs light, not a closed box.", "tip": "Plants use light to grow."},
    {"a": "Air", "b": "A sealed jar", "a_pic": "🌬️", "b_pic": "🫙", "a_move": "wiggle", "b_move": "still",
     "kid_tip": "A plant needs air.", "tip": "Living plants need air."},
    {"a": "Soil", "b": "A candy wrapper", "a_pic": "🌱", "b_pic": "🍬", "a_move": "grow", "b_move": "still",
     "kid_tip": "Roots need soil, not a wrapper.", "tip": "Soil holds water and food for plants."},
    {"a": "Rain", "b": "A toy car", "a_pic": "🌧️", "b_pic": "🚗", "a_move": "splash", "b_move": "still",
     "kid_tip": "Rain can water a plant. A toy car cannot.", "tip": "Water helps a plant grow."},
    {"a": "Window light", "b": "A dark closet", "a_pic": "🪟", "b_pic": "🚪", "a_move": "grow", "b_move": "still",
     "kid_tip": "Window light helps. A closet is too dark.", "tip": "Plants need light."},
    {"a": "A drink of water", "b": "A hat", "a_pic": "🚰", "b_pic": "🎩", "a_move": "splash", "b_move": "still",
     "kid_tip": "A thirsty plant needs water, not a hat.", "tip": "Living things need water."},
    {"a": "Fresh air", "b": "A plastic bag", "a_pic": "🍃", "b_pic": "🛍️", "a_move": "wiggle", "b_move": "still",
     "kid_tip": "Fresh air helps. A bag can block air.", "tip": "Plants need air."},
    {"a": "Garden soil", "b": "A sock", "a_pic": "🟤", "b_pic": "🧦", "a_move": "grow", "b_move": "still",
     "kid_tip": "Soil helps roots. A sock does not.", "tip": "Roots grow in soil."},
    {"a": "Sun", "b": "A night-light only", "a_pic": "🌞", "b_pic": "💡", "a_move": "grow", "b_move": "still",
     "kid_tip": "Sunlight is the plant’s best light.", "tip": "Plants grow well with sunlight."},
)

EATS = (
    {"a": "Grass", "b": "Pebbles", "a_pic": "🌱", "b_pic": "🪨", "a_move": "grow", "b_move": "still",
     "kid_tip": "A rabbit eats grass, not pebbles.", "tip": "Rabbits eat plants such as grass."},
    {"a": "Carrot", "b": "A key", "a_pic": "🥕", "b_pic": "🔑", "a_move": "bob", "b_move": "still",
     "kid_tip": "A rabbit can eat a carrot, not a key.", "tip": "Animals eat food that fits them."},
    {"a": "Seeds", "b": "A button", "a_pic": "🌾", "b_pic": "🔘", "a_move": "bob", "b_move": "still",
     "kid_tip": "A bird eats seeds, not a button.", "tip": "Birds eat food such as seeds."},
    {"a": "Fish food", "b": "A coin", "a_pic": "🐟", "b_pic": "🪙", "a_move": "bob", "b_move": "still",
     "kid_tip": "A fish needs fish food, not a coin.", "tip": "Fish need food."},
    {"a": "Bamboo", "b": "A book", "a_pic": "🎋", "b_pic": "📘", "a_move": "grow", "b_move": "still",
     "kid_tip": "A panda eats bamboo, not a book.", "tip": "Pandas eat bamboo."},
    {"a": "Leaves", "b": "A shoe", "a_pic": "🍃", "b_pic": "👟", "a_move": "grow", "b_move": "still",
     "kid_tip": "A caterpillar eats leaves, not a shoe.", "tip": "Caterpillars eat leaves."},
    {"a": "Nectar", "b": "A marble", "a_pic": "🍯", "b_pic": "⚪", "a_move": "wiggle", "b_move": "still",
     "kid_tip": "A bee drinks nectar, not a marble.", "tip": "Bees drink nectar from flowers."},
    {"a": "Berries", "b": "A sock", "a_pic": "🫐", "b_pic": "🧦", "a_move": "bob", "b_move": "still",
     "kid_tip": "A bear can eat berries, not a sock.", "tip": "Bears eat food such as berries."},
    {"a": "Hay", "b": "A crayon", "a_pic": "🌾", "b_pic": "🖍️", "a_move": "grow", "b_move": "still",
     "kid_tip": "A horse eats hay, not a crayon.", "tip": "Horses eat plants such as hay."},
    {"a": "Worms", "b": "A toy", "a_pic": "🪱", "b_pic": "🧸", "a_move": "wiggle", "b_move": "still",
     "kid_tip": "A bird can eat a worm, not a toy.", "tip": "Animals eat food, not toys."},
)

HOME = (
    {"a": "Pond", "b": "Dry sandbox", "a_pic": "🐟", "b_pic": "🏖️", "a_move": "bob", "b_move": "still",
     "kid_tip": "A fish belongs in a pond, not a dry sandbox.", "tip": "A pond gives fish water and food."},
    {"a": "Nest", "b": "Refrigerator", "a_pic": "🪺", "b_pic": "❄️", "a_move": "bob", "b_move": "shiver",
     "kid_tip": "A bird belongs in a nest, not a fridge.", "tip": "A nest is a bird’s home."},
    {"a": "Forest", "b": "Bathtub", "a_pic": "🌲", "b_pic": "🛁", "a_move": "grow", "b_move": "still",
     "kid_tip": "A deer belongs in a forest.", "tip": "A habitat is a fitting home."},
    {"a": "Hive", "b": "Pencil box", "a_pic": "🐝", "b_pic": "✏️", "a_move": "wiggle", "b_move": "still",
     "kid_tip": "A bee belongs in a hive.", "tip": "A hive is a bee’s home."},
    {"a": "Burrow", "b": "Oven", "a_pic": "🐇", "b_pic": "🔥", "a_move": "hop", "b_move": "steam",
     "kid_tip": "A rabbit belongs in a burrow, not an oven.", "tip": "A burrow is a rabbit home."},
    {"a": "Ocean", "b": "Closet", "a_pic": "🌊", "b_pic": "🚪", "a_move": "splash", "b_move": "still",
     "kid_tip": "A whale belongs in the ocean.", "tip": "An ocean is a fitting water home."},
    {"a": "Tree", "b": "Shoebox", "a_pic": "🌳", "b_pic": "📦", "a_move": "grow", "b_move": "still",
     "kid_tip": "A squirrel belongs in a tree.", "tip": "A tree can be a squirrel home."},
    {"a": "Pond weeds", "b": "Bookshelf", "a_pic": "🐸", "b_pic": "📚", "a_move": "hop", "b_move": "still",
     "kid_tip": "A frog belongs by pond weeds.", "tip": "Frogs need a wet home."},
    {"a": "Meadow", "b": "Cookie jar", "a_pic": "🌼", "b_pic": "🍪", "a_move": "grow", "b_move": "still",
     "kid_tip": "A butterfly belongs in a meadow.", "tip": "A meadow has flowers for food."},
    {"a": "Web", "b": "Toothbrush cup", "a_pic": "🕷️", "b_pic": "🪥", "a_move": "wiggle", "b_move": "still",
     "kid_tip": "A spider belongs on a web.", "tip": "A web is a spider’s home."},
)

run_what_does_it_need = compare_game(
    game_id="living_things_intermediate_what_does_it_need",
    title="What Does It Need?",
    tagline="What helps it grow? What does not help?",
    picture="🌱",
    pairs=NEEDS,
    q_for_a="What helps this living thing grow?",
    q_for_b="What does not help it grow?",
    tip="Plants need water, light, and air.",
)

run_who_eats_what = compare_game(
    game_id="living_things_intermediate_who_eats_what",
    title="Who Eats What?",
    tagline="What should it eat? What is not food?",
    picture="🐇",
    pairs=EATS,
    q_for_a="What should it eat?",
    q_for_b="What is not food?",
    tip="Animals eat food that fits them.",
)

run_home_habitat = compare_game(
    game_id="living_things_intermediate_home_habitat",
    title="Home Habitat",
    tagline="Where does it belong? Where does it not belong?",
    picture="🐟",
    pairs=HOME,
    q_for_a="Where does it belong?",
    q_for_b="Where does it not belong?",
    tip="A habitat is a living thing’s fitting home.",
)
