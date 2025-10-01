"""
test_game.py
------------
A simple test suite for the GuessingGame class using only `assert` statements.

Each test creates a new GuessingGame instance with a forced number
so that the behavior is deterministic. If an assertion fails, Python
will raise an AssertionError.
"""

from game import GuessingGame

tests_run = 0

# -----------------------------
# Test cases
# -----------------------------

# Test 1: Correct number guessed on first try
g = GuessingGame(1, 100, forced_number=50)
assert g.check_guess(50) is True
assert g.attempts == 1
tests_run += 1

# Test 2: Guess too low then correct
g2 = GuessingGame(1, 100, forced_number=50)
assert g2.check_guess(25) is False
assert g2.check_guess(50) is True
assert g2.attempts == 2
tests_run += 1

# Test 3: Too high then correct
g3 = GuessingGame(1, 100, forced_number=30)
assert g3.check_guess(70) is False
assert g3.check_guess(30) is True
assert g3.attempts == 2
tests_run += 1

# Test 4: Non-integer low should raise TypeError
try: 
    GuessingGame("1", 100)
    assert False, "Expected TypeError for non-integer low"
except TypeError:
    tests_run += 1

# Test 5: Non-integer high should raise TypeError
try:
    GuessingGame(1, "100")
    assert False, "Expected TypeError for non-integer high"
except TypeError:
    tests_run += 1

# Test 6: low must be less than high
try:
    GuessingGame(10, 5, forced_number=7)
    assert False, "Expected ValueError when low >= high"
except ValueError:
    tests_run += 1

# Test 7: Guess below the range
g4 = GuessingGame(1, 100, forced_number=42)
result = g4.check_guess(0)
assert result is False
assert g4.attempts == 1
tests_run += 1

# Test 8: Guess above the range
g5 = GuessingGame(1, 100, forced_number=42)
result = g5.check_guess(200)
assert result is False
assert g5.attempts == 1
tests_run += 1

# Test 9: Attempts counter increments every guess
g6 = GuessingGame(1, 100, forced_number=10)
g6.check_guess(1)   # too low
g6.check_guess(20)  # too high
g6.check_guess(10)  # correct
assert g6.attempts == 3
tests_run += 1 

# Test 10: Guess must be integer
g7 = GuessingGame(1, 100, forced_number=42)
try:
    g7.check_guess("12")
    assert False, "Expected TypeError for non-integer guess"
except TypeError:
    tests_run += 1

# Test 11: new game resets attempts
g8 = GuessingGame(1, 100, forced_number=42)
g8.check_guess(10)   # one attempt
assert g8.attempts == 1
# re-initialize
g8.__init__(1, 100, forced_number=50)  
assert g8.attempts == 0
tests_run += 1


# -----------------------------
# Test summary
# -----------------------------
if __name__ == "__main__":
    print(f"{tests_run} tests ran successfully ✅")
