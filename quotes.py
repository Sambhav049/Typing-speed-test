"""Text prompts used by the typing speed test, grouped by difficulty."""

import random

QUOTES = {
    "easy": [
        "The quick brown fox jumps over the lazy dog.",
        "A journey of a thousand miles begins with a single step.",
        "Practice makes perfect when you keep trying every day.",
        "She sells seashells by the seashore every summer.",
        "Coding every day helps you learn something new.",
    ],
    "medium": [
        "Success is not final, failure is not fatal, it is the courage to continue that counts.",
        "The only way to do great work is to love what you do and never stop improving.",
        "Programming is the art of telling another human being what one wants the computer to do.",
        "In the middle of difficulty lies opportunity, so keep your eyes open for it.",
        "Simplicity is the soul of efficiency, and clarity is the key to good design.",
    ],
    "hard": [
        "The greatest glory in living lies not in never falling, but in rising every time we fall, "
        "no matter how many times it takes to get back up.",
        "Artificial intelligence, machine learning, and computer vision are transforming the way "
        "software interacts with the physical world around us.",
        "It is not the strongest of the species that survives, nor the most intelligent, but the "
        "one most responsive to change and adaptation.",
        "Whether you think you can or you think you can't, you're probably right, because belief "
        "shapes the effort you're willing to put in.",
        "The function of good software is to make the complex appear to be simple, hiding the "
        "messy details behind a clean and intuitive interface.",
    ],
}


def get_random_quote(difficulty: str = "medium") -> str:
    """Return a random quote for the given difficulty level."""
    difficulty = difficulty.lower()
    pool = QUOTES.get(difficulty, QUOTES["medium"])
    return random.choice(pool)
