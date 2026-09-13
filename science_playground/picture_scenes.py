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


def _tower_stack(kind: str, size: str) -> str:
    """HTML for one tower. `size` is wide (stays) or tiny (tips)."""
    wide = size == "wide"
    if kind == "cups":
        widths = (100, 88, 76, 64) if wide else (30, 40, 50, 62)
        bits = "".join(f'<div class="cup" style="width:{w}px"></div>' for w in widths)
        return bits
    if kind == "books":
        palette = ("#e63946", "#457b9d", "#2a9d8f", "#f4a261")
        widths = (112, 96, 84, 72) if wide else (38, 70, 88, 104)
        bits = "".join(
            f'<div class="book" style="width:{w}px;background:{color}"><i></i></div>'
            for w, color in zip(widths, palette)
        )
        return bits
    if kind == "boxes":
        widths = (110, 96, 84, 72) if wide else (36, 40, 38, 42)
        bits = "".join(f'<div class="box-bit" style="width:{w}px"></div>' for w in widths)
        return bits
    if kind == "pyramid":
        widths = (112, 86, 60, 36) if wide else (36, 60, 86, 112)
        bits = "".join(f'<div class="block stone" style="width:{w}px"></div>' for w in widths)
        return bits
    if kind == "cans":
        widths = (88, 72, 60, 50) if wide else (28, 48, 64, 80)
        bits = "".join(f'<div class="can" style="width:{w}px"><i></i></div>' for w in widths)
        return bits
    if kind == "sand":
        if wide:
            return (
                '<div class="keep wide-keep">'
                '<div class="merlon"></div><div class="merlon"></div><div class="merlon"></div>'
                '<div class="keep-body"></div></div>'
            )
        return (
            '<div class="keep tiny-keep">'
            '<div class="merlon"></div>'
            '<div class="keep-body thin"></div></div>'
        )
    if kind == "stool":
        if wide:
            return (
                '<div class="stool small"><div class="seat"></div>'
                '<div class="leg a"></div><div class="leg b"></div></div>'
                '<div class="stool"><div class="seat"></div>'
                '<div class="leg a"></div><div class="leg b"></div></div>'
            )
        return (
            '<div class="pencils">'
            '<div class="pencil"></div><div class="pencil"></div><div class="pencil"></div>'
            '</div>'
        )
    if kind == "pillows":
        widths = (108, 96, 86) if wide else (36, 40, 34)
        colors = ("#ffafcc", "#bde0fe", "#cdb4db")
        bits = "".join(
            f'<div class="pillow" style="width:{w}px;background:{color}"></div>'
            for w, color in zip(widths, colors)
        )
        return bits
    if kind == "stones":
        if wide:
            return (
                '<div class="rock r1"></div><div class="rock r2"></div>'
                '<div class="rock r3"></div><div class="rock r4"></div>'
            )
        return (
            '<div class="rock s1"></div><div class="rock s2"></div>'
            '<div class="rock s3"></div><div class="rock s4"></div>'
        )
    widths = (118, 100, 88, 76) if wide else (44, 44, 44, 44)
    bits = "".join(f'<div class="block" style="width:{w}px"></div>' for w in widths)
    return bits


