# Science Playground

Playful, picture-first STEM games for advanced 5–6 year olds. Physics leads, engineering is woven in, and matter, living things, and gentle computing round out the playground.

## Run

```powershell
python -m pip install -r requirements.txt
streamlit run science_playground/app.py
```

Or double-click `start-game.bat` on Windows. That script stops any leftover game still using port 8501, then starts a fresh one. If a browser tab is already on http://localhost:8501, press Ctrl+Shift+R or open a new tab.

## What is included

- 7 topics
- Beginner, Intermediate, and Advanced levels
- 3 playable games per topic per level (63 games total)
- Deterministic tap choices, large SVG scenes, and 2.4-second feedback overlays
- Grown-up tips for every game
- 21 guided lessons (one per topic per level): Look → Name → Play
- Waves 1 and 2 are picture-first (all 7 beginner topics plus Intermediate Motion)

See `science_playground/lessons/README.md` for the full map and what to draw next.
