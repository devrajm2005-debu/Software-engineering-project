
from game import WordleGame


def main():
    print("=== WORDLE ===")
    print("1. 4-letter mode")
    print("2. 5-letter mode")
    print("3. 6-letter mode")

    modes = {"1": 4, "2": 5, "3": 6}

    while True:
        choice = input("Choose a mode (1/2/3): ").strip()

        if choice in modes:
            WordleGame(length=modes[choice]).run()
            break

        print("Invalid choice. Enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