def _scene_tower_fall(round_no: int, spec: dict | None = None, **kwargs) -> str:
    spec = spec or {}
    pose = _pose(kwargs)
    wide = str(spec.get("wide") or "Wide bottom")
    tiny = str(spec.get("tiny") or "Tiny bottom")
    kind = str(spec.get("tower_kind") or "blocks")
    wide_left = _truthy(spec.get("wide_left", True))
    left_name, left_cls = (wide, "wide") if wide_left else (tiny, "tiny")
    right_name, right_cls = (tiny, "tiny") if wide_left else (wide, "wide")
    css = """
    .stage{background:linear-gradient(180deg,#caf0f8 0 72%,#95d5b2 72%)}
    .col{position:absolute;top:18px;bottom:18px;width:42%}
    .col.left{left:6%}.col.right{right:6%}
    .label{text-align:center;font-weight:800;font-size:20px;color:#1d3557}
    .stack{position:absolute;left:50%;width:120px;margin-left:-60px;bottom:8px}
    .block{height:32px;margin:4px auto;border-radius:8px;background:#e76f51;box-shadow:0 4px 0 #9d0208}
    .block.stone{background:#8d99ae;box-shadow:0 4px 0 #495057}
    .cup{height:30px;margin:5px auto 0;background:#90e0ef;border-radius:0 0 14px 14px;border:3px solid #48cae4;box-sizing:border-box}
    .book{height:26px;margin:4px auto;border-radius:3px;box-shadow:0 3px 0 rgba(0,0,0,.2);position:relative}
    .book i{position:absolute;left:8px;top:4px;bottom:4px;width:5px;background:rgba(255,255,255,.45)}
    .box-bit{height:30px;margin:4px auto;background:#e9c46a;border:3px solid #bc6c25;border-radius:4px;box-sizing:border-box}
    .can{height:34px;margin:5px auto 0;background:linear-gradient(90deg,#adb5bd,#f8f9fa 40%,#6c757d);border-radius:8px;position:relative}
    .can i{position:absolute;left:6%;right:6%;top:-5px;height:10px;background:#dee2e6;border-radius:50%;border:2px solid #adb5bd}
    .keep{position:relative;margin:0 auto}
    .wide-keep{width:112px}.tiny-keep{width:36px}
    .keep-body{height:110px;background:#e9c46a;border-radius:6px 6px 0 0;box-shadow:inset 0 12px 0 #f4a261}
    .keep-body.thin{height:130px}
    .merlon{display:inline-block;width:28%;height:16px;margin:0 2%;background:#e9c46a;border-radius:3px 3px 0 0}
    .stool{position:relative;width:100px;height:70px;margin:6px auto 0}
    .stool.small{width:78px;height:54px}
    .seat{height:16px;background:#bc6c25;border-radius:8px}
    .leg{position:absolute;bottom:0;width:10px;height:52px;background:#6c584c;border-radius:4px}
    .stool.small .leg{height:38px}
    .leg.a{left:12px}.leg.b{right:12px}
    .pencils{display:flex;justify-content:center;gap:8px;align-items:flex-end;height:150px}
    .pencil{width:14px;height:140px;background:linear-gradient(#e9c46a 0 78%,#f4a261 78% 88%,#e76f51 88%);border-radius:3px 3px 0 0}
    .pillow{height:38px;margin:6px auto;border-radius:18px;box-shadow:0 4px 0 rgba(0,0,0,.12)}
    .rock{margin:3px auto;background:#6c757d;border-radius:50%;box-shadow:inset -6px -6px 0 #495057}
    .r1{width:38px;height:28px}.r2{width:70px;height:36px}.r3{width:96px;height:40px}.r4{width:112px;height:46px}
    .s1{width:28px;height:26px}.s2{width:30px;height:28px}.s3{width:26px;height:24px}.s4{width:32px;height:30px}
    .pose-play .tiny,.pose-end .tiny{transform-origin:50% 100%;animation:tip 1.4s ease-in forwards}
    .pose-end .tiny{transform:rotate(78deg) translate(36px,28px)}
    @keyframes tip{60%{transform:rotate(18deg)}100%{transform:rotate(78deg) translate(36px,28px)}}
    """
    body = f"""
    <div class="col left">
      <div class="label">{html.escape(left_name)}</div>
      <div class="stack {left_cls} kind-{html.escape(kind)}">{_tower_stack(kind, left_cls)}</div>
    </div>
    <div class="col right">
      <div class="label">{html.escape(right_name)}</div>
      <div class="stack {right_cls} kind-{html.escape(kind)}">{_tower_stack(kind, right_cls)}</div>
    </div>
    """
    return _page(css, body, f"{wide} stays. {tiny} tips.", f"pose-{pose}", round_no=round_no)


def _ramp_path_art(kind: str) -> str:
    if kind == "stairs":
        return (
            '<div class="step s1"></div><div class="step s2"></div>'
            '<div class="step s3"></div><div class="step s4"></div>'
            '<div class="step s5"></div>'
        )
    if kind == "book":
        return '<div class="slope-fill"></div><div class="slope-face book-face"><i></i><i class="p2"></i></div>'
    if kind == "playground":
        return (
            '<div class="slope-fill"></div><div class="slope-face slide-face"></div>'
            '<div class="rail top"></div><div class="rail bot"></div>'
            '<div class="ladder"><b></b><b></b><b></b><b></b><i></i><i></i><i></i></div>'
        )
    if kind == "hill":
        return '<div class="hill-mound"></div><div class="slope-face hill-path"></div>'
    if kind == "driveway":
        return (
            '<div class="slope-fill"></div>'
            '<div class="slope-face drive-face"><i></i><i></i><i></i></div>'
        )
    if kind == "cardboard":
        return '<div class="slope-fill"></div><div class="slope-face card-face"><i></i><i></i></div>'
    if kind == "wedge":
        return '<div class="wedge-body"></div><div class="slope-face wedge-face"></div>'
    if kind == "slide":
        return (
            '<div class="slope-fill"></div><div class="slope-face slide-face"></div>'
            '<div class="rail top"></div><div class="rail bot"></div>'
        )
    return (
        '<div class="slope-fill"></div>'
        '<div class="slope-face wood-face"><i></i><i></i><i></i></div>'
    )


