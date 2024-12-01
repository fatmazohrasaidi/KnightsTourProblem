import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import time

def visualize_knights_tour(chessboard_img, knight_img, path, delay=0.5):
    """
    Visualize the Knight's Tour with images and numbers.
    
    Args:
        chessboard_img (str): Path to the chessboard image (800x800 pixels).
        knight_img (str): Path to the knight image (100x100 pixels).
        path (list): List of positions in the Knight's Tour (e.g., [(0, 0), (2, 1), ...]).
        delay (float): Time delay between moves (in seconds).
    """
    # Load chessboard and knight images
    chessboard = mpimg.imread(chessboard_img)
    knight = Image.open(knight_img)
    
    # Resize knight to fit within a single square (100x100 pixels)
    knight = knight.resize((100, 100))
    knight = mpimg.pil_to_array(knight)

    # Set up the plot
    fig, ax = plt.subplots(figsize=(8, 8))  # 800x800 pixels, 8x8 grid
    ax.imshow(chessboard, extent=[0, 8, 0, 8])  # Set chessboard as background

    # Track visited squares and move the knight
    for step, (x, y) in enumerate(path):
        # Clear previous knight positions
        ax.clear()
        ax.imshow(chessboard, extent=[0, 8, 0, 8])  # Redraw the chessboard
        
        # Add all visited square numbers
        for prev_step, (px, py) in enumerate(path[:step + 1]):
            ax.text(px + 0.5, 7.5 - py, str(prev_step + 1), color="black", 
                    ha="center", va="center", fontsize=15, weight="bold")
        
        # Place the knight at the current position
        ax.imshow(knight, extent=[x, x + 1, 7 - y, 8 - y])  # Flip the y-axis
        
        # Customize grid and labels
        ax.set_xticks(range(9))
        ax.set_yticks(range(9))
        ax.grid(True, color="black", linestyle="-", linewidth=0.5)
        ax.set_xlim(0, 8)
        ax.set_ylim(0, 8)
        
        # Display the plot
        plt.pause(delay)  # Pause to create an animation effect
    
    # Keep the final state displayed
    plt.show()



