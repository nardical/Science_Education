"""Guided lesson map: 21 stories (7 topics × 3 levels) wrapping the 63 games.

Lessons are not extra quizzes. Each one is a grown-up + kid picture walk:
Look → Name → (sometimes Change) → Play the matching games.
"""
from __future__ import annotations

from typing import Any

Lesson = dict[str, Any]
Scene = dict[str, Any]


def _g(label: str, file: str, entry: str, icon: str) -> dict[str, str]:
    return {"label": label, "file": file, "entry": entry, "icon": icon}


def _ask(question: str, choices: list[str], answer: str, kid_tip: str) -> dict[str, Any]:
    return {"question": question, "choices": choices, "answer": answer, "kid_tip": kid_tip}


def _scene(
    title: str,
    icon: str,
    look: str,
    name: dict[str, Any],
    game: dict[str, str],
    *,
    change: dict[str, Any] | None = None,
    science: str = "",
    look_scene: dict[str, Any] | None = None,
    look_pose: str | None = None,
) -> Scene:
    scene: Scene = {
        "title": title,
        "icon": icon,
        "look": look,
        "name": name,
        "game": game,
        "science": science,
    }
    if change:
        scene["change"] = change
    if look_scene:
        scene["look_scene"] = look_scene
        scene["look_pose"] = look_pose or "start"
    return scene


# --- Beginner ---------------------------------------------------------------

_BEGINNER_MOTION = {
    "id": "beginner_motion",
    "level": "Beginner",
    "topic": "Motion",
    "label": "Go, Stop, Push, Pull",
    "icon": "🚗",
    "blurb": "See fast and slow. Watch stop and go. Feel push and pull.",
    "minutes": 6,
    "wave": 1,
    "playable": True,
    "big_idea": "Things can move fast or slow. A push or a pull can start a move.",
    "kid_words": ["fast", "slow", "stop", "go", "push", "pull"],
    "grown_up": "Sit together. Read the blue line aloud. Let the child tap. Do not score.",
    "hands_on": "Push a toy car away, then pull it back. Say “push.” Say “pull.”",
    "scenes": [
        _scene(
            "Fast or Slow",
            "🏎️",
            "Watch the race car and the snail. One zooms. One creeps.",
            _ask("Which one is fast?", ["Race car", "Snail"], "Race car", "The car zooms. The snail creeps."),
            _g("Fast or Slow", "motion_beginner.py", "run_fast_or_slow", "🏎️"),
            science="Fast means it gets there sooner.",
            look_scene={"id": "lesson_fast_slow", "scene": "fast_slow", "picture": "🏎️", "question": "Which one is fast?"},
            look_pose="play",
        ),
        _scene(
            "Stop or Go",
            "🚦",
            "The light is green. Watch the car.",
            _ask("The light is green. What should the car do?", ["Go", "Stop"], "Go", "Green light means go!"),
            _g("Stop or Go", "motion_beginner.py", "run_stop_or_go", "🚦"),
            change={
                "say": "Now the light is red.",
                "look_scene": {"id": "lesson_stop_go_red", "scene": "stop_go", "picture": "🚦", "light": "red", "question": "What should the car do?"},
                "look_pose": "start",
                **_ask("The light is red. What should the car do?", ["Go", "Stop"], "Stop", "Red light means stop!"),
            },
            science="Green means go. Red means stop.",
            look_scene={"id": "lesson_stop_go", "scene": "stop_go", "picture": "🚦", "light": "green", "question": "What should the car do?"},
            look_pose="start",
        ),
        _scene(
            "Push or Pull",
            "🛒",
            "The kid wants the wagon closer.",
            _ask("Move the wagon toward the kid.", ["Push", "Pull"], "Pull", "Pull brings the wagon toward the kid."),
            _g("Push or Pull", "motion_beginner.py", "run_push_or_pull", "🛒"),
            science="A pull moves something toward you. A push moves it away.",
            look_scene={
                "id": "lesson_push_pull",
                "scene": "push_pull",
                "picture": "🛒",
                "kind": "wagon",
                "actor": "kid",
                "action": "pull",
                "question": "Move the wagon toward the kid.",
            },
            look_pose="idle",
        ),
    ],
}

_BEGINNER_FORCES = {
    "id": "beginner_forces",
    "level": "Beginner",
    "topic": "Forces & Stuff",
    "label": "Heavy, Float, Sticky",
    "icon": "🧲",
    "blurb": "Feel heavy and light. Guess sink or float. Spot sticky or slippy.",
    "minutes": 6,
    "wave": 1,
    "playable": True,
    "big_idea": "Some things feel heavy. Some things float. Some floors are slippy.",
    "kid_words": ["heavy", "light", "sink", "float", "sticky", "slippy"],
    "grown_up": "Use real objects if you can: a rock, a leaf, a rubber duck, a coin.",
    "hands_on": "Hold a rock and a leaf. Drop both. Which hits first? Then try a duck and a coin in water.",
    "scenes": [
        _scene(
            "Heavy or Light",
            "🪨",
            "A rock and a feather fall. Watch how they move.",
            _ask("Which one is heavy?", ["Rock", "Feather"], "Rock", "The rock is heavier than the feather."),
            _g("Heavy or Light", "forces_stuff_beginner.py", "run_heavy_or_light", "🪨"),
            science="Heavy things are harder to lift.",
            look_scene={
                "id": "lesson_heavy_light",
                "scene": "heavy_light",
                "picture": "🪨",
                "heavy": "Rock",
                "light": "Feather",
                "heavy_pic": "🪨",
                "light_pic": "🪶",
                "question": "Which one is heavy?",
            },
            look_pose="play",
        ),
        _scene(
            "Sink or Float",
            "🦆",
            "We drop a rubber duck in a tank of water.",
            _ask("Will the duck sink or float?", ["Float", "Sink"], "Float", "A rubber duck is light for its size, so it floats."),
            _g("Sink or Float", "forces_stuff_beginner.py", "run_sink_or_float", "🦆"),
            change={
                "say": "Now we drop a rock in the same water.",
                "look_scene": {
                    "id": "lesson_sink_float_rock",
                    "scene": "sink_float",
                    "picture": "🪨",
                    "item": "Rock",
                    "kind": "rock",
                    "answer": "Sink",
                    "question": "Will the rock sink or float?",
                },
                "look_pose": "play",
                **_ask("Will the rock sink or float?", ["Float", "Sink"], "Sink", "The rock sinks."),
            },
            science="Some things stay on top of water. Some go down.",
            look_scene={
                "id": "lesson_sink_float_duck",
                "scene": "sink_float",
                "picture": "🦆",
                "item": "Rubber duck",
                "kind": "duck",
                "answer": "Float",
                "question": "Will the duck sink or float?",
            },
            look_pose="play",
        ),
        _scene(
            "Sticky or Slippy",
            "⛸️",
            "A box sits on a rug. Another box sits on ice. Watch which box slides.",
            _ask("Which floor is slippy?", ["Smooth ice", "Rough rug"], "Smooth ice", "The ice lets the box slide."),
            _g("Sticky or Slippy", "forces_stuff_beginner.py", "run_sticky_or_slippy", "⛸️"),
            science="Slippy floors have less grip. Sticky floors hold on.",
            look_scene={
                "id": "lesson_sticky",
                "scene": "sticky_slippy",
                "picture": "⛸️",
                "sticky": "Rough rug",
                "slippy": "Smooth ice",
                "sticky_kind": "rug",
                "slippy_kind": "ice",
                "sticky_left": True,
                "question": "Which floor is slippy?",
            },
            look_pose="play",
        ),
    ],
}