def _ramp_block_art(kind: str) -> str:
    if kind == "slide":
        return '<div class="blocker fence"><b></b><b></b><b></b><b></b><i></i><i class="low"></i></div>'
    if kind == "hill":
        return '<div class="blocker cliff"></div>'
    if kind == "door":
        return '<div class="blocker door"><i class="knob"></i><i class="panel"></i></div>'
    if kind == "playground":
        return '<div class="blocker brick"></div>'
    if kind == "driveway":
        return '<div class="blocker garage"><i></i><i></i><i></i></div>'
    if kind == "book":
        return '<div class="blocker book-wall"><i></i></div>'
    if kind == "cardboard":
        return '<div class="blocker card-wall"><i></i><i></i></div>'
    if kind == "wedge":
        return '<div class="blocker cube"></div>'
    if kind == "stairs":
        return '<div class="blocker gate"><b></b><b></b><b></b><i></i></div>'
    return '<div class="blocker wall"></div>'


def _scene_ramp_or_wall(round_no: int, spec: dict | None = None, **kwargs) -> str:
    spec = spec or {}
    pose = _pose(kwargs)
    path = str(spec.get("path") or "Ramp")
    block = str(spec.get("block") or "Wall")
    kind = str(spec.get("ramp_kind") or "board")
    css = """
    .stage{background:linear-gradient(180deg,#caf0f8 0 62%,#6c757d 62% 68%,#2d6a4f 68%)}
    .half{position:absolute;top:0;bottom:0;width:50%}
    .half.left{left:0}.half.right{right:0}
    .label{position:absolute;top:10px;left:8%;right:8%;text-align:center;font-size:20px;font-weight:800;color:#1d3557}
    .path-box,.block-box{position:absolute;left:6%;right:4%;bottom:14%;height:150px}
    .slope-fill{position:absolute;left:0;bottom:0;width:0;height:0;z-index:1;
      border-bottom:128px solid #bc6c25;border-right:220px solid transparent}
    .slope-face{position:absolute;left:0;bottom:120px;width:254px;height:16px;background:#d4a373;z-index:2;
      transform-origin:left center;transform:rotate(30deg);border-radius:8px}
    .wood-face{background:repeating-linear-gradient(90deg,#d4a373 0 16px,#bc6c25 16px 18px,#e9c46a 18px 34px)}
    .wood-face i{position:absolute;top:4px;bottom:4px;width:3px;background:rgba(109,68,26,.35)}
    .wood-face i:nth-child(1){left:28px}.wood-face i:nth-child(2){left:92px}.wood-face i:nth-child(3){left:168px}
    .kind-slide .slope-fill{border-bottom-color:#ffd166}
    .slide-face{background:#f4a261;height:22px;bottom:117px}
    .rail{position:absolute;left:0;width:250px;height:6px;background:#e76f51;z-index:2;
      transform-origin:left center;transform:rotate(30deg);border-radius:4px}
    .rail.top{bottom:136px}.rail.bot{bottom:108px}
    .kind-hill .slope-fill{display:none}
    .hill-mound{position:absolute;left:0;bottom:0;width:220px;height:128px;z-index:1;
      background:linear-gradient(180deg,#95d5b2,#2d6a4f);clip-path:polygon(0 0,100% 100%,0 100%)}
    .hill-path{background:#6c584c;height:14px;bottom:121px}
    .kind-door .slope-fill{border-bottom-color:#bc6c25}
    .kind-playground .slope-fill{border-bottom-color:#ffd166}
    .ladder{position:absolute;left:0;bottom:0;width:22px;height:128px;z-index:2}
    .ladder b{position:absolute;left:0;right:0;height:6px;background:#e76f51;border-radius:3px}
    .ladder b:nth-child(1){bottom:24px}.ladder b:nth-child(2){bottom:52px}
    .ladder b:nth-child(3){bottom:80px}.ladder b:nth-child(4){bottom:108px}
    .ladder i{position:absolute;top:0;bottom:0;width:6px;background:#c1121f;border-radius:3px}
    .ladder i:nth-of-type(1){left:0}.ladder i:nth-of-type(2){right:0}.ladder i:nth-of-type(3){display:none}
    .kind-driveway .slope-fill{border-bottom-color:#6c757d}
    .drive-face{background:#495057;height:22px;bottom:117px}
    .drive-face i{position:absolute;top:8px;height:4px;width:28px;background:#ffd166;border-radius:2px}
    .drive-face i:nth-child(1){left:24px}.drive-face i:nth-child(2){left:88px}.drive-face i:nth-child(3){left:152px}
    .kind-book .slope-fill{border-bottom-color:#9d0208}
    .book-face{background:#e63946;height:28px;bottom:114px}
    .book-face i{position:absolute;left:16px;top:6px;bottom:6px;width:6px;background:rgba(255,255,255,.45)}
    .book-face i.p2{left:28px}
    .kind-cardboard .slope-fill{border-bottom-color:#e9c46a}
    .card-face{background:repeating-linear-gradient(90deg,#e9c46a 0 10px,#f4a261 10px 12px);height:20px;bottom:118px}
    .card-face i{position:absolute;top:3px;bottom:3px;width:4px;background:rgba(188,108,37,.4)}
    .card-face i:nth-child(1){left:40px}.card-face i:nth-child(2){left:140px}
    .wedge-body{position:absolute;left:8px;bottom:0;width:0;height:0;z-index:1;
      border-bottom:88px solid #f4a261;border-right:150px solid transparent}
    .wedge-face{background:#e76f51;width:176px;bottom:80px}
    .step{position:absolute;background:#adb5bd;border-top:5px solid #dee2e6;z-index:1;box-shadow:2px 0 0 #6c757d}
    .s1{left:0;bottom:100px;width:48px;height:28px}
    .s2{left:44px;bottom:75px;width:48px;height:28px}
    .s3{left:88px;bottom:50px;width:48px;height:28px}
    .s4{left:132px;bottom:25px;width:48px;height:28px}
    .s5{left:176px;bottom:0;width:52px;height:28px}
    .blocker.wall{position:absolute;right:18%;bottom:0;width:30px;height:140px;background:#6c757d;border-radius:6px}
    .blocker.fence{position:absolute;right:12%;bottom:0;width:90px;height:120px}
    .blocker.fence b{position:absolute;bottom:0;width:10px;height:120px;background:#6c584c}
    .blocker.fence b:nth-child(1){left:0}.blocker.fence b:nth-child(2){left:26px}
    .blocker.fence b:nth-child(3){left:52px}.blocker.fence b:nth-child(4){left:78px}
    .blocker.fence i{position:absolute;left:0;right:0;height:10px;background:#a98467}
    .blocker.fence i{top:28px}.blocker.fence i.low{top:68px}
    .blocker.cliff{position:absolute;right:10%;bottom:0;width:70px;height:150px;
      background:#6c757d;clip-path:polygon(20% 0,100% 0,100% 100%,0 100%,8% 62%,28% 40%)}
    .blocker.door{position:absolute;right:16%;bottom:0;width:54px;height:130px;background:#6c584c;border-radius:8px 8px 0 0}
    .blocker.door .knob{position:absolute;right:8px;top:62px;width:10px;height:10px;border-radius:50%;background:#ffd166}
    .blocker.door .panel{position:absolute;left:8px;right:8px;top:12px;height:40px;border:3px solid #4a3728;border-radius:4px}
    .blocker.brick{position:absolute;right:14%;bottom:0;width:70px;height:140px;border-radius:4px;
      background:repeating-linear-gradient(#bc4749 0 16px,#f2e8cf 16px 18px)}
    .blocker.garage{position:absolute;right:10%;bottom:0;width:80px;height:120px;background:#adb5bd;border:4px solid #495057}
    .blocker.garage i{display:block;height:8px;margin:14px 8px 0;background:#6c757d}
    .blocker.book-wall{position:absolute;right:18%;bottom:0;width:36px;height:130px;background:#457b9d;border-radius:4px}
    .blocker.book-wall i{position:absolute;left:8px;top:12px;bottom:12px;width:6px;background:rgba(255,255,255,.35)}
    .blocker.card-wall{position:absolute;right:16%;bottom:0;width:40px;height:130px;background:#e9c46a;border:3px solid #bc6c25}
    .blocker.card-wall i{position:absolute;left:8px;right:8px;height:6px;background:#bc6c25}
    .blocker.card-wall i:nth-child(1){top:18px}.blocker.card-wall i:nth-child(2){top:36px}
    .blocker.cube{position:absolute;right:18%;bottom:0;width:64px;height:64px;background:#457b9d;border-radius:8px}
    .blocker.gate{position:absolute;right:10%;bottom:0;width:90px;height:110px}
    .blocker.gate b{position:absolute;bottom:0;width:10px;height:110px;background:#6c584c}
    .blocker.gate b:nth-child(1){left:0}.blocker.gate b:nth-child(2){left:40px}.blocker.gate b:nth-child(3){left:80px}
    .blocker.gate i{position:absolute;left:0;right:0;top:18px;height:14px;background:#bc6c25}
    .car{position:absolute;width:56px;height:24px;z-index:3}
    .car b{display:block;height:18px;background:#e63946;border-radius:8px 14px 6px 6px}
    .car i{position:absolute;bottom:-6px;width:12px;height:12px;background:#1d3557;border-radius:50%;border:3px solid #fff}
    .car i.a{left:6px}.car i.b{right:6px}
    .car.go{left:8px;bottom:110px;transform:rotate(30deg);transform-origin:center bottom}
    .car.stuck{left:10%;bottom:8px}
    .car.stuck b{background:#457b9d}
    .pose-play .go,.pose-end .go{animation:rollDown 1.6s ease-in forwards}
    .pose-end .go{left:158px;bottom:14px;transform:rotate(30deg)}
    .pose-play .stuck,.pose-end .stuck{animation:bump 1.1s ease-in forwards}
    .pose-end .stuck{left:46%}
    @keyframes rollDown{from{left:8px;bottom:110px;transform:rotate(30deg)}to{left:158px;bottom:14px;transform:rotate(30deg)}}
    @keyframes bump{0%{left:10%}70%{left:46%}100%{left:46%}}
    """
    body = f"""
    <div class="half left">
      <div class="label">{html.escape(path)}</div>
      <div class="path-box kind-{html.escape(kind)}">{_ramp_path_art(kind)}
        <div class="car go"><b></b><i class="a"></i><i class="b"></i></div>
      </div>
    </div>
    <div class="half right">
      <div class="label">{html.escape(block)}</div>
      <div class="block-box kind-{html.escape(kind)}">{_ramp_block_art(kind)}
        <div class="car stuck"><b></b><i class="a"></i><i class="b"></i></div>
      </div>
    </div>
    """
    return _page(css, body, f"A car rolls down {path}. {block} stops a car.", f"pose-{pose}", round_no=round_no)


