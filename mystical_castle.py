#!/usr/local/bin/python3
#
# mystical_castle.py : a maze solver
#
# Code by : Rishikesh Kakde (rkakde)

import sys
import heapq

# Parse the map from a given filename
def parse_map(filename):
        with open(filename, "r") as f:
                lines = f.read().splitlines()
                map_data = lines[4:]  # Skip the first 4 lines (metadata)
                return [list(line) for line in map_data]
                
# Check if a row,col index pair is on the map
def valid_index(pos, n, m):
        return 0 <= pos[0] < n and 0 <= pos[1] < m

# Find the possible moves from position (row, col)
def moves(castle_map, row, col):
        moves = [(row + 1, col), (row - 1, col), (row, col - 1), (row, col + 1)]

        # Return only moves that are within the castle_map and legal (i.e. go through open space ".")
        return [move for move in moves if valid_index(move, len(castle_map), len(castle_map[0])) and (castle_map[move[0]][move[1]] in ".@")]

# Perform search on the map
#
# This function MUST take a single parameter as input -- the castle map --
# and return a tuple of the form (move_count, move_string), where:
# - move_count is the number of moves required to navigate from start to finish, or -1
#    if no such route exists
# - move_string is a string indicating the path, consisting of U, L, R, and D characters
#    (for up, left, right, and down)
#It initializes the start position as current_loc and a fringe with the initial state (current_loc, 0), where 0 represents the current distance.
#It then enters a loop where it pops the current move and distance from the fringe.
#It maintains a priority queue (fringe) where each node is a tuple containing the distance, current position, and the path taken so far.
#It keeps track of visited positions to avoid revisiting them. The search is conducted until the goal is reached or all possible paths are explored.
#When the goal is reached, it returns a tuple with the number of moves and the move string representing the path.
def search(castle_map):
        start = [(row_i, col_i) for col_i in range(len(castle_map[0])) for row_i in range(len(castle_map)) if castle_map[row_i][col_i] == "p"][0]
        fringe = [(0, start, "")]
        visited = set()

        while fringe:
                (curr_dist, curr_pos, curr_path) = heapq.heappop(fringe)

                if castle_map[curr_pos[0]][curr_pos[1]] == "@":
                        return (curr_dist, curr_path)

                if curr_pos in visited:
                        continue

                visited.add(curr_pos)

                for move in moves(castle_map, *curr_pos):
                        new_dist = curr_dist + 1
                        new_path = curr_path + move_direction(curr_pos, move)
                        heapq.heappush(fringe, (new_dist, move, new_path))

        return (-1, "")

def move_direction(start, end):
        if start[0] < end[0]:
                return 'D'
        elif start[0] > end[0]:
                return 'U'
        elif start[1] < end[1]:
                return 'R'
        else:
                return 'L'

# Main Function
if __name__ == "__main__":
        castle_map=parse_map(sys.argv[1])
        print("Shhhh... quiet while I navigate!")
        solution = search(castle_map)
        print("Here's the solution I found:")
        print(str(solution[0]) + " " + solution[1])

