"""Three playable science games."""
from __future__ import annotations
import sys
from pathlib import Path
_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))
from pair_trials import flip_two_choice
from science_utils import run_game

LIVING = (
    {"a": "Puppy", "b": "Toy car", "a_pic": "🐶", "b_pic": "🚗", "a_move": "bob", "b_move": "still",
     "kid_tip": "A puppy is living. A toy car is not.", "tip": "A puppy grows and needs food."},
    {"a": "Tree", "b": "Rock", "a_pic": "🌳", "b_pic": "🪨", "a_move": "grow", "b_move": "still",
     "kid_tip": "A tree is living. A rock is not.", "tip": "A tree grows. A rock does not."},
    {"a": "Fish", "b": "Boat", "a_pic": "🐟", "b_pic": "🚤", "a_move": "bob", "b_move": "still",
     "kid_tip": "A fish is living. A boat is not.", "tip": "A fish needs food and water."},
    {"a": "Bee", "b": "Bell", "a_pic": "🐝", "b_pic": "🔔", "a_move": "wiggle", "b_move": "still",
     "kid_tip": "A bee is living. A bell is not.", "tip": "A bee is a living insect."},
    {"a": "Flower", "b": "Crayon", "a_pic": "🌸", "b_pic": "🖍️", "a_move": "grow", "b_move": "still",
     "kid_tip": "A flower is living. A crayon is not.", "tip": "A flower grows. A crayon does not."},
    {"a": "Bird", "b": "Kite", "a_pic": "🐦", "b_pic": "🪁", "a_move": "bob", "b_move": "still",
     "kid_tip": "A bird is living. A kite is not.", "tip": "A bird eats and grows."},
    {"a": "Child", "b": "Doll", "a_pic": "🧒", "b_pic": "🪆", "a_move": "hop", "b_move": "still",
     "kid_tip": "A child is living. A doll is not.", "tip": "People are living. Dolls are toys."},
    {"a": "Worm", "b": "String", "a_pic": "🪱", "b_pic": "🧵", "a_move": "wiggle", "b_move": "still",
     "kid_tip": "A worm is living. String is not.", "tip": "A worm moves and eats."},
    {"a": "Grass", "b": "Paper", "a_pic": "🌱", "b_pic": "📄", "a_move": "grow", "b_move": "still",
     "kid_tip": "Grass is living. Paper is not.", "tip": "Grass grows. Paper does not."},
    {"a": "Cat", "b": "Cup", "a_pic": "🐱", "b_pic": "🥤", "a_move": "hop", "b_move": "still",
     "kid_tip": "A cat is living. A cup is not.", "tip": "A cat needs food and water."},
)

PLANT_ANIMAL = (
    {"a": "Sunflower", "b": "Rabbit", "a_pic": "🌻", "b_pic": "🐇", "a_move": "grow", "b_move": "hop",
     "kid_tip": "A sunflower is a plant. A rabbit is an animal.", "tip": "Plants stay put and grow. Animals can move around."},
    {"a": "Tree", "b": "Bird", "a_pic": "🌳", "b_pic": "🐦", "a_move": "grow", "b_move": "bob",
     "kid_tip": "A tree is a plant. A bird is an animal.", "tip": "A tree is a plant. A bird is an animal."},
    {"a": "Grass", "b": "Puppy", "a_pic": "🌱", "b_pic": "🐶", "a_move": "grow", "b_move": "bob",
     "kid_tip": "Grass is a plant. A puppy is an animal.", "tip": "Grass is a plant. A puppy is an animal."},
    {"a": "Cactus", "b": "Lizard", "a_pic": "🌵", "b_pic": "🦎", "a_move": "still", "b_move": "hop",
     "kid_tip": "A cactus is a plant. A lizard is an animal.", "tip": "A cactus is a plant. A lizard is an animal."},
    {"a": "Fern", "b": "Frog", "a_pic": "🌿", "b_pic": "🐸", "a_move": "grow", "b_move": "hop",
     "kid_tip": "A fern is a plant. A frog is an animal.", "tip": "A fern is a plant. A frog is an animal."},
    {"a": "Apple tree", "b": "Squirrel", "a_pic": "🍎", "b_pic": "🐿️", "a_move": "grow", "b_move": "hop",
     "kid_tip": "An apple tree is a plant. A squirrel is an animal.", "tip": "Trees are plants. Squirrels are animals."},
    {"a": "Tulip", "b": "Bee", "a_pic": "🌷", "b_pic": "🐝", "a_move": "grow", "b_move": "wiggle",
     "kid_tip": "A tulip is a plant. A bee is an animal.", "tip": "A tulip is a plant. A bee is an animal."},
    {"a": "Moss", "b": "Snail", "a_pic": "🥬", "b_pic": "🐌", "a_move": "still", "b_move": "bob",
     "kid_tip": "Moss is a plant. A snail is an animal.", "tip": "Moss is a plant. A snail is an animal."},
    {"a": "Corn", "b": "Pig", "a_pic": "🌽", "b_pic": "🐷", "a_move": "grow", "b_move": "hop",
     "kid_tip": "Corn is a plant. A pig is an animal.", "tip": "Corn is a plant. A pig is an animal."},
    {"a": "Seaweed", "b": "Fish", "a_pic": "🌾", "b_pic": "🐟", "a_move": "wiggle", "b_move": "bob",
     "kid_tip": "Seaweed is a plant. A fish is an animal.", "tip": "Seaweed is a plant. A fish is an animal."},
)

