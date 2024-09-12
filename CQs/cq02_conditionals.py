""""Practice with Conditionals, Local Variables, and User Input"""

__author__ = "730474650"


def guess_a_number() -> None:
    """Signature function will be displayed in the terminal"""


secret: int = 7  # This is the secret number the player will guess


guess = int(input("Guess a number:"))
print(f"Your guess was {guess}.")
if guess == secret:
    print("You got it!")
elif guess < secret:
    print(f"Your guess was too low! The secret number is {secret}.")
else:
    print(f"Your guess was too high! The secret number is {secret}.")

if __name__ == "__main__":
    guess_a_number()
