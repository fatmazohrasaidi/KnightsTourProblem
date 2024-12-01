from collections import deque


class CSP:
    def __init__(self, board_size=8):
        self.board_size = board_size
        self.variables = [(i, j) for i in range(board_size) for j in range(board_size)]
        
        # Domain: Each variable's domain should be a list containing numbers from 0 to 7
        self.domains = list(range(8))
        # Constraints: A function that checks if a knight's move is valid
        self.constraints = self.is_legal_move

    def is_legal_move(self, next_position, path):
        """Check if a knight's move is valid (not off the board and not revisiting a square)."""
        # Check if next position is within bounds and hasn't been visited
        if next_position in path:
            return False
        else: 
            x, y = next_position
            if 0 <= x < self.board_size-1 and 0 <= y < self.board_size-1:
                return True
            else:
                return False
    




# A = CSP()
# print(A.board_size)         # Output: 8
# print(A.variables)          # Output: List of all positions on the board
# print('domains',A.domains)            # Output: Dictionary with positions as keys and valid moves as values
# print(A.constraints)        # Output: List with the knight move constraint function
