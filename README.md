# Tricksy Battle - A 2-Player Card Game

## Overview
**Tricksy Battle** is a Python implementation of a turn-based 2-player card game where players compete by playing cards from a modified deck. The game is designed to showcase good software design patterns and avoid common antipatterns, as part of a consolidation project.

## How to Run the Game
1. Make sure you have **Python** installed.
To install Python, visit the [Python Downloads](https://www.python.org/downloads)

2. Clone this repository or download the ZIP file and extract it.
3. In your terminal, navigate to the project directory.
4. Run the game using:
```bash
python consolidation.py
```

## Game Rules
- The game uses a 48-card deck (standard deck minus Kings).
- Each player is dealt 8 cards initially.
- Each round:
    - One player leads by playing a card.
    - The second player must follow suit if they can, or play any card otherwise.
    - The highest card in the lead suit wins the round.
- After each round:
    - One card is drawn from the deck and revealed (not used).
    - Winner earns a point and leads the next round.
- When both players have 4 cards left, each gets 4 new cards (twice during the game).
- Game ends after 16 rounds.
- If one player scores 16 and the other 0, it's a "shot the moon" win.