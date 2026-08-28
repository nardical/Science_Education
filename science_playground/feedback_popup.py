"""Correct / Nice try overlay shared by every science game."""
from __future__ import annotations

import streamlit.components.v1 as components

OVERLAY_ID = "science-playground-feedback"
DEFAULT_AUTO_CLEAR_MS = 2500


def _escape(text: str) -> str:
    return (
        text.replace("\\", "\\\\")
        .replace("`", "\\`")
        .replace("$", "\\$")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace("\n", "<br>")
    )


def clear_feedback_overlay() -> None:
    """Remove a leftover popup from the parent page."""
    components.html(
        f"""
        <script>
        (function () {{
          const old = parent.document.getElementById("{OVERLAY_ID}");
          if (old) old.remove();
        }})();
        </script>
        """,
        height=1,
    )


def show_feedback_overlay(
    message: str,
    was_correct: bool,
    detail: str = "",
    auto_clear_ms: int = DEFAULT_AUTO_CLEAR_MS,
) -> None:
    """Draw a viewport overlay. Call this during a render that stays up ~2–3s."""
    bg, border = ("#d8f3dc", "#2A9D8F") if was_correct else ("#fff3cd", "#D62828")
    safe_message = _escape(message)
    detail_html = ""
    if detail:
        detail_html = (
            f'<div style="font-size:1.25rem;margin-top:.8rem;font-weight:700;'
            f'line-height:1.35">{_escape(detail)}</div>'
        )
    components.html(
        f"""
        <script>
        (function () {{
          const id = "{OVERLAY_ID}";
          const old = parent.document.getElementById(id);
          if (old) old.remove();
          const o = parent.document.createElement("div");
          o.id = id;
          o.style.cssText = [
            "position:fixed",
            "inset:0",
            "z-index:2147483647",
            "display:flex",
            "align-items:center",
            "justify-content:center",
            "background:rgba(43,43,43,.28)",
            "pointer-events:none",
          ].join(";");
          o.innerHTML = `<div style="background:{bg};border:5px solid {border};border-radius:28px;padding:2rem 2.75rem;font:800 2.1rem system-ui,Segoe UI,sans-serif;color:#2b2b2b;text-align:center;box-shadow:0 16px 48px #0004;max-width:min(85vw,32rem)">{safe_message}{detail_html}</div>`;
          parent.document.body.appendChild(o);
          setTimeout(function () {{
            const node = parent.document.getElementById(id);
            if (node) node.remove();
          }}, {int(auto_clear_ms)});
        }})();
        </script>
        """,
        height=1,
    )
