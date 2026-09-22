"""Build ten-round, flipping two-choice trial banks for picture-first games."""
from __future__ import annotations

from typing import Any


def pair_a_left(index: int) -> bool:
    """Put pair item A on the left independently of which question we ask.

    Alternating questions used to reuse the same even/odd bit for side, which
    pinned the correct picture to one box. A four-round cycle places the
    answer left, right, right, left.
    """
    return index % 4 < 2


def flip_two_choice(
    pairs: tuple[dict[str, Any], ...],
    *,
    a: str,
    b: str,
    q_for_a: str,
    q_for_b: str,
    scene: str,
    pic_a: str = "a_pic",
    pic_b: str = "b_pic",
    move_a: str = "a_move",
    move_b: str = "b_move",
) -> tuple[dict[str, Any], ...]:
    trials: list[dict[str, Any]] = []
    for i, pair in enumerate(pairs):
        ask_a = i % 2 == 0
        a_name = str(pair[a])
        b_name = str(pair[b])
        a_pic = str(pair.get(pic_a) or "🔵")
        b_pic = str(pair.get(pic_b) or "🔴")
        a_mv = str(pair.get(move_a) or "bob")
        b_mv = str(pair.get(move_b) or "still")
        a_left = pair_a_left(i)
        trial: dict[str, Any] = dict(pair)
        trial["scene"] = scene
        trial["question"] = q_for_a if ask_a else q_for_b
        trial["choices"] = [a_name, b_name]
        trial["answer"] = a_name if ask_a else b_name
        trial["left_name"] = a_name if a_left else b_name
        trial["right_name"] = b_name if a_left else a_name
        trial["left_pic"] = a_pic if a_left else b_pic
        trial["right_pic"] = b_pic if a_left else a_pic
        trial["left_move"] = a_mv if a_left else b_mv
        trial["right_move"] = b_mv if a_left else a_mv
        trial["picture"] = a_pic if ask_a else b_pic
        trials.append(trial)
    return tuple(trials)


def compare_game(
    *,
    game_id: str,
    title: str,
    tagline: str,
    picture: str,
    pairs: tuple[dict[str, Any], ...],
    q_for_a: str,
    q_for_b: str,
    tip: str,
    kid_tip: str | None = None,
    scene: str = "compare",
    a: str = "a",
    b: str = "b",
):
    from science_utils import run_game

    def run() -> None:
        first = pairs[0]
        run_game({
            "id": game_id,
            "title": title,
            "tagline": tagline,
            "question": q_for_a,
            "choices": [first[a], first[b]],
            "answer": first[a],
            "picture": picture,
            "scene": scene,
            "animate_mode": "once",
            "trials": flip_two_choice(
                pairs, a=a, b=b, q_for_a=q_for_a, q_for_b=q_for_b, scene=scene,
            ),
            "kid_tip": kid_tip or first.get("kid_tip") or tip,
            "tip": tip,
        })

    return run


def step_trials(rows: tuple[dict[str, Any], ...], scene: str) -> tuple[dict[str, Any], ...]:
    trials: list[dict[str, Any]] = []
    for row in rows:
        trial: dict[str, Any] = dict(row)
        trial["scene"] = scene
        trial["picture"] = str(row.get("picture") or row.get("icon") or "🔁")
        trials.append(trial)
    return tuple(trials)


def named_trials(
    rows: tuple[dict[str, Any], ...],
    scene: str,
    q_for_a: str,
    q_for_b: str,
    *,
    a: str = "a",
    b: str = "b",
    picture: str = "🗼",
) -> tuple[dict[str, Any], ...]:
    trials: list[dict[str, Any]] = []
    for i, row in enumerate(rows):
        ask_a = i % 2 == 0
        trial: dict[str, Any] = dict(row)
        trial["scene"] = scene
        trial["question"] = q_for_a if ask_a else q_for_b
        trial["choices"] = [row[a], row[b]]
        trial["answer"] = row[a] if ask_a else row[b]
        trial["wide_left"] = pair_a_left(i)
        trial["picture"] = picture
        trials.append(trial)
    return tuple(trials)


def step_game(
    *,
    game_id: str,
    title: str,
    tagline: str,
    picture: str,
    rows: tuple[dict[str, Any], ...],
    scene: str,
    tip: str,
    kid_tip: str | None = None,
):
    from science_utils import run_game

    def run() -> None:
        first = rows[0]
        run_game({
            "id": game_id,
            "title": title,
            "tagline": tagline,
            "question": first["question"],
            "choices": list(first["choices"]),
            "answer": first["answer"],
            "picture": picture,
            "scene": scene,
            "animate_mode": "once",
            "trials": step_trials(rows, scene),
            "kid_tip": kid_tip or first.get("kid_tip") or tip,
            "tip": tip,
        })

    return run


def play_compare(
    *,
    game_id: str,
    title: str,
    tagline: str,
    picture: str,
    pairs: tuple[dict[str, Any], ...],
    q_for_a: str,
    q_for_b: str,
    tip: str,
    kid_tip: str | None = None,
    scene: str = "compare",
    a: str = "a",
    b: str = "b",
) -> None:
    compare_game(
        game_id=game_id,
        title=title,
        tagline=tagline,
        picture=picture,
        pairs=pairs,
        q_for_a=q_for_a,
        q_for_b=q_for_b,
        tip=tip,
        kid_tip=kid_tip,
        scene=scene,
        a=a,
        b=b,
    )()
