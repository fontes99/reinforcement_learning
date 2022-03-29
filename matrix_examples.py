import numpy as np
from copy import deepcopy

def find_N(v, n):
    for line in range(3):
        for col in range(3):
            if (v[line][col] == n):
                return line, col

goal = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]
]

init_state = [
    [8, 1, 3],
    [0, 7, 2],
    [6, 5, 4]
]

h = 0

for n in range(9):
    px, py = find_N(init_state, n)
    gx, gy = find_N(goal, n)

    h += abs(px - gx) + abs(py - gy)

print(h)