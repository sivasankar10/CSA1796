from itertools import product
from copy import deepcopy
countries = ["A", "B", "C"]
neighbors = {
    "A": ["B", "C"],
    "B": ["A", "C"],
    "C": ["A", "B"]
}
colors = ["Red", "Green", "Blue"]
assignment = {}
def is_consistent(country, color, assignment):
    for neighbor in neighbors[country]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True
def backtrack(assignment):
    if len(assignment) == len(countries):
        return assignment  # All countries are assigned a color

    unassigned_country = next(iter(countries - assignment.keys()))

    for color in colors:
        if is_consistent(unassigned_country, color, assignment):
            new_assignment = deepcopy(assignment)
            new_assignment[unassigned_country] = color
            result = backtrack(new_assignment)
            if result is not None:
                return result
    return None
solution = backtrack(assignment)
if solution:
    print("Map Coloring Solution:")
    for country, color in solution.items():
        print(f"{country}: {color}")
else:
    print("No solution found.")
