import random
import string
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

def generate_word_search(size, words):
    # Create an empty grid
    grid = [[' ' for _ in range(size)] for _ in range(size)]
    
    # Fill the grid with random letters
    for i in range(size):
        for j in range(size):
            if grid[i][j] == ' ':
                grid[i][j] = random.choice(string.ascii_uppercase)
    
    # Place words in the grid
    for word in words:
        placed = False
        while not placed:
            # Choose a random starting position and direction
            start_row = random.randint(0, size-1)
            start_col = random.randint(0, size-1)
            direction = random.choice([(0, 1), (1, 0), (1, 1)])
            
            # Check if the word can fit in the chosen direction
            end_row = start_row + direction[0] * (len(word) - 1)
            end_col = start_col + direction[1] * (len(word) - 1)
            if 0 <= end_row < size and 0 <= end_col < size:
                placed = True
                # Place the word in the grid
                for i in range(len(word)):
                    row = start_row + direction[0] * i
                    col = start_col + direction[1] * i
                    grid[row][col] = word[i]
    
    return grid

def display_word_search(grid):
    size = len(grid)
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_axis_off()
    ax.set_facecolor('lightgray')  # Set background color
    
    table = ax.table(cellText=grid, loc='center', cellLoc='center', edges='closed')
    
    # Set cell dimensions to be square
    cell_width = 1.0 / size
    cell_height = 1.0 / size
    for i in range(size):
        for j in range(size):
            cell = table[i, j]
            cell.set_width(cell_width)
            cell.set_height(cell_height)
    
    # Increase font size
    table.auto_set_font_size(False)
    table.set_fontsize(14)
    
    # Add legend
    legend_elements = [Patch(facecolor='lightgray', edgecolor='black', label=word) for word in word_list]
    legend = ax.legend(handles=legend_elements, loc='center', bbox_to_anchor=(0.5, -0.1), ncol=len(word_list))
    legend.get_frame().set_facecolor('lightgray')
    legend.get_frame().set_edgecolor('black')
    legend.get_frame().set_linewidth(1.0)
    legend.get_frame().set_alpha(0.7)
    
    plt.show()

# Example usage
word_list = ['GITHUB', 'CODE', 'PYTHON']
word_search = generate_word_search(15, word_list)
display_word_search(word_search)