def _hole_piece(art: str, side: str, role: str) -> str:
    extras = {
        "cookie": "<i></i><i></i><i></i>",
        "cracker": "<i></i><i></i><i></i><i></i>",
        "ball": "<i></i>",
        "block": "<i></i>",
        "coin": "<i></i>",
        "ticket": "<i></i>",
        "lid": "<i></i>",
        "book": "<i></i>",
        "button": "<i></i><i></i><i></i><i></i>",
        "stamp": "<i></i>",
        "orange": "<i></i>",
        "box": "<i></i>",
        "wheel": "<i></i><b></b>",
        "crate": "<i></i><i></i>",
        "plate": "<i></i>",
        "napkin": "<i></i>",
        "donut": "<i></i>",
        "toast": "<i></i>",
    }
    return (
        f'<div class="shape {html.escape(side)} art-{html.escape(art)} {html.escape(role)}">'
        f"{extras.get(art, '')}</div>"
    )


def _scene_fit_the_hole(round_no: int, spec: dict | None = None, **kwargs) -> str:
    spec = spec or {}
    pose = _pose(kwargs)
    hole = str(spec.get("hole") or "circle")
    if hole not in ("circle", "square"):
        hole = "circle"
    round_name = str(spec.get("a") or "Circle")
    square_name = str(spec.get("b") or "Square")
    round_art = str(spec.get("round_art") or "circle")
    square_art = str(spec.get("square_art") or "square")
    fits = str(spec.get("fits") or (square_name if hole == "square" else round_name))
    misses = str(spec.get("misses") or (round_name if hole == "square" else square_name))
    round_role = "fit" if fits == round_name else "miss"
    square_role = "fit" if fits == square_name else "miss"
    css = """
    .stage{background:linear-gradient(180deg,#fff1c7,#ffe8d6)}
    .board{position:absolute;left:50%;top:118px;width:240px;height:110px;margin-left:-120px;
           background:#6c584c;border-radius:18px}
    .hole{position:absolute;left:50%;top:142px;width:78px;height:78px;margin-left:-39px;
          background:#1d3557;box-shadow:inset 0 0 0 6px #3d405b}
    .hole-circle{border-radius:50%}
    .hole-square{border-radius:8px}
    .shape{position:absolute;top:28px;width:72px;height:72px;z-index:2}
    .shape.left{left:12%}
    .shape.right{right:12%}
    .art-circle{background:#2a9d8f;border-radius:50%}
    .art-square{background:#e76f51;border-radius:10px}
    .art-cookie{background:#d4a373;border-radius:50%;box-shadow:inset -6px -8px 0 #bc6c25}
    .art-cookie i{position:absolute;width:10px;height:10px;border-radius:50%;background:#6c584c}
    .art-cookie i:nth-child(1){left:16px;top:18px}.art-cookie i:nth-child(2){left:40px;top:14px}
    .art-cookie i:nth-child(3){left:28px;top:40px}
    .art-cracker{background:#e9c46a;border-radius:8px}
    .art-cracker i{position:absolute;width:8px;height:8px;border-radius:50%;background:#bc6c25}
    .art-cracker i:nth-child(1){left:14px;top:16px}.art-cracker i:nth-child(2){right:14px;top:16px}
    .art-cracker i:nth-child(3){left:14px;bottom:16px}.art-cracker i:nth-child(4){right:14px;bottom:16px}
    .art-ball{background:#e63946;border-radius:50%}
    .art-ball i{position:absolute;left:12px;top:10px;width:18px;height:14px;border-radius:50%;background:#fff6}
    .art-block{background:#bc6c25;border-radius:8px;box-shadow:inset 0 -10px 0 #6c584c}
    .art-block i{position:absolute;left:8px;right:8px;top:16px;height:6px;background:#e9c46a}
    .art-coin{background:#ffd166;border-radius:50%;box-shadow:inset 0 0 0 6px #f4a261}
    .art-coin i{position:absolute;left:26px;top:18px;width:20px;height:36px;border-radius:4px;background:#bc6c25}
    .art-ticket{background:#f8edeb;border-radius:6px;border:3px dashed #e76f51;box-sizing:border-box}
    .art-ticket i{position:absolute;left:10px;top:16px;right:10px;height:8px;background:#e76f51}
    .art-lid{background:#90e0ef;border-radius:50%;box-shadow:inset 0 0 0 10px #48cae4}
    .art-lid i{position:absolute;left:26px;top:26px;width:20px;height:20px;border-radius:50%;background:#caf0f8}
    .art-book{background:#457b9d;border-radius:4px}
    .art-book i{position:absolute;left:10px;top:8px;bottom:8px;width:8px;background:#fff6}
    .art-button{background:#e76f51;border-radius:50%}
    .art-button i{position:absolute;width:10px;height:10px;border-radius:50%;background:#fff}
    .art-button i:nth-child(1){left:18px;top:18px}.art-button i:nth-child(2){right:18px;top:18px}
    .art-button i:nth-child(3){left:18px;bottom:18px}.art-button i:nth-child(4){right:18px;bottom:18px}
    .art-stamp{background:#caf0f8;border-radius:4px;
      background-image:radial-gradient(#fff 42%,transparent 44%);background-size:10px 10px}
    .art-stamp i{position:absolute;left:14px;top:22px;right:14px;height:10px;background:#e63946}
    .art-orange{background:#f4a261;border-radius:50%}
    .art-orange i{position:absolute;left:30px;top:-4px;width:12px;height:16px;background:#2d6a4f;border-radius:4px}
    .art-box{background:#e9c46a;border-radius:6px;border:3px solid #bc6c25;box-sizing:border-box}
    .art-box i{position:absolute;left:8px;right:8px;top:8px;height:16px;background:#f4a261}
    .art-wheel{background:#6c757d;border-radius:50%;box-shadow:inset 0 0 0 8px #1d3557}
    .art-wheel i{position:absolute;left:26px;top:26px;width:20px;height:20px;border-radius:50%;background:#adb5bd}
    .art-wheel b{position:absolute;left:34px;top:8px;width:6px;bottom:8px;background:#adb5bd}
    .art-crate{background:#bc6c25;border-radius:6px}
    .art-crate i{position:absolute;left:10px;right:10px;height:8px;background:#e9c46a}
    .art-crate i:nth-child(1){top:16px}.art-crate i:nth-child(2){top:36px}
    .art-plate{background:#f8edeb;border-radius:50%;box-shadow:inset 0 0 0 10px #d6ccc2}
    .art-plate i{position:absolute;left:22px;top:22px;width:28px;height:28px;border-radius:50%;background:#fff}
    .art-napkin{background:#fff;border-radius:6px;box-shadow:inset 8px 8px 0 #e9ecef}
    .art-napkin i{position:absolute;right:8px;bottom:8px;width:22px;height:22px;background:#f8edeb}
    .art-donut{background:#e76f51;border-radius:50%;box-shadow:inset 0 0 0 16px #f4a261}
    .art-donut i{position:absolute;left:24px;top:24px;width:24px;height:24px;border-radius:50%;background:#fff1c7}
    .art-toast{background:#e9c46a;border-radius:10px;box-shadow:inset 0 0 0 8px #bc6c25}
    .art-toast i{position:absolute;left:16px;top:22px;width:40px;height:8px;background:#f4a261;border-radius:4px}
    .pose-play .fit,.pose-end .fit{animation:dropIn 1.4s ease-in forwards}
    .pose-end .fit{top:148px;left:calc(50% - 36px);right:auto}
    .pose-play .miss.right,.pose-end .miss.right{animation:bounceRight 1.4s ease-in forwards}
    .pose-end .miss.right{top:28px;right:8%}
    .pose-play .miss.left,.pose-end .miss.left{animation:bounceLeft 1.4s ease-in forwards}
    .pose-end .miss.left{top:28px;left:8%}
    @keyframes dropIn{to{top:148px;left:calc(50% - 36px);right:auto}}
    @keyframes bounceRight{40%{top:118px;right:22%}100%{top:28px;right:8%}}
    @keyframes bounceLeft{40%{top:118px;left:22%}100%{top:28px;left:8%}}
    """
    hole_word = "square" if hole == "square" else "round"
    body = f"""
    <div class="tag" style="top:8px;left:8%;font-size:20px;color:#1d6a62">{html.escape(round_name)}</div>
    <div class="tag" style="top:8px;right:8%;font-size:20px;color:#9d0208">{html.escape(square_name)}</div>
    <div class="board"></div><div class="hole hole-{html.escape(hole)}"></div>
    {_hole_piece(round_art, "left", round_role)}
    {_hole_piece(square_art, "right", square_role)}
    """
    return _page(
        css, body,
        f"{fits} fits the {hole_word} hole. {misses} does not.",
        f"pose-{pose}",
        round_no=round_no,
    )


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
        cards += (
            f'<div class="card{miss}" style="left:{left}%">'
            f'<b>{html.escape(str(step.get("n") or i + 1))}</b>'
            f'<span class="pic">{html.escape(str(step.get("pic") or ""))}</span>'
            f'<span>{html.escape(str(step.get("label") or ""))}</span></div>'
        )
    css = """
    .stage{background:linear-gradient(180deg,#ffe8d6,#e9f8ff)}
    .title{position:absolute;top:12px;left:12px;right:12px;text-align:center;font-size:22px;font-weight:800;color:#1d3557}
    .card{position:absolute;top:78px;width:28%;height:180px;border-radius:18px;background:#fff;border:4px solid #457b9d;text-align:center;font-weight:800;color:#1d3557}
    .card b{display:block;font-size:28px;margin-top:10px}
    .card .pic{display:block;font-size:42px;margin-top:8px}
    .card span{display:block;margin-top:8px;font-size:18px}
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
            {"n": "1", "label": spec.get("first") or "Socks", "pic": spec.get("first_pic") or "🧦"},
            {"n": "2", "label": spec.get("next") or "Shoes", "pic": spec.get("next_pic") or "👟"},
            {"n": "3", "label": spec.get("later") or "Hat", "pic": spec.get("later_pic") or "🎩"},
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
