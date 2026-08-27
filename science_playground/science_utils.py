"""Shared visual and interaction engine for Science Playground."""
from __future__ import annotations
import html
import streamlit as st
from feedback_popup import show_feedback_overlay

def inject_form_css() -> None:
    st.markdown("""<style>
    div[data-testid="stHorizontalBlock"] button {min-height:4.2rem;font-size:1.25rem;font-weight:750;border-radius:18px}
    .science-card{background:linear-gradient(135deg,#e9f8ff,#fff7dd);border:3px solid #79b9d1;border-radius:24px;padding:1rem;text-align:center}
    </style>""", unsafe_allow_html=True)

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

def run_game(spec: dict) -> None:
    inject_form_css()
    key = "science_" + spec["id"]
    started = st.session_state.get(key + "_started", False)
    round_no = st.session_state.get(key + "_round", 0)
    st.title(spec["picture"] + " " + spec["title"])
    st.caption(spec["tagline"])
    if not started:
        st.markdown(scene_svg(spec["picture"], 0), unsafe_allow_html=True)
        if st.button("▶️ Play", use_container_width=True, key=key+"_play"):
            st.session_state[key+"_started"] = True
            st.rerun()
        with st.expander("Grown-up tip"):
            st.write(spec["tip"])
        return
    st.markdown(scene_svg(spec["picture"], round_no), unsafe_allow_html=True)
    st.subheader(spec["question"])
    choices = list(spec["choices"])
    # Rotate positions each round without randomness or trick scoring.
    shift = round_no % len(choices)
    choices = choices[shift:] + choices[:shift]
    cols = st.columns(len(choices))
    for col, choice in zip(cols, choices):
        if col.button(choice, use_container_width=True, key=f"{key}_{round_no}_{choice}"):
            correct = choice == spec["answer"]
            show_feedback_overlay("Correct! 🌟" if correct else "Nice try! 💛", correct, spec["tip"])
            st.session_state[key+"_round"] = round_no + 1
            st.rerun()
    with st.expander("Grown-up tip"):
        st.write(spec["tip"])
