"""EX03 - Structured Wordle"""

__author__ = "730474650"


def contains_char(search_string: str, char: str) -> bool:
    """Checks if a single character is present in the given string."""
    assert len(char) == 1, f"len ('{char}') is not 1"
    for current_char in search_string:
        if current_char == char:
            return True
    return False


def emojified(guess: str, secret: str) -> str:
    """Returns a string of emojis indicating the accuracy of the guess."""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    assert len(guess) == len(secret), "Guess must be same length as secret."
    result = ""
    index = 0

    while index < len(guess):
        if guess[index] == secret[index]:
            result += GREEN_BOX
        elif contains_char(secret, guess[index]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        index += 1

    return result


def input_guess(correct_length: int) -> str:
    """Prompts the user for a guess of the correct length."""
    while True:
        user_guess = input(f"Enter a {correct_length} character word: ")
        if len(user_guess) == correct_length:
            return user_guess
        else:
            print(f"That wasn't {correct_length} chars! Try again:")


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    max_turns: int = 6
    current_turn = 1

    while current_turn <= max_turns:
        print(f" === Turn {current_turn}/{max_turns} ===")

        user_guess = input_guess(len(secret))
        result_emoji = emojified(user_guess, secret)
        print("Result:", result_emoji)

        if user_guess == secret:
            print(f"You won in {current_turn}/{max_turns} turns!")
            return
        current_turn += 1

    print(f"X/{max_turns} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
