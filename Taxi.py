import SearchAlgorithms as sa
from Graph import State
import gym

class MeuTaxi(State):

    def __init__(self, desc, state, op):

        self.operator = op

        self.s = state
        
        self.taxi_row, self.taxi_col, self.pass_idx, self.dest_idx = self.s
        
        self.taxi_col_r = (self.taxi_col*2)+1
        self.desc = desc[1:-1]
        
        self.here = self.desc[self.taxi_row][self.taxi_col_r].decode("utf-8") 

        self.loc = {
            0 : 'R',
            1 : 'G',
            2 : 'Y',
            3 : 'B'
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
            sucessors.append(MeuTaxi(self.desc, [self.taxi_row+1, self.taxi_col, self.pass_idx, self.dest_idx], 0))

        #go north = está fora da primeira linha
        if self.taxi_row > 0:
            sucessors.append(MeuTaxi(self.desc, [self.taxi_row-1, self.taxi_col, self.pass_idx, self.dest_idx], 1))
        
        #go east = esta fora da ultima coluna && a casa da esquerda == ':'
        if self.taxi_col_r < 4:
            if self.desc[self.taxi_row][self.taxi_col_r+1].decode("utf-8") != '|':
                sucessors.append(MeuTaxi(self.desc, [self.taxi_row, self.taxi_col+1, self.pass_idx, self.dest_idx], 2))
        
        #go west = esta fora da primeira coluna && a casa da direita == ':'
        if self.taxi_col_r > 0:
            if self.desc[self.taxi_row][self.taxi_col_r-1].decode("utf-8") != '|':
                sucessors.append(MeuTaxi(self.desc, [self.taxi_row, self.taxi_col-1, self.pass_idx, self.dest_idx], 3))
        
        if self.loc[self.pass_idx] == self.here:
            sucessors.append(MeuTaxi(self.desc, self.s, 4))

        if self.loc[self.dest_idx] == self.here:
            sucessors.append(MeuTaxi(self.desc, self.s, 5))
        

        return sucessors
    
    def is_goal(self):
        pass
    
    def description(self):
        return "Describe the problem"
    
    def cost(self):
        return 1

    def print(self):
        return str(self.operator)

    def path(self):
        path = []

        state = MeuTaxi('')
        algorithm = sa.BuscaProfundidadeIterativa()
        result = algorithm.search(state)
        if result != None:
            print(result.show_path())

        return path
    
    def env(self):
        #
        # IMPORTANTE: este não apenas deve retornar uma descrição do environment, mas 
        # deve também retornar um valor que descreva aquele nodo em específico. Pois 
        # esta representação é utilizada para verificar se um nodo deve ou ser adicionado 
        # na lista de abertos.
        #
        # Exemplos de especificações adequadas: 
        # - para o problema do soma 1 e 2: return str(self.number)+"#"+str(self.cost)
        # - para o problema das cidades: return self.city+"#"+str(self.cost())
        #
        # Exemplos de especificações NÃO adequadas: 
        # - para o problema do soma 1 e 2: return str(self.number)
        # - para o problema das cidades: return self.city
        #
        None


def main():


    env = gym.make("Taxi-v3").env
    state = env.reset()
    env.render()
    
    taxi = MeuTaxi(env.desc, env.decode(state))

    for a in taxi.path():
        state, reward, done, info = env.step(a)
        env.render()

    if done:
        print("Soube encontrar a solucao correta")

    else:
        print("Não soube encontrar a solução")

    

if __name__ == '__main__':
    main()