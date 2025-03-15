from Knight import Knight

def select_mrv(knight):
    """Select the next move based on the MRV heuristic."""
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
             (-2, -1), (-1, -2), (1, -2), (2, -1)]
    
    mrv_values = []  # List to store (onward moves, direction) tuples

    for direction in range(len(moves)):
        next_position = knight.move_forward(direction)

        # Check if the move is valid and not already visited
        if next_position not in knight.path and 0 <= next_position[0] < 8 and 0 <= next_position[1] < 8:
            onward_moves = 0
            for dx, dy in moves:
                new_x, new_y = next_position[0] + dx, next_position[1] + dy
                if (0 <= new_x < 8 and 0 <= new_y < 8 and 
                        (new_x, new_y) not in knight.path):
                    onward_moves += 1
            mrv_values.append((onward_moves, direction))

    # Sort by the number of onward moves (ascending)
    mrv_values.sort(key=lambda x: x[0])

    # Return the directions in MRV order
    return [direction for _, direction in mrv_values]


def select_unassigned_variable(knight, variables):
    for var in variables:
        if var not in knight.path:  # Check if the variable is not yet assigned
            return var
    return None  # No unassigned variables remain
def order_domain_values(var, domains):
    return domains  # Return all values in the domain of var

def complete(assignment):
    if len(assignment) == 63:
        return True
    else:
        return False

#optimized
def backtracking(knight ,csp):
    # Check if the knight has completed all 63 moves (for an 8x8 board)
    if complete(knight.assignment):
        return knight  # Solution found
    
    # Select an unassigned variable
    var = select_unassigned_variable(knight, csp.variables)
    
    for direction in select_mrv(knight):
      
        # Check if the move is consistent with the current path
        if knight.consistent(direction, csp.constraints ):
            knight.add_move(direction)  # Make the move
            result = backtracking(knight,csp)  # Recur to make the next move
            if result:  # If a solution is found, return it
                return result
            knight.remove_move(direction)  # Backtrack if no solution

    return None  # No solution found



# def backtracking(knight ,csp):
#     # Check if the knight has completed all 63 moves (for an 8x8 board)
#     if complete(knight.assignment):
#         return knight  # Solution found
    
#     # Select an unassigned variable
#     var = select_unassigned_variable(knight, csp.variables)
    
#     for direction in order_domain_values(var, csp.domains):
      
#         # Check if the move is consistent with the current path
#         if knight.consistent(direction):
#             knight.add_move(direction)  # Make the move
#             result = backtracking(knight,csp)  # Recur to make the next move
#             if result:  # If a solution is found, return it
#                 return result
#             knight.remove_move(direction)  # Backtrack if no solution

#     return None  # No solution found



# from csp import CSP
# knight=Knight()
# csp=CSP()
# d=select_unassigned_variable(knight, csp.variables)
# print(d)
# d=select_unassigned_variable(knight, csp.variables)
# print(d)
# print(csp.domains)