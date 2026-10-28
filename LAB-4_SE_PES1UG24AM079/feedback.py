
def evaluate(target, guess):
    target = target.upper()
    guess = guess.upper()

    if len(target) != len(guess):
        raise ValueError(
            "Target and guess must have the same length."
        )

    result = ["gray"] * len(guess)
    remaining = {}

    # Pass 1: Mark exact matches as green.
    # Count unmatched target letters.
    for i, ch in enumerate(guess):
        if ch == target[i]:
            result[i] = "green"
        else:
            target_letter = target[i]
            remaining[target_letter] = (
                remaining.get(target_letter, 0) + 1
            )

    # Pass 2: Mark misplaced letters as yellow.
    for i, ch in enumerate(guess):
        if result[i] == "green":
            continue

        if remaining.get(ch, 0) > 0:
            result[i] = "yellow"
            remaining[ch] -= 1

    return result