_BEGINNER_LIGHT = {
    "id": "beginner_light_sound",
    "level": "Beginner",
    "topic": "Light & Sound",
    "label": "Bright, Loud, High",
    "icon": "🔦",
    "blurb": "Find light and dark. Hear loud and quiet. Hear high and low.",
    "minutes": 6,
    "wave": 2,
    "playable": True,
    "big_idea": "Light makes a place bright. Sounds can be loud or quiet, high or low.",
    "kid_words": ["light", "dark", "loud", "quiet", "high", "low"],
    "grown_up": "Whisper, then clap. Ring a small bell, then tap a pot. Keep it playful.",
    "hands_on": "Open a closet, then a sunny window. Whisper, then clap. Tiny bell, then a big pot.",
    "scenes": [
        _scene(
            "Light or Dark",
            "☀️",
            "A sunny yard and a closed closet.",
            _ask("Which place is light?", ["Sunny yard", "Closed closet"], "Sunny yard", "Sunlight makes the yard bright."),
            _g("Light or Dark", "light_sound_beginner.py", "run_light_or_dark", "☀️"),
            science="Light makes things easy to see.",
            look_scene={"id": "lesson_light_dark", "scene": "light_or_dark", "picture": "☀️", "question": "Which place is light?"},
            look_pose="play",
        ),
        _scene(
            "Loud or Quiet",
            "🥁",
            "A whisper and a drum.",
            _ask("Which sound is loud?", ["Drum", "Whisper"], "Drum", "A drum makes a loud sound."),
            _g("Loud or Quiet", "light_sound_beginner.py", "run_loud_or_quiet", "🥁"),
            science="Loud sounds are bigger in our ears.",
            look_scene={"id": "lesson_loud_quiet", "scene": "loud_or_quiet", "picture": "🥁", "question": "Which sound is loud?"},
            look_pose="play",
        ),
        _scene(
            "High or Low",
            "🔔",
            "A tiny bell and a big drum.",
            _ask("Which makes a high sound?", ["Tiny bell", "Big drum"], "Tiny bell", "A tiny bell often has high pitch."),
            _g("High or Low", "light_sound_beginner.py", "run_high_or_low", "🔔"),
            science="High sounds are squeaky. Low sounds are boomy.",
            look_scene={"id": "lesson_high_low", "scene": "high_or_low", "picture": "🔔", "question": "Which makes a high sound?"},
            look_pose="play",
        ),
    ],
}

_BEGINNER_MATTER = {
    "id": "beginner_matter",
    "level": "Beginner",
    "topic": "Matter",
    "label": "Splash, Cold, Melt",
    "icon": "🧊",
    "blurb": "Spot splashy stuff. Feel hot and cold. Watch ice melt.",
    "minutes": 6,
    "wave": 2,
    "playable": True,
    "big_idea": "Some stuff holds its shape. Water can splash. Warm ice melts.",
    "kid_words": ["solid", "splash", "hot", "cold", "melt", "freeze"],
    "grown_up": "An ice cube on a plate is the whole lab. Watch it together.",
    "hands_on": "Put an ice cube on a plate in a warm room. Check again later. What happened?",
    "scenes": [
        _scene(
            "Solid or Splash",
            "💦",
            "A wood block and a puddle of water.",
            _ask("Which one can splash?", ["Water", "Wood block"], "Water", "Liquid water can splash."),
            _g("Solid or Splash", "matter_beginner.py", "run_solid_or_splash", "💦"),
            science="Water takes the shape of its cup. A block keeps its own shape.",
            look_scene={"id": "lesson_solid_splash", "scene": "solid_or_splash", "picture": "💦", "question": "Which one can splash?"},
            look_pose="play",
        ),
        _scene(
            "Hot or Cold",
            "🧊",
            "An ice cube and warm soup.",
            _ask("Which one feels cold?", ["Ice cube", "Warm soup"], "Ice cube", "Ice is cold."),
            _g("Hot or Cold", "matter_beginner.py", "run_hot_or_cold", "🧊"),
            science="Cold and hot are how something feels.",
            look_scene={"id": "lesson_hot_cold", "scene": "hot_or_cold", "picture": "🧊", "question": "Which one feels cold?"},
            look_pose="play",
        ),
        _scene(
            "Melt or Freeze",
            "🌡️",
            "The ice cube sits in a warm room.",
            _ask("Ice warms. What happens?", ["Melt", "Freeze"], "Melt", "Warm ice melts into water."),
            _g("Melt or Freeze", "matter_beginner.py", "run_melt_or_freeze", "🌡️"),
            science="Warm ice becomes water.",
            look_scene={"id": "lesson_melt", "scene": "melt_or_freeze", "picture": "🌡️", "question": "Ice warms. What happens?"},
            look_pose="play",
        ),
    ],
}

