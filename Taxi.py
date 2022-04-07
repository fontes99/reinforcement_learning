import SearchAlgorithms as sa
from Graph import State
import gym

class MeuTaxi(State):

    def __init__(self, desc, state, op):

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
        if self.taxi_row < 4:
            sucessors.append(MeuTaxi(self.desc, [self.taxi_row+1, self.taxi_col, self.pass_idx, self.dest_idx], '0'))

        #go north = está fora da primeira linha
        if self.taxi_row > 0:
            sucessors.append(MeuTaxi(self.desc, [self.taxi_row-1, self.taxi_col, self.pass_idx, self.dest_idx], '1'))
        
        #go east = esta fora da ultima coluna && a casa da esquerda == ':'
        if self.taxi_col_r < 8:
            if self.desc[self.taxi_row][self.taxi_col_r+1] != '|':
                sucessors.append(MeuTaxi(self.desc, [self.taxi_row, self.taxi_col+1, self.pass_idx, self.dest_idx], '2'))
        
        #go west = esta fora da primeira coluna && a casa da direita == ':'
        if self.taxi_col_r > 0:
            if self.desc[self.taxi_row][self.taxi_col_r-1] != '|':
                sucessors.append(MeuTaxi(self.desc, [self.taxi_row, self.taxi_col-1, self.pass_idx, self.dest_idx], '3'))
        
        if self.loc[self.pass_idx] == self.desc[self.taxi_row][self.taxi_col_r] :
            sucessors.append(MeuTaxi(self.desc, [self.taxi_row, self.taxi_col, 4, self.dest_idx], '4'))

        if self.loc[self.dest_idx] == self.desc[self.taxi_row][self.taxi_col_r]  and self.pass_idx == 4:
            sucessors.append(MeuTaxi(self.desc, [self.taxi_row, self.taxi_col, self.dest_idx, self.dest_idx], '5'))
        

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

        path = []

        algorithm = sa.AEstrela()
        result = algorithm.search(self)

        # if result != None:
        #     print('Achou!')
        #     print(result.show_path())
        # else:
        #     print('Nao achou solucao')

        path_raw = result.show_path()

        return path
    
    def env(self):
        return str(self.s)

    def h(self):
        return 1


def main():

    env = gym.make("Taxi-v3").env
    s = env.reset(seed=14)

    map = []
    for idx, row in enumerate(env.desc):
        new_row = []
        if idx in [0, (len(env.desc)-1)]:
            continue
        for idx_col, v in enumerate(row):
            if idx_col in [0, len(row)-1]:
                continue
            new_row.append(v.decode("utf-8"))
        map.append(new_row)

    state = MeuTaxi(map, env.decode(s), '')
    

    env.render()

    # env = gym.make("Taxi-v3").env
    # state = env.reset()
    # env.render()
    
    # taxi = MeuTaxi(env.desc, env.decode(state))

    # for a in taxi.path():
    #     state, reward, done, info = env.step(a)
    #     env.render()

    # if done:
    #     print("Soube encontrar a solucao correta")

    # else:
    #     print("Não soube encontrar a solução")

    

if __name__ == '__main__':
    main()