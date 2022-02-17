# 2.Έστω ένα τετράγωνο 3*3 στο οποίο τοποθετείτε “καπάκια”. Έχετε στην κατοχή σας 27 “καπάκια”, 9 για κάθε μέγεθος (μικρό, μεσαίο, μεγάλο). Μια τριάδα που τερματίζει το παιχίνδι γίνεται οριζόντια, κάθετα ή διαγώνια. Η τριάδα αποτελείται από καπάκια είτε του ίδιου μεγέθους είτε από το μικρό προς το μεγαλύτερο. Επειδή έχετε καπάκια, ένα καπάκι μπορεί να μπει σε οποιοδήποτε τετράγωνο, αρκεί να είναι ελεύθερο ή να υπάρχει εκεί μικρότερο καπάκι. Γράψτε ένα πρόγραμμα το οποίο παίζει τυχαία το παιχνίδι 100 φορές και επιστρέφει το μέσο όρο των βημάτων για να λήξει το παιχνίδι.

import random as r

def check_triads(grid):
    flag = False

    # Check Horizontal
    for i in range(len(grid)):
        if grid[i][0] == grid[i][1] and grid[i][1] == grid[i][2] and grid[i][0] > -1:
            flag = True

    # Check Vertical
    for j in range(len(grid)):
        if grid[0][j] == grid[1][j] and grid[1][j] == grid[2][j] and grid[0][j] > -1:
            flag = True

    # Check Diagonal
    if grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2] and grid[1][1] > -1:
        flag = True

    if grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0] and grid[1][1] > -1:
        flag = True

    return flag

step_list = [] # List to collect the steps for each run

for i in range(100): # Run the game 100 times

    # Each cup size has 9 cups
    # Here we represent the sizes as follows
    # Small: 0
    # Medium : 1
    # Large: 2
    cups = {0: 9,
            1: 9,
            2: 9}

    # Instantiate an empty grid
    grid = [[-1 for _ in range(3)] for _ in range(3)]

    # Counter for the steps needed in the run
    steps = 0

    # Initial Game Loop
    while True:
        # Add the new step to the counter
        steps += 1

        # Choose a ranfom cup size
        cup = r.randint(0,2)
        # Check if there are cups left for that size
        while cups[cup] == 0:
            cup = r.randint(0,2)

        # Choose a random tile
        x = r.randint(0,2)
        y = r.randint(0,2)

        # Check if the tile is empty or contains a smaller cup
        if cup > grid[x][y]:
            # Add the cup to the tile
            grid[x][y] = cup
            # Remove the cup from the available cups
            cups[cup] -= 1

        # Check if there are any triads
        if check_triads(grid):
            # Append the steps needed to the list
            step_list.append(steps)
            break

# Print the average number of steps needed
print("The average number of steps needed was:", sum(step_list) / len(step_list))
