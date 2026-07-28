"""Persistence for typing speed test results (stored as JSON)."""

import json
import os
from datetime import datetime

SCORES_FILE = os.path.join(os.path.dirname(__file__), "scores.json")


def load_scores() -> list:
    if not os.path.exists(SCORES_FILE):
        return []
    try:
        with open(SCORES_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return []


def save_score(name: str, wpm: float, accuracy: float, difficulty: str) -> None:
    scores = load_scores()
    scores.append({
        "name": name,
        "wpm": round(wpm, 1),
        "accuracy": round(accuracy, 1),
        "difficulty": difficulty,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
    })
    # Keep only the top 10 by WPM
    scores.sort(key=lambda s: s["wpm"], reverse=True)
    scores = scores[:10]
    with open(SCORES_FILE, "w") as f:
        json.dump(scores, f, indent=2)


def print_leaderboard() -> None:
    scores = load_scores()
    if not scores:
        print("\nNo scores yet — be the first to set a record!\n")
        return

    print("\n===== LEADERBOARD (Top 10) =====")
    print(f"{'#':<3}{'Name':<15}{'WPM':<10}{'Accuracy':<12}{'Level':<8}{'Date'}")
    print("-" * 65)
    for i, s in enumerate(scores, start=1):
        wpm_str = f"{s['wpm']:.1f}"
        acc_str = f"{s['accuracy']:.1f}%"
        print(f"{i:<3}{s['name']:<15}{wpm_str:<10}{acc_str:<12}{s['difficulty']:<8}{s['date']}")
    print()
