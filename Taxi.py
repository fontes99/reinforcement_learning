import SearchAlgorithms as sa
from Graph import State
import gym

class MeuTaxi(State):

    def __init__(self, desc, state, coords, op):

        self.coords = coords

        self.operator = op

        self.s = state
        
        self.taxi_row, self.taxi_col, self.pass_idx, self.dest_idx = self.s
        
        self.taxi_col_r = (self.taxi_col*2)
        self.desc = desc

        self.loc = {
            0 : 'R',
            1 : 'G',
            2 : 'Y',
            3 : 'B',
            4 : None
        }
        
    def sucessors(self):
        sucessors = []

        # actions:
        # 0 = south
        # 1 = north
        # 2 = east
        # 3 = west
        # 4 = pickup
        # 5 = dropoff
        
        #go south = está fora da ultima linha
        if self.taxi_row < len(self.desc)-1:
            sucessors.append(MeuTaxi(self.desc, [self.taxi_row+1, self.taxi_col, self.pass_idx, self.dest_idx], self.coords, '0'))

        #go north = está fora da primeira linha
        if self.taxi_row > 0:
            sucessors.append(MeuTaxi(self.desc, [self.taxi_row-1, self.taxi_col, self.pass_idx, self.dest_idx], self.coords, '1'))
        
        #go east = esta fora da ultima coluna && a casa da esquerda == ':'
        if self.taxi_col_r < len(self.desc[0])-1:
            if self.desc[self.taxi_row][self.taxi_col_r+1] != '|':
                sucessors.append(MeuTaxi(self.desc, [self.taxi_row, self.taxi_col+1, self.pass_idx, self.dest_idx], self.coords, '2'))
        
        #go west = esta fora da primeira coluna && a casa da direita == ':'
        if self.taxi_col_r > 0:
            if self.desc[self.taxi_row][self.taxi_col_r-1] != '|':
                sucessors.append(MeuTaxi(self.desc, [self.taxi_row, self.taxi_col-1, self.pass_idx, self.dest_idx], self.coords, '3'))
        
        if self.loc[self.pass_idx] == self.desc[self.taxi_row][self.taxi_col_r] :
            sucessors.append(MeuTaxi(self.desc, [self.taxi_row, self.taxi_col, 4, self.dest_idx], self.coords, '4'))

        if self.loc[self.dest_idx] == self.desc[self.taxi_row][self.taxi_col_r]  and self.pass_idx == 4:
            sucessors.append(MeuTaxi(self.desc, [self.taxi_row, self.taxi_col, self.dest_idx, self.dest_idx], self.coords, '5'))
        

        return sucessors
    
    def is_goal(self):
        return self.pass_idx == self.dest_idx
    
    def description(self):
        return "Describe the problem"
    
    def cost(self):
        return 1

    def print(self):
        return str(self.operator)

    def path(self):

        algorithm = sa.AEstrela()
        result = algorithm.search(self)

        if result != None:
            path_raw = result.show_path()
            path = [int(i) for i in path_raw if i.isalnum()]
            return path

        else:
            print('Nao achou solucao')
            return result

    
    def env(self):
        return str(self.s)

    def h(self):

        if self.loc[self.pass_idx] != None:
            dist = ((self.coords[self.loc[self.pass_idx]][0]-self.taxi_row)**2 + (self.coords[self.loc[self.pass_idx]][1]-self.taxi_col)**2)**(1/2)
        else:
            dist = ((self.coords[self.loc[self.dest_idx]][0]-self.taxi_row)**2 + (self.coords[self.loc[self.dest_idx]][1]-self.taxi_col)**2)**(1/2)

        return dist

def makeMap(desc):
    city = []
    coords = {}

    for idx_row, row in enumerate(desc):
        new_row = []
        coords = {}
        
        if idx_row in [0, (len(desc)-1)]:
            continue
        
        for idx_col, item in enumerate(row):
            
            if idx_col in [0, len(row)-1]:
                continue
            
            new_row.append(item.decode("utf-8"))
        
        city.append(new_row)

    for idx_row, row in enumerate(city):
        for idx_col, item in enumerate(row):
            if item.isalpha():
                coords[item] = (idx_row, idx_col/2)

    return city, coords


def main():

    env = gym.make("Taxi-v3").env
    state = env.reset()
    env.render()

    city, coords = makeMap(env.desc)

    taxi = MeuTaxi(city, env.decode(state), coords, '')    

    for a in taxi.path():
        state, reward, done, info = env.step(a)
        env.render()

    if done:
        print("\nSoube encontrar a solucao correta")
        print(taxi.path())

    else:
        print("\nNão soube encontrar a solução")


if __name__ == '__main__':
    main()