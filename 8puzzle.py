import numpy as np
import SearchAlgorithms as sa
from Graph import State
from copy import deepcopy

class Puzzle(State):

    def __init__(self, puzzle, op):
        self.operator = op
        self.puzzle = puzzle
        self.goal = [
            [1, 2, 3],
            [8, 0, 4],
            [7, 6, 5]
        ]
    
    def find_0(self, v):
        for line in range(3):
            for col in range(3):
                if (v[line][col] == 0):
                    return line, col 
    
    def sucessors(self):
        sucessors = []
        
        x, y = self.find_0(self.puzzle)
        
        # Move UP
        if x != 0 and self.operator != 'DOWN':

            movUp = deepcopy(self.puzzle)
            movUp[x][y], movUp[x-1][y] = movUp[x-1][y], movUp[x][y]
            
            sucessors.append(Puzzle(movUp, 'UP'))

        # Move DOWN
        if x != 2 and self.operator != 'UP':

            movDown = deepcopy(self.puzzle)
            movDown[x][y], movDown[x+1][y] = movDown[x+1][y], movDown[x][y]
            
            sucessors.append(Puzzle(movDown, 'DOWN'))

        # Move LEFT
        if y != 0 and self.operator != 'RIGHT':

            movLeft = deepcopy(self.puzzle)
            movLeft[x][y], movLeft[x][y-1] = movLeft[x][y-1], movLeft[x][y]
            
            sucessors.append(Puzzle(movLeft, 'LEFT'))

        # Move RIGHT
        if y != 2 and self.operator != 'LEFT':

            movRight = deepcopy(self.puzzle)
            movRight[x][y], movRight[x][y+1] = movRight[x][y+1], movRight[x][y]
            
            sucessors.append(Puzzle(movRight, 'RIGHT'))

        return sucessors
    
    def is_goal(self):
        # puz = str([n for line in self.puzzle for n in line])
        # go = str([n for line in self.goal for n in line])
        return self.puzzle == self.goal

    def description(self):
        return "Resolve an 8 Puzzle"
    
    def cost(self):
        return 1

    def h(self):
        return 1 #implementar manhattan

    def print(self):
        return str(self.operator)
    
    def env(self):
        return str([n for line in self.puzzle for n in line])

# As próximas duas funções foram retiradas de https://www.geeksforgeeks.org/check-instance-8-puzzle-solvable/
# A utility function to count
# inversions in given array 'arr[]'
def getInvCount(arr):
    inv_count = 0
    empty_value = -1
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
                inv_count += 1
    return inv_count

# This function returns true
# if given 8 puzzle is solvable.
def isSolvable(puzzle) :
 
    # Count inversions in given 8 puzzle
    inv_count = getInvCount([j for sub in puzzle for j in sub])
 
    # return true if inversion count is even.
    return (inv_count % 2 == 0)

def main():

    init_state = [
        [8, 1, 3],
        [0, 7, 2],
        [6, 5, 4]
    ]

    if isSolvable(init_state):
            
        state = Puzzle(init_state, '')
        algorithm = sa.AEstrela()

        print('Buscando...')
        result = algorithm.search(state)
        if result != None:
            print('Achou!')
            print(result.show_path())
        else:
            print('Nao achou solucao')
    else:
        print('Puzzle impossível')

if __name__ == '__main__':
    main()