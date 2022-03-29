import numpy as np
from copy import deepcopy

goal = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]
]

def find_0(v):
    for line in range(3):
        for col in range(3):
            if (v[line][col] == 0):
                return line, col 

mv = deepcopy(goal)
mv[1][1], mv[0][1] = mv[0][1], mv[1][1]

print(goal)
print(mv)
puz = str([n for line in goal for n in line])
go = str([n for line in goal for n in line])
print(puz == go)