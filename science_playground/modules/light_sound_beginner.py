"""Three playable science games."""
from __future__ import annotations
import sys
from pathlib import Path
_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path: sys.path.insert(0, str(_ROOT))
from pair_trials import pair_a_left
from science_utils import run_game

# Cycle in order, then wrap. Question alternates light / dark by index.
LIGHT_DARK_PAIRS: tuple[dict[str, str], ...] = (
    {
        "light": "Sunny yard",
        "dark": "Closed closet",
        "light_kind": "yard",
        "dark_kind": "closet",
        "kid_tip": "The yard is bright. The closet is dark.",
        "tip": "Sunlight makes the yard light.",
    },
    {
        "light": "Lit lamp",
        "dark": "Dark cave",
        "light_kind": "lamp",
        "dark_kind": "cave",
        "kid_tip": "The lamp makes light. The cave stays dark.",
        "tip": "A lamp adds light. A cave has almost none.",
    },
    {
        "light": "Open window",
        "dark": "Tunnel",
        "light_kind": "window",
        "dark_kind": "tunnel",
        "kid_tip": "The window lets sun in. The tunnel is dark.",
        "tip": "Daylight through a window makes a room light.",
    },
    {
        "light": "Lighthouse",
        "dark": "Basement",
        "light_kind": "lighthouse",
        "dark_kind": "basement",
        "kid_tip": "The lighthouse shines. The basement is dark.",
        "tip": "A lighthouse is made to send out light.",
    },
    {
        "light": "Campfire",
        "dark": "Woods at night",
        "light_kind": "fire",
        "dark_kind": "woods",
        "kid_tip": "The fire glows. The night woods are dark.",
        "tip": "Fire makes light. Night woods have very little.",
    },
    {
        "light": "Flashlight",
        "dark": "Under the bed",
        "light_kind": "flashlight",
        "dark_kind": "bed",
        "kid_tip": "The flashlight makes a bright spot. Under the bed is dark.",
        "tip": "A flashlight adds a beam of light.",
    },
    {
        "light": "Sunny beach",
        "dark": "Movie theater",
        "light_kind": "beach",
        "dark_kind": "theater",
        "kid_tip": "The beach is bright. The theater is dark for the movie.",
        "tip": "A movie theater is kept dark on purpose.",
    },
    {
        "light": "Birthday candles",
        "dark": "Closed box",
        "light_kind": "candles",
        "dark_kind": "box",
        "kid_tip": "Candles glow. A closed box stays dark inside.",
        "tip": "Little flames still make light.",
    },
    {
        "light": "Streetlight",
        "dark": "Attic",
        "light_kind": "street",
        "dark_kind": "attic",
        "kid_tip": "The streetlight shines. The attic is dark.",
        "tip": "Streetlights make a night path light.",
    },
    {
        "light": "Daytime park",
        "dark": "Midnight room",
        "light_kind": "park",
        "dark_kind": "midnight",
        "kid_tip": "The park in day is light. Midnight is dark.",
        "tip": "Daytime sun makes the park light.",
    },
)


def _light_trials() -> tuple[dict[str, str | list[str] | bool], ...]:
    trials: list[dict[str, str | list[str] | bool]] = []
    for i, pair in enumerate(LIGHT_DARK_PAIRS):
        ask_light = i % 2 == 0
        light = pair["light"]
        dark = pair["dark"]
        trial: dict[str, str | list[str] | bool] = dict(pair)
        trial["question"] = "Which place is light?" if ask_light else "Which place is dark?"
        trial["choices"] = [light, dark]
        trial["answer"] = light if ask_light else dark
        trial["light_left"] = pair_a_left(i)
        trial["picture"] = "☀️" if ask_light else "🌙"
        trials.append(trial)
    return tuple(trials)


def run_light_or_dark() -> None:
    run_game({
        'id': 'light_sound_beginner_light_or_dark',
        'title': 'Light or Dark',
        'tagline': 'Which place is light? Which place is dark?',
        'question': 'Which place is light?',
        'choices': ['Sunny yard', 'Closed closet'],
        'answer': 'Sunny yard',
        'picture': '☀️',
        'scene': 'light_or_dark',
        'animate_mode': 'once',
        'trials': _light_trials(),
        'kid_tip': 'The yard is bright. The closet is dark.',
        'tip': 'Sunlight makes the yard light.',
    })