_BEGINNER_LIVING = {
    "id": "beginner_living",
    "level": "Beginner",
    "topic": "Living Things",
    "label": "Alive, Plant, Hungry",
    "icon": "🌱",
    "blurb": "Spot living things. Tell plant from animal. Feed a hungry bird.",
    "minutes": 6,
    "wave": 2,
    "playable": True,
    "big_idea": "Living things grow and need food. Plants and animals are both alive.",
    "kid_words": ["living", "plant", "animal", "hungry", "food"],
    "grown_up": "A houseplant and a stuffed toy make this concrete. The toy is not living.",
    "hands_on": "Look at a plant and a toy car. Which one grows if you give it water and light?",
    "scenes": [
        _scene(
            "Living or Not",
            "🐶",
            "A puppy and a toy car.",
            _ask("Which one is living?", ["Puppy", "Toy car"], "Puppy", "A puppy grows and needs food."),
            _g("Living or Not", "living_things_beginner.py", "run_living_or_not", "🐶"),
            science="Living things grow and need food.",
            look_scene={"id": "lesson_living_or_not", "scene": "living_or_not", "picture": "🐶", "question": "Which one is living?"},
            look_pose="play",
        ),
        _scene(
            "Plant or Animal",
            "🌻",
            "A sunflower and a rabbit.",
            _ask("Which one is a plant?", ["Sunflower", "Rabbit"], "Sunflower", "A sunflower is a plant."),
            _g("Plant or Animal", "living_things_beginner.py", "run_plant_or_animal", "🌻"),
            science="Plants and animals are both living. They look different.",
            look_scene={"id": "lesson_plant_animal", "scene": "plant_or_animal", "picture": "🌻", "question": "Which one is a plant?"},
            look_pose="play",
        ),
        _scene(
            "Hungry or Full",
            "🐦",
            "A bird opens its beak.",
            _ask("What does the hungry bird need?", ["Food", "A toy"], "Food", "Living animals need food."),
            _g("Hungry or Full", "living_things_beginner.py", "run_hungry_or_full", "🐦"),
            science="When living things are hungry, they need food.",
            look_scene={"id": "lesson_hungry", "scene": "hungry_or_full", "picture": "🐦", "question": "What does the hungry bird need?"},
            look_pose="play",
        ),
    ],
}

_BEGINNER_MAKE = {
    "id": "beginner_make_test",
    "level": "Beginner",
    "topic": "Make & Test",
    "label": "Steady, Ramp, Fit",
    "icon": "🌉",
    "blurb": "Build a tower that stays. Pick a ramp. Fit the round hole.",
    "minutes": 6,
    "wave": 1,
    "playable": True,
    "big_idea": "We can build things, try them, and make them work better.",
    "kid_words": ["steady", "ramp", "fit", "try"],
    "grown_up": "Blocks or cups are enough. Knock things down cheerfully. Trying again is the point.",
    "hands_on": "Stack cups: tiny bottom vs wide bottom. Which tower stays? Then roll a car down a book.",
    "scenes": [
        _scene(
            "Will the Tower Fall?",
            "🗼",
            "Two towers. One has a wide bottom. One has a tiny bottom.",
            _ask("Which tower will stay up?", ["Wide bottom", "Tiny bottom"], "Wide bottom", "A wide base helps a tower stay steady."),
            _g("Will the Tower Fall?", "make_test_beginner.py", "run_will_the_tower_fall", "🗼"),
            science="A wide bottom helps a tower stay steady.",
            look_scene={"id": "lesson_tower", "scene": "tower_fall", "picture": "🗼", "question": "Which tower will stay up?"},
            look_pose="play",
        ),
        _scene(
            "Ramp or Wall?",
            "🛝",
            "A car needs a path down.",
            _ask("Which helps the car roll down?", ["Ramp", "Wall"], "Ramp", "A ramp gives the car a sloping path."),
            _g("Ramp or Wall?", "make_test_beginner.py", "run_ramp_or_wall", "🛝"),
            science="A ramp is a sloping path.",
            look_scene={"id": "lesson_ramp", "scene": "ramp_or_wall", "picture": "🛝", "question": "Which helps the car roll down?"},
            look_pose="play",
        ),
        _scene(
            "Fit the Hole",
            "⭕",
            "A board has a round hole.",
            _ask("Which shape fits the round hole?", ["Circle", "Square"], "Circle", "The circle matches the round hole."),
            _g("Fit the Hole", "make_test_beginner.py", "run_fit_the_hole", "⭕"),
            science="The matching shape fits.",
            look_scene={"id": "lesson_fit", "scene": "fit_the_hole", "picture": "⭕", "question": "Which shape fits the round hole?"},
            look_pose="play",
        ),
    ],
}

_BEGINNER_STEPS = {
    "id": "beginner_follow_the_steps",
    "level": "Beginner",
    "topic": "Follow the Steps",
    "label": "First, Next, Again",
    "icon": "🤖",
    "blurb": "Do steps in order. Spot the missing step. Do it again.",
    "minutes": 6,
    "wave": 2,
    "playable": True,
    "big_idea": "Steps have an order. Repeat means do it again.",
    "kid_words": ["first", "next", "missing", "repeat"],
    "grown_up": "Getting dressed is the lesson. Socks, then shoes. Cheer when the order is right.",
    "hands_on": "Put on socks, then shoes. Mix the order once and laugh. Then do a clap-clap-clap repeat.",
    "scenes": [
        _scene(
            "First Then Next",
            "🧦",
            "First we put on socks.",
            _ask("First socks. What comes next?", ["Shoes", "Hat"], "Shoes", "Socks come before shoes."),
            _g("First Then Next", "follow_the_steps_beginner.py", "run_first_then_next", "🧦"),
            science="Some steps only work in order.",
            look_scene={"id": "lesson_first_next", "scene": "first_then_next", "picture": "🧦", "question": "First socks. What comes next?"},
            look_pose="play",
        ),
        _scene(
            "Which Step Is Missing?",
            "🧼",
            "Wash, then dry… something is missing.",
            _ask("Wash, dry, then what?", ["Put away", "Make muddy"], "Put away", "Put it away after it is dry."),
            _g("Which Step Is Missing?", "follow_the_steps_beginner.py", "run_which_step_is_missing", "🧼"),
            science="A missing step can stop the job.",
            look_scene={"id": "lesson_missing", "scene": "missing_step", "picture": "🧼", "question": "Wash, dry, then what?"},
            look_pose="play",
        ),
        _scene(
            "Do It Again",
            "🔁",
            "Clap. Now the card says Repeat.",
            _ask("Repeat means what?", ["Do it again", "Stop forever"], "Do it again", "Repeat means do the step again."),
            _g("Do It Again", "follow_the_steps_beginner.py", "run_do_it_again", "🔁"),
            science="Repeat means do the step again.",
            look_scene={"id": "lesson_repeat", "scene": "do_it_again", "picture": "🔁", "question": "Repeat means what?"},
            look_pose="play",
        ),
    ],
}

