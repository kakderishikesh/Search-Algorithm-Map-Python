#!/usr/local/bin/python3
#
# place_turrets.py : arrange turrets on a grid, avoiding conflicts
#
# Code by : Rishikesh Kakde (rkakde)


import sys

# Parse the map from a given filename
def parse_map(filename):
    with open(filename, "r") as f:
        return [[char for char in line] for line in f.read().rstrip("\n").split("\n")][3:]

# Count total # of turrets on castle_map
def count_turrets(castle_map):
    return sum([row.count('p') for row in castle_map])

# Return a string with the castle_map rendered in a human-turretly format
def printable_castle_map(castle_map):
    return "\n".join(["".join(row) for row in castle_map])

# Check if placing a turret at (row, col) would violate visibility constraints
def is_valid_placement(castle_map, row, col):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                    (-1, -1), (-1, 1), (1, -1), (1, 1)]

    for dr, dc in directions:
        r, c = row, col
        while 0 <= r < len(castle_map) and 0 <= c < len(castle_map[0]):
            if castle_map[r][c] == 'X':
                break
            if castle_map[r][c] == 'p':
                return False
            r, c = r + dr, c + dc

    return True

# Add a turret to the castle_map at the given position, and return a new castle_map (doesn't change original)
def add_turret(castle_map, row, col):
    return castle_map[0:row] + [castle_map[row][0:col] + ['p', ] + castle_map[row][col + 1:]] + castle_map[row + 1:]

# Get list of valid successors of given castle_map state
def successors(castle_map):
    return [add_turret(castle_map, r, c) for r in range(0, len(castle_map)) for c in range(0, len(castle_map[0]))
            if castle_map[r][c] == '.' and is_valid_placement(castle_map, r, c)]

# check if castle_map is a goal state
def is_goal(castle_map, k):
    return count_turrets(castle_map) == k

# Arrange turrets on the map
#
# This function MUST take two parameters as input -- the castle map and the value k --
# and return a tuple of the form (new_castle_map, success), where:
# - new_castle_map is a new version of the map with k turrets,
# - success is True if a solution was found, and False otherwise.
#It uses DFS to explore possible turret placements, considering visibility constraints when generating successors.
def solve(initial_castle_map, k):
    fringe = [initial_castle_map]
    while len(fringe) > 0:
        for new_castle_map in successors(fringe.pop()):
            if is_goal(new_castle_map, k):
                return new_castle_map, True
            fringe.append(new_castle_map)
    return initial_castle_map, False

# Main Function
if __name__ == "__main__":
    castle_map = parse_map(sys.argv[1])
    # This is k, the number of turrets
    k = int(sys.argv[2])
    print("Starting from initial castle map:\n" + printable_castle_map(castle_map) + "\n\nLooking for solution...\n")
    solution, success = solve(castle_map, k)
    print("Here's what we found:")
    print(printable_castle_map(solution) if success else "False")
