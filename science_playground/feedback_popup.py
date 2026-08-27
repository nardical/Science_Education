"""Correct / Nice try overlay shared by every science game."""
from __future__ import annotations
import streamlit.components.v1 as components

def show_feedback_overlay(message: str, was_correct: bool, detail: str = "") -> None:
    bg, border = ("#d8f3dc", "#2A9D8F") if was_correct else ("#fff3cd", "#D62828")
    safe = lambda s: s.replace("\\", "\\\\").replace("`", "\\`").replace("$", "\\$").replace("<", "&lt;").replace(">", "&gt;")
    components.html(f"""
    <script>(function(){{
      const id="science-playground-feedback"; const old=parent.document.getElementById(id); if(old) old.remove();
      const o=parent.document.createElement("div"); o.id=id;
      o.style.cssText="position:fixed;inset:0;z-index:2147483647;display:flex;align-items:center;justify-content:center;background:rgba(43,43,43,.28);pointer-events:none";
      o.innerHTML=`<div style="background:{bg};border:5px solid {border};border-radius:28px;padding:2rem 2.75rem;font:800 2.1rem system-ui;color:#2b2b2b;text-align:center;box-shadow:0 16px 48px #0004;max-width:85vw">{safe(message)}<div style="font-size:1.25rem;margin-top:.8rem">{safe(detail)}</div></div>`;
      parent.document.body.appendChild(o); setTimeout(()=>o.remove(),2400);
    }})();</script>""", height=1)
