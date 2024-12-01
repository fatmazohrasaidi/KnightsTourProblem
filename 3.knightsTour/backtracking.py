from Knight import Knight




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



def backtracking(knight ,csp):
    # Check if the knight has completed all 63 moves (for an 8x8 board)
    if complete(knight.assignment):
        return knight  # Solution found
    
    # Select an unassigned variable
    var = select_unassigned_variable(knight, csp.variables)
    
    for direction in order_domain_values(var, csp.domains):
      
        # Check if the move is consistent with the current path
        if knight.consistent(direction):
            knight.add_move(direction)  # Make the move
            result = backtracking(knight,csp)  # Recur to make the next move
            if result:  # If a solution is found, return it
                return result
            knight.remove_move(direction)  # Backtrack if no solution

    return None  # No solution found



# from csp import CSP
# knight=Knight()
# csp=CSP()
# d=select_unassigned_variable(knight, csp.variables)
# print(d)
# d=select_unassigned_variable(knight, csp.variables)
# print(d)
# print(csp.domains)