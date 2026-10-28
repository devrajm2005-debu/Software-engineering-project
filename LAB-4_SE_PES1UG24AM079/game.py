
import random
from words import WORDS
from feedback import evaluate


class WordleGame:
    def __init__(self, length=5, max_guesses=6):
        if length not in (4, 5, 6):
            raise ValueError("Word length must be 4, 5, or 6.")

        self.length = length
        self.max_guesses = max_guesses

        available_words = [
            word.lower()
            for word in WORDS
            if len(word) == length and word.isalpha()
        ]

        if not available_words:
            raise ValueError(
                f"No {length}-letter words available in WORDS."
            )

        self.target = random.choice(available_words)
        self.history = []

    def display_history(self):
        """Display all accepted guesses and their feedback."""
        print("\n--- Guess History ---")

        if not self.history:
            print("No guesses recorded yet.")
            return

        for number, (guess, feedback) in enumerate(
            self.history, start=1
        ):
            print(
                f"{number}. {guess.upper()} | "
                f"{' '.join(feedback)}"
            )

    def display_summary(self, result):
        """Display the final session summary."""
        print("\n=== Session Summary ===")
        print(f"Word length: {self.length} letters")
        print(f"Guesses used: {len(self.history)}/{self.max_guesses}")
        print(f"Result: {result}")
        print(f"Secret word: {self.target.upper()}")

        self.display_history()
        print("=======================\n")

    def run(self):
        print(
            f"Wordle — {self.length} letters, "
            f"{self.max_guesses} guesses."
        )
        print("Enter 'q' at any time to quit.")

        while len(self.history) < self.max_guesses:
            guess = input("> ").strip().lower()

            # Quitting does not consume a guess.
            if guess == "q":
                print("Game ended.")
                self.display_summary("Quit")
                return

            # Invalid attempts must not enter history.
            if len(guess) != self.length or not guess.isalpha():
                print(
                    f"Enter a valid {self.length}-letter word "
                    "using letters only."
                )
                continue

            # Record only accepted guesses.
            feedback = evaluate(self.target, guess)
            self.history.append((guess, feedback))

            print(f"Feedback: {' '.join(feedback)}")

            # Display the history after every accepted guess.
            self.display_history()

            print(
                f"Guesses used: {len(self.history)}/"
                f"{self.max_guesses}"
            )

            if guess == self.target:
                print(
                    f"You win! Solved in "
                    f"{len(self.history)} guess(es)."
                )
                self.display_summary("Won")
                return

        print("Game over! You used all your guesses.")
        self.display_summary("Lost")


if __name__ == "__main__":
    WordleGame().run()
