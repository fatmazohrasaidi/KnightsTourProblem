from csp import CSP

class Knight:
    def __init__(self):
        self.position = (0, 0)  # Starting position at (0, 0)
        self.assignment = []  # Sequence of moves (this can be used to track move sequence)
        self.path = [(0, 0)]  # Initial position saved in the path

    def move_forward(self, direction):
        # All possible knight moves (8 in total)
        moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
                 (-2, -1), (-1, -2), (1, -2), (2, -1)]
        dx, dy = moves[direction]
        return self.position[0] + dx, self.position[1] + dy

    def move_backward(self, direction):
        # Reverse knight's moves for backtracking
        moves = [(-2, -1), (-1, -2), (1, -2), (2, -1),
                 (2, 1), (1, 2), (-1, 2), (-2, 1)]
        dx, dy = moves[direction]
        return self.position[0] + dx, self.position[1] + dy

    def consistent(self, direction, constraints):
        """Checks if a move is consistent with the knight's current path"""
        new_position = self.move_forward(direction)
        # Check if the move is within bounds and not already visited
        return 0 <= new_position[0] < 8 and 0 <= new_position[1] < 8 and new_position not in self.path

    def add_move(self, direction):
        """Add a move to the path and update position"""
        self.assignment.append(direction)
        self.position = self.move_forward(direction)
        self.path.append(self.position)

    def remove_move(self, direction):
        """Remove a move from the path and backtrack"""
        self.assignment.pop()
        self.position = self.move_backward(direction)
        self.path.pop()

