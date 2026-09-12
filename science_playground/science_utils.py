"""Shared visual and interaction engine for Science Playground."""
from __future__ import annotations

import html
import time

import streamlit as st
import streamlit.components.v1 as components

from feedback_popup import clear_feedback_overlay, show_feedback_overlay

FEEDBACK_SECONDS = 2.5
ANIM_SECONDS = 2.0
SCENE_HEIGHT = 340

# These games have hand-built scenes and trial banks.  Everything else uses
# the discovery deck below, so an older one-question module still receives the
# same ten-round, one-shot flow without changing its public entry point.
_BESPOKE_GAMES = {
    "motion_beginner_fast_or_slow",
    "motion_beginner_stop_or_go",
    "motion_beginner_push_or_pull",
    "forces_stuff_beginner_heavy_or_light",
    "forces_stuff_beginner_sink_or_float",
    "light_sound_beginner_light_or_dark",
    "light_sound_beginner_loud_or_quiet",
    "light_sound_beginner_high_or_low",
}

_DISCOVERY_DECKS = {
    "motion": (
        ("🛝", "Playground"), ("🚲", "Bike path"), ("⚽", "Ball field"),
        ("🚌", "Bus stop"), ("🛶", "River"), ("🛹", "Skate park"),
        ("🚂", "Train track"), ("🎢", "Fun fair"), ("🛷", "Snow hill"),
        ("🏁", "Race track"),
    ),
    "forces_stuff": (
        ("📦", "Moving boxes"), ("🧸", "Toy room"), ("🛒", "Market"),
        ("🏖️", "Beach"), ("🧲", "Magnet table"), ("🛝", "Playground"),
        ("🧱", "Building site"), ("⛸️", "Ice rink"), ("🪵", "Wood shop"),
        ("⚖️", "Balance table"),
    ),
    "light_sound": (
        ("🔦", "Flashlight den"), ("🥁", "Music room"), ("🌙", "Night walk"),
        ("🔔", "Bell tower"), ("☀️", "Sunny yard"), ("🗣️", "Empty hall"),
        ("🎸", "Concert"), ("🕯️", "Candle table"), ("🏔️", "Mountain"),
        ("🎵", "Sound lab"),
    ),
    "matter": (
        ("🧊", "Ice tray"), ("💧", "Water table"), ("🍫", "Kitchen"),
        ("🏺", "Clay studio"), ("🥛", "Mixing cup"), ("🌧️", "Rainy yard"),
        ("🕯️", "Warm window"), ("🧱", "Block shelf"), ("❄️", "Freezer"),
        ("☀️", "Sunny puddle"),
    ),
    "living_things": (
        ("🌱", "Garden"), ("🐟", "Pond"), ("🐦", "Bird feeder"),
        ("🌳", "Woodland"), ("🐝", "Flower patch"), ("🐇", "Meadow"),
        ("🦉", "Night forest"), ("🪴", "Window plant"), ("🐣", "Farm"),
        ("🌊", "Rock pool"),
    ),
    "make_test": (
        ("🌉", "Bridge bench"), ("🗼", "Tower table"), ("🛝", "Ramp test"),
        ("⭕", "Shape board"), ("🏎️", "Car track"), ("🔺", "Frame shop"),
        ("🟠", "Marble run"), ("🧱", "Block yard"), ("🔬", "Test station"),
        ("🛠️", "Fix-it table"),
    ),
    "follow_the_steps": (
        ("🤖", "Robot mat"), ("🧦", "Getting dressed"), ("🧼", "Wash time"),
        ("🚦", "Road crossing"), ("🔁", "Dance loop"), ("🍞", "Snack steps"),
        ("🪥", "Brush time"), ("🌱", "Planting"), ("⬜", "Shape path"),
        ("🌧️", "Rainy-day rule"),
    ),
}


def _topic_for(game_id: str) -> str:
    for topic in _DISCOVERY_DECKS:
        if game_id.startswith(topic + "_"):
            return topic
    return "motion"


def _with_discovery_trials(spec: dict) -> dict:
    """Give every legacy game ten ordered, named examples and a held end pose."""
    if spec["id"] in _BESPOKE_GAMES or spec.get("trials"):
        return spec
    deck = _DISCOVERY_DECKS[_topic_for(spec["id"])]
    trials = []
    for index, (icon, place) in enumerate(deck):
        trials.append({
            "scene": "discovery",
            "context_icon": icon,
            "context": place,
            "question": f"{place}: {spec['question']}",
            "choices": list(spec["choices"]),
            "answer": spec["answer"],
            "picture": icon,
            "kid_tip": spec.get("kid_tip") or spec["tip"],
            "trial_style": index % 5,
        })
    return {**spec, "animate_mode": "once", "trials": tuple(trials)}


def inject_form_css() -> None:
    st.markdown(
        """<style>
    div[data-testid="stHorizontalBlock"] button {min-height:4.2rem;font-size:1.25rem;font-weight:750;border-radius:18px}
    .science-card{background:linear-gradient(135deg,#e9f8ff,#fff7dd);border:3px solid #79b9d1;border-radius:24px;padding:1rem;text-align:center}
    </style>""",
        unsafe_allow_html=True,
    )


def scene_svg(picture: str, round_no: int) -> str:
    x = 180 + (round_no % 3) * 70
    p = html.escape(picture)
    return f"""<svg viewBox="0 0 800 300" role="img" aria-label="Game picture" style="width:100%;max-height:300px">
      <defs><linearGradient id="sky" x2="0" y2="1"><stop stop-color="#dff5ff"/><stop offset="1" stop-color="#fff4c7"/></linearGradient></defs>
      <rect width="800" height="300" rx="28" fill="url(#sky)"/>
      <circle cx="690" cy="60" r="34" fill="#ffd166"/><path d="M0 245 Q180 195 360 240 T800 220 V300 H0Z" fill="#8bd17c"/>
      <text x="{x}" y="185" text-anchor="middle" font-size="118">{p}</text>
      <g fill="#457b9d"><circle cx="90" cy="255" r="10"/><circle cx="130" cy="255" r="10"/><circle cx="170" cy="255" r="10"/></g>
      <text x="690" y="270" text-anchor="middle" font-family="system-ui" font-size="24" fill="#345">Round {round_no + 1}</text>
    </svg>"""


def _page(inner_css: str, inner_html: str, aria: str, round_no: int, extra_stage: str = "") -> str:
    stage_cls = "stage " + extra_stage if extra_stage else "stage"
    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"/>