# --- Intermediate -----------------------------------------------------------

_INTERMEDIATE_MOTION = {
    "id": "intermediate_motion",
    "level": "Intermediate",
    "topic": "Motion",
    "label": "Farther, Faster, Downhill",
    "icon": "🚗",
    "blurb": "Compare how far. Spot speeding up. Guess which way it rolls.",
    "minutes": 7,
    "wave": 1,
    "playable": True,
    "big_idea": "We can compare how far and how fast. Things roll downhill.",
    "kid_words": ["farther", "speeding up", "downhill"],
    "grown_up": "Name the science word after the picture, not before. “Farther” comes last.",
    "hands_on": "Roll two cars. Mark where they stop. Walk a ball to the top of a cushion hill and let go.",
    "scenes": [
        _scene(
            "Who Went Farther?",
            "🏁",
            "Two cars start together. The red car stops farther down the path.",
            _ask("Which car went farther?", ["Red car", "Blue car"], "Red car", "The red car ends farther from start."),
            _g("Who Went Farther?", "motion_intermediate.py", "run_who_went_farther", "🏁"),
            science="Farther means more path from the start.",
            look_scene={"id": "lesson_farther", "scene": "who_went_farther", "picture": "🏁", "question": "Which car went farther?"},
            look_pose="play",
        ),
        _scene(
            "Speeding Up?",
            "🚙",
            "The gaps between the car pictures get bigger.",
            _ask("The gaps grow. What happens?", ["Speeding up", "Slowing down"], "Speeding up", "Growing gaps show increasing speed."),
            _g("Speeding Up?", "motion_intermediate.py", "run_speeding_up", "🚙"),
            science="Growing gaps mean it is speeding up.",
            look_scene={"id": "lesson_speeding", "scene": "speeding_up", "picture": "🚙", "question": "The gaps grow. What happens?"},
            look_pose="play",
        ),
        _scene(
            "Which Way Does It Roll?",
            "⚽",
            "A ball sits on a hill.",
            _ask("Which way will the ball roll?", ["Downhill", "Uphill"], "Downhill", "Gravity pulls the ball downhill."),
            _g("Which Way Does It Roll?", "motion_intermediate.py", "run_which_way_does_it_roll", "⚽"),
            science="Things roll downhill unless something stops them.",
            look_scene={"id": "lesson_downhill", "scene": "roll_downhill", "picture": "⚽", "question": "Which way will the ball roll?"},
            look_pose="play",
        ),
    ],
}

_INTERMEDIATE_FORCES = {
    "id": "intermediate_forces",
    "level": "Intermediate",
    "topic": "Forces & Stuff",
    "label": "Balance, Slide, Stronger",
    "icon": "🧲",
    "blurb": "Balance a seesaw. Find the slippy surface. Watch the stronger push win.",
    "minutes": 7,
    "wave": 3,
    "playable": False,
    "big_idea": "A stronger push wins. Smooth things slide more. Heavy things sit closer to the middle to balance.",
    "kid_words": ["balance", "friction", "force"],
    "grown_up": "Say the word after they see it. “Friction is the grip.” Keep numbers out of it.",
    "hands_on": "A ruler and two toys make a seesaw. Slide a block on a towel, then on a table.",
    "scenes": [
        _scene(
            "Balance the Seesaw",
            "⚖️",
            "A heavy bear wants to sit on a seesaw with a light bunny.",
            _ask("Where should the heavy bear sit?", ["Near the middle", "Far away"], "Near the middle", "A heavy object balances closer to the middle."),
            _g("Balance the Seesaw", "forces_stuff_intermediate.py", "run_balance_the_seesaw", "⚖️"),
            science="Heavy sits closer to the middle to make it fair.",
        ),
        _scene(
            "Will It Slide?",
            "📦",
            "A box on sandpaper. A box on smooth tile.",
            _ask("Which surface has less friction?", ["Smooth tile", "Sandpaper"], "Smooth tile", "Smooth tile has less friction."),
            _g("Will It Slide?", "forces_stuff_intermediate.py", "run_will_it_slide", "📦"),
            science="Friction is the grip. Smooth has less grip.",
        ),
        _scene(
            "Stronger Push Wins",
            "💪",
            "Two people push a box from opposite sides. One push is bigger.",
            _ask("Which push wins?", ["Big push", "Small push"], "Big push", "The stronger force wins."),
            _g("Stronger Push Wins", "forces_stuff_intermediate.py", "run_stronger_push_wins", "💪"),
            science="The stronger push wins.",
        ),
    ],
}

_INTERMEDIATE_LIGHT = {
    "id": "intermediate_light_sound",
    "level": "Intermediate",
    "topic": "Light & Sound",
    "label": "Shadow, Louder, Echo",
    "icon": "🔦",
    "blurb": "Make a shadow. Read a louder wave. Find where echoes live.",
    "minutes": 7,
    "wave": 3,
    "playable": False,
    "big_idea": "A shadow needs a blocker. Bigger waves sound louder. Hard walls send sound back.",
    "kid_words": ["shadow", "block", "louder", "echo"],
    "grown_up": "A flashlight and a stuffed animal make shadows. Clap in a bathroom for an echo.",
    "hands_on": "Shine a flashlight at a wall. Put a toy in the way. Then clap in a hall and in a pillow pile.",
    "scenes": [
        _scene(
            "Make a Shadow",
            "🔦",
            "A flashlight shines at a wall.",
            _ask("What must block the light?", ["An object", "More light"], "An object", "An object blocks light and makes a shadow."),
            _g("Make a Shadow", "light_sound_intermediate.py", "run_make_a_shadow", "🔦"),
            science="A shadow is the dark where light was blocked.",
        ),
        _scene(
            "Which Is Louder?",
            "〰️",
            "Two sound-wave pictures. One is tall. One is tiny.",
            _ask("Which wave looks louder?", ["Big wave", "Small wave"], "Big wave", "A bigger sound wave means louder."),
            _g("Which Is Louder?", "light_sound_intermediate.py", "run_which_is_louder", "〰️"),
            science="A bigger wave picture means a louder sound.",
        ),
        _scene(
            "Echo or No Echo",
            "🗣️",
            "An empty cave and a pile of pillows.",
            _ask("Where will you hear an echo?", ["Empty cave", "Open pillow pile"], "Empty cave", "Hard cave walls reflect sound."),
            _g("Echo or No Echo", "light_sound_intermediate.py", "run_echo_or_no_echo", "🗣️"),
            science="Hard walls can send sound back. That bounce is an echo.",
        ),
    ],
}

