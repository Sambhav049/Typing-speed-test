"""
Typing Speed Test
------------------
A terminal-based typing speed test that measures WPM (words per minute)
and accuracy, with difficulty levels and a persistent leaderboard.
"""

import time
import sys

from quotes import get_random_quote
from scores import save_score, print_leaderboard

# ANSI colors for terminal output
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
RESET = "\033[0m"


def countdown(seconds: int = 3) -> None:
    for i in range(seconds, 0, -1):
        print(f"Starting in {i}...", end="\r")
        time.sleep(1)
    print(" " * 20, end="\r")


def diff_highlight(target: str, typed: str) -> str:
    """Return the typed text with correct chars green and wrong chars red."""
    result = []
    for i, ch in enumerate(typed):
        if i < len(target) and ch == target[i]:
            result.append(f"{GREEN}{ch}{RESET}")
        else:
            result.append(f"{RED}{ch}{RESET}")
    return "".join(result)


def calculate_accuracy(target: str, typed: str) -> float:
    if not typed:
        return 0.0
    correct = sum(1 for t, u in zip(target, typed) if t == u)
    return (correct / len(target)) * 100


def calculate_wpm(target: str, elapsed_seconds: float) -> float:
    # Floor elapsed time at 1 second to avoid absurd/divide-by-near-zero WPM
    # values if input is pasted or the timer starts and stops almost instantly.
    elapsed_seconds = max(elapsed_seconds, 1.0)
    words = len(target.split())
    minutes = elapsed_seconds / 60
    return words / minutes


def run_test(difficulty: str) -> tuple:
    quote = get_random_quote(difficulty)

    print(f"\n{BOLD}{CYAN}Type the following text as fast and accurately as you can:{RESET}\n")
    print(f"{YELLOW}{quote}{RESET}\n")
    countdown(3)

    start = time.time()
    typed = input("> ")
    elapsed = time.time() - start

    accuracy = calculate_accuracy(quote, typed)
    wpm = calculate_wpm(quote, elapsed)

    print("\nYour input, highlighted:")
    print(diff_highlight(quote, typed))

    print(f"\n{BOLD}Time:{RESET}     {elapsed:.1f} seconds")
    print(f"{BOLD}WPM:{RESET}       {wpm:.1f}")
    print(f"{BOLD}Accuracy:{RESET}  {accuracy:.1f}%\n")

    return wpm, accuracy, quote


def choose_difficulty() -> str:
    print(f"\n{BOLD}Choose difficulty:{RESET}")
    print("  1. Easy")
    print("  2. Medium")
    print("  3. Hard")
    choice = input("Enter 1, 2, or 3 (default: 2): ").strip()
    return {"1": "easy", "2": "medium", "3": "hard"}.get(choice, "medium")


def main() -> None:
    print(f"{BOLD}{CYAN}=== TYPING SPEED TEST ==={RESET}")
    print("Test your typing speed and accuracy. Press Ctrl+C anytime to quit.\n")

    while True:
        difficulty = choose_difficulty()
        wpm, accuracy, _ = run_test(difficulty)

        name = input("Enter your name to save this score (or press Enter to skip): ").strip()
        if name:
            save_score(name, wpm, accuracy, difficulty)
            print(f"{GREEN}Score saved!{RESET}")

        print_leaderboard()

        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print(f"\n{CYAN}Thanks for playing! Keep practicing.{RESET}")
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}Test interrupted. Goodbye!{RESET}")
        sys.exit(0)