# Cycle in order, then wrap. Question alternates loud / quiet by index.
LOUD_QUIET_PAIRS: tuple[dict[str, str], ...] = (
    {
        "loud": "Drum",
        "quiet": "Whisper",
        "loud_kind": "drum",
        "quiet_kind": "whisper",
        "hear_loud": "drum",
        "hear_quiet": "whisper",
        "kid_tip": "The drum is loud. The whisper is quiet.",
        "tip": "A drum makes a big sound. A whisper is tiny.",
    },
    {
        "loud": "Thunder",
        "quiet": "Soft rain",
        "loud_kind": "thunder",
        "quiet_kind": "rain",
        "hear_loud": "thunder",
        "hear_quiet": "rain",
        "kid_tip": "Thunder is loud. Soft rain is quiet.",
        "tip": "Thunder is a big sound. Rain can be a tiny one.",
    },
    {
        "loud": "Cymbals",
        "quiet": "Pages turning",
        "loud_kind": "cymbal",
        "quiet_kind": "pages",
        "hear_loud": "cymbal",
        "hear_quiet": "pages",
        "kid_tip": "Cymbals crash loud. Pages are quiet.",
        "tip": "Cymbals make a big crash. Turning pages is quiet.",
    },
    {
        "loud": "Dog bark",
        "quiet": "Cat purr",
        "loud_kind": "bark",
        "quiet_kind": "purr",
        "hear_loud": "bark",
        "hear_quiet": "purr",
        "kid_tip": "A bark is loud. A purr is quiet.",
        "tip": "A bark is a big sound. A purr is a little one.",
    },
    {
        "loud": "Alarm clock",
        "quiet": "Tick tock",
        "loud_kind": "alarm",
        "quiet_kind": "tick",
        "hear_loud": "alarm",
        "hear_quiet": "tick",
        "kid_tip": "The alarm is loud. The tick is quiet.",
        "tip": "An alarm is meant to be loud. A tick is soft.",
    },
    {
        "loud": "Crash",
        "quiet": "Leaves rustle",
        "loud_kind": "crash",
        "quiet_kind": "rustle",
        "hear_loud": "crash",
        "hear_quiet": "rustle",
        "kid_tip": "A crash is loud. Leaves are quiet.",
        "tip": "A crash is a big sound. Rustling leaves are tiny.",
    },
    {
        "loud": "Gong",
        "quiet": "Drip",
        "loud_kind": "gong",
        "quiet_kind": "drip",
        "hear_loud": "gong",
        "hear_quiet": "drip",
        "kid_tip": "The gong is loud. The drip is quiet.",
        "tip": "A gong rings big. A drip is a little sound.",
    },
    {
        "loud": "Trumpet",
        "quiet": "Hum",
        "loud_kind": "trumpet",
        "quiet_kind": "hum",
        "hear_loud": "trumpet",
        "hear_quiet": "hum",
        "kid_tip": "The trumpet is loud. The hum is quiet.",
        "tip": "A trumpet is a big sound. A hum can be tiny.",
    },
    {
        "loud": "Fire truck",
        "quiet": "Lullaby",
        "loud_kind": "siren",
        "quiet_kind": "lullaby",
        "hear_loud": "siren",
        "hear_quiet": "lullaby",
        "kid_tip": "The fire truck is loud. The lullaby is quiet.",
        "tip": "A siren is loud on purpose. A lullaby is soft.",
    },
    {
        "loud": "Lion",
        "quiet": "Mouse",
        "loud_kind": "roar",
        "quiet_kind": "squeak",
        "hear_loud": "roar",
        "hear_quiet": "squeak",
        "kid_tip": "The lion is loud. The mouse is quiet.",
        "tip": "A roar is a big sound. A squeak is a tiny one.",
    },
)


def _loud_trials() -> tuple[dict[str, str | list[str] | bool], ...]:
    trials: list[dict[str, str | list[str] | bool]] = []
    for i, pair in enumerate(LOUD_QUIET_PAIRS):
        ask_loud = i % 2 == 0
        loud = pair["loud"]
        quiet = pair["quiet"]
        trial: dict[str, str | list[str] | bool] = dict(pair)
        trial["question"] = "Which sound is loud?" if ask_loud else "Which sound is quiet?"
        trial["choices"] = [loud, quiet]
        trial["answer"] = loud if ask_loud else quiet
        trial["answer_sound"] = pair["hear_loud"] if ask_loud else pair["hear_quiet"]
        loud_left = pair_a_left(i)
        trial["loud_left"] = loud_left
        trial["hear_left"] = pair["hear_loud"] if loud_left else pair["hear_quiet"]
        trial["hear_right"] = pair["hear_quiet"] if loud_left else pair["hear_loud"]
        trial["picture"] = "🥁" if ask_loud else "🤫"
        trials.append(trial)
    return tuple(trials)