_INTERMEDIATE_MATTER = {
    "id": "intermediate_matter",
    "level": "Intermediate",
    "topic": "Matter",
    "label": "Heat, Same Stuff, Settle",
    "icon": "🧊",
    "blurb": "Heat turns ice to water. Melted chocolate is still chocolate. Sand settles.",
    "minutes": 7,
    "wave": 3,
    "playable": False,
    "big_idea": "Heating can change how stuff looks. It is often still the same stuff. Some mixes settle.",
    "kid_words": ["heating", "melting", "settle"],
    "grown_up": "Melt a chocolate chip on a warm plate if you can. Sand in a jar of water is the settle demo.",
    "hands_on": "Warm an ice cube in your hand. Shake sand in water, then wait.",
    "scenes": [
        _scene(
            "Ice to Water",
            "🧊",
            "A cube of ice sits in a warm place.",
            _ask("What changed the ice?", ["Heating", "Cooling"], "Heating", "Heating changes solid ice to liquid water."),
            _g("Ice to Water", "matter_intermediate.py", "run_ice_to_water", "🧊"),
            science="Heating can turn ice into water.",
        ),
        _scene(
            "Same Stuff, New Look",
            "🍫",
            "A chocolate chip melts into a puddle.",
            _ask("Melted chocolate is still what?", ["Chocolate", "Stone"], "Chocolate", "Melting changes its form, not the stuff."),
            _g("Same Stuff, New Look", "matter_intermediate.py", "run_same_stuff_new_look", "🍫"),
            science="Melting changes the look, not the stuff.",
        ),
        _scene(
            "Mix or Settle",
            "🥛",
            "Sand is shaken into water.",
            _ask("Sand in water will what?", ["Settle", "Disappear"], "Settle", "Sand settles to the bottom."),
            _g("Mix or Settle", "matter_intermediate.py", "run_mix_or_settle", "🥛"),
            science="Sand does not disappear. It settles.",
        ),
    ],
}

_INTERMEDIATE_LIVING = {
    "id": "intermediate_living",
    "level": "Intermediate",
    "topic": "Living Things",
    "label": "Needs, Food, Home",
    "icon": "🌱",
    "blurb": "Give a plant what it needs. Feed the rabbit. Put the fish in the pond.",
    "minutes": 7,
    "wave": 4,
    "playable": False,
    "big_idea": "Living things need food, water, and a fitting home.",
    "kid_words": ["needs", "food", "habitat"],
    "grown_up": "Habitat means home. Use the kid word first: “home.” Then say habitat once.",
    "hands_on": "Water a plant. Look at a picture book: who eats grass? Who lives in water?",
    "scenes": [
        _scene(
            "What Does It Need?",
            "🌱",
            "A thirsty plant droops.",
            _ask("What helps this plant grow?", ["Water", "Plastic beads"], "Water", "Plants need water, light, and air."),
            _g("What Does It Need?", "living_things_intermediate.py", "run_what_does_it_need", "🌱"),
            science="Plants need water, light, and air.",
        ),
        _scene(
            "Who Eats What?",
            "🐇",
            "A rabbit looks hungry.",
            _ask("What should the rabbit eat?", ["Grass", "Pebbles"], "Grass", "Rabbits eat plants such as grass."),
            _g("Who Eats What?", "living_things_intermediate.py", "run_who_eats_what", "🐇"),
            science="Animals eat food that fits them.",
        ),
        _scene(
            "Home Habitat",
            "🐟",
            "A fish needs a place to live.",
            _ask("Where does a fish belong?", ["Pond", "Dry sandbox"], "Pond", "A pond gives fish water and food."),
            _g("Home Habitat", "living_things_intermediate.py", "run_home_habitat", "🐟"),
            science="A habitat is a living thing’s fitting home.",
        ),
    ],
}

_INTERMEDIATE_MAKE = {
    "id": "intermediate_make_test",
    "level": "Intermediate",
    "topic": "Make & Test",
    "label": "Predict, Test, Fix",
    "icon": "🌉",
    "blurb": "Test a bridge. Fix a ramp. Predict, then try.",
    "minutes": 7,
    "wave": 3,
    "playable": False,
    "big_idea": "Engineers predict, test, and fix. Trying is how we learn.",
    "kid_words": ["predict", "test", "fix"],
    "grown_up": "Celebrate the fix, not a perfect first try. “What should we change?” is the whole lesson.",
    "hands_on": "Build a paper bridge. Put coins on it. If it sags, fold the paper and test again.",
    "scenes": [
        _scene(
            "Test the Bridge",
            "🌉",
            "We built a toy bridge. We need to know if it is strong.",
            _ask("Which test checks the bridge?", ["Add toy cars", "Paint it"], "Add toy cars", "A load test checks if it holds weight."),
            _g("Test the Bridge", "make_test_intermediate.py", "run_test_the_bridge", "🌉"),
            science="A test asks: does it work?",
        ),
        _scene(
            "Fix the Ramp",
            "🏎️",
            "The car stops halfway down a flat ramp.",
            _ask("Car stops early. What should change?", ["Make steeper", "Make flatter"], "Make steeper", "A steeper ramp can give more speed."),
            _g("Fix the Ramp", "make_test_intermediate.py", "run_fix_the_ramp", "🏎️"),
            science="If it does not work, change one thing and try again.",
        ),
        _scene(
            "Predict Then Try",
            "🔬",
            "We have a guess about which ramp is faster.",
            _ask("What comes after predict?", ["Test it", "Forget it"], "Test it", "Engineers predict, test, and learn."),
            _g("Predict Then Try", "make_test_intermediate.py", "run_predict_then_try", "🔬"),
            science="Predict means guess. Then we test the guess.",
        ),
    ],
}

