"""Picture-first stages for Wave 1 and Wave 2 lessons."""
from __future__ import annotations

import html


def _page(inner_css: str, inner_html: str, aria: str, extra_stage: str = "", round_no: int | None = None) -> str:
    stage_cls = "stage " + extra_stage if extra_stage else "stage"
    round_html = "" if round_no is None or round_no < 0 else f'<div class="round">Round {round_no + 1}</div>'
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
{round_html}
</div>
</body></html>"""


def _pose(kwargs: dict) -> str:
    pose = str(kwargs.get("pose") or "play")
    if pose == "idle":
        return "start"
    return pose if pose in ("start", "play", "end") else "play"


def _scene_tower_fall(round_no: int, spec: dict | None = None, **kwargs) -> str:
    spec = spec or {}
    pose = _pose(kwargs)
    wide = str(spec.get("wide") or "Wide bottom")
    tiny = str(spec.get("tiny") or "Tiny bottom")
    wide_left = _truthy(spec.get("wide_left", True))
    left_name, left_cls = (wide, "wide") if wide_left else (tiny, "tiny")
    right_name, right_cls = (tiny, "tiny") if wide_left else (wide, "wide")
    css = """
    .stage{background:linear-gradient(180deg,#caf0f8 0 72%,#95d5b2 72%)}
    .col{position:absolute;top:18px;bottom:18px;width:42%}
    .col.left{left:6%}.col.right{right:6%}
    .label{text-align:center;font-weight:800;font-size:22px;color:#1d3557}
    .stack{position:absolute;left:50%;width:120px;margin-left:-60px;bottom:8px}
    .block{height:36px;margin:4px auto;border-radius:8px;background:#e76f51;box-shadow:0 4px 0 #9d0208}
    .wide .block{width:118px}
    .tiny .block{width:44px}
    .pose-play .tiny,.pose-end .tiny{transform-origin:50% 100%;animation:tip 1.4s ease-in forwards}
    .pose-end .tiny{transform:rotate(78deg) translate(36px,28px)}
    @keyframes tip{60%{transform:rotate(18deg)}100%{transform:rotate(78deg) translate(36px,28px)}}
    """
    body = f"""
    <div class="col left">
      <div class="label">{html.escape(left_name)}</div>
      <div class="stack {left_cls}">
        <div class="block"></div><div class="block"></div><div class="block"></div>
        <div class="block"></div>
      </div>
    </div>
    <div class="col right">
      <div class="label">{html.escape(right_name)}</div>
      <div class="stack {right_cls}">
        <div class="block"></div><div class="block"></div><div class="block"></div>
        <div class="block"></div>
      </div>
    </div>
    """
    return _page(css, body, "A wide tower stays. A tiny-bottom tower falls.", f"pose-{pose}", round_no=round_no)


def _scene_ramp_or_wall(round_no: int, spec: dict | None = None, **kwargs) -> str:
    pose = _pose(kwargs)
    css = """
    .stage{background:linear-gradient(180deg,#caf0f8 0 58%,#6c757d 58% 64%,#2d6a4f 64%)}
    .half{position:absolute;top:0;bottom:0;width:50%}
    .half.left{left:0}.half.right{right:0}
    .ramp{position:absolute;left:8%;bottom:18%;width:0;height:0;
          border-bottom:110px solid #bc6c25;border-right:210px solid transparent}
    .wall{position:absolute;right:18%;bottom:18%;width:28px;height:150px;background:#6c757d;border-radius:6px}
    .car{position:absolute;width:90px;height:36px;bottom:22%}
    .car b{display:block;height:26px;background:#e63946;border-radius:10px 14px 6px 6px}
    .car i{position:absolute;bottom:-8px;width:16px;height:16px;background:#1d3557;border-radius:50%;border:3px solid #fff}
    .car i.a{left:10px}.car i.b{right:10px}
    .go{left:10%}
    .stuck{right:22%}
    .pose-play .go,.pose-end .go{animation:roll 1.8s ease-in forwards}
    .pose-end .go{left:38%}
    .pose-play .stuck{animation:bump 1.1s ease-in forwards}
    .pose-end .stuck{right:22%}
    @keyframes roll{from{left:10%}to{left:38%}}
    @keyframes bump{0%{right:38%}70%{right:22%}100%{right:22%}}
    """
    body = f"""
    <div class="tag" style="top:10px;left:8%;font-size:24px;color:#9c6644">{html.escape(str((spec or {}).get("path") or "Ramp"))}</div>
    <div class="tag" style="top:10px;right:10%;font-size:24px;color:#343a40">{html.escape(str((spec or {}).get("block") or "Wall"))}</div>
    <div class="half left"><div class="ramp"></div>
      <div class="car go"><b></b><i class="a"></i><i class="b"></i></div>
    </div>
    <div class="half right"><div class="wall"></div>
      <div class="car stuck"><b style="background:#457b9d"></b><i class="a"></i><i class="b"></i></div>
    </div>
    """
    return _page(css, body, "A car rolls down a ramp. A wall stops a car.", f"pose-{pose}")


def _scene_fit_the_hole(round_no: int, spec: dict | None = None, **kwargs) -> str:
    pose = _pose(kwargs)
    css = """
    .stage{background:linear-gradient(180deg,#fff1c7,#ffe8d6)}
    .board{position:absolute;left:50%;top:118px;width:240px;height:110px;margin-left:-120px;
           background:#6c584c;border-radius:18px}
    .hole{position:absolute;left:50%;top:142px;width:78px;height:78px;margin-left:-39px;
          background:#1d3557;border-radius:50%;box-shadow:inset 0 0 0 6px #3d405b}
    .shape{position:absolute;top:28px;width:72px;height:72px}
    .circle{left:18%;background:#2a9d8f;border-radius:50%}
    .square{right:16%;background:#e76f51;border-radius:10px}
    .pose-play .circle,.pose-end .circle{animation:dropIn 1.3s ease-in forwards}
    .pose-end .circle{top:148px;left:calc(50% - 36px)}
    .pose-play .square,.pose-end .square{animation:bounceOff 1.3s ease-in forwards}
    .pose-end .square{top:28px;right:10%}
    @keyframes dropIn{to{top:148px;left:calc(50% - 36px)}}
    @keyframes bounceOff{40%{top:118px;right:22%}100%{top:28px;right:10%}}
    """
    body = f"""
    <div class="tag" style="top:8px;left:12%;font-size:22px;color:#1d6a62">{html.escape(str((spec or {}).get("fits") or "Circle"))}</div>
    <div class="tag" style="top:8px;right:10%;font-size:22px;color:#9d0208">{html.escape(str((spec or {}).get("misses") or "Square"))}</div>
    <div class="board"></div><div class="hole"></div>
    <div class="shape circle"></div><div class="shape square"></div>
    """
    return _page(css, body, "A circle fits a round hole. A square does not.", f"pose-{pose}")


def _scene_who_went_farther(round_no: int, spec: dict | None = None, **kwargs) -> str:
    spec = spec or {}
    pose = _pose(kwargs)
    near_name = str(spec.get("near_name") or spec.get("b") or "Blue car")
    far_name = str(spec.get("far_name") or spec.get("a") or "Red car")
    css = """
    .stage{background:linear-gradient(180deg,#caf0f8 0 46%,#6c757d 46% 54%,#2d6a4f 54%)}
    .lane{position:absolute;left:4%;right:4%;height:8px;background:repeating-linear-gradient(90deg,#fff 0 18px,transparent 18px 34px)}
    .car{position:absolute;width:100px;height:38px}
    .car b{display:block;height:28px;border-radius:12px 16px 8px 8px}
    .car i{position:absolute;bottom:-8px;width:16px;height:16px;background:#1d3557;border-radius:50%;border:3px solid #fff}
    .car i.a{left:12px}.car i.b{right:12px}
    .blue{top:58px;left:8%}
    .red{top:168px;left:8%}
    .flag{position:absolute;top:8px;left:8%;font-size:22px;font-weight:800;color:#1d3557}
    .pose-play .blue,.pose-end .blue{animation:shortDrive 1.6s ease-out forwards}
    .pose-end .blue{left:38%}
    .pose-play .red,.pose-end .red{animation:longDrive 1.6s ease-out forwards}
    .pose-end .red{left:72%}
    @keyframes shortDrive{to{left:38%}}
    @keyframes longDrive{to{left:72%}}
    """
    body = f"""
    <div class="flag">START</div>
    <div class="tag" style="top:58px;right:8%;font-size:20px;color:#1d3557">{html.escape(near_name)}</div>
    <div class="tag" style="top:168px;right:8%;font-size:20px;color:#c1121f">{html.escape(far_name)}</div>
    <div class="lane" style="top:108px"></div>
    <div class="lane" style="top:218px"></div>
    <div class="car blue"><b style="background:#457b9d"></b><i class="a"></i><i class="b"></i></div>
    <div class="car red"><b style="background:#e63946"></b><i class="a"></i><i class="b"></i></div>
    """
    return _page(css, body, f"{far_name} stops farther from start than {near_name}.", f"pose-{pose}", round_no=round_no)


def _scene_speeding_up(round_no: int, spec: dict | None = None, **kwargs) -> str:
    spec = spec or {}
    pose = _pose(kwargs)
    name = str(spec.get("vehicle") or spec.get("left_name") or "Car")
    gaps = str(spec.get("gaps") or "grow")
    spots = ("10%", "24%", "44%", "70%") if gaps == "grow" else ("10%", "28%", "42%", "52%")
    css = """
    .stage{background:linear-gradient(180deg,#dff5ff 0 70%,#95d5b2 70%)}
    .path{position:absolute;left:6%;right:6%;top:168px;height:10px;background:#6c757d;border-radius:6px}
    .stamp{position:absolute;top:118px;width:54px;height:28px;background:#e63946;border-radius:10px 12px 6px 6px;
           opacity:.45}
    .stamp:after{content:"";position:absolute;bottom:-8px;left:8px;width:12px;height:12px;background:#1d3557;border-radius:50%}
    .now{position:absolute;top:104px;width:78px;height:36px;background:#c1121f;border-radius:12px 16px 8px 8px}
    .pose-play .now,.pose-end .now{animation:zoom 1.7s ease-in forwards}
    .pose-end .now{left:78%}
    @keyframes zoom{from{left:8%}to{left:78%}}
    """
    body = f"""
    <div class="tag" style="top:16px;left:12px;font-size:24px;color:#1d3557">{html.escape(name)}</div>
    <div class="path"></div>
    <div class="stamp" style="left:{spots[0]}"></div>
    <div class="stamp" style="left:{spots[1]};opacity:.55"></div>
    <div class="stamp" style="left:{spots[2]};opacity:.7"></div>
    <div class="stamp" style="left:{spots[3]};opacity:.9"></div>
    <div class="now" style="left:8%"></div>
    """
    aria = f"{name} leaves marks along the path."
    return _page(css, body, aria, f"pose-{pose}", round_no=round_no)


def _scene_roll_downhill(round_no: int, spec: dict | None = None, **kwargs) -> str:
    spec = spec or {}
    pose = _pose(kwargs)
    name = str(spec.get("ball") or spec.get("left_name") or "Ball")
    pic = str(spec.get("ball_pic") or spec.get("left_pic") or "⚽")
    css = """
    .stage{background:linear-gradient(180deg,#caf0f8,#90e0ef)}
    .hill{position:absolute;left:0;right:0;bottom:0;height:210px;background:#52b69a;
          clip-path:polygon(0 18%,100% 88%,100% 100%,0 100%)}
    .ball{position:absolute;top:58px;left:10%;font-size:54px;line-height:1}
    .pose-play .ball,.pose-end .ball{animation:rollHill 1.8s ease-in forwards}
    .pose-end .ball{top:210px;left:78%}
    @keyframes rollHill{to{top:210px;left:78%}}
    """
    body = f"""
    <div class="tag" style="top:12px;left:10%;font-size:24px;color:#1d3557">{html.escape(name)}</div>
    <div class="hill"></div>
    <div class="ball">{html.escape(pic)}</div>
    """
    return _page(css, body, f"{name} rolls down the hill.", f"pose-{pose}", round_no=round_no)


def _truthy(value: object, default: bool = True) -> bool:
    if value is None:
        return default
    if isinstance(value, str):
        return value.lower() not in ("0", "false", "no")
    return bool(value)


def _light_panel(kind: str) -> str:
    if kind == "closet":
        return '<div class="door"></div><div class="knob"></div>'
    if kind == "cave":
        return '<div class="cave"></div>'
    if kind == "lamp":
        return '<div class="lamp"></div><div class="glow"></div>'
    if kind == "window":
        return '<div class="window"></div>'
    if kind == "tunnel":
        return '<div class="tunnel"></div>'
    if kind == "lighthouse":
        return '<div class="tower"></div><div class="beam"></div>'
    if kind == "basement":
        return '<div class="stairs"></div>'
    if kind == "fire":
        return '<div class="fire"></div>'
    if kind == "woods":
        return '<div class="tree a"></div><div class="tree b"></div>'
    if kind == "flashlight":
        return '<div class="torch"></div><div class="cone"></div>'
    if kind == "bed":
        return '<div class="bed"></div>'
    if kind == "beach":
        return '<div class="sun-ball"></div><div class="wave-line"></div>'
    if kind == "theater":
        return '<div class="screen"></div>'
    if kind == "candles":
        return '<div class="cake"></div>'
    if kind == "box":
        return '<div class="lid-box"></div>'
    if kind == "street":
        return '<div class="pole"></div><div class="sun-ball small"></div>'
    if kind == "attic":
        return '<div class="rafter"></div>'
    if kind == "park":
        return '<div class="sun-ball"></div><div class="tree a"></div>'
    if kind == "midnight":
        return '<div class="moon"></div>'
    return '<div class="sun-ball"></div>'


def _scene_light_or_dark(round_no: int, spec: dict | None = None, **kwargs) -> str:
    spec = spec or {}
    pose = _pose(kwargs)
    light = str(spec.get("light") or "Sunny yard")
    dark = str(spec.get("dark") or "Closed closet")
    light_kind = str(spec.get("light_kind") or "yard")
    dark_kind = str(spec.get("dark_kind") or "closet")
    light_left = _truthy(spec.get("light_left", True))
    left_name, left_kind, left_cls = light, light_kind, "sun"
    right_name, right_kind, right_cls = dark, dark_kind, "dark"
    if not light_left:
        left_name, left_kind, left_cls, right_name, right_kind, right_cls = (
            right_name, right_kind, right_cls, left_name, left_kind, left_cls
        )
    css = """
    .stage{background:#fff}
    .half{position:absolute;top:0;bottom:0;width:50%}
    .sun{background:linear-gradient(180deg,#fff3bf,#90e0ef 55%,#95d5b2 55%)}
    .dark{background:linear-gradient(180deg,#212529,#343a40 70%,#1d3557 70%)}
    .name{position:absolute;top:12px;left:8%;right:8%;text-align:center;font-size:22px;font-weight:800;z-index:3}
    .sun .name{color:#9c6644}.dark .name{color:#fff;text-shadow:none}
    .sun-ball{position:absolute;left:18%;top:58px;width:64px;height:64px;border-radius:50%;background:#ffd166;box-shadow:0 0 24px #ffd166}
    .sun-ball.small{width:28px;height:28px;left:62%;top:46px}
    .door{position:absolute;left:28%;top:90px;width:90px;height:160px;background:#6c584c;border-radius:8px 8px 0 0}
    .knob{position:absolute;left:72%;top:168px;width:12px;height:12px;border-radius:50%;background:#ffd166}
    .cave{position:absolute;left:18%;bottom:20px;width:64%;height:160px;background:#111;border-radius:80px 80px 0 0}
    .lamp{position:absolute;left:42%;top:70px;width:16px;height:70px;background:#6c584c}
    .glow{position:absolute;left:28%;top:48px;width:70px;height:40px;background:#ffd166;border-radius:50%;box-shadow:0 0 28px #ffd166}
    .window{position:absolute;left:22%;top:70px;width:56%;height:110px;background:#90e0ef;border:8px solid #8d6e63;box-shadow:inset 0 0 0 6px #fff}
    .tunnel{position:absolute;left:20%;top:80px;width:60%;height:150px;background:#111;border-radius:50%}
    .tower{position:absolute;left:38%;bottom:20px;width:36px;height:150px;background:#dee2e6}
    .beam{position:absolute;left:52%;top:70px;border-top:24px solid transparent;border-bottom:24px solid transparent;border-left:90px solid rgba(255,209,102,.7)}
    .stairs{position:absolute;left:22%;bottom:20px;width:56%;height:14px;background:#495057;box-shadow:0 -22px 0 #343a40,0 -44px 0 #495057,0 -66px 0 #343a40}
    .fire{position:absolute;left:38%;bottom:36px;width:40px;height:54px;background:radial-gradient(circle at 50% 70%,#ffd166,#e63946);border-radius:50% 50% 40% 40%;box-shadow:0 0 20px #e63946}
    .tree{position:absolute;bottom:20px;width:0;height:0;border-left:28px solid transparent;border-right:28px solid transparent;border-bottom:90px solid #1b4332}
    .tree.a{left:16%}.tree.b{left:48%}
    .torch{position:absolute;left:18%;bottom:70px;width:54px;height:16px;background:#6c757d;border-radius:8px}
    .cone{position:absolute;left:68px;bottom:40px;border-top:40px solid transparent;border-bottom:40px solid transparent;border-left:110px solid rgba(255,241,199,.75)}
    .bed{position:absolute;left:14%;bottom:24px;width:72%;height:50px;background:#3d405b;border-radius:8px}
    .wave-line{position:absolute;left:0;right:0;bottom:36px;height:16px;background:#48cae4}
    .screen{position:absolute;left:16%;top:70px;width:68%;height:90px;background:#111;border:6px solid #6c757d}
    .cake{position:absolute;left:30%;bottom:40px;width:70px;height:40px;background:#ffafcc;border-radius:8px;box-shadow:18px -22px 0 -22px #ffd166,36px -22px 0 -22px #ffd166,52px -22px 0 -22px #ffd166}
    .lid-box{position:absolute;left:24%;top:110px;width:52%;height:80px;background:#bc6c25;border-radius:8px}
    .pole{position:absolute;left:46%;bottom:20px;width:10px;height:140px;background:#6c757d}
    .rafter{position:absolute;left:8%;top:70px;width:84%;height:10px;background:#6c584c;transform:rotate(-8deg)}
    .moon{position:absolute;left:22%;top:50px;width:50px;height:50px;border-radius:50%;background:#f8f9fa;box-shadow:-12px 0 0 #212529}
    """
    body = f"""
    <div class="half {left_cls}" style="left:0">
      <div class="name">{html.escape(left_name)}</div>
      {_light_panel(left_kind)}
    </div>
    <div class="half {right_cls}" style="left:50%">
      <div class="name">{html.escape(right_name)}</div>
      {_light_panel(right_kind)}
    </div>
    """
    aria = f"{light} is light. {dark} is dark."
    return _page(css, body, aria, f"pose-{pose}", round_no=round_no)


def _sound_icon(kind: str, fallback: str) -> str:
    icons = {
        "whisper": "🤫", "drum": "🥁", "rain": "🌧️", "thunder": "⚡",
        "pages": "📖", "cymbal": "💥", "purr": "🐱", "bark": "🐶",
        "tick": "🕐", "alarm": "⏰", "rustle": "🍃", "crash": "💥",
        "drip": "💧", "gong": "🔔", "hum": "😮", "trumpet": "🎺",
        "lullaby": "🎵", "siren": "🚒", "squeak": "🐭", "roar": "🦁",
    }
    return icons.get(kind, fallback)


def _scene_loud_or_quiet(round_no: int, spec: dict | None = None, **kwargs) -> str:
    spec = spec or {}
    pose = _pose(kwargs)
    loud = str(spec.get("loud") or "Drum")
    quiet = str(spec.get("quiet") or "Whisper")
    loud_kind = str(spec.get("loud_kind") or "drum")
    quiet_kind = str(spec.get("quiet_kind") or "whisper")
    loud_left = _truthy(spec.get("loud_left"), False)
    left_name, left_kind, left_cls = quiet, quiet_kind, "tiny"
    right_name, right_kind, right_cls = loud, loud_kind, "big"
    if loud_left:
        left_name, left_kind, left_cls, right_name, right_kind, right_cls = (
            right_name, right_kind, right_cls, left_name, left_kind, left_cls
        )
    css = """
    .stage{background:linear-gradient(180deg,#f3e8ff,#fff)}
    .col{position:absolute;top:20px;bottom:20px;width:46%}
    .col.left{left:4%}.col.right{right:4%}
    .name{text-align:center;font-size:22px;font-weight:800;color:#1d3557}
    .pic{font-size:72px;line-height:1;text-align:center;margin-top:28px}
    .ring{position:absolute;left:50%;bottom:70px;border:5px solid #6a4c93;border-radius:50%;opacity:.35}
    .pose-play .big,.pose-end .big{animation:pulseBig 1.2s ease-out infinite}
    .pose-play .tiny,.pose-end .tiny{animation:pulseTiny 1.8s ease-out infinite}
    @keyframes pulseBig{from{width:40px;height:40px;margin:-20px 0 0 -20px;opacity:.65}to{width:190px;height:190px;margin:-95px 0 0 -95px;opacity:0}}
    @keyframes pulseTiny{from{width:14px;height:14px;margin:-7px 0 0 -7px;opacity:.45}to{width:46px;height:46px;margin:-23px 0 0 -23px;opacity:0}}
    """
    body = f"""
    <div class="col left">
      <div class="name">{html.escape(left_name)}</div>
      <div class="pic">{_sound_icon(left_kind, "🔈")}</div>
      <div class="ring {left_cls}"></div>
    </div>
    <div class="col right">
      <div class="name">{html.escape(right_name)}</div>
      <div class="pic">{_sound_icon(right_kind, "🔊")}</div>
      <div class="ring {right_cls}"></div>
    </div>
    """
    aria = f"{quiet} is quiet. {loud} is loud."
    return _page(css, body, aria, f"pose-{pose}", round_no=round_no)


def _scene_high_or_low(round_no: int, spec: dict | None = None, **kwargs) -> str:
    spec = spec or {}
    pose = _pose(kwargs)
    high = str(spec.get("high") or "Tiny bell")
    low = str(spec.get("low") or "Big drum")
    high_pic = str(spec.get("high_pic") or "🔔")
    low_pic = str(spec.get("low_pic") or "🥁")
    high_left = _truthy(spec.get("high_left", True))
    left_name, left_pic, left_cls = high, high_pic, "fast"
    right_name, right_pic, right_cls = low, low_pic, "slow"
    if not high_left:
        left_name, left_pic, left_cls, right_name, right_pic, right_cls = (
            right_name, right_pic, right_cls, left_name, left_pic, left_cls
        )
    css = """
    .stage{background:linear-gradient(180deg,#e8f5e9,#fff1c7)}
    .col{position:absolute;top:0;bottom:0;width:50%}
    .col.left{left:0}.col.right{right:0}
    .name{position:absolute;top:14px;left:8%;right:8%;text-align:center;font-size:22px;font-weight:800;color:#1d3557}
    .pic{position:absolute;top:58px;left:0;right:0;text-align:center;font-size:64px;line-height:1}
    .wave{position:absolute;left:8%;right:8%;top:170px;height:80px}
    .pose-play .fast path,.pose-end .fast path{animation:wiggle 0.32s linear infinite}
    .pose-play .slow path,.pose-end .slow path{animation:wiggle 1.5s linear infinite}
    @keyframes wiggle{from{transform:translateX(0)}to{transform:translateX(-24px)}}
    """
    body = f"""
    <div class="col left">
      <div class="name">{html.escape(left_name)}</div>
      <div class="pic">{html.escape(left_pic)}</div>
      <svg class="wave {left_cls}" viewBox="0 0 200 80">
        <path d="{'M0 40 q12 -28 24 0 t24 0 t24 0 t24 0 t24 0 t24 0 t24 0 t24 0' if left_cls=='fast' else 'M0 40 q40 -18 80 0 t80 0 t80 0'}" fill="none" stroke="#2a9d8f" stroke-width="8"/>
      </svg>
    </div>
    <div class="col right">
      <div class="name">{html.escape(right_name)}</div>
      <div class="pic">{html.escape(right_pic)}</div>
      <svg class="wave {right_cls}" viewBox="0 0 200 80">
        <path d="{'M0 40 q12 -28 24 0 t24 0 t24 0 t24 0 t24 0 t24 0 t24 0 t24 0' if right_cls=='fast' else 'M0 40 q40 -18 80 0 t80 0 t80 0'}" fill="none" stroke="#1d3557" stroke-width="10"/>
      </svg>
    </div>
    """
    aria = f"{high} is high. {low} is low."
    return _page(css, body, aria, f"pose-{pose}", round_no=round_no)


def _scene_compare(round_no: int, spec: dict | None = None, **kwargs) -> str:
    """Two named pictures. Motion (bob, steam, splash, still) matches the idea."""
    spec = spec or {}
    pose = _pose(kwargs)
    left_name = str(spec.get("left_name") or "Left")
    right_name = str(spec.get("right_name") or "Right")
    left_pic = str(spec.get("left_pic") or "🔵")
    right_pic = str(spec.get("right_pic") or "🔴")
    left_move = str(spec.get("left_move") or "still")
    right_move = str(spec.get("right_move") or "still")
    css = """
    .stage{background:linear-gradient(180deg,#e9f8ff,#fff7dd)}
    .col{position:absolute;top:18px;bottom:18px;width:46%}
    .col.left{left:4%}.col.right{right:4%}
    .name{text-align:center;font-size:22px;font-weight:800;color:#1d3557}
    .pic{font-size:88px;line-height:1;text-align:center;margin-top:36px}
    .pose-play .bob,.pose-end .bob{animation:bob 0.8s ease-in-out infinite}
    .pose-play .steam,.pose-end .steam{animation:steam 1.4s ease-in-out infinite}
    .pose-play .splash,.pose-end .splash{animation:splash 1.1s ease-in infinite}
    .pose-play .grow,.pose-end .grow{animation:grow 1.5s ease-out forwards}
    .pose-play .hop,.pose-end .hop{animation:hop 0.7s ease-in-out infinite}
    .pose-play .wiggle,.pose-end .wiggle{animation:wiggle 0.35s linear infinite}
    .pose-play .shiver,.pose-end .shiver{animation:shiver 0.2s linear infinite}
    .pose-play .slide,.pose-end .slide{animation:slide 1.4s ease-in forwards}
    @keyframes bob{50%{transform:translateY(-12px)}}
    @keyframes steam{0%{transform:translateY(8px);opacity:.55}100%{transform:translateY(-14px);opacity:.15}}
    @keyframes splash{0%{transform:translateY(-8px) scale(1)}100%{transform:translateY(18px) scale(.92)}}
    @keyframes grow{from{transform:scale(.75)}to{transform:scale(1)}}
    @keyframes hop{50%{transform:translateY(-16px)}}
    @keyframes wiggle{from{transform:rotate(-6deg)}to{transform:rotate(6deg)}}
    @keyframes shiver{from{transform:translateX(-3px)}to{transform:translateX(3px)}}
    @keyframes slide{from{transform:translateX(0)}to{transform:translateX(40px)}}
    """
    body = f"""
    <div class="col left">
      <div class="name">{html.escape(left_name)}</div>
      <div class="pic {html.escape(left_move)}">{html.escape(left_pic)}</div>
    </div>
    <div class="col right">
      <div class="name">{html.escape(right_name)}</div>
      <div class="pic {html.escape(right_move)}">{html.escape(right_pic)}</div>
    </div>
    """
    aria = f"{left_name} and {right_name}."
    return _page(css, body, aria, f"pose-{pose}", round_no=round_no)


def _step_art(kind: str) -> str:
    if kind == "car-seat":
        return (
            '<div class="car-seat" aria-hidden="true">'
            '<div class="seat-back"></div><div class="seat-base"></div>'
            '<div class="kid-body"></div><div class="kid-head"></div>'
            "</div>"
        )
    if kind == "seatbelt":
        return (
            '<div class="car-seat belted" aria-hidden="true">'
            '<div class="seat-back"></div><div class="seat-base"></div>'
            '<div class="kid-body"></div><div class="kid-head"></div>'
            '<div class="belt-shoulder"></div><div class="belt-lap"></div>'
            '<div class="belt-buckle"></div>'
            "</div>"
        )
    return ""


def _scene_steps(round_no: int, spec: dict | None = None, **kwargs) -> str:
    spec = spec or {}
    pose = _pose(kwargs)
    steps = spec.get("steps") or (
        {"n": "1", "label": "First", "pic": "1️⃣"},
        {"n": "2", "label": "Next", "pic": "2️⃣"},
        {"n": "?", "label": "Then", "pic": "❓"},
    )
    title = str(spec.get("steps_title") or "")
    cards = ""
    count = max(1, min(3, len(list(steps))))
    for i, step in enumerate(list(steps)[:3]):
        miss = " miss" if step.get("missing") else ""
        left = (8 + i * 31) if count == 3 else (18 + i * 38)
        hide_missing = bool(step.get("missing")) and pose not in ("play", "end")
        if hide_missing:
            cards += (
                f'<div class="card miss hidden" style="left:{left}%">'
                f"<b>?</b>"
                f'<span class="pic">❓</span>'
                f'<span class="blank">?</span></div>'
            )
            continue
        art = _step_art(str(step.get("art") or ""))
        picture = art or f'<span class="pic">{html.escape(str(step.get("pic") or ""))}</span>'
        cards += (
            f'<div class="card{miss}" style="left:{left}%">'
            f'<b>{html.escape(str(step.get("n") or i + 1))}</b>'
            f"{picture}"
            f'<span>{html.escape(str(step.get("label") or ""))}</span></div>'
        )
    css = """
    .stage{background:linear-gradient(180deg,#ffe8d6,#e9f8ff)}
    .title{position:absolute;top:12px;left:12px;right:12px;text-align:center;font-size:22px;font-weight:800;color:#1d3557}
    .card{position:absolute;top:78px;width:28%;height:180px;border-radius:18px;background:#fff;border:4px solid #457b9d;text-align:center;font-weight:800;color:#1d3557}
    .card b{display:block;font-size:28px;margin-top:10px}
    .card .pic{display:block;font-size:42px;margin-top:8px}
    .card span{display:block;margin-top:8px;font-size:18px}
    .car-seat{position:relative;width:58px;height:70px;margin:6px auto 0}
    .seat-back{position:absolute;left:12px;top:0;width:34px;height:44px;background:#457b9d;border-radius:12px 12px 4px 4px}
    .seat-base{position:absolute;left:4px;bottom:2px;width:50px;height:18px;background:#1d3557;border-radius:8px}
    .kid-head{position:absolute;left:20px;top:8px;width:18px;height:18px;background:#f4a261;border-radius:50%}
    .kid-body{position:absolute;left:18px;top:24px;width:22px;height:24px;background:#2a9d8f;border-radius:8px}
    .belt-shoulder{position:absolute;left:16px;top:6px;width:8px;height:46px;background:#e63946;
      transform:rotate(-32deg);border-radius:4px;z-index:2}
    .belt-lap{position:absolute;left:8px;bottom:16px;width:42px;height:8px;background:#e63946;border-radius:4px;z-index:2}
    .belt-buckle{position:absolute;left:22px;bottom:12px;width:16px;height:12px;background:#ffd166;
      border:2px solid #bc6c25;border-radius:3px;box-sizing:border-box;z-index:3}
    .miss{border-style:dashed;border-color:#e63946;background:#fff5f5}
    .pose-play .card,.pose-end .card{animation:pop 0.7s ease-out forwards}
    .pose-play .miss,.pose-end .miss{animation:blink 1s ease-in-out infinite}
    @keyframes pop{from{transform:scale(.9)}to{transform:scale(1)}}
    @keyframes blink{50%{background:#ffe5ec}}
    """
    body = f'<div class="title">{html.escape(title)}</div>{cards}'
    return _page(css, body, title or "Follow the steps.", f"pose-{pose}", round_no=round_no)


def _scene_solid_or_splash(round_no: int, spec: dict | None = None, **kwargs) -> str:
    spec = spec or {}
    return _scene_compare(round_no, {
        "left_name": spec.get("left_name") or spec.get("solid") or "Wood block",
        "right_name": spec.get("right_name") or spec.get("liquid") or "Water",
        "left_pic": spec.get("left_pic") or spec.get("solid_pic") or "🧱",
        "right_pic": spec.get("right_pic") or spec.get("liquid_pic") or "💦",
        "left_move": spec.get("left_move") or "still",
        "right_move": spec.get("right_move") or "splash",
    }, **kwargs)


def _scene_hot_or_cold(round_no: int, spec: dict | None = None, **kwargs) -> str:
    spec = spec or {}
    return _scene_compare(round_no, {
        "left_name": spec.get("left_name") or spec.get("cold") or "Ice cube",
        "right_name": spec.get("right_name") or spec.get("hot") or "Warm soup",
        "left_pic": spec.get("left_pic") or spec.get("cold_pic") or "🧊",
        "right_pic": spec.get("right_pic") or spec.get("hot_pic") or "🍲",
        "left_move": spec.get("left_move") or "shiver",
        "right_move": spec.get("right_move") or "steam",
    }, **kwargs)


def _scene_melt_or_freeze(round_no: int, spec: dict | None = None, **kwargs) -> str:
    spec = spec or {}
    pose = _pose(kwargs)
    action = str(spec.get("action") or "melt")
    stuff = str(spec.get("stuff") or "Ice")
    pic = str(spec.get("stuff_pic") or "🧊")
    css = """
    .stage{background:linear-gradient(180deg,#fff1c7,#caf0f8)}
    .sky{position:absolute;right:24px;top:16px;font-size:54px}
    .name{position:absolute;top:18px;left:12px;font-size:24px;font-weight:800;color:#1d3557}
    .bit{position:absolute;left:50%;top:78px;font-size:92px;margin-left:-50px}
    .pose-play .melt,.pose-end .melt{animation:melt 1.7s ease-in forwards}
    .pose-play .freeze,.pose-end .freeze{animation:freeze 1.7s ease-out forwards}
    @keyframes melt{to{transform:translateY(70px) scaleX(1.45) scaleY(.35)}}
    @keyframes freeze{from{transform:translateY(70px) scaleX(1.45) scaleY(.35)}to{transform:none}}
    """
    sky = "☀️" if action == "melt" else "❄️"
    body = f"""
    <div class="name">{html.escape(stuff)}</div>
    <div class="sky">{sky}</div>
    <div class="bit {html.escape(action)}">{html.escape(pic)}</div>
    """
    aria = f"{stuff} will {action}."
    return _page(css, body, aria, f"pose-{pose}", round_no=round_no)


def _scene_living_or_not(round_no: int, spec: dict | None = None, **kwargs) -> str:
    spec = spec or {}
    return _scene_compare(round_no, {
        "left_name": spec.get("left_name") or spec.get("living") or "Puppy",
        "right_name": spec.get("right_name") or spec.get("not_living") or "Toy car",
        "left_pic": spec.get("left_pic") or spec.get("living_pic") or "🐶",
        "right_pic": spec.get("right_pic") or spec.get("not_pic") or "🚗",
        "left_move": spec.get("left_move") or "bob",
        "right_move": spec.get("right_move") or "still",
    }, **kwargs)


def _scene_plant_or_animal(round_no: int, spec: dict | None = None, **kwargs) -> str:
    spec = spec or {}
    return _scene_compare(round_no, {
        "left_name": spec.get("left_name") or spec.get("plant") or "Sunflower",
        "right_name": spec.get("right_name") or spec.get("animal") or "Rabbit",
        "left_pic": spec.get("left_pic") or spec.get("plant_pic") or "🌻",
        "right_pic": spec.get("right_pic") or spec.get("animal_pic") or "🐇",
        "left_move": spec.get("left_move") or "grow",
        "right_move": spec.get("right_move") or "hop",
    }, **kwargs)


def _scene_hungry_or_full(round_no: int, spec: dict | None = None, **kwargs) -> str:
    spec = spec or {}
    return _scene_compare(round_no, {
        "left_name": spec.get("left_name") or spec.get("need") or "Food",
        "right_name": spec.get("right_name") or spec.get("not_need") or "A toy",
        "left_pic": spec.get("left_pic") or spec.get("need_pic") or "🪱",
        "right_pic": spec.get("right_pic") or spec.get("not_pic") or "🧸",
        "left_move": spec.get("left_move") or "bob",
        "right_move": spec.get("right_move") or "still",
    }, **kwargs)


def _scene_first_then_next(round_no: int, spec: dict | None = None, **kwargs) -> str:
    spec = spec or {}
    if spec.get("steps"):
        return _scene_steps(round_no, spec, **kwargs)
    return _scene_steps(round_no, {
        "steps_title": spec.get("steps_title") or "First, then next",
        "steps": (
            {"n": "1", "label": spec.get("first") or "Socks", "pic": spec.get("first_pic") or "🧦",
             "art": spec.get("first_art")},
            {"n": "2", "label": spec.get("next") or "Shoes", "pic": spec.get("next_pic") or "👟",
             "art": spec.get("next_art")},
            {"n": "3", "label": spec.get("later") or "Hat", "pic": spec.get("later_pic") or "🎩",
             "art": spec.get("later_art")},
        ),
    }, **kwargs)


def _scene_missing_step(round_no: int, spec: dict | None = None, **kwargs) -> str:
    spec = spec or {}
    if spec.get("steps"):
        return _scene_steps(round_no, spec, **kwargs)
    return _scene_steps(round_no, {
        "steps_title": spec.get("steps_title") or "Which step is missing?",
        "steps": (
            {"n": "1", "label": spec.get("one") or "Wash", "pic": spec.get("one_pic") or "🧼"},
            {"n": "2", "label": spec.get("two") or "Dry", "pic": spec.get("two_pic") or "💨"},
            {"n": "?", "label": spec.get("missing") or "Put away", "pic": spec.get("missing_pic") or "🧺", "missing": True},
        ),
    }, **kwargs)


def _scene_do_it_again(round_no: int, spec: dict | None = None, **kwargs) -> str:
    spec = spec or {}
    action = str(spec.get("action") or "Clap")
    pic = str(spec.get("action_pic") or "👏")
    return _scene_steps(round_no, {
        "steps_title": spec.get("steps_title") or "Repeat means do it again",
        "steps": (
            {"n": "1", "label": action, "pic": pic},
            {"n": "2", "label": action, "pic": pic},
            {"n": "3", "label": action, "pic": pic},
        ),
    }, **kwargs)


EXTRA_SCENES = {
    "tower_fall": _scene_tower_fall,
    "ramp_or_wall": _scene_ramp_or_wall,
    "fit_the_hole": _scene_fit_the_hole,
    "who_went_farther": _scene_who_went_farther,
    "speeding_up": _scene_speeding_up,
    "roll_downhill": _scene_roll_downhill,
    "light_or_dark": _scene_light_or_dark,
    "loud_or_quiet": _scene_loud_or_quiet,
    "high_or_low": _scene_high_or_low,
    "solid_or_splash": _scene_solid_or_splash,
    "hot_or_cold": _scene_hot_or_cold,
    "melt_or_freeze": _scene_melt_or_freeze,
    "living_or_not": _scene_living_or_not,
    "plant_or_animal": _scene_plant_or_animal,
    "hungry_or_full": _scene_hungry_or_full,
    "first_then_next": _scene_first_then_next,
    "missing_step": _scene_missing_step,
    "do_it_again": _scene_do_it_again,
    "compare": _scene_compare,
    "steps": _scene_steps,
}
