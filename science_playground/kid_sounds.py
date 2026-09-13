"""Short WAV clips for beginner sound games. Stdlib only."""
from __future__ import annotations

import io
import math
import random
import struct
import wave

RATE = 22050


def _wav(samples: list[float]) -> bytes:
    buf = io.BytesIO()
    with wave.open(buf, "wb") as writer:
        writer.setnchannels(1)
        writer.setsampwidth(2)
        writer.setframerate(RATE)
        frames = bytearray()
        for sample in samples:
            frames += struct.pack("<h", max(-32767, min(32767, int(sample * 32767))))
        writer.writeframes(frames)
    return buf.getvalue()


def _silence(seconds: float) -> list[float]:
    return [0.0] * int(RATE * seconds)


def _noise(seconds: float, amp: float, seed: int) -> list[float]:
    rng = random.Random(seed)
    return [amp * (rng.random() * 2 - 1) for _ in range(int(RATE * seconds))]


def _tone(freq: float, seconds: float, amp: float, decay: bool = True) -> list[float]:
    n = int(RATE * seconds)
    samples: list[float] = []
    for i in range(n):
        t = i / RATE
        env = (1 - t / seconds) ** 1.4 if decay else 1.0
        samples.append(amp * env * math.sin(2 * math.pi * freq * t))
    return samples


def _thump(amp: float) -> list[float]:
    body = _tone(78, 0.28, amp, decay=True)
    click = _noise(0.06, amp * 0.55, seed=3)
    out = list(body)
    for i, sample in enumerate(click):
        out[i] = max(-1.0, min(1.0, out[i] + sample))
    return out


def _bell(freq: float, amp: float) -> list[float]:
    a = _tone(freq, 0.55, amp, decay=True)
    b = _tone(freq * 2.4, 0.35, amp * 0.25, decay=True)
    return [x + (b[i] if i < len(b) else 0) for i, x in enumerate(a)]


def render_sound(kind: str) -> bytes:
    """Return a WAV for a named kid sound. Loud clips are much bigger than quiet ones."""
    kind = kind.lower()
    clips: dict[str, list[float]] = {
        "whisper": _noise(0.55, 0.045, seed=11),
        "drum": _thump(0.92),
        "rain": _noise(0.7, 0.05, seed=21),
        "thunder": _thump(0.95) + _noise(0.35, 0.4, seed=22),
        "pages": _noise(0.4, 0.06, seed=31),
        "cymbal": _noise(0.45, 0.85, seed=32),
        "purr": _tone(40, 0.7, 0.07, decay=False),
        "bark": _tone(220, 0.22, 0.88, decay=True) + _thump(0.55),
        "tick": _tone(1200, 0.06, 0.08, decay=True) + _silence(0.12) + _tone(1200, 0.06, 0.08, decay=True),
        "alarm": _tone(880, 0.18, 0.8, decay=False) + _silence(0.06) + _tone(880, 0.18, 0.8, decay=False),
        "rustle": _noise(0.5, 0.05, seed=41),
        "crash": _noise(0.35, 0.9, seed=42) + _thump(0.6),
        "drip": _tone(980, 0.12, 0.07, decay=True),
        "gong": _tone(110, 0.8, 0.85, decay=True),
        "hum": _tone(196, 0.65, 0.06, decay=False),
        "trumpet": _tone(349, 0.45, 0.82, decay=True) + _tone(440, 0.25, 0.7, decay=True),
        "lullaby": _tone(262, 0.35, 0.06, decay=True) + _tone(330, 0.35, 0.06, decay=True),
        "siren": _tone(620, 0.25, 0.8, decay=False) + _tone(480, 0.25, 0.8, decay=False),
        "squeak": _tone(1400, 0.18, 0.07, decay=True),
        "roar": _tone(90, 0.5, 0.9, decay=True) + _noise(0.3, 0.35, seed=51),
        "high": _bell(1046, 0.55),
        "low": _tone(98, 0.7, 0.7, decay=True),
    }
    samples = clips.get(kind) or _tone(440, 0.3, 0.4, decay=True)
    return _wav(samples)


def render_pair(left_kind: str, right_kind: str) -> bytes:
    left = list(_wav_samples(left_kind))
    right = list(_wav_samples(right_kind))
    return _wav(left + _silence(0.35) + right)


def _wav_samples(kind: str) -> list[float]:
    raw = render_sound(kind)
    with wave.open(io.BytesIO(raw), "rb") as reader:
        frames = reader.readframes(reader.getnframes())
    return [struct.unpack_from("<h", frames, i)[0] / 32767 for i in range(0, len(frames), 2)]