_INTERMEDIATE_STEPS = {
    "id": "intermediate_follow_the_steps",
    "level": "Intermediate",
    "topic": "Follow the Steps",
    "label": "Sequence, If-Then, Loop",
    "icon": "🤖",
    "blurb": "Drive a three-step robot. Follow if-then. Repeat three times.",
    "minutes": 7,
    "wave": 4,
    "playable": False,
    "big_idea": "Robots follow steps in order. If-then is a rule. A loop repeats.",
    "kid_words": ["sequence", "if-then", "loop"],
    "grown_up": "Play robot: the child is the robot, you give three steps. Then swap.",
    "hands_on": "Give three steps across a rug: forward, turn, forward. Then: if the sock is red, then hop.",
    "scenes": [
        _scene(
            "Three-Step Robot",
            "🤖",
            "The card says: Forward, turn, then…",
            _ask("Forward, turn, then what?", ["Forward", "Sleep"], "Forward", "The robot follows each step in order."),
            _g("Three-Step Robot", "follow_the_steps_intermediate.py", "run_three_step_robot", "🤖"),
            science="Do the steps in order, one after another.",
        ),
        _scene(
            "If Red, Then Stop",
            "🚦",
            "The rule is: if the light is red, then stop.",
            _ask("The light turns red. Do what?", ["Stop", "Go"], "Stop", "The if-then rule says red means stop."),
            _g("If Red, Then Stop", "follow_the_steps_intermediate.py", "run_if_red_then_stop", "🚦"),
            science="If-then is a rule: if this, then that.",
        ),
        _scene(
            "Repeat 3 Times",
            "🔁",
            "The card says Tap, and Repeat 3 times.",
            _ask("Tap repeats three times. How many taps?", ["3", "1", "5"], "3", "A loop repeats the action three times."),
            _g("Repeat 3 Times", "follow_the_steps_intermediate.py", "run_repeat_3_times", "🔁"),
            science="A loop repeats a step a number of times.",
        ),
    ],
}

# --- Advanced ---------------------------------------------------------------

_ADVANCED_MOTION = {
    "id": "advanced_motion",
    "level": "Advanced",
    "topic": "Motion",
    "label": "Steeper, Add Up, Race",
    "icon": "🚗",
    "blurb": "Steeper ramps go faster. Two pushes add. Less time means faster.",
    "minutes": 8,
    "wave": 4,
    "playable": False,
    "big_idea": "A steeper ramp speeds you up more. Pushes in the same direction add. Less time for the same trip means faster.",
    "kid_words": ["steeper", "add", "faster"],
    "grown_up": "Keep it as a chain: “this, so that.” No formulas. A book as a ramp is enough.",
    "hands_on": "Roll a car down a book, then prop the book steeper. Two gentle pushes on a toy, both the same way.",
    "scenes": [
        _scene(
            "Steeper Goes Faster",
            "🛝",
            "Two ramps. One is almost flat. One is steep.",
            _ask("Which ramp makes more speed?", ["Steep ramp", "Flat ramp"], "Steep ramp", "A steeper ramp makes it speed up more."),
            _g("Steeper Goes Faster", "motion_advanced.py", "run_steeper_goes_faster", "🛝"),
            science="Steeper can mean more speed at the bottom.",
        ),
        _scene(
            "Two Pushes Add Up",
            "➡️",
            "Two hands push a box, both to the right.",
            _ask("Two pushes point right. Then what?", ["Moves right", "Moves left"], "Moves right", "Pushes in one direction add together."),
            _g("Two Pushes Add Up", "motion_advanced.py", "run_two_pushes_add_up", "➡️"),
            science="Pushes the same way add up.",
        ),
        _scene(
            "Race the Clock",
            "⏱️",
            "Two cars take the same path. One finishes in 3 seconds. One in 6.",
            _ask("Same trip. Who is faster?", ["3-second car", "6-second car"], "3-second car", "Less time for the same trip means faster."),
            _g("Race the Clock", "motion_advanced.py", "run_race_the_clock", "⏱️"),
            science="Same path, less time, faster.",
        ),
    ],
}

_ADVANCED_FORCES = {
    "id": "advanced_forces",
    "level": "Advanced",
    "topic": "Forces & Stuff",
    "label": "Fair, Smooth, Lift",
    "icon": "🧲",
    "blurb": "Make a fair balance. Compare rough and smooth ramps. Lift with a lever.",
    "minutes": 8,
    "wave": 4,
    "playable": False,
    "big_idea": "Equal weights can balance. Less grip lets a car go farther. A pivot near the load makes a lever easier.",
    "kid_words": ["fair", "smooth", "lever", "pivot"],
    "grown_up": "A spoon and a dried bean are a lever. Pivot near the bean, lift with the long end.",
    "hands_on": "See-saw two equal books. Then roll a car on a towel ramp vs a smooth board. Then lift a book with a spoon lever.",
    "scenes": [
        _scene(
            "Fair Balance",
            "⚖️",
            "A seesaw with two sides.",
            _ask("How can both sides balance?", ["Equal weights", "One heavy side"], "Equal weights", "Equal weights at equal distances balance."),
            _g("Fair Balance", "forces_stuff_advanced.py", "run_fair_balance", "⚖️"),
            science="Same weight, same place, it balances.",
        ),
        _scene(
            "Rough vs Smooth Ramp",
            "🏎️",
            "One ramp is sandpaper. One is smooth.",
            _ask("Which car travels farther?", ["Smooth ramp", "Rough ramp"], "Smooth ramp", "Less friction lets the car travel farther."),
            _g("Rough vs Smooth Ramp", "forces_stuff_advanced.py", "run_rough_vs_smooth_ramp", "🏎️"),
            science="Less grip can mean a longer roll.",
        ),
        _scene(
            "Lift With a Lever",
            "🪵",
            "A stick, a rock, and a pivot.",
            _ask("Where should the pivot go?", ["Near the rock", "Near your hand"], "Near the rock", "A nearby pivot makes lifting easier."),
            _g("Lift With a Lever", "forces_stuff_advanced.py", "run_lift_with_a_lever", "🪵"),
            science="A lever helps you lift. Put the pivot near the heavy thing.",
        ),
    ],
}

