from Knight import Knight
from backtracking import backtracking
from csp import CSP

import visualize

def main():
    knight = Knight()  # Create a new Knight
    csp=CSP()
    solution = backtracking(knight,csp)  # Run the backtracking algorithm

    if solution:
        print("Knight's Assignment (Moves):", solution.assignment)
        print("Knight's Path:", solution.path)
        chessboard_img = "chessboard.png"  # Path to your chessboard image (800x800 pixels)
        knight_img = "knight.png" 
        visualize.visualize_knights_tour(chessboard_img, knight_img, knight.path, delay=0.5)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
