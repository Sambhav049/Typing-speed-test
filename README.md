# Typing-speed-test

# Typing Speed Test

A terminal-based typing speed test written in Python. Measures your
**WPM (words per minute)** and **accuracy**, with three difficulty levels
and a saved leaderboard.

## Features
- Random text prompts across **Easy / Medium / Hard** difficulty
- Live-style highlighted feedback (green = correct, red = wrong)
- WPM and accuracy calculation
- Persistent top-10 leaderboard saved to `scores.json`
- Play multiple rounds in one session

## Requirements
- Python 3.7+ (no external dependencies)

## How to Run
```bash
python3 main.py
```

Then:
1. Choose a difficulty (1 = Easy, 2 = Medium, 3 = Hard)
2. Read the displayed sentence
3. Type it as fast and accurately as you can, then press Enter
4. See your WPM, accuracy, and highlighted results
5. Optionally save your score and check the leaderboard

## Project Structure
```
typing_speed_test/
├── main.py      # Game loop, timing, WPM/accuracy calculation, CLI
├── quotes.py    # Text prompts by difficulty
├── scores.py    # Leaderboard persistence (JSON)
└── README.md
```

## Notes
- WPM is calculated as `(word count / elapsed minutes)`, with elapsed time
  floored at 1 second to avoid unrealistic values from pasted input.
- Accuracy compares your typed text character-by-character against the
  original sentence.