_ADVANCED_LIGHT = {
    "id": "advanced_light_sound",
    "level": "Advanced",
    "topic": "Light & Sound",
    "label": "Bigger Shadow, Pitch, Blocked",
    "icon": "🔦",
    "blurb": "Bigger blockers make bigger shadows. Fast wiggles sound high. Walls block light.",
    "minutes": 8,
    "wave": 5,
    "playable": False,
    "big_idea": "A bigger blocker can make a bigger shadow. Faster wiggles sound higher. Light does not go through an opaque wall.",
    "kid_words": ["bigger shadow", "pitch", "blocked"],
    "grown_up": "Flashlight plus a small toy and a big toy. Hum low, then squeak high.",
    "hands_on": "Make shadows with a spoon and a book. Hum a low sound, then a high one. Can a flashlight shine through a notebook?",
    "scenes": [
        _scene(
            "Bigger Block, Bigger Shadow",
            "⬛",
            "A small block and a big block in the same light.",
            _ask("Which makes the bigger shadow?", ["Big block", "Small block"], "Big block", "A bigger blocker can make a bigger shadow."),
            _g("Bigger Block, Bigger Shadow", "light_sound_advanced.py", "run_bigger_block_bigger_shadow", "⬛"),
            science="A bigger blocker can make a bigger shadow.",
        ),
        _scene(
            "Pitch Ladder",
            "🎵",
            "Two wiggly sound pictures. One wiggles fast. One wiggles slow.",
            _ask("Which note has highest pitch?", ["Fast wiggles", "Slow wiggles"], "Fast wiggles", "Faster vibrations make a higher pitch."),
            _g("Pitch Ladder", "light_sound_advanced.py", "run_pitch_ladder", "🎵"),
            science="Fast wiggles sound high. Slow wiggles sound low.",
        ),
        _scene(
            "Light Path Blocked",
            "🧱",
            "A flashlight, a wall, and a dark room behind the wall.",
            _ask("Can light go through the wall?", ["No", "Yes"], "No", "An opaque wall blocks the light path."),
            _g("Light Path Blocked", "light_sound_advanced.py", "run_light_path_blocked", "🧱"),
            science="Some things block the path of light.",
        ),
    ],
}

_ADVANCED_MATTER = {
    "id": "advanced_matter",
    "level": "Advanced",
    "topic": "Matter",
    "label": "Puddle, Clay, Shape",
    "icon": "🧊",
    "blurb": "Warm puddles rise as vapor. Baked clay gets hard. Solids hold shape.",
    "minutes": 8,
    "wave": 5,
    "playable": False,
    "big_idea": "Warm water can become vapor. Heating can harden clay. Solids keep their own shape.",
    "kid_words": ["vapor", "harder", "solid"],
    "grown_up": "A wet sidewalk in sun is the water-cycle picture. Play-dough vs a wood block is shape.",
    "hands_on": "Watch a wet spoon dry in sun. Squeeze play-dough, then tap a block. The block keeps its shape.",
    "scenes": [
        _scene(
            "Water Cycle Pictures",
            "🌦️",
            "A rain puddle sits in the sun.",
            _ask("What comes after a rain puddle warms?", ["Water vapor rises", "Ice forms"], "Water vapor rises", "Warm water can become vapor and rise."),
            _g("Water Cycle Pictures", "matter_advanced.py", "run_water_cycle_pictures", "🌦️"),
            science="Warm puddles can become vapor and rise.",
        ),
        _scene(
            "Soft to Hard",
            "🏺",
            "Soft clay goes into a hot oven.",
            _ask("Clay is baked. What happens?", ["Gets harder", "Gets wetter"], "Gets harder", "Heating can make clay hard."),
            _g("Soft to Hard", "matter_advanced.py", "run_soft_to_hard", "🏺"),
            science="Heating can make some stuff harder.",
        ),
        _scene(
            "What Holds Shape?",
            "🧱",
            "Juice in a cup and a wood block on the table.",
            _ask("Which keeps its own shape?", ["Wood block", "Juice"], "Wood block", "A solid holds its own shape."),
            _g("What Holds Shape?", "matter_advanced.py", "run_what_holds_shape", "🧱"),
            science="A solid holds its own shape. A liquid takes the cup’s shape.",
        ),
    ],
}

_ADVANCED_LIVING = {
    "id": "advanced_living",
    "level": "Advanced",
    "topic": "Living Things",
    "label": "Cycle, Night, Grow",
    "icon": "🌱",
    "blurb": "Put a life cycle in order. Meet night animals. Help a pale plant.",
    "minutes": 8,
    "wave": 5,
    "playable": False,
    "big_idea": "Living things change as they grow. Some animals wake at night. Plants need light.",
    "kid_words": ["life cycle", "night", "light"],
    "grown_up": "Egg, chick, hen is enough. No need for every animal. Pale plant on a windowsill is the grow test.",
    "hands_on": "Order three pictures: egg, chick, hen. Look for the moon and an owl in a book. Move a pale plant toward a window.",
    "scenes": [
        _scene(
            "Life Cycle Order",
            "🐣",
            "An egg sits in a nest.",
            _ask("What comes after an egg?", ["Chick", "Adult chicken"], "Chick", "A chick hatches before becoming an adult."),
            _g("Life Cycle Order", "living_things_advanced.py", "run_life_cycle_order", "🐣"),
            science="Egg, then chick, then hen. That order is a life cycle.",
        ),
        _scene(
            "Day and Night Animals",
            "🦉",
            "The moon is up.",
            _ask("Which animal is awake at night?", ["Owl", "Butterfly"], "Owl", "Many owls are active at night."),
            _g("Day and Night Animals", "living_things_advanced.py", "run_day_and_night_animals", "🦉"),
            science="Some animals are awake at night.",
        ),
        _scene(
            "Help It Grow",
            "🪴",
            "A plant looks pale and weak.",
            _ask("Plant is pale. What should change?", ["Give light", "Hide in dark"], "Give light", "Plants use light to help make food."),
            _g("Help It Grow", "living_things_advanced.py", "run_help_it_grow", "🪴"),
            science="Plants need light to grow well.",
        ),
    ],
}

_ADVANCED_MAKE = {
    "id": "advanced_make_test",
    "level": "Advanced",
    "topic": "Make & Test",
    "label": "Triangle, Compare, Path",
    "icon": "🌉",
    "blurb": "Pick a strong shape. Compare two tests. Finish a marble path.",
    "minutes": 8,
    "wave": 4,
    "playable": False,
    "big_idea": "Triangles make strong frames. Test results help us pick. A gap needs a firm bridge.",
    "kid_words": ["triangle", "compare", "path"],
    "grown_up": "Straws or rolled paper make triangles vs squares. Push gently. Then a marble and a book-gap.",
    "hands_on": "Build a triangle and a floppy square from straws. Which holds a push? Then bridge a gap for a marble.",
    "scenes": [
        _scene(
            "Stronger Shape",
            "🔺",
            "A triangle frame and a wobbly curve.",
            _ask("Which shape makes a strong frame?", ["Triangle", "Wobbly curve"], "Triangle", "Triangles help frames keep their shape."),
            _g("Stronger Shape", "make_test_advanced.py", "run_stronger_shape", "🔺"),
            science="Triangles help a frame keep its shape.",
        ),
        _scene(
            "Two Tests, Pick Better",
            "🌉",
            "Bridge A held more toy cars than Bridge B.",
            _ask("Bridge A holds more. Pick which?", ["Bridge A", "Bridge B"], "Bridge A", "Test results show Bridge A is stronger."),
            _g("Two Tests, Pick Better", "make_test_advanced.py", "run_two_tests_pick_better", "🌉"),
            science="We pick the one that did better on the test.",
        ),
        _scene(
            "Build a Path",
            "🟠",
            "A marble path has a gap.",
            _ask("Gap blocks the marble. Add what?", ["Short bridge", "Soft pillow"], "Short bridge", "A firm bridge completes the path."),
            _g("Build a Path", "make_test_advanced.py", "run_build_a_path", "🟠"),
            science="A firm bridge completes the path.",
        ),
    ],
}

