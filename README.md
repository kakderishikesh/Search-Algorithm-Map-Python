# rkakde-a0
Rishikesh Kakde's submission for the first assignment


 Part 1: Searching a map for Path

My program uses Breadth-First Search to find the optimal path to the destination(@)
    Set of Valid States:
        The "valid states" are all the different ways you can put turrets ('p') and empty spaces ('.') on the grid while following the visibility rules.
    Successor Function: 
        The successor function creates new valid states from the current state (castle_map). It accomplishes this by examining all potential locations where a turret ('.') can be positioned and verifying if putting a turret in those spots would meet the visibility rules. This function is denoted as successors(castle_map).
    Cost Function:
        When you go from one state to another, it doesn't really have a "cost." The main goal is to find a good way to arrange the turrets, and we don't think about how much it takes to move between states.
    Goal State Definition:
        The Goal state is determined by a requirement that a certain number of turrets (k) must be placed correctly on the map, and all the visibility rules must be satisfied. We consider the goal state to be achieved when the number of turrets placed matches the value of k. This check is performed in the is_goal(castle_map, k) function.
    Initial State:
        The initial state is the starting configuration of the grid, which is provided as input to the solve function. It represents the map at the beginning before any turrets are placed.

Please note the following points about my code:

1. I have imported heapq module to use priority queues.
2. I updated the Parse_map function. Now, it splits it into lines, and directly creates a 2D list where each character in the file corresponds to a cell in the map. Also, It skips the first 3 lines (assuming they contain metadata) and starts reading the map from the 4th line.
3. The Moves function is updated to use touple of possible moves rather than a list. I also checks if the moves are valid.
4. Search Function: It initializes the start position as current_loc and a fringe with the initial state (current_loc, 0), where 0 represents the current distance. It then enters a loop where it pops the current move and distance from the fringe. It maintains a priority queue (fringe) where each node is a tuple containing the distance, current position, and the path taken so far. It keeps track of visited positions to avoid revisiting them. The search is conducted until the goal is reached or all possible paths are explored. When the goal is reached, it returns a tuple with the number of moves and the move string representing the path.
5. The main function is not changed. It still prints the exact same things and displays output in the desired fashion.

Part 2: Search for Design
The code relies on Depth-First Search (DFS) to explore the different states, and it uses backtracking to navigate and trim unnecessary branches of the search tree. It's a mix of DFS and backtracking working together.
    State Space:
        The state space represents all possible configurations of turrets on a castle map. Each state is a 2D grid where each cell can be one of three values: '.' (Where turret can be palced), 'X' (Where turret cannot be placed, wall), or 'p'(placed turret).
    Initial State:
        The initial state is the starting configuration of the castle map as read from the input file. It contains obstacles ('X') and empty cells ('.').
    Goal State:
        The goal state is achieved when you arrange the turrets on the castle map in a way that satisfies the visibility rules, and you have exactly the specified number of turrets (k), meaning there are precisely k 'p' cells on the map.
    Successor Function:
        The successor function makes new castle maps from the current one by following these steps: First, it finds all the empty spots where you can put turrets. Then, it checks each of these spots to make sure that if you put a turret there, it won't break the visibility rules. If it's okay, it creates a fresh map with a turret in that spot. So basically, the successor function creates all the possible new maps that you can make from the current map without breaking the rules.
    Cost Function:
        We're not really thinking about how much things cost. We're more interested in figuring out the best way to put turrets in the right places without worrying about how hard it is to do each step. The main goal is to get to the final state where we have the right number of turrets and they're all in the right spots according to the rules.


Please note the following points about my code:
1. The code introduces the is_valid_placement function, which checks visibility constraints in eight directions (N, S, E, W, and diagonals) to ensure that placing a turret at a specific position does not violate these constraints.
2. The code uses the successors function to generate valid successors. It checks each empty cell and ensures that placing a turret there is valid according to the visibility constraints defined in is_valid_placement.
3. Solve function: It uses DFS to explore possible turret placements, considering visibility constraints when generating successors. It also returns the result as (new_castle_map, success) instead of a tuple that needs to be indexed for access.
4. The main function is not changed. It prints the results in the desired format.



Sources I have used for this code:
1. Stackoverflow: All my errors I was able to resolve using this website. i could find answers to all my programming queries and the genral github problems i was facing.
2. geeksforgeeks.org: I used to this website to see the implementation of the search algorithms in Python and C++ (I know C++ well, but was not familiar with Python).
