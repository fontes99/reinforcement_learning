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
    
    def find_N(self, v, n):
        for line in range(3):
            for col in range(3):
                if (v[line][col] == n):
                    return line, col 
    
    def sucessors(self):

        sucessors = []
        # print(self.solvable)

        if self.getParity(self.puzzle) == self.getParity(self.goal):
            x, y = self.find_N(self.puzzle, 0)
            
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
        return "Solve an 8-Puzzle"
    
    def cost(self):
        return 1

    def h(self):

        # Sum of manhattan distance for all Ns in puzzle and all Ns in goal
        h = 0

        for n in range(9):
            px, py = self.find_N(self.puzzle, n)
            gx, gy = self.find_N(self.goal, n)

            h += abs(px - gx) + abs(py - gy)
        
        return h

    def print(self):
        return str(self.operator)
    
    def env(self):
        return str([n for line in self.puzzle for n in line])

    def getParity(self, puzzle):
        inv_count = 0
        arr = [j for sub in puzzle for j in sub if j != 0]

        for i in range(1, len(arr)):
            for j in range(i-1, -1, -1):
                if arr[j] <= arr[j+1]: break
                arr[j+1], arr[j] = arr[j], arr[j+1];
                inv_count += 1
                
        return inv_count%2

def main():

    # init_state = [
    #     [8, 1, 3],
    #     [0, 7, 2],
    #     [6, 5, 4]
    # ]

    init_state = [
        [3, 4, 8],
        [1, 2, 5],
        [7, 0, 6]
    ]

    state = Puzzle(init_state, '')
    algorithm = sa.AEstrela()

    print('Buscando...')
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()