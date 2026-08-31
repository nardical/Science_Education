"""Play a guided lesson: Look → Name → (Change) → hands-on → games."""
from __future__ import annotations

import time
from typing import Any

import streamlit as st

from feedback_popup import clear_feedback_overlay, show_feedback_overlay
from science_utils import FEEDBACK_SECONDS, inject_form_css, show_scene

from .catalog import BUILD_PRIORITY, Lesson, get_lesson


def _key(lesson_id: str, suffix: str) -> str:
    return f"lesson_{lesson_id}_{suffix}"


def _beats(lesson: Lesson) -> list[dict[str, Any]]:
    beats: list[dict[str, Any]] = []
    for scene in lesson["scenes"]:
        beats.append({"kind": "look", "scene": scene})
        beats.append({"kind": "name", "scene": scene})
        if scene.get("change"):
            beats.append({"kind": "change", "scene": scene})
    beats.append({"kind": "hands_on"})
    beats.append({"kind": "play"})
    return beats


def _picture(scene: dict[str, Any], *, change: bool = False) -> None:
    spec = None
    pose = None
    if change:
        spec = scene.get("change", {}).get("look_scene")
        pose = scene.get("change", {}).get("look_pose")
    else:
        spec = scene.get("look_scene")
        pose = scene.get("look_pose")
    if spec:
        show_scene(spec, 0, pose=pose)
        return
    icon = scene.get("icon") or "🔬"
    st.markdown(
        f'<div class="science-card" style="font-size:4.5rem;padding:1.6rem">{icon}</div>',
        unsafe_allow_html=True,
    )


def _progress(lesson: Lesson, index: int, total: int) -> None:
    wave = lesson["wave"]
    picture = "🎬 Picture-first" if lesson.get("playable") else f"📝 Script · Wave {wave}"
    st.caption(f"{picture} · Step {index + 1} of {total} · about {lesson['minutes']} minutes")
    st.progress((index + 1) / total)


def _ask_and_wait(lesson_id: str, beat_id: str, ask: dict[str, Any]) -> bool:
    """Show a tap question. Return True once the overlay has finished."""
    pending_key = _key(lesson_id, f"{beat_id}_pending")
    done_key = _key(lesson_id, f"{beat_id}_done")
    if st.session_state.get(done_key):
        return True
    pending = st.session_state.get(pending_key)
    if pending:
        show_feedback_overlay(pending["message"], pending["correct"], pending["detail"])
        time.sleep(FEEDBACK_SECONDS)
        st.session_state[pending_key] = None
        if pending["correct"]:
            st.session_state[done_key] = True
        st.rerun()
    st.subheader(ask["question"])
    choices = list(ask["choices"])
    cols = st.columns(len(choices))
    for col, choice in zip(cols, choices):
        if col.button(choice, use_container_width=True, key=_key(lesson_id, f"{beat_id}_{choice}")):
            correct = choice == ask["answer"]
            st.session_state[pending_key] = {
                "message": "Yes! 🌟" if correct else "Try the other one. 💛",
                "correct": correct,
                "detail": ask["kid_tip"],
            }
            st.rerun()
    return False


def _next_button(lesson_id: str, step: int, label: str = "I see it!") -> None:
    if st.button(label, use_container_width=True, key=_key(lesson_id, f"next_{step}")):
        st.session_state[_key(lesson_id, "step")] = step + 1
        st.rerun()


def _reset(lesson_id: str) -> None:
    prefix = f"lesson_{lesson_id}_"
    for key in list(st.session_state.keys()):
        if str(key).startswith(prefix):
            del st.session_state[key]


def run_lesson(lesson: Lesson) -> None:
    inject_form_css()
    lesson_id = lesson["id"]
    playing = st.session_state.get(_key(lesson_id, "playing"))
    if playing:
        _run_linked_game(lesson, playing)
        return

    st.title(f"{lesson['icon']} {lesson['label']}")
    st.caption(f"{lesson['level']} · {lesson['topic']} · {lesson['big_idea']}")

    beats = _beats(lesson)
    step = int(st.session_state.get(_key(lesson_id, "step"), 0))
    step = max(0, min(step, len(beats) - 1))
    _progress(lesson, step, len(beats))
    beat = beats[step]
    kind = beat["kind"]
    showing_overlay = False
    if kind in ("name", "change"):
        showing_overlay = bool(
            st.session_state.get(_key(lesson_id, f"{kind}_{step}_pending"))
        )
    if not showing_overlay:
        # Game overlays inject into the parent page and can survive a rerun.
        clear_feedback_overlay()

    if kind == "look":
        scene = beat["scene"]
        st.markdown(f"### {scene['icon']} Look · {scene['title']}")
        _picture(scene)
        st.info(scene["look"])
        _next_button(lesson_id, step)
    elif kind == "name":
        scene = beat["scene"]
        st.markdown(f"### {scene['icon']} Name · {scene['title']}")
        _picture(scene)
        if _ask_and_wait(lesson_id, f"name_{step}", scene["name"]):
            if scene.get("science"):
                st.success(scene["science"])
            _next_button(lesson_id, step, "Next")
    elif kind == "change":
        scene = beat["scene"]
        change = scene["change"]
        st.markdown(f"### {scene['icon']} Change · {scene['title']}")
        _picture(scene, change=True)
        st.info(change["say"])
        if _ask_and_wait(lesson_id, f"change_{step}", change):
            _next_button(lesson_id, step, "Next")
    elif kind == "hands_on":
        st.markdown("### ✋ Try it for real")
        st.write(lesson["hands_on"])
        st.caption("No extra kit. Toys, cups, a window, or getting dressed are enough.")
        _next_button(lesson_id, step, "We tried it")
    else:
        _play_wrap(lesson)

    with st.expander("Grown-up tip"):
        st.write(lesson["grown_up"])
        st.write("Kid words: " + ", ".join(lesson["kid_words"]) + ".")
        if not lesson.get("playable"):
            rank = BUILD_PRIORITY.index(lesson_id) + 1
            st.write(
                f"This lesson runs as a picture script today. "
                f"A full animated scene is build priority {rank} of {len(BUILD_PRIORITY)}."
            )


def _play_wrap(lesson: Lesson) -> None:
    st.markdown("### 🎮 Play the games")
    st.write("The lesson taught the idea. The games let the child try lots of examples.")
    for scene in lesson["scenes"]:
        game = scene["game"]
        label = f"{game['icon']} Play {game['label']}"
        if st.button(label, use_container_width=True, key=_key(lesson["id"], "play_" + game["entry"])):
            st.session_state[_key(lesson["id"], "playing")] = game
            st.rerun()
    if st.button("Start this lesson over", key=_key(lesson["id"], "restart")):
        _reset(lesson["id"])
        st.rerun()


def _run_linked_game(lesson: Lesson, game: dict[str, str]) -> None:
    from pathlib import Path
    import importlib.util
    import sys

    if st.button("← Back to the lesson", key=_key(lesson["id"], "back")):
        st.session_state[_key(lesson["id"], "playing")] = None
        st.rerun()
        return
    st.caption(f"Playing from lesson: {lesson['label']}")
    modules_dir = Path(__file__).resolve().parents[1] / "modules"
    path = modules_dir / game["file"]
    name = "science_playground_lesson_" + path.stem
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    getattr(module, game["entry"])()


def run_lesson_id(lesson_id: str) -> None:
    run_lesson(get_lesson(lesson_id))