HUNGRY = (
    {"a": "Food", "b": "A toy", "a_pic": "🪱", "b_pic": "🧸", "a_move": "bob", "b_move": "still",
     "kid_tip": "A hungry bird needs food, not a toy.", "tip": "Living animals need food."},
    {"a": "Water", "b": "A hat", "a_pic": "💧", "b_pic": "🎩", "a_move": "splash", "b_move": "still",
     "kid_tip": "A thirsty puppy needs water, not a hat.", "tip": "Living animals need water."},
    {"a": "Seeds", "b": "A rock", "a_pic": "🌾", "b_pic": "🪨", "a_move": "bob", "b_move": "still",
     "kid_tip": "A hungry hamster needs seeds, not a rock.", "tip": "Animals eat food, not rocks."},
    {"a": "Grass", "b": "A ball", "a_pic": "🌱", "b_pic": "⚽", "a_move": "grow", "b_move": "still",
     "kid_tip": "A hungry cow needs grass, not a ball.", "tip": "Cows eat plants such as grass."},
    {"a": "Fish food", "b": "A button", "a_pic": "🐟", "b_pic": "🔘", "a_move": "bob", "b_move": "still",
     "kid_tip": "A hungry fish needs fish food, not a button.", "tip": "Fish need food."},
    {"a": "Carrot", "b": "A key", "a_pic": "🥕", "b_pic": "🔑", "a_move": "bob", "b_move": "still",
     "kid_tip": "A hungry rabbit needs a carrot, not a key.", "tip": "Rabbits eat plants such as carrots."},
    {"a": "Leaves", "b": "A shoe", "a_pic": "🍃", "b_pic": "👟", "a_move": "grow", "b_move": "still",
     "kid_tip": "A hungry caterpillar needs leaves, not a shoe.", "tip": "Caterpillars eat leaves."},
    {"a": "Nectar", "b": "A coin", "a_pic": "🍯", "b_pic": "🪙", "a_move": "wiggle", "b_move": "still",
     "kid_tip": "A hungry bee needs nectar, not a coin.", "tip": "Bees drink nectar from flowers."},
    {"a": "Bamboo", "b": "A book", "a_pic": "🎋", "b_pic": "📘", "a_move": "grow", "b_move": "still",
     "kid_tip": "A hungry panda needs bamboo, not a book.", "tip": "Pandas eat bamboo."},
    {"a": "Berries", "b": "A sock", "a_pic": "🫐", "b_pic": "🧦", "a_move": "bob", "b_move": "still",
     "kid_tip": "A hungry bear needs berries, not a sock.", "tip": "Bears eat food such as berries."},
)


def run_living_or_not() -> None:
    run_game({
        "id": "living_things_beginner_living_or_not",
        "title": "Living or Not",
        "tagline": "Which one is living? Which one is not living?",
        "question": "Which one is living?",
        "choices": ["Puppy", "Toy car"],
        "answer": "Puppy",
        "picture": "🐶",
        "scene": "living_or_not",
        "animate_mode": "once",
        "trials": flip_two_choice(
            LIVING, a="a", b="b",
            q_for_a="Which one is living?", q_for_b="Which one is not living?",
            scene="living_or_not",
        ),
        "kid_tip": "A puppy is living. A toy car is not.",
        "tip": "A puppy grows and needs food.",
    })


def run_plant_or_animal() -> None:
    run_game({
        "id": "living_things_beginner_plant_or_animal",
        "title": "Plant or Animal",
        "tagline": "Which one is a plant? Which one is an animal?",
        "question": "Which one is a plant?",
        "choices": ["Sunflower", "Rabbit"],
        "answer": "Sunflower",
        "picture": "🌻",
        "scene": "plant_or_animal",
        "animate_mode": "once",
        "trials": flip_two_choice(
            PLANT_ANIMAL, a="a", b="b",
            q_for_a="Which one is a plant?", q_for_b="Which one is an animal?",
            scene="plant_or_animal",
        ),
        "kid_tip": "A sunflower is a plant. A rabbit is an animal.",
        "tip": "A sunflower is a plant.",
    })


def run_hungry_or_full() -> None:
    run_game({
        "id": "living_things_beginner_hungry_or_full",
        "title": "Hungry or Full",
        "tagline": "What does a living thing need?",
        "question": "What does the hungry bird need?",
        "choices": ["Food", "A toy"],
        "answer": "Food",
        "picture": "🐦",
        "scene": "hungry_or_full",
        "animate_mode": "once",
        "trials": flip_two_choice(
            HUNGRY, a="a", b="b",
            q_for_a="What does the hungry one need?", q_for_b="What does the hungry one not need?",
            scene="hungry_or_full",
        ),
        "kid_tip": "A hungry bird needs food, not a toy.",
        "tip": "Living animals need food.",
    })
