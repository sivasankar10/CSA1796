from itertools import permutations

def solve_cryptarithmetic_puzzle(puzzle):
    letters = set("".join(puzzle))
    if len(letters) != 10:
        return None
    digit_permutations = permutations('0123456789', len(letters))
    for perm in digit_permutations:
        letter_to_digit = dict(zip(letters, perm))
        base_num = int("".join(letter_to_digit[letter] for letter in puzzle[0:4]))
        ball_num = int("".join(letter_to_digit[letter] for letter in puzzle[5:9]))
        games_num = int("".join(letter_to_digit[letter] for letter in puzzle[10:15]))
        if base_num + ball_num == games_num:
            return letter_to_digit
    return None

puzzle = "base + ball = games"
solution = solve_cryptarithmetic_puzzle(puzzle)
if solution:
    print("Solution found:")
    for letter, digit in solution.items():
        print(f"{letter} = {digit}")
else:
    print("No solution found.")
