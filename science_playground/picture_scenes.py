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
    return pose if pose in ("start", "play", "end") else "play"


def _scene_tower_fall(round_no: int, spec: dict | None = None, **kwargs) -> str:
    pose = _pose(kwargs)
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
    body = """
    <div class="col left">
      <div class="label">WIDE BOTTOM</div>
      <div class="stack wide">
        <div class="block"></div><div class="block"></div><div class="block"></div>
        <div class="block" style="width:118px;background:#2a9d8f;box-shadow:0 4px 0 #1d6a62"></div>
      </div>
    </div>
    <div class="col right">
      <div class="label">TINY BOTTOM</div>
      <div class="stack tiny">
        <div class="block"></div><div class="block"></div><div class="block"></div>
        <div class="block" style="width:44px"></div>
      </div>
    </div>
    """
    return _page(css, body, "A wide tower stays. A tiny-bottom tower falls.", f"pose-{pose}")


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
    body = """
    <div class="tag" style="top:10px;left:8%;font-size:24px;color:#9c6644">RAMP</div>
    <div class="tag" style="top:10px;right:10%;font-size:24px;color:#343a40">WALL</div>
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
    body = """
    <div class="tag" style="top:8px;left:12%;font-size:22px;color:#1d6a62">CIRCLE FITS</div>
    <div class="tag" style="top:8px;right:10%;font-size:22px;color:#9d0208">SQUARE DOES NOT</div>
    <div class="board"></div><div class="hole"></div>
    <div class="shape circle"></div><div class="shape square"></div>
    """
    return _page(css, body, "A circle fits a round hole. A square does not.", f"pose-{pose}")


def _scene_who_went_farther(round_no: int, spec: dict | None = None, **kwargs) -> str:
    pose = _pose(kwargs)
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
    body = """
    <div class="flag">START</div>
    <div class="tag" style="top:58px;right:8%;font-size:20px;color:#1d3557">BLUE</div>
    <div class="tag" style="top:168px;right:8%;font-size:20px;color:#c1121f">RED — FARTHER</div>
    <div class="lane" style="top:108px"></div>
    <div class="lane" style="top:218px"></div>
    <div class="car blue"><b style="background:#457b9d"></b><i class="a"></i><i class="b"></i></div>
    <div class="car red"><b style="background:#e63946"></b><i class="a"></i><i class="b"></i></div>
    """
    return _page(css, body, "The red car stops farther from start than the blue car.", f"pose-{pose}")


def _scene_speeding_up(round_no: int, spec: dict | None = None, **kwargs) -> str:
    pose = _pose(kwargs)
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
    body = """
    <div class="tag" style="top:16px;left:12px;font-size:24px;color:#c1121f">GAPS GROW — SPEEDING UP</div>
    <div class="path"></div>
    <div class="stamp" style="left:10%"></div>
    <div class="stamp" style="left:24%;opacity:.55"></div>
    <div class="stamp" style="left:44%;opacity:.7"></div>
    <div class="stamp" style="left:70%;opacity:.9"></div>
    <div class="now" style="left:8%"></div>
    """
    return _page(css, body, "Car stamps get farther apart as the car speeds up.", f"pose-{pose}")


def _scene_roll_downhill(round_no: int, spec: dict | None = None, **kwargs) -> str:
    pose = _pose(kwargs)
    css = """
    .stage{background:linear-gradient(180deg,#caf0f8,#90e0ef)}
    .hill{position:absolute;left:0;right:0;bottom:0;height:210px;background:#52b69a;
          clip-path:polygon(0 18%,100% 88%,100% 100%,0 100%)}
    .ball{position:absolute;width:54px;height:54px;border-radius:50%;background:radial-gradient(circle at 30% 30%,#fff,#e63946);
          top:58px;left:10%}
    .pose-play .ball,.pose-end .ball{animation:rollHill 1.8s ease-in forwards}
    .pose-end .ball{top:210px;left:78%}
    @keyframes rollHill{to{top:210px;left:78%}}
    """
    body = """
    <div class="tag" style="top:12px;left:10%;font-size:24px;color:#1d3557">UPHILL</div>
    <div class="tag" style="top:12px;right:10%;font-size:24px;color:#c1121f">DOWNHILL</div>
    <div class="hill"></div>
    <div class="ball"></div>
    """
    return _page(css, body, "A ball rolls downhill.", f"pose-{pose}")


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


def _scene_solid_or_splash(round_no: int, spec: dict | None = None, **kwargs) -> str:
    pose = _pose(kwargs)
    css = """
    .stage{background:linear-gradient(180deg,#caf0f8 0 70%,#95d5b2 70%)}
    .block{position:absolute;left:12%;bottom:48px;width:110px;height:90px;background:#d4a373;border:5px solid #bc6c25;border-radius:10px}
    .puddle{position:absolute;right:12%;bottom:40px;width:160px;height:36px;background:#0077b6;border-radius:50%}
    .drop{position:absolute;right:22%;width:22px;height:28px;background:#48cae4;border-radius:50% 50% 50% 0;transform:rotate(-30deg)}
    .pose-play .drop,.pose-end .drop{animation:drip 1.2s ease-in infinite}
    @keyframes drip{from{top:40px;opacity:1}to{top:210px;opacity:.2}}
    """
    body = """
    <div class="tag" style="top:12px;left:10%;font-size:22px;color:#9c6644">WOOD BLOCK</div>
    <div class="tag" style="top:12px;right:10%;font-size:22px;color:#0077b6">WATER — SPLASH</div>
    <div class="block"></div>
    <div class="puddle"></div>
    <div class="drop"></div>
    """
    return _page(css, body, "A wood block holds shape. Water can splash.", f"pose-{pose}")


def _scene_hot_or_cold(round_no: int, spec: dict | None = None, **kwargs) -> str:
    pose = _pose(kwargs)
    css = """
    .stage{background:linear-gradient(90deg,#caf0f8 0 50%,#ffe8d6 50%)}
    .ice{position:absolute;left:14%;top:90px;width:90px;height:90px;background:#90e0ef;border:5px solid #48cae4;border-radius:16px}
    .bowl{position:absolute;right:14%;top:120px;width:130px;height:70px;background:#e76f51;border-radius:0 0 70px 70px}
    .steam{position:absolute;right:20%;top:48px;width:12px;height:50px;background:#adb5bd;border-radius:8px;opacity:.55}
    .pose-play .steam,.pose-end .steam{animation:rise 1.5s ease-in-out infinite}
    @keyframes rise{0%{transform:translateY(10px);opacity:.2}50%{opacity:.7}100%{transform:translateY(-16px);opacity:0}}
    """
    body = """
    <div class="tag" style="top:12px;left:10%;font-size:22px;color:#0077b6">ICE — COLD</div>
    <div class="tag" style="top:12px;right:10%;font-size:22px;color:#c1121f">SOUP — HOT</div>
    <div class="ice"></div>
    <div class="steam" style="right:24%"></div>
    <div class="steam" style="right:18%;height:40px"></div>
    <div class="steam" style="right:12%"></div>
    <div class="bowl"></div>
    """
    return _page(css, body, "Ice is cold. Soup is hot.", f"pose-{pose}")


def _scene_melt_or_freeze(round_no: int, spec: dict | None = None, **kwargs) -> str:
    pose = _pose(kwargs)
    css = """
    .stage{background:linear-gradient(180deg,#fff1c7,#caf0f8)}
    .sun{position:absolute;right:24px;top:16px;width:58px;height:58px;border-radius:50%;background:#ffd166}
    .ice{position:absolute;left:50%;top:70px;width:100px;height:100px;margin-left:-50px;background:#90e0ef;border:5px solid #48cae4;border-radius:18px}
    .puddle{position:absolute;left:50%;bottom:36px;width:40px;height:16px;margin-left:-20px;background:#0077b6;border-radius:50%;opacity:.2}
    .pose-play .ice,.pose-end .ice{animation:melt 1.8s ease-in forwards}
    .pose-end .ice{top:150px;width:160px;height:28px;margin-left:-80px;border-radius:40px}
    .pose-play .puddle,.pose-end .puddle{animation:grow 1.8s ease-in forwards}
    .pose-end .puddle{width:180px;height:28px;margin-left:-90px;opacity:1}
    @keyframes melt{to{top:150px;width:160px;height:28px;margin-left:-80px;border-radius:40px}}
    @keyframes grow{to{width:180px;height:28px;margin-left:-90px;opacity:1}}
    """
    body = """
    <div class="tag" style="top:18px;left:12px;font-size:24px;color:#c1121f">WARM — MELT</div>
    <div class="sun"></div>
    <div class="ice"></div>
    <div class="puddle"></div>
    """
    return _page(css, body, "Warm ice melts into a puddle.", f"pose-{pose}")


def _scene_living_or_not(round_no: int, spec: dict | None = None, **kwargs) -> str:
    pose = _pose(kwargs)
    css = """
    .stage{background:linear-gradient(180deg,#e8f5e9,#fff)}
    .pup{position:absolute;left:12%;bottom:50px;width:140px;height:90px}
    .pup .body{position:absolute;left:20px;bottom:16px;width:90px;height:44px;background:#b08968;border-radius:40px}
    .pup .head{position:absolute;right:8px;top:8px;width:54px;height:48px;background:#d4a373;border-radius:50%}
    .car{position:absolute;right:10%;bottom:54px;width:130px;height:58px}
    .car .cab{position:absolute;left:36px;top:0;width:48px;height:24px;background:#8ecae6;border-radius:8px 10px 0 0}
    .car .body{position:absolute;left:4px;top:18px;width:120px;height:24px;background:#6c757d;border-radius:8px}
    .car .wheel{position:absolute;bottom:0;width:18px;height:18px;background:#1d3557;border-radius:50%;border:3px solid #fff}
    .car .wheel.a{left:18px}.car .wheel.b{right:18px}
    .pose-play .pup,.pose-end .pup{animation:bob 0.8s ease-in-out infinite}
    @keyframes bob{50%{transform:translateY(-10px)}}
    """
    body = """
    <div class="tag" style="top:12px;left:10%;font-size:22px;color:#7f5539">PUPPY — LIVING</div>
    <div class="tag" style="top:12px;right:8%;font-size:22px;color:#495057">TOY CAR</div>
    <div class="pup"><div class="body"></div><div class="head"></div></div>
    <div class="car"><div class="cab"></div><div class="body"></div><div class="wheel a"></div><div class="wheel b"></div></div>
    """
    return _page(css, body, "A puppy is living. A toy car is not.", f"pose-{pose}")


def _scene_plant_or_animal(round_no: int, spec: dict | None = None, **kwargs) -> str:
    pose = _pose(kwargs)
    css = """
    .stage{background:linear-gradient(180deg,#caf0f8 0 68%,#95d5b2 68%)}
    .flower{position:absolute;left:16%;bottom:40px}
    .stem{width:14px;height:120px;background:#2d6a4f;margin:0 auto}
    .head{width:78px;height:78px;background:#ffd166;border-radius:50%;border:10px solid #f4a261;margin:0 auto}
    .bunny{position:absolute;right:14%;bottom:48px;width:90px;height:110px}
    .bunny .ear{position:absolute;top:0;width:18px;height:48px;background:#fff;border-radius:12px}
    .bunny .body{position:absolute;bottom:0;left:8px;width:70px;height:70px;background:#fff;border-radius:40px}
    .pose-play .head,.pose-end .head{animation:grow 1.6s ease-out forwards}
    @keyframes grow{from{transform:scale(.7)}to{transform:scale(1)}}
    """
    body = """
    <div class="tag" style="top:12px;left:8%;font-size:22px;color:#2d6a4f">SUNFLOWER — PLANT</div>
    <div class="tag" style="top:12px;right:8%;font-size:22px;color:#6c584c">RABBIT — ANIMAL</div>
    <div class="flower"><div class="head"></div><div class="stem"></div></div>
    <div class="bunny"><div class="ear" style="left:18px"></div><div class="ear" style="left:48px"></div><div class="body"></div></div>
    """
    return _page(css, body, "A sunflower is a plant. A rabbit is an animal.", f"pose-{pose}")


def _scene_hungry_or_full(round_no: int, spec: dict | None = None, **kwargs) -> str:
    pose = _pose(kwargs)
    css = """
    .stage{background:linear-gradient(180deg,#caf0f8,#e8f5e9)}
    .bird{position:absolute;left:50%;top:70px;width:90px;height:70px;margin-left:-45px}
    .bird .body{width:90px;height:54px;background:#457b9d;border-radius:50%}
    .bird .beak{position:absolute;right:-22px;top:22px;width:28px;height:16px;background:#f77f00;clip-path:polygon(0 0,100% 50%,0 100%)}
    .food{position:absolute;left:12%;bottom:48px;width:70px;height:28px;background:#e76f51;border-radius:0 0 40px 40px}
    .seed{position:absolute;left:18%;bottom:70px;width:16px;height:16px;background:#ffd166;border-radius:50%}
    .toy{position:absolute;right:12%;bottom:54px;width:70px;height:44px;background:#6c757d;border-radius:10px}
    .pose-play .beak,.pose-end .beak{animation:open 0.8s ease-in-out infinite}
    @keyframes open{50%{transform:rotate(12deg)}}
    """
    body = """
    <div class="tag" style="top:12px;left:8%;font-size:22px;color:#c1121f">FOOD</div>
    <div class="tag" style="top:12px;right:8%;font-size:22px;color:#6c757d">A TOY</div>
    <div class="food"></div><div class="seed"></div>
    <div class="bird"><div class="body"></div><div class="beak"></div></div>
    <div class="toy"></div>
    """
    return _page(css, body, "A hungry bird needs food, not a toy.", f"pose-{pose}")


def _scene_first_then_next(round_no: int, spec: dict | None = None, **kwargs) -> str:
    pose = _pose(kwargs)
    css = """
    .stage{background:linear-gradient(180deg,#ffe8d6,#fff)}
    .card{position:absolute;top:70px;width:150px;height:170px;border-radius:18px;background:#fff;border:4px solid #457b9d;text-align:center;font-weight:800;color:#1d3557}
    .card b{display:block;font-size:42px;margin-top:18px}
    .card span{display:block;margin-top:12px;font-size:22px}
    .one{left:8%}.two{left:50%;margin-left:-75px}.three{right:8%;opacity:.35}
    .arrow{position:absolute;top:140px;left:28%;font-size:42px;color:#e76f51;font-weight:800}
    .pose-play .two,.pose-end .two{animation:pop 0.8s ease-out forwards}
    @keyframes pop{from{transform:scale(.85)}to{transform:scale(1)}}
    """
    body = """
    <div class="tag" style="top:12px;left:12px;font-size:22px;color:#9c6644">FIRST, THEN NEXT</div>
    <div class="card one"><b>1</b><span>SOCKS</span></div>
    <div class="arrow">→</div>
    <div class="card two"><b>2</b><span>SHOES</span></div>
    <div class="card three"><b>3</b><span>HAT</span></div>
    """
    return _page(css, body, "First socks, then shoes. Not the hat yet.", f"pose-{pose}")


def _scene_missing_step(round_no: int, spec: dict | None = None, **kwargs) -> str:
    pose = _pose(kwargs)
    css = """
    .stage{background:linear-gradient(180deg,#e9f8ff,#fff)}
    .card{position:absolute;top:80px;width:140px;height:150px;border-radius:18px;background:#fff;border:4px solid #2a9d8f;text-align:center;font-weight:800;color:#1d3557}
    .card b{display:block;font-size:36px;margin-top:16px}
    .card span{display:block;margin-top:10px;font-size:20px}
    .miss{border-style:dashed;border-color:#e63946;background:#fff5f5}
    .pose-play .miss,.pose-end .miss{animation:blink 1s ease-in-out infinite}
    @keyframes blink{50%{background:#ffe5ec}}
    """
    body = """
    <div class="tag" style="top:14px;left:12px;font-size:22px;color:#c1121f">WHICH STEP IS MISSING?</div>
    <div class="card" style="left:8%"><b>1</b><span>WASH</span></div>
    <div class="card" style="left:50%;margin-left:-70px"><b>2</b><span>DRY</span></div>
    <div class="card miss" style="right:8%"><b>?</b><span>PUT AWAY</span></div>
    """
    return _page(css, body, "Wash, dry, then put away. The last step was missing.", f"pose-{pose}")


def _scene_do_it_again(round_no: int, spec: dict | None = None, **kwargs) -> str:
    pose = _pose(kwargs)
    css = """
    .stage{background:linear-gradient(180deg,#f3e8ff,#fff)}
    .clap{position:absolute;left:50%;top:90px;width:120px;height:80px;margin-left:-60px;background:#ef476f;border-radius:40px}
    .loop{position:absolute;left:50%;top:46px;width:200px;height:200px;margin-left:-100px;border:10px dashed #6a4c93;border-radius:50%}
    .pose-play .loop,.pose-end .loop{animation:spin 3s linear infinite}
    .pose-play .clap,.pose-end .clap{animation:clap 0.7s ease-in-out infinite}
    @keyframes spin{to{transform:rotate(360deg)}}
    @keyframes clap{50%{transform:scale(1.08)}}
    """
    body = """
    <div class="tag" style="top:14px;left:12px;font-size:24px;color:#6a4c93">REPEAT — DO IT AGAIN</div>
    <div class="loop"></div>
    <div class="clap"></div>
    """
    return _page(css, body, "Repeat means do the step again.", f"pose-{pose}")


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
}