_ADVANCED_STEPS = {
    "id": "advanced_follow_the_steps",
    "level": "Advanced",
    "topic": "Follow the Steps",
    "label": "Debug, Loop, If-Wet",
    "icon": "🤖",
    "blurb": "Fix a wrong turn. Loop a square. If wet, then boots.",
    "minutes": 8,
    "wave": 5,
    "playable": False,
    "big_idea": "If a step is wrong, change that step. A loop can draw a square. If-then rules still work in the world.",
    "kid_words": ["debug", "loop", "if-then"],
    "grown_up": "Debug means “find the wrong step.” Keep it kind. The robot is not in trouble.",
    "hands_on": "Tape a square on the floor. Walk: forward, turn, four times. If the grass is wet, put on boots.",
    "scenes": [
        _scene(
            "Debug the Path",
            "🐞",
            "The robot turned the wrong way.",
            _ask("Robot turns wrong. What should change?", ["Turn step", "Battery color"], "Turn step", "Debug the incorrect turn instruction."),
            _g("Debug the Path", "follow_the_steps_advanced.py", "run_debug_the_path", "🐞"),
            science="Debug means find the wrong step and change it.",
        ),
        _scene(
            "Loop the Square",
            "⬜",
            "We want the robot to walk a square.",
            _ask("Which steps repeat four times?", ["Forward, turn", "Jump, sleep"], "Forward, turn", "Forward then turn repeated makes a square."),
            _g("Loop the Square", "follow_the_steps_advanced.py", "run_loop_the_square", "⬜"),
            science="Forward, turn, four times makes a square.",
        ),
        _scene(
            "If Wet, Then Boots",
            "🌧️",
            "The ground is wet. The rule is: if wet, then boots.",
            _ask("The ground is wet. Wear what?", ["Boots", "Slippers"], "Boots", "The condition is wet, so choose boots."),
            _g("If Wet, Then Boots", "follow_the_steps_advanced.py", "run_if_wet_then_boots", "🌧️"),
            science="If the ground is wet, then wear boots.",
        ),
    ],
}


LESSONS: list[Lesson] = [
    _BEGINNER_MOTION,
    _BEGINNER_FORCES,
    _BEGINNER_LIGHT,
    _BEGINNER_MATTER,
    _BEGINNER_LIVING,
    _BEGINNER_MAKE,
    _BEGINNER_STEPS,
    _INTERMEDIATE_MOTION,
    _INTERMEDIATE_FORCES,
    _INTERMEDIATE_LIGHT,
    _INTERMEDIATE_MATTER,
    _INTERMEDIATE_LIVING,
    _INTERMEDIATE_MAKE,
    _INTERMEDIATE_STEPS,
    _ADVANCED_MOTION,
    _ADVANCED_FORCES,
    _ADVANCED_LIGHT,
    _ADVANCED_MATTER,
    _ADVANCED_LIVING,
    _ADVANCED_MAKE,
    _ADVANCED_STEPS,
]

LEVELS = ("Beginner", "Intermediate", "Advanced")
TOPIC_ORDER = (
    "Motion",
    "Forces & Stuff",
    "Light & Sound",
    "Matter",
    "Living Things",
    "Make & Test",
    "Follow the Steps",
)

# Build picture-first scenes first, in this order. Scripts for all 21 already run.
BUILD_PRIORITY: list[str] = [
    "beginner_motion",
    "beginner_forces",
    "beginner_make_test",
    "intermediate_motion",
    "beginner_light_sound",
    "beginner_matter",
    "beginner_living",
    "beginner_follow_the_steps",
    "intermediate_forces",
    "intermediate_light_sound",
    "intermediate_make_test",
    "intermediate_matter",
    "intermediate_living",
    "intermediate_follow_the_steps",
    "advanced_motion",
    "advanced_forces",
    "advanced_make_test",
    "advanced_light_sound",
    "advanced_matter",
    "advanced_living",
    "advanced_follow_the_steps",
]


def get_lesson(lesson_id: str) -> Lesson:
    for lesson in LESSONS:
        if lesson["id"] == lesson_id:
            return lesson
    raise KeyError(lesson_id)


def lessons_for(level: str, topic: str) -> list[Lesson]:
    return [lesson for lesson in LESSONS if lesson["level"] == level and lesson["topic"] == topic]


def lesson_menu_for(level: str) -> dict[str, list[dict[str, str]]]:
    """Sidebar entries shaped like the games catalog."""
    menu: dict[str, list[dict[str, str]]] = {topic: [] for topic in TOPIC_ORDER}
    for lesson in LESSONS:
        if lesson["level"] != level:
            continue
        menu[lesson["topic"]].append({
            "label": lesson["label"],
            "icon": lesson["icon"],
            "blurb": lesson["blurb"],
            "id": lesson["id"],
        })
    return menu


def validate_catalog() -> None:
    ids = [lesson["id"] for lesson in LESSONS]
    assert len(LESSONS) == 21, len(LESSONS)
    assert len(set(ids)) == 21
    assert set(BUILD_PRIORITY) == set(ids)
    for level in LEVELS:
        assert sum(1 for lesson in LESSONS if lesson["level"] == level) == 7
    playable_ids = {lesson["id"] for lesson in LESSONS if lesson["playable"]}
    assert playable_ids == set(BUILD_PRIORITY[:8]), playable_ids
    for lesson in LESSONS:
        assert len(lesson["scenes"]) == 3, lesson["id"]
        for scene in lesson["scenes"]:
            assert scene["name"]["answer"] in scene["name"]["choices"], lesson["id"]
            if "change" in scene:
                assert scene["change"]["answer"] in scene["change"]["choices"], lesson["id"]
            if lesson["playable"]:
                assert scene.get("look_scene") and scene["look_scene"].get("scene"), lesson["id"]
