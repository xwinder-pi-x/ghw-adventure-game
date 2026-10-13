# GHW Adventure Game: The Lost Lighthouse

A small command-line choose-your-own-adventure game in Python, built for the MLH Global Hack Week: Hacktoberfest challenge "Use GitHub Copilot to Build a Simple Application".

## Run

```bash
python3 adventure.py
```

Type the number of a choice and press Enter. Find the way to light the beacon to win.

## Test

```bash
pip install pytest
pytest
```

## How it was built

The story is a dictionary of scenes. Each scene has text and numbered choices that point to other scenes; scenes with no choices are endings.

Note: this code was written by hand from the command line. GitHub Copilot was not available in that environment, so Copilot was not used.
