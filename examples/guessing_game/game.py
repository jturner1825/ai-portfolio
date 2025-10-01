import random

class GuessingGame:
    """
    A simple number guessing game.

    The game generates a random number (or accepts a forced number for testing).
    The player guesses until they find the correct number, receiving feedback
    whether their guess is too high, too low, or correct.
    """

    def __init__(self, low: int = 1, high: int = 100, forced_number: int = None):
        """
        Initialize the guessing game.

        Args:
            low (int): The lower bound of the guessing range (inclusive).
            high (int): The upper bound of the guessing range (inclusive).
            forced_number (int, optional): If provided, sets the "random"
                number for predictable testing. Defaults to None.

        Raises:
            ValueError: If low >= high.
        """
        if low >= high:
            raise ValueError("Low must be less than high!")

        self.low = low
        self.high = high
        # Allow ability to set a known number for tests, otherwise randomize
        self.__random_number = forced_number if forced_number is not None else random.randint(low, high)
        self.attempts = 0

    def get_guess(self) -> int:
        """
        Prompt the user for a valid integer guess within the range.

        Returns:
            int: The user's guess.
        """
        while True:
            try:
                guess = int(input(f"Enter a number between {self.low} and {self.high}: "))
                return guess
            except ValueError:
                print("Invalid input! Please enter a valid integer!")

    def check_guess(self, guess: int) -> bool:
        """
        Compare the user's guess with the target number.

        Args:
            guess (int): The number guessed by the user.

        Returns:
            bool: True if the guess is correct, False otherwise.
        """
        if not isinstance(guess, int):
            raise TypeError("Guess must be an integer!")

        self.attempts += 1

        if guess > self.__random_number:
            print("Too high!")
            return False
        elif guess < self.__random_number:
            print("Too low!")
            return False
        else:
            print(f"Correct! You guessed it in {self.attempts} tries!")
            return True

    def play(self):
        """
        Run the main game loop.
        """
        print(f"I'm thinking of a number between {self.low} and {self.high}...")
        while True:
            guess = self.get_guess()
            if self.check_guess(guess):
                break


# Run the game only when this script is executed directly
if __name__ == "__main__":
    game = GuessingGame(1, 100)
    game.play()