def run_loud_or_quiet() -> None:
    run_game({
        'id': 'light_sound_beginner_loud_or_quiet',
        'title': 'Loud or Quiet',
        'tagline': 'Which sound is loud? Which sound is quiet?',
        'question': 'Which sound is loud?',
        'choices': ['Whisper', 'Drum'],
        'answer': 'Drum',
        'picture': '🥁',
        'scene': 'loud_or_quiet',
        'animate_mode': 'once',
        'trials': _loud_trials(),
        'kid_tip': 'The drum is loud. The whisper is quiet.',
        'tip': 'A drum makes a big sound. A whisper is tiny.',
    })

# Cycle in order, then wrap. Question alternates high / low by index.
HIGH_LOW_PAIRS: tuple[dict[str, str], ...] = (
    {
        "high": "Tiny bell",
        "low": "Big drum",
        "high_pic": "🔔",
        "low_pic": "🥁",
        "kid_tip": "The tiny bell is high. The big drum is low.",
        "tip": "A tiny bell often sounds high. A big drum sounds low.",
    },
    {
        "high": "Bird",
        "low": "Frog",
        "high_pic": "🐦",
        "low_pic": "🐸",
        "kid_tip": "The bird is high. The frog is low.",
        "tip": "A bird chirp is high. A frog croak is lower.",
    },
    {
        "high": "Whistle",
        "low": "Tuba",
        "high_pic": "🎵",
        "low_pic": "🎺",
        "kid_tip": "The whistle is high. The tuba is low.",
        "tip": "A whistle is a high sound. A tuba is a low one.",
    },
    {
        "high": "Kitten",
        "low": "Cow",
        "high_pic": "🐱",
        "low_pic": "🐄",
        "kid_tip": "The kitten is high. The cow is low.",
        "tip": "A kitten mew is high. A cow moo is low.",
    },
    {
        "high": "Flute",
        "low": "Bass drum",
        "high_pic": "🎶",
        "low_pic": "🥁",
        "kid_tip": "The flute is high. The bass drum is low.",
        "tip": "A flute sounds high. A bass drum sounds low.",
    },
    {
        "high": "Cricket",
        "low": "Big dog",
        "high_pic": "🦗",
        "low_pic": "🐕",
        "kid_tip": "The cricket is high. The big dog is low.",
        "tip": "A cricket chirp is high. A big dog woof is lower.",
    },
    {
        "high": "Triangle",
        "low": "Timpani",
        "high_pic": "📐",
        "low_pic": "🥁",
        "kid_tip": "The triangle is high. The timpani is low.",
        "tip": "A triangle ting is high. Timpani drums are low.",
    },
    {
        "high": "Piccolo",
        "low": "Tuba",
        "high_pic": "🎼",
        "low_pic": "🎺",
        "kid_tip": "The piccolo is high. The tuba is low.",
        "tip": "A piccolo is a very high flute. A tuba is low.",
    },
    {
        "high": "Squeaky toy",
        "low": "Big drum",
        "high_pic": "🧸",
        "low_pic": "🥁",
        "kid_tip": "The squeaky toy is high. The big drum is low.",
        "tip": "A squeak is high. A big drum is low.",
    },
    {
        "high": "High piano",
        "low": "Low piano",
        "high_pic": "🎹",
        "low_pic": "🎹",
        "kid_tip": "The right-hand keys sound high. The left-hand keys sound low.",
        "tip": "On a piano, the right side is higher than the left.",
    },
)


def _high_trials() -> tuple[dict[str, str | list[str] | bool], ...]:
    trials: list[dict[str, str | list[str] | bool]] = []
    for i, pair in enumerate(HIGH_LOW_PAIRS):
        ask_high = i % 2 == 0
        high = pair["high"]
        low = pair["low"]
        trial: dict[str, str | list[str] | bool] = dict(pair)
        trial["question"] = "Which makes a high sound?" if ask_high else "Which makes a low sound?"
        trial["choices"] = [high, low]
        trial["answer"] = high if ask_high else low
        trial["answer_sound"] = "high" if ask_high else "low"
        high_left = pair_a_left(i)
        trial["high_left"] = high_left
        trial["hear_left"] = "high" if high_left else "low"
        trial["hear_right"] = "low" if high_left else "high"
        trial["picture"] = pair.get("high_pic") or "🔔"
        trials.append(trial)
    return tuple(trials)


def run_high_or_low() -> None:
    run_game({
        'id': 'light_sound_beginner_high_or_low',
        'title': 'High or Low',
        'tagline': 'Which makes a high sound? Which makes a low sound?',
        'question': 'Which makes a high sound?',
        'choices': ['Tiny bell', 'Big drum'],
        'answer': 'Tiny bell',
        'picture': '🔔',
        'scene': 'high_or_low',
        'animate_mode': 'once',
        'trials': _high_trials(),
        'kid_tip': 'The tiny bell is high. The big drum is low.',
        'tip': 'A tiny bell often sounds high. A big drum sounds low.',
    })
