import numpy as np


unique_digits = []

solved_puzzle = "534678912\
672195348\
198342567\
859761423\
426853791\
713924856\
961537284\
287419635\
345286179".replace('\n', '')

puzzle_array = np.array([int(i) for i in solved_puzzle]).reshape([9, 9])

# Checks for duplicate values in rows and columns
for i in range(0,9):
    unique_digits.append(len(set(puzzle_array[i])))
    unique_digits.append(len(set(puzzle_array[:, i])))

# Checks for duplicate values in grid regions
for i in range(0,3):
    unique_digits.append(len(set(puzzle_array[0:3, 0 + (3 * i):3 + (3 * i)].flatten())))
    unique_digits.append(len(set(puzzle_array[3:6, 0 + (3 * i):3 + (3 * i)].flatten())))
    unique_digits.append(len(set(puzzle_array[6:9, 0 + (3 * i):3 + (3 * i)].flatten())))

# Checks if the grid solution is correct
if set(unique_digits) != {9}:
    print("Wrong answer!")
else:
    print("Right answer!")