<style>
  html,body{{margin:0;padding:0;overflow:hidden;font-family:system-ui,Segoe UI,sans-serif}}
  .stage{{position:relative;width:100%;height:320px;border-radius:24px;overflow:hidden;border:3px solid #79b9d1}}
  .tag{{position:absolute;font-weight:800;letter-spacing:.04em;text-shadow:0 1px 0 #fff;z-index:2}}
  .round{{position:absolute;right:14px;bottom:10px;font-weight:700;color:#345;font-size:16px;z-index:2}}
  {inner_css}
</style></head>
<body>
<div class="{stage_cls}" role="img" aria-label="{html.escape(aria)}">
{inner_html}
{'' if round_no < 0 else f'<div class="round">Round {round_no + 1}</div>'}
</div>
</body></html>"""


def _speed_drawing(kind: str, pic: str) -> str:
    if kind == "car":
        return (
            '<div class="car-body"><div class="car-win"></div>'
            '<div class="wheel" style="left:14px"></div>'
            '<div class="wheel" style="right:14px"></div></div>'
        )
    if kind == "snail":
        return (
            '<div class="snail-draw"><div class="eye"></div>'
            '<div class="eye" style="left:16px"></div>'
            '<div class="slug"></div><div class="shell"></div></div>'
        )
    if kind == "rocket":
        return '<div class="rocket"><i></i></div>'
    if kind == "balloon":
        return '<div class="balloon"><i></i><b></b></div>'
    if kind == "boat":
        return '<div class="boat-draw"><i class="hull"></i><i class="sail"></i></div>'
    return f'<div class="pic">{html.escape(pic or "•")}</div>'


def _scene_fast_slow(round_no: int, spec: dict | None = None, **kwargs) -> str:
    spec = spec or {}
    pose = str(kwargs.get("pose") or "loop")
    if pose not in ("start", "play", "end", "loop"):
        pose = "loop"
    fast = str(spec.get("fast") or "Race car")
    slow = str(spec.get("slow") or "Snail")
    if "fast" in spec:
        fast_kind = str(spec.get("fast_kind") or "")
        slow_kind = str(spec.get("slow_kind") or "")
    else:
        fast_kind = str(spec.get("fast_kind") or "car")
        slow_kind = str(spec.get("slow_kind") or "snail")
    fast_pic = str(spec.get("fast_pic") or "🏎️")
    slow_pic = str(spec.get("slow_pic") or "🐌")
    fast_top = spec.get("fast_top", True)
    if isinstance(fast_top, str):
        fast_top = fast_top.lower() not in ("0", "false", "no")
    top_name, top_draw, top_cls = (fast, _speed_drawing(fast_kind, fast_pic), "fast")
    bot_name, bot_draw, bot_cls = (slow, _speed_drawing(slow_kind, slow_pic), "slow")
    if not fast_top:
        top_name, top_draw, top_cls, bot_name, bot_draw, bot_cls = (
            bot_name, bot_draw, bot_cls, top_name, top_draw, top_cls
        )
    css = """
    .stage{background:linear-gradient(180deg,#caf0f8 0%,#90e0ef 42%,#52b69a 42%,#52b69a 48%,#d8f3dc 48%,#d8f3dc 88%,#95d5b2 88%)}
    .lane{position:absolute;left:0;right:0;height:6px;background:repeating-linear-gradient(90deg,#fff 0 28px,transparent 28px 48px);opacity:.85}
    .mover{position:absolute;left:16px;width:120px;height:58px}
    .top{top:38px}.bot{top:168px}
    .pose-start .mover{left:16px}
    .pose-play .fast{animation:dashFast 1.5s linear forwards}
    .pose-loop .fast{animation:dashFast 1.5s linear infinite}
    .pose-play .slow{animation:dashSlow 5.5s linear forwards}
    .pose-loop .slow{animation:dashSlow 7s linear infinite}
    .pose-end .fast{left:72%}.pose-end .slow{left:18%}
    @keyframes dashFast{from{left:16px}to{left:72%}}
    @keyframes dashSlow{from{left:16px}to{left:18%}}
    .car-body{width:118px;height:36px;background:#e63946;border-radius:16px 22px 10px 10px;position:relative;box-shadow:0 5px 0 #9d0208;margin-top:10px}
    .car-win{position:absolute;top:-16px;left:36px;width:48px;height:20px;background:#8ecae6;border-radius:10px 12px 0 0}
    .wheel{position:absolute;bottom:-12px;width:22px;height:22px;background:#1d3557;border-radius:50%;border:3px solid #fff}
    .snail-draw{position:relative;width:92px;height:58px}
    .shell{position:absolute;left:34px;top:0;width:50px;height:50px;border-radius:50%;background:conic-gradient(#b08968,#ddb892,#7f5539,#b08968);border:5px solid #7f5539}
    .slug{position:absolute;left:0;bottom:4px;width:70px;height:20px;background:#6a994e;border-radius:20px}
    .eye{position:absolute;left:8px;top:18px;width:4px;height:18px;background:#386641;border-radius:4px}
    .rocket{width:0;height:0;margin-top:8px;border-left:78px solid #e63946;border-top:18px solid transparent;border-bottom:18px solid transparent;filter:drop-shadow(-10px 0 0 #ffd166)}
    .balloon{width:48px;height:58px;margin:0 auto;background:radial-gradient(circle at 30% 28%,#fff,#ef476f);border-radius:50% 50% 50% 50%;position:relative}
    .balloon i{position:absolute;bottom:-10px;left:22px;width:4px;height:18px;background:#6c584c}
    .balloon b{position:absolute;bottom:-16px;left:16px;width:16px;height:10px;border:3px solid #6c584c;border-top:0;border-radius:0 0 10px 10px}
    .boat-draw{position:relative;width:110px;height:52px;margin-top:6px}
    .boat-draw .hull{position:absolute;left:0;bottom:0;width:100px;height:22px;background:#bc6c25;clip-path:polygon(4% 0,96% 0,86% 100%,14% 100%)}
    .boat-draw .sail{position:absolute;left:48px;top:0;border-left:32px solid #f8f9fa;border-top:8px solid transparent;border-bottom:20px solid transparent}
    .pic{font-size:64px;line-height:1;text-align:center}
    """
    body = f"""
    <div class="tag" style="top:8px;left:12px;font-size:22px;color:#1d3557">{html.escape(top_name)}</div>
    <div class="tag" style="top:138px;left:12px;font-size:22px;color:#1d3557">{html.escape(bot_name)}</div>
    <div class="lane" style="top:108px"></div>
    <div class="lane" style="top:248px"></div>
    <div class="mover top {top_cls}">{top_draw}</div>
    <div class="mover bot {bot_cls}">{bot_draw}</div>
    """
    aria = f"{fast} is fast. {slow} is slow."
    return _page(css, body, aria, round_no, extra_stage=f"pose-{pose}")


def _scene_stop_go(round_no: int, spec: dict | None = None, **kwargs) -> str:
    spec = spec or {}
    pose = str(kwargs.get("pose") or "start")
    if pose not in ("start", "play", "end"):
        pose = "start"
    light = str(spec.get("light") or "green").lower()
    if light not in ("green", "yellow", "red"):
        light = "green"
    aria = {
        "green": "The light is green. The car goes all the way.",
        "yellow": "The light is yellow. The car slows down.",
        "red": "The light is red. The car stops.",
    }[light]
    css = """
    .stage{background:linear-gradient(180deg,#caf0f8 0 58%,#6c757d 58% 64%,#2d6a4f 64%)}
    .pole{position:absolute;left:70px;top:28px;width:18px;height:220px;background:#343a40;border-radius:6px}
    .box{position:absolute;left:42px;top:28px;width:74px;height:160px;background:#212529;border-radius:16px;border:4px solid #495057}
    .lamp{width:42px;height:42px;border-radius:50%;margin:10px auto;background:#6c757d}
    .light-green .lamp.g{background:#52b788;box-shadow:0 0 18px 8px #95d5b2;animation:pulseG 1s ease-in-out infinite}
    .light-yellow .lamp.y{background:#ffd166;box-shadow:0 0 18px 8px #ffe8a3;animation:pulseY 1s ease-in-out infinite}
    .light-red .lamp.r{background:#e63946;box-shadow:0 0 18px 8px #f4a3a8;animation:pulseR 1s ease-in-out infinite}
    .stopline{position:absolute;left:calc(42% + 110px);top:182px;width:10px;height:30px;background:repeating-linear-gradient(#fff 0 7px,#fff0 7px 11px);border-radius:2px;box-shadow:0 0 0 2px #1d3557}
    .car{position:absolute;top:175px;width:120px;height:48px;left:140px}
    .car-body{width:118px;height:36px;background:#457b9d;border-radius:16px 22px 10px 10px;position:relative}
    .car-win{position:absolute;top:-16px;left:36px;width:48px;height:20px;background:#caf0f8;border-radius:10px 12px 0 0}
    .wheel{position:absolute;bottom:-12px;width:22px;height:22px;background:#1d3557;border-radius:50%;border:3px solid #fff}
    .pose-play.light-green .car{animation:goDrive 1.7s ease-in forwards}
    .pose-play.light-yellow .car{animation:slowDrive 3.2s ease-out forwards}
    .pose-play.light-red .car{animation:stopDrive 1.5s cubic-bezier(.15,.8,.2,1) forwards}
    .pose-end.light-green .car{left:108%}
    .pose-end.light-yellow .car{left:108%}
    .pose-end.light-red .car{left:42%}
    .pose-play.light-green .wheel{animation:spin .32s linear infinite}
    .pose-play.light-yellow .wheel{animation:spin .7s linear infinite}
    .pose-play.light-red .wheel{animation:spin .45s linear 3}
    @keyframes pulseG{50%{box-shadow:0 0 26px 12px #d8f3dc}}
    @keyframes pulseY{50%{box-shadow:0 0 26px 12px #fff3bf}}
    @keyframes pulseR{50%{box-shadow:0 0 26px 12px #ffc9c9}}
    @keyframes spin{to{transform:rotate(360deg)}}
    @keyframes goDrive{from{left:140px}to{left:108%}}
    @keyframes slowDrive{from{left:140px}to{left:108%}}
    @keyframes stopDrive{from{left:140px}to{left:42%}}
    """
    body = """
    <div class="pole"></div>
    <div class="box"><div class="lamp r"></div><div class="lamp y"></div><div class="lamp g"></div></div>
    <div class="stopline"></div>
    <div class="car"><div class="car-body"><div class="car-win"></div>
      <div class="wheel" style="left:14px"></div><div class="wheel" style="right:14px"></div>
    </div></div>
    """
    return _page(css, body, aria, round_no, extra_stage=f"pose-{pose} light-{light}")


# Push/pull uses SVG groups + SMIL so contact stays glued in viewBox units
# even when the scene scales. Walk is a short 2-step bob, one-shot, then freeze.
_PP_DUR = "1.8s"
_PP_GROUND = 250
_PP_ACTORS = {
    "kid": {"h": 118, "hand_x": 80, "hand_y": 84, "label": "kid"},
    "girl": {"h": 118, "hand_x": 80, "hand_y": 84, "label": "girl"},
    "hero": {"h": 118, "hand_x": 80, "hand_y": 84, "label": "hero"},
    "parent": {"h": 118, "hand_x": 80, "hand_y": 84, "label": "parent"},
    "firefighter": {"h": 118, "hand_x": 80, "hand_y": 84, "label": "firefighter"},
    "robot": {"h": 104, "hand_x": 90, "hand_y": 68, "label": "robot"},
    "ant": {"h": 44, "hand_x": 80, "hand_y": 20, "label": "ant"},
    "dog": {"h": 74, "hand_x": 126, "hand_y": 28, "label": "dog"},
}
_PP_OBJECTS = {
    "wagon": {"w": 124, "h": 54, "grip": 42, "cy": 16},
    "ant_rock": {"w": 88, "h": 58, "grip": 0, "cy": 30},
    "girl_car": {"w": 152, "h": 58, "grip": 0, "cy": 32},
    "sled": {"w": 132, "h": 44, "grip": 40, "cy": 16},
    "dog_toy": {"w": 50, "h": 50, "grip": 36, "cy": 14},
    "hero_bus": {"w": 210, "h": 80, "grip": 0, "cy": 40},
    "box": {"w": 94, "h": 86, "grip": 0, "cy": 42},
    "crate": {"w": 92, "h": 80, "grip": 0, "cy": 40},
    "suitcase": {"w": 74, "h": 88, "grip": 28, "cy": 14},
    "teddy": {"w": 72, "h": 86, "grip": 8, "cy": 60},
    "stroller": {"w": 108, "h": 72, "grip": 0, "cy": 40},
    "hose": {"w": 172, "h": 44, "grip": 32, "cy": 20},
}


def _smil_translate(x0: float, x_mid: float, x1: float, y: float) -> str:
    """One-shot x move: start → mid (contact) → end, then freeze."""
    return (
        f'<animateTransform attributeName="transform" type="translate" '
        f'values="{x0},{y};{x_mid},{y};{x1},{y}" keyTimes="0;0.4;1" '
        f'keySplines="0.42 0 0.58 1;0 0 1 1" calcMode="spline" '
        f'dur="{_PP_DUR}" fill="freeze"/>'
    )


def _smil_bob() -> str:
    return (
        '<animateTransform attributeName="transform" type="translate" '
        'values="0,0;0,-6;0,0;0,-6;0,0;0,-6;0,0;0,-6;0,0" '
        f'dur="{_PP_DUR}" fill="freeze" calcMode="linear"/>'
    )


def _smil_stride(cx: float, cy: float) -> str:
    return (
        f'<animateTransform attributeName="transform" type="rotate" '
        f'values="0 {cx} {cy};-16 {cx} {cy};16 {cx} {cy};-16 {cx} {cy};'
        f'16 {cx} {cy};0 {cx} {cy}" dur="{_PP_DUR}" fill="freeze" calcMode="linear"/>'
    )


def _push_pull_layout(kind: str, actor: str, motion: str) -> dict[str, float | str]:
    """Start / contact / end x so the hand stays on the object edge while coupled."""
    ag = _PP_ACTORS.get(actor, _PP_ACTORS["kid"])
    og = _PP_OBJECTS.get(kind, _PP_OBJECTS["wagon"])
    contact_local = -float(og["grip"]) if motion == "pull" else 0.0
    hand = float(ag["hand_x"])
    ax0 = 28.0
    walk = 120.0
    ox_max = 780.0 - float(og["w"])
    ax_c = ax0 + walk
    ox0 = ax_c + hand - contact_local
    if ox0 > ox_max:
        ox0 = ox_max
        ax_c = ox0 + contact_local - hand
        ax0 = max(8.0, min(ax0, ax_c - 56.0))
    # Hand (or mandibles / nose) on the object's near edge / grip at contact.
    ax_c = ox0 + contact_local - hand
    if motion == "push":
        travel = max(70.0, min(150.0, ox_max - ox0))
    else:
        travel = -min(64.0, max(40.0, ax_c - 16.0))
        if ax_c + travel < 8:
            travel = 8.0 - ax_c
    ax1 = ax_c + travel
    ox1 = ox0 + travel
    ay = float(_PP_GROUND - ag["h"])
    oy_ground = float(_PP_GROUND - og["h"])
    oy_align = ay + float(ag["hand_y"]) - float(og["cy"])
    # Held toys rise to the hand; wagons, rocks, and boxes stay on the path.
    if kind in ("teddy", "dog_toy"):
        oy = min(oy_ground, oy_align)
    else:
        oy = oy_ground
    return {
        "ax0": ax0, "ax_c": ax_c, "ax1": ax1, "ay": ay,
        "ox0": ox0, "ox1": ox1, "oy": oy,
        "label": str(ag["label"]),
        "grip": float(og["grip"]),
    }


def _person_svg(actor: str, pose: str) -> str:
    bob = _smil_bob() if pose == "play" else ""
    def leg(x: float, y: float, fill: str) -> str:
        stride = _smil_stride(x + 5.5, y) if pose == "play" else ""
        return f'<rect x="{x}" y="{y}" width="11" height="42" rx="5" fill="{fill}">{stride}</rect>'

    def reach_arm(fill: str) -> str:
        # From the right shoulder, hang down, then reach toward the object.
        return (
            f'<circle cx="48" cy="38" r="6" fill="{fill}"/>'
            f'<path d="M48 38 L60 66 L80 84" fill="none" stroke="{fill}" '
            f'stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<circle cx="80" cy="84" r="7" fill="{fill}"/>'
        )

    if actor == "ant":
        def aleg(x: float) -> str:
            stride = _smil_stride(x + 2, 28) if pose == "play" else ""
            return (
                f'<g>{stride}<rect x="{x}" y="28" width="4" height="14" rx="2" fill="#2b2d42"/></g>'
            )
        return f"""
        <g class="bob">{bob}
          <ellipse cx="16" cy="20" rx="15" ry="12" fill="#3d405b"/>
          <ellipse cx="38" cy="20" rx="12" ry="11" fill="#2b2d42"/>
          <circle cx="58" cy="20" r="11" fill="#3d405b"/>
          <path d="M68 13 L80 9" stroke="#2b2d42" stroke-width="3" stroke-linecap="round"/>
          <path d="M68 27 L80 31" stroke="#2b2d42" stroke-width="3" stroke-linecap="round"/>
          {aleg(24)}{aleg(38)}{aleg(50)}
        </g>"""
    if actor == "dog":
        def dleg(x: float) -> str:
            stride = _smil_stride(x + 5, 46) if pose == "play" else ""
            return f'<rect x="{x}" y="46" width="10" height="26" rx="5" fill="#6c584c">{stride}</rect>'
        return f"""
        <g class="bob">{bob}
          <ellipse cx="18" cy="22" rx="12" ry="6" fill="#b08968"/>
          <ellipse cx="58" cy="32" rx="40" ry="18" fill="#7f5539"/>
          <ellipse cx="102" cy="26" rx="22" ry="18" fill="#b08968"/>
          <ellipse cx="118" cy="30" rx="10" ry="7" fill="#b08968"/>
          <circle cx="126" cy="28" r="4" fill="#3d405b"/>
          <ellipse cx="94" cy="10" rx="8" ry="12" fill="#6c584c"/>
          <circle cx="108" cy="22" r="4" fill="#1d3557"/>
          {dleg(38)}{dleg(56)}{dleg(78)}{dleg(98)}
        </g>"""
    if actor == "robot":
        def rleg(x: float) -> str:
            stride = _smil_stride(x + 5, 74) if pose == "play" else ""
            return f'<rect x="{x}" y="74" width="10" height="30" rx="4" fill="#2b2d42">{stride}</rect>'
        return f"""
        <g class="bob">{bob}
          <rect x="22" y="2" width="28" height="24" rx="5" fill="#8d99ae"/>
          <circle cx="30" cy="14" r="4" fill="#90e0ef"/>
          <circle cx="42" cy="14" r="4" fill="#90e0ef"/>
          <rect x="16" y="28" width="40" height="46" rx="6" fill="#2b2d42"/>
          <rect x="24" y="40" width="24" height="10" rx="2" fill="#ef476f"/>
          <path d="M54 38 L90 68" stroke="#8d99ae" stroke-width="10" stroke-linecap="round"/>
          <rect x="84" y="62" width="14" height="14" rx="3" fill="#8d99ae"/>
          {rleg(20)}{rleg(42)}
        </g>"""
    if actor == "girl":
        return f"""
        <g class="bob">{bob}
          <circle cx="18" cy="14" r="9" fill="#6d4c41"/>
          <circle cx="46" cy="14" r="9" fill="#6d4c41"/>
          <circle cx="32" cy="20" r="16" fill="#f4a261"/>
          <path d="M16 38 L48 38 L52 78 L12 78 Z" fill="#ef476f"/>
          {reach_arm("#f4a261")}
          {leg(20, 76, "#f4a261")}{leg(34, 76, "#f4a261")}
        </g>"""
    if actor == "hero":
        return f"""
        <g class="bob">{bob}
          <path d="M8 44 L28 44 L18 108 Z" fill="#118ab2"/>
          <circle cx="32" cy="18" r="16" fill="#f4a261"/>
          <rect x="16" y="34" width="32" height="42" rx="8" fill="#073b4c"/>
          {reach_arm("#f4a261")}
          {leg(18, 76, "#073b4c")}{leg(34, 76, "#073b4c")}
        </g>"""
    if actor == "parent":
        return f"""
        <g class="bob">{bob}
          <circle cx="32" cy="16" r="15" fill="#6d4c41"/>
          <circle cx="32" cy="20" r="14" fill="#f4a261"/>
          <rect x="16" y="34" width="32" height="42" rx="8" fill="#2a9d8f"/>
          {reach_arm("#f4a261")}
          {leg(20, 76, "#264653")}{leg(34, 76, "#264653")}
        </g>"""
    if actor == "firefighter":
        return f"""
        <g class="bob">{bob}
          <ellipse cx="32" cy="10" rx="18" ry="12" fill="#e63946"/>
          <rect x="14" y="14" width="36" height="7" rx="2" fill="#ffd166"/>
          <circle cx="32" cy="24" r="13" fill="#f4a261"/>
          <rect x="14" y="36" width="36" height="42" rx="8" fill="#c1121f"/>
          <rect x="14" y="52" width="36" height="8" fill="#ffd166"/>
          {reach_arm("#f4a261")}
          {leg(20, 76, "#212529")}{leg(34, 76, "#212529")}
        </g>"""
    return f"""
        <g class="bob">{bob}
          <circle cx="32" cy="18" r="16" fill="#f4a261"/>
          <rect x="16" y="34" width="32" height="42" rx="8" fill="#e76f51"/>
          {reach_arm("#f4a261")}
          {leg(20, 76, "#264653")}{leg(34, 76, "#264653")}
        </g>"""


def _object_svg(kind: str, motion: str, grip: float) -> str:
    rope = (
        f'<rect x="{-grip}" y="14" width="{grip}" height="8" rx="4" fill="#6c584c"/>'
        if grip
        else ""
    )
    if kind == "ant_rock":
        return (
            '<ellipse cx="44" cy="30" rx="42" ry="28" fill="#6c757d"/>'
            '<ellipse cx="34" cy="24" rx="14" ry="10" fill="#adb5bd" opacity=".45"/>'
        )
    if kind == "girl_car":
        return """
          <rect x="40" y="2" width="70" height="22" rx="10" fill="#8ecae6"/>
          <rect x="0" y="18" width="148" height="28" rx="10" fill="#e63946"/>
          <circle cx="28" cy="50" r="11" fill="#1d3557"/>
          <circle cx="118" cy="50" r="11" fill="#1d3557"/>"""
    if kind == "sled":
        return f"""
          {rope}
          <rect x="0" y="8" width="128" height="22" rx="8" fill="#d62828"/>
          <path d="M8 36 H120" stroke="#6c757d" stroke-width="6" fill="none" stroke-linecap="round"/>"""
    if kind == "dog_toy":
        return f"""
          {rope}
          <circle cx="25" cy="25" r="23" fill="#fcbf49" stroke="#f77f00" stroke-width="4"/>"""
    if kind == "hero_bus":
        return """
          <rect x="0" y="8" width="206" height="52" rx="10" fill="#ffd166" stroke="#f4a261" stroke-width="4"/>
          <rect x="16" y="18" width="28" height="20" rx="4" fill="#90e0ef"/>
          <rect x="54" y="18" width="28" height="20" rx="4" fill="#90e0ef"/>
          <rect x="92" y="18" width="28" height="20" rx="4" fill="#90e0ef"/>
          <rect x="130" y="18" width="28" height="20" rx="4" fill="#90e0ef"/>
          <circle cx="36" cy="68" r="12" fill="#1d3557"/>
          <circle cx="170" cy="68" r="12" fill="#1d3557"/>"""
    if kind == "box":
        return (
            '<rect x="0" y="0" width="90" height="82" rx="6" fill="#d4a373" stroke="#bc6c25" stroke-width="4"/>'
            '<rect x="4" y="58" width="82" height="20" fill="#c08a5c"/>'
        )
    if kind == "suitcase":
        return f"""
          {rope}
          <rect x="0" y="8" width="70" height="68" rx="10" fill="#457b9d" stroke="#1d3557" stroke-width="4"/>
          <circle cx="16" cy="80" r="8" fill="#1d3557"/>
          <circle cx="54" cy="80" r="8" fill="#1d3557"/>"""
    if kind == "teddy":
        return """
          <circle cx="22" cy="14" r="10" fill="#c4a574"/>
          <circle cx="54" cy="14" r="10" fill="#c4a574"/>
          <circle cx="38" cy="30" r="20" fill="#d4a373"/>
          <ellipse cx="38" cy="64" rx="22" ry="20" fill="#d4a373"/>
          <ellipse cx="4" cy="60" rx="14" ry="10" fill="#c4a574"/>
          <ellipse cx="66" cy="60" rx="10" ry="8" fill="#c4a574"/>
          <circle cx="31" cy="28" r="3" fill="#3d405b"/>
          <circle cx="45" cy="28" r="3" fill="#3d405b"/>
          <ellipse cx="38" cy="36" rx="5" ry="4" fill="#6c584c"/>"""
    if kind == "stroller":
        return """
          <path d="M4 40 L4 16 L18 16" stroke="#1d3557" stroke-width="7" fill="none"
                stroke-linecap="round" stroke-linejoin="round"/>
          <rect x="0" y="36" width="18" height="8" rx="4" fill="#1d3557"/>
          <path d="M36 6 Q86 0 98 38 L40 38 Q36 22 36 6Z" fill="#457b9d"/>
          <rect x="34" y="36" width="64" height="16" rx="6" fill="#a8dadc"/>
          <path d="M16 40 L40 40 L44 58 M88 40 L92 58" stroke="#1d3557" stroke-width="4" fill="none"/>
          <circle cx="42" cy="60" r="12" fill="#1d3557"/>
          <circle cx="90" cy="60" r="12" fill="#1d3557"/>"""
    if kind == "crate":
        return """
          <rect x="0" y="0" width="88" height="76" rx="4" fill="#c9a227" stroke="#7f5539" stroke-width="4"/>
          <path d="M0 25 H88 M0 50 H88 M29 0 V76 M59 0 V76" stroke="#7f5539" stroke-width="3" fill="none"/>"""
    if kind == "hose":
        return f"""
          {rope}
          <rect x="0" y="12" width="22" height="14" rx="3" fill="#adb5bd"/>
          <path d="M22 20 C50 8, 70 36, 100 18 C120 8, 140 28, 168 22" stroke="#e63946"
                stroke-width="10" fill="none" stroke-linecap="round"/>"""
    # wagon: handle on the pull side so a push meets the bed, not a floating bar
    handle = (
        f'<rect x="{-grip}" y="12" width="{grip}" height="8" rx="4" fill="#6c584c"/>'
        if motion == "pull"
        else '<rect x="120" y="12" width="42" height="8" rx="4" fill="#6c584c"/>'
    )
    return f"""
          {handle}
          <rect x="0" y="4" width="120" height="32" rx="8" fill="#e9c46a" stroke="#bc6c25" stroke-width="4"/>
          <circle cx="24" cy="44" r="11" fill="#1d3557"/>
          <circle cx="96" cy="44" r="11" fill="#1d3557"/>"""


def _pp_group(x0: float, x_mid: float, x1: float, y: float, pose: str, inner: str) -> str:
    if pose == "end":
        x, anim = x1, ""
    elif pose == "play":
        x, anim = x0, _smil_translate(x0, x_mid, x1, y)
    else:
        x, anim = x0, ""
    return f'<g transform="translate({x},{y})">{anim}{inner}</g>'


def _scene_push_pull(round_no: int, spec: dict | None = None, **kwargs) -> str:
    spec = spec or {}
    kind = str(spec.get("kind") or "wagon")
    actor = str(spec.get("actor") or "kid")
    pose = str(kwargs.get("pose") or "idle")
    motion = str(kwargs.get("motion") or "").lower()
    if motion not in ("push", "pull"):
        motion = str(spec.get("action") or "pull").lower()
    move = motion if motion in ("push", "pull") else "pull"
    show_tag = pose in ("play", "end")
    lay = _push_pull_layout(kind, actor, move)
    css = """
    .stage{background:#ffe8d6}
    .stage svg{display:block;width:100%;height:320px}
    """
    tag = html.escape(move.upper()) if show_tag else ""
    tag_svg = (
        f'<text x="400" y="36" text-anchor="middle" font-family="system-ui" '
        f'font-size="30" font-weight="800" fill="#9c6644">{tag}</text>'
        if tag
        else ""
    )
    who = html.escape(str(lay["label"]))
    actor_svg = _pp_group(
        float(lay["ax0"]), float(lay["ax_c"]), float(lay["ax1"]), float(lay["ay"]),
        pose, _person_svg(actor, pose),
    )
    object_svg = _pp_group(
        float(lay["ox0"]), float(lay["ox0"]), float(lay["ox1"]), float(lay["oy"]),
        pose, _object_svg(kind, move, float(lay["grip"])),
    )
    body = f"""
    <svg viewBox="0 0 800 320" xmlns="http://www.w3.org/2000/svg" role="img">
      <rect width="800" height="320" fill="#ffe8d6"/>
      <rect y="242" width="800" height="18" fill="#bc6c25"/>
      <rect y="260" width="800" height="60" fill="#606c38"/>
      {tag_svg}
      {actor_svg}
      {object_svg}
      <text x="18" y="308" font-family="system-ui" font-size="20" font-weight="800" fill="#fefae0">{who}</text>
    </svg>"""
    aria = spec.get("question") or "A person moves an object."
    return _page(css, body, str(aria), round_no, extra_stage=f"kind-{kind} pose-{pose}")


def _fall_drawing(pic: str, kind: str) -> str:
    if kind == "bowling":
        return '<div class="bowling"><i></i><i></i><i></i></div>'
    if kind == "marshmallow":
        return '<div class="mallow"></div>'
    if kind == "anvil":
        return '<div class="anvil"></div>'
    if kind == "bubble":
        return '<div class="bubble"></div>'
    if kind == "dumbbell":
        return '<div class="dumbbell"><b></b><span></span><b></b></div>'
    if kind == "paper_plane":
        return '<div class="paper-plane"></div>'
    if kind == "cotton":
        return '<div class="cotton"><i></i><i></i><i></i></div>'
    return f'<div class="pic">{html.escape(pic or "•")}</div>'


def _scene_heavy_light(round_no: int, spec: dict | None = None, **kwargs) -> str:
    spec = spec or {}
    pose = str(kwargs.get("pose") or "play")
    if pose not in ("start", "play", "end"):
        pose = "play"
    heavy = str(spec.get("heavy") or "Rock")
    light = str(spec.get("light") or "Feather")
    heavy_pic = str(spec.get("heavy_pic") or "🪨")
    light_pic = str(spec.get("light_pic") or "🪶")
    heavy_kind = str(spec.get("heavy_kind") or "")
    light_kind = str(spec.get("light_kind") or "")
    heavy_left = spec.get("heavy_left", True)
    if isinstance(heavy_left, str):
        heavy_left = heavy_left.lower() not in ("0", "false", "no")
    left_name, left_draw, left_cls = (heavy, _fall_drawing(heavy_pic, heavy_kind), "heavy")
    right_name, right_draw, right_cls = (light, _fall_drawing(light_pic, light_kind), "light")
    if not heavy_left:
        left_name, left_draw, left_cls, right_name, right_draw, right_cls = (
            right_name, right_draw, right_cls, left_name, left_draw, left_cls
        )
    css = """
    .stage{background:linear-gradient(180deg,#caf0f8 0 72%,#6a994e 72%)}
    .col{position:absolute;top:0;bottom:0;width:44%}
    .col.left{left:4%}.col.right{right:4%}
    .name{position:absolute;top:8px;left:0;right:0;text-align:center;font-size:24px;font-weight:800;color:#1d3557;z-index:2}
    .item{position:absolute;left:50%;width:120px;margin-left:-60px;text-align:center}
    .pose-start .item,.pose-play .item{top:52px}
    .pose-end .item{top:208px}
    .pose-end .light{margin-left:-44px}
    .pose-play .heavy{animation:drop 1.15s ease-in forwards}
    .pose-play .light{animation:drift 2.4s ease-in-out forwards}
    @keyframes drop{from{top:52px}to{top:208px}}
    @keyframes drift{0%{top:52px;margin-left:-60px}40%{top:118px;margin-left:-22px}100%{top:208px;margin-left:-44px}}
    .pic{font-size:72px;line-height:1}
    .bowling{width:72px;height:72px;margin:0 auto;background:#212529;border-radius:50%;position:relative;box-shadow:inset -8px -6px 0 #000}
    .bowling i{position:absolute;width:8px;height:8px;background:#adb5bd;border-radius:50%}
    .bowling i:nth-child(1){top:18px;left:28px}
    .bowling i:nth-child(2){top:28px;left:20px}
    .bowling i:nth-child(3){top:28px;left:36px}
    .mallow{width:48px;height:66px;margin:0 auto;background:#ffe5ec;border:3px solid #ffafcc;border-radius:16px;box-shadow:inset 0 -12px 0 #ffc2d4}
    .anvil{width:90px;height:64px;margin:8px auto 0;background:#343a40;clip-path:polygon(8% 0,92% 0,80% 26%,68% 26%,68% 44%,96% 68%,96% 100%,4% 100%,4% 68%,32% 44%,32% 26%,20% 26%)}
    .bubble{width:64px;height:64px;margin:0 auto;border-radius:50%;background:radial-gradient(circle at 30% 30%,#fff,rgba(144,224,239,.15) 42%,rgba(72,202,228,.45));border:3px solid #90e0ef}
    .dumbbell{display:flex;align-items:center;justify-content:center;height:72px}
    .dumbbell b{width:28px;height:52px;background:#495057;border-radius:8px}
    .dumbbell span{width:52px;height:12px;background:#adb5bd;border-radius:6px}
    .paper-plane{width:0;height:0;margin:18px auto 0;border-left:70px solid #f8f9fa;border-top:18px solid transparent;border-bottom:28px solid transparent;filter:drop-shadow(3px 3px 0 #adb5bd)}
    .cotton{position:relative;width:80px;height:58px;margin:8px auto 0}
    .cotton i{position:absolute;background:#fff;border:2px solid #dee2e6;border-radius:50%}
    .cotton i:nth-child(1){width:40px;height:40px;left:8px;top:10px}
    .cotton i:nth-child(2){width:36px;height:36px;left:32px;top:4px}
    .cotton i:nth-child(3){width:34px;height:34px;left:22px;top:18px}
    """
    body = f"""
    <div class="col left">
      <div class="name">{html.escape(left_name)}</div>
      <div class="item {left_cls}">{left_draw}</div>
    </div>
    <div class="col right">
      <div class="name">{html.escape(right_name)}</div>
      <div class="item {right_cls}">{right_draw}</div>
    </div>
    """
    aria = f"{heavy} and {light}."
    return _page(css, body, aria, round_no, extra_stage=f"pose-{pose}")


def _float_drawing(kind: str) -> str:
    if kind == "duck":
        return '<div class="duck"><i class="body"></i><i class="head"></i><i class="beak"></i><i class="eye"></i></div>'
    if kind == "rock":
        return '<div class="rock"></div>'
    if kind == "boat":
        return '<div class="boat"><i class="hull"></i><i class="mast"></i><i class="sail"></i></div>'
    if kind == "coin":
        return '<div class="coin"></div>'
    if kind == "beachball":
        return '<div class="beachball"></div>'
    if kind == "spoon":
        return '<div class="spoon"><i class="bowl"></i><i class="handle"></i></div>'
    if kind == "apple":
        return '<div class="apple"><i class="stem"></i><i class="leaf"></i></div>'
    if kind == "key":
        return '<div class="key"><i class="head"></i><i class="shaft"></i><i class="tooth"></i></div>'
    if kind == "bottle":
        return '<div class="bottle"><i class="cap"></i><i class="neck"></i><i class="body"></i></div>'
    if kind == "toy_car":
        return '<div class="toy-car"><i class="cab"></i><i class="body"></i><i class="wheel a"></i><i class="wheel b"></i></div>'
    return '<div class="rock"></div>'


def _scene_sink_float(round_no: int, spec: dict | None = None, **kwargs) -> str:
    spec = spec or {}
    pose = str(kwargs.get("pose") or "play")
    if pose not in ("start", "play", "end"):
        pose = "play"
    item = str(spec.get("item") or "Rubber duck")
    kind = str(spec.get("kind") or "duck")
    answer = str(spec.get("answer") or "Float")
    cls = "float" if answer.lower() == "float" else "sink"
    css = """
    .stage{background:linear-gradient(180deg,#caf0f8 0 88%,#b7e4c7 88%)}
    .name{position:absolute;top:6px;left:0;right:0;text-align:center;font-size:24px;font-weight:800;color:#1d3557;z-index:4}
    .tank{position:absolute;left:16%;right:16%;top:42px;bottom:18px;border:7px solid #8d99ae;border-top:12px solid #adb5bd;border-radius:8px 8px 28px 28px;overflow:hidden;background:linear-gradient(180deg,#e0f7ff 0 36%,#90e0ef 36% 40%,#0077b6 40% 90%,#023e8a 90%);box-shadow:inset 12px 0 0 rgba(255,255,255,.2),inset -8px 0 0 rgba(0,0,0,.08)}
    .wave{position:absolute;left:0;right:0;top:36%;height:10px;background:linear-gradient(180deg,#caf0f8,#48cae4);z-index:1}
    .wet{position:absolute;left:0;right:0;top:38%;bottom:0;background:rgba(2,62,138,.18);z-index:3;pointer-events:none}
    .item{position:absolute;left:50%;width:120px;margin-left:-60px;text-align:center;z-index:2}
    .item i{display:block}
    .pose-start .item,.pose-play .item{top:6px}
    .pose-end .float{top:58px}
    .pose-end .sink{top:168px}
    .pose-play .float{animation:splashBob 2.1s ease-in-out forwards}
    .pose-play .sink{animation:plunge 1.35s ease-in forwards}
    @keyframes splashBob{0%{top:6px}38%{top:58px}52%{top:46px}68%{top:66px}84%{top:54px}100%{top:58px}}
    @keyframes plunge{from{top:6px}to{top:168px}}
    .duck{position:relative;width:88px;height:62px;margin:0 auto}
    .duck .body{position:absolute;left:2px;bottom:0;width:68px;height:40px;background:#ffd166;border-radius:50% 50% 42% 42%;box-shadow:inset 0 -8px 0 #f4a261}
    .duck .head{position:absolute;right:4px;top:0;width:36px;height:36px;background:#ffd166;border-radius:50%}
    .duck .beak{position:absolute;right:-10px;top:16px;width:22px;height:12px;background:#f77f00;border-radius:6px}
    .duck .eye{position:absolute;right:14px;top:10px;width:8px;height:8px;background:#1d3557;border-radius:50%}
    .rock{width:74px;height:50px;margin:10px auto 0;background:#6c757d;border-radius:42% 55% 48% 52%;box-shadow:inset -10px -8px 0 #495057}
    .boat{position:relative;width:100px;height:58px;margin:6px auto 0}
    .boat .hull{position:absolute;left:0;bottom:0;width:100px;height:26px;background:#bc6c25;clip-path:polygon(4% 0,96% 0,86% 100%,14% 100%)}
    .boat .mast{position:absolute;left:48px;top:2px;width:5px;height:30px;background:#6c584c}
    .boat .sail{position:absolute;left:53px;top:4px;border-left:32px solid #f8f9fa;border-top:8px solid transparent;border-bottom:20px solid transparent;filter:drop-shadow(2px 2px 0 #adb5bd)}
    .coin{width:54px;height:54px;margin:8px auto 0;border-radius:50%;background:radial-gradient(circle at 32% 30%,#ffe8a3,#e9c46a 55%,#bc6c25);border:5px solid #c9a227;box-shadow:inset 0 0 0 7px rgba(255,255,255,.18)}
    .beachball{width:64px;height:64px;margin:4px auto 0;border-radius:50%;background:conic-gradient(#e63946 0 90deg,#fff 90deg 180deg,#457b9d 180deg 270deg,#ffd166 270deg);border:3px solid #1d3557}
    .spoon{width:30px;height:78px;margin:0 auto;position:relative}
    .spoon .bowl{width:30px;height:34px;background:#ced4da;border-radius:50%;box-shadow:inset -5px -4px 0 #6c757d}
    .spoon .handle{width:10px;height:46px;margin:-4px auto 0;background:#adb5bd;border-radius:5px}
    .apple{position:relative;width:56px;height:56px;margin:12px auto 0;background:radial-gradient(circle at 30% 28%,#f94144,#c1121f);border-radius:50% 50% 46% 46%}
    .apple .stem{position:absolute;top:-10px;left:24px;width:6px;height:14px;background:#6c584c;border-radius:3px}
    .apple .leaf{position:absolute;top:-12px;left:30px;width:18px;height:12px;background:#52b788;border-radius:0 50% 0 50%}
    .key{position:relative;width:86px;height:36px;margin:18px auto 0}
    .key .head{width:28px;height:28px;border:7px solid #e9c46a;border-radius:50%}
    .key .shaft{position:absolute;left:26px;top:10px;width:52px;height:10px;background:#e9c46a;border-radius:3px}
    .key .tooth{position:absolute;right:6px;top:20px;width:10px;height:14px;background:#e9c46a}
    .bottle{width:38px;height:76px;margin:2px auto 0}
    .bottle .cap{width:18px;height:8px;margin:0 auto;background:#e63946;border-radius:3px}
    .bottle .neck{width:16px;height:16px;margin:0 auto;background:rgba(144,224,239,.4);border:3px solid #48cae4;border-top:0}
    .bottle .body{width:36px;height:46px;margin:0 auto;background:rgba(144,224,239,.28);border:3px solid #48cae4;border-radius:8px}
    .toy-car{position:relative;width:96px;height:52px;margin:10px auto 0}
    .toy-car .cab{position:absolute;left:28px;top:0;width:40px;height:22px;background:#8ecae6;border-radius:8px 10px 0 0}
    .toy-car .body{position:absolute;left:4px;top:16px;width:88px;height:22px;background:#e63946;border-radius:8px}
    .toy-car .wheel{position:absolute;bottom:0;width:16px;height:16px;background:#1d3557;border-radius:50%;border:3px solid #fff}
    .toy-car .wheel.a{left:16px}.toy-car .wheel.b{right:16px}
    """
    body = f"""
    <div class="name">{html.escape(item)}</div>
    <div class="tank">
      <div class="wave"></div>
      <div class="item {cls}">{_float_drawing(kind)}</div>
      <div class="wet"></div>
    </div>
    """
    aria = f"{item} in a water tank."
    return _page(css, body, aria, round_no, extra_stage=f"pose-{pose}")


def _scene_sticky_slippy(round_no: int, spec: dict | None = None, **kwargs) -> str:
    css = """
    .stage{background:#fff}
    .half{position:absolute;top:0;bottom:0;width:50%}
    .rug{left:0;background:repeating-linear-gradient(90deg,#bc4749 0 18px,#f2e8cf 18px 28px)}
    .ice{right:0;background:linear-gradient(180deg,#caf0f8,#90e0ef)}
    .box{position:absolute;width:70px;height:48px;border-radius:10px;bottom:70px}
    .still{left:18%;background:#e76f51;box-shadow:0 6px 0 #9d0208}
    .slide{background:#457b9d;animation:slide 1.8s linear infinite}
    @keyframes slide{0%{left:54%}100%{left:86%}}
    """
    body = """
    <div class="half rug"></div>
    <div class="half ice"></div>
    <div class="tag" style="top:10px;left:8%;font-size:24px;color:#fff">STICKY</div>
    <div class="tag" style="top:10px;right:8%;font-size:24px;color:#023e8a">SLIPPY</div>
    <div class="box still"></div>
    <div class="box slide"></div>
    """
    return _page(css, body, "A rug is sticky. Ice is slippy.", round_no)


def _scene_discovery(round_no: int, spec: dict | None = None, **kwargs) -> str:
    """A large topic-specific experiment card with one-shot, held motion."""
    spec = spec or {}
    pose = str(kwargs.get("pose") or "play")
    topic = _topic_for(str(spec.get("id") or "motion"))
    icon = html.escape(str(spec.get("context_icon") or spec.get("picture") or "🔬"))
    context = html.escape(str(spec.get("context") or "Science table"))
    style = int(spec.get("trial_style") or 0)
    palettes = (
        ("#dff5ff", "#90e0ef", "#e63946"),
        ("#fff1c7", "#95d5b2", "#457b9d"),
        ("#f3e8ff", "#cdb4db", "#f77f00"),
        ("#e8f5e9", "#80ed99", "#6a4c93"),
        ("#ffe8d6", "#ffafcc", "#118ab2"),
    )
    sky, ground, accent = palettes[style % len(palettes)]
    topic_art = {
        "motion": """
          <path d="M90 238 Q300 80 710 238" fill="none" stroke="#6c757d" stroke-width="18"/>
          <circle class="idea mover" cx="120" cy="210" r="30" fill="{accent}"/>
          <g stroke="#fff" stroke-width="7"><path d="M105 210h30"/><path d="M120 195v30"/></g>""",
        "forces_stuff": """
          <path d="M180 210 H620" stroke="#6c584c" stroke-width="18" stroke-linecap="round"/>
          <path d="M400 210 l-54 72 h108z" fill="#457b9d"/>
          <rect class="idea bob" x="230" y="138" width="86" height="66" rx="12" fill="{accent}"/>
          <circle cx="555" cy="170" r="38" fill="#ffd166"/>""",
        "light_sound": """
          <circle cx="150" cy="185" r="58" fill="#ffd166"/>
          <path class="idea beam" d="M215 155 L650 80 L650 260 L215 215 Z" fill="{accent}" opacity=".42"/>
          <path d="M260 185 q35-55 70 0t70 0t70 0t70 0" fill="none" stroke="#6a4c93" stroke-width="12"/>""",
        "matter": """
          <rect x="210" y="90" width="380" height="170" rx="25" fill="#fff" opacity=".68" stroke="#457b9d" stroke-width="7"/>
          <g class="idea particles" fill="{accent}">
            <circle cx="280" cy="150" r="18"/><circle cx="355" cy="205" r="18"/>
            <circle cx="445" cy="145" r="18"/><circle cx="520" cy="210" r="18"/>
          </g>""",
        "living_things": """
          <path d="M400 250 V145" stroke="#2d6a4f" stroke-width="18" stroke-linecap="round"/>
          <ellipse class="idea leaf" cx="350" cy="160" rx="62" ry="30" fill="#52b788" transform="rotate(25 350 160)"/>
          <ellipse cx="450" cy="135" rx="62" ry="30" fill="#80ed99" transform="rotate(-25 450 135)"/>
          <circle cx="400" cy="95" r="40" fill="{accent}"/>""",
        "make_test": """
          <path d="M150 245 H650 M210 245 L300 115 L390 245 L480 115 L590 245" fill="none" stroke="#457b9d" stroke-width="18" stroke-linejoin="round"/>
          <rect class="idea tester" x="330" y="72" width="140" height="54" rx="12" fill="{accent}"/>""",
        "follow_the_steps": """
          <g fill="none" stroke="#457b9d" stroke-width="14" stroke-linecap="round" stroke-linejoin="round">
            <path d="M145 205 H290"/><path d="M270 180 l25 25 -25 25"/>
            <path d="M330 205 H475"/><path d="M455 180 l25 25 -25 25"/>
            <path d="M515 205 H650"/><path d="M630 180 l25 25 -25 25"/>
          </g>
          <circle class="idea stepper" cx="145" cy="205" r="34" fill="{accent}"/>""",
    }[topic].format(accent=accent)
    css = f"""
    .stage{{background:linear-gradient(180deg,{sky} 0 72%,{ground} 72%)}}
    .stage svg{{display:block;width:100%;height:320px}}
    .pose-start .idea{{animation:none!important}}
    .pose-play .mover{{animation:travel 1.8s ease-in-out forwards}}
    .pose-play .bob{{animation:bobOnce 1.8s ease-in-out forwards}}
    .pose-play .beam{{animation:shine 1.8s ease-out forwards}}
    .pose-play .particles{{animation:swirl 1.8s ease-in-out forwards;transform-origin:400px 175px}}
    .pose-play .leaf{{animation:grow 1.8s ease-out forwards;transform-origin:400px 210px}}
    .pose-play .tester{{animation:test 1.8s ease-in-out forwards}}
    .pose-play .stepper{{animation:steps 1.8s ease-in-out forwards}}
    .pose-end .mover{{transform:translateX(540px)}} .pose-end .beam{{opacity:.82}}
    .pose-end .particles{{transform:rotate(90deg)}} .pose-end .leaf{{transform:scale(1.12) rotate(25deg)}}
    .pose-end .tester{{transform:translateY(92px)}} .pose-end .stepper{{transform:translateX(505px)}}
    @keyframes travel{{to{{transform:translateX(540px)}}}}
    @keyframes bobOnce{{40%{{transform:translateY(-32px)}}100%{{transform:translateY(0)}}}}
    @keyframes shine{{to{{opacity:.82}}}}
    @keyframes swirl{{to{{transform:rotate(90deg)}}}}
    @keyframes grow{{to{{transform:scale(1.12) rotate(25deg)}}}}
    @keyframes test{{50%,100%{{transform:translateY(92px)}}75%{{transform:translateY(75px)}}}}
    @keyframes steps{{to{{transform:translateX(505px)}}}}
    """
    body = f"""
    <svg viewBox="0 0 800 320" xmlns="http://www.w3.org/2000/svg">
      <text x="400" y="38" text-anchor="middle" font-family="system-ui" font-size="28"
            font-weight="850" fill="#17324d">{context}</text>
      <text x="70" y="92" text-anchor="middle" font-size="54">{icon}</text>
      {topic_art}
    </svg>"""
    return _page(
        css, body, f"{context}. A short science demonstration.", round_no,
        extra_stage=f"pose-{pose}",
    )


_SCENES = {
    "fast_slow": _scene_fast_slow,
    "stop_go": _scene_stop_go,
    "push_pull": _scene_push_pull,
    "heavy_light": _scene_heavy_light,
    "sink_float": _scene_sink_float,
    "sticky_slippy": _scene_sticky_slippy,
    "discovery": _scene_discovery,
}


def play_kid_audio(spec: dict, when: str, token: str) -> None:
    """Play a generated clip once per token. Used for Loud or Quiet and High or Low."""
    flag = f"_hear_{token}_{when}"
    if st.session_state.get(flag):
        return
    from kid_sounds import render_pair, render_sound
    if when == "pair" and spec.get("hear_left") and spec.get("hear_right"):
        st.session_state[flag] = True
        st.caption("Listen")
        st.audio(
            render_pair(str(spec["hear_left"]), str(spec["hear_right"])),
            format="audio/wav",
            autoplay=True,
        )
        return
    if when == "answer" and spec.get("answer_sound"):
        st.session_state[flag] = True
        st.caption("Listen to the matching sound")
        st.audio(render_sound(str(spec["answer_sound"])), format="audio/wav", autoplay=True)


def show_scene(spec: dict, round_no: int, pose: str | None = None, motion: str | None = None) -> None:
    builder = _SCENES.get(spec.get("scene"))
    if builder is None:
        from picture_scenes import EXTRA_SCENES
        builder = EXTRA_SCENES.get(spec.get("scene"))
    if builder:
        components.html(builder(round_no, spec, pose=pose, motion=motion), height=SCENE_HEIGHT)
        if pose == "play":
            play_kid_audio(spec, "pair", f"{spec.get('id')}_{round_no}_pair")
        return
    st.markdown(scene_svg(spec["picture"], round_no), unsafe_allow_html=True)


def _active_spec(spec: dict, round_no: int) -> dict:
    trials = spec.get("trials")
    if not trials:
        return spec
    return {**spec, **trials[round_no % len(trials)]}


def run_game(spec: dict) -> None:
    inject_form_css()
    spec = _with_discovery_trials(spec)
    key = "science_" + spec["id"]
    started = st.session_state.get(key + "_started", False)
    round_no = st.session_state.get(key + "_round", 0)
    pending = st.session_state.get(key + "_pending")
    spec = _active_spec(spec, round_no)
    animate_mode = spec.get("animate_mode", "loop")
    st.title(spec["picture"] + " " + spec["title"])
    st.caption(spec["tagline"])

    if not started:
        pose = None
        if animate_mode == "once":
            pose = "start"
        elif animate_mode == "on_answer":
            pose = "idle"
        show_scene(spec, round_no, pose=pose)
        if st.button("▶️ Play", use_container_width=True, key=key + "_play"):
            st.session_state[key + "_started"] = True
            st.rerun()
        with st.expander("Grown-up tip"):
            st.write(spec["tip"])
        return

    if pending:
        if animate_mode == "on_answer" and pending.get("phase") != "overlay":
            motion = str(spec["answer"]).lower()
            show_scene(spec, round_no, pose="play", motion=motion)
            time.sleep(float(spec.get("anim_seconds", ANIM_SECONDS)))
            st.session_state[key + "_pending"] = {**pending, "phase": "overlay"}
            st.rerun()
            return
        if animate_mode == "once":
            show_scene(spec, round_no, pose="end")
        elif animate_mode == "on_answer":
            show_scene(spec, round_no, pose="end", motion=str(spec["answer"]).lower())
        else:
            show_scene(spec, round_no)
        play_kid_audio(spec, "answer", f"{key}_{round_no}_ans")
        show_feedback_overlay(pending["message"], pending["correct"], pending["detail"])
        time.sleep(FEEDBACK_SECONDS)
        st.session_state[key + "_pending"] = None
        st.session_state[key + "_round"] = round_no + 1
        if spec.get("play_each_round"):
            st.session_state[key + "_started"] = False
        st.rerun()
        return

    pose = None
    if animate_mode == "once":
        pose = "play"
    elif animate_mode == "on_answer":
        pose = "idle"
    show_scene(spec, round_no, pose=pose)
    clear_feedback_overlay()
    st.subheader(spec["question"])
    choices = list(spec["choices"])
    # Rotate positions each round without randomness or trick scoring.
    shift = round_no % len(choices)
    choices = choices[shift:] + choices[:shift]
    cols = st.columns(len(choices))
    kid_detail = spec.get("kid_tip") or spec["tip"]
    for col, choice in zip(cols, choices):
        if col.button(choice, use_container_width=True, key=f"{key}_{round_no}_{choice}"):
            correct = choice == spec["answer"]
            st.session_state[key + "_pending"] = {
                "message": "Correct! 🌟" if correct else "Nice try! 💛",
                "correct": correct,
                "detail": kid_detail,
                "phase": "animate" if animate_mode == "on_answer" else "overlay",
            }
            st.rerun()
    with st.expander("Grown-up tip"):
        st.write(spec["tip"])
