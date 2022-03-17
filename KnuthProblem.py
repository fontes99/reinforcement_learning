from SearchAlgorithms import BuscaLargura
from Graph import State

from math import factorial

#
# Initial state: 4
# Operations: sqrt, factorial and round down
# Final state: any int number bigger than 0
#

class KnuthProblem(State):

    def __init__(self, number, op, Goal):
        self.number = number
        self.operator = op
        self.Goal = Goal

    def env(self):
        pass
    
    def sucessors(self):
        sucessors = []

        if self.number >= self.Goal**2:
            sucessors.append(KnuthProblem(self.number**(1/2), 'sqrt', self.Goal))

        if type(self.number) == int and self.number <= self.Goal**2:
            sucessors.append(KnuthProblem(factorial(self.number), 'factorial', self.Goal))

        if type(self.number) != int:
            sucessors.append(KnuthProblem(int(self.number), 'round_down', self.Goal))

        return sucessors
    
    def is_goal(self):
        return self.number == self.Goal
    
    def description(self):
        return "Problema simples com operadores de soma 1 e soma 2. Estados representados apenas por um numero"
    
    def cost(self):
        return 1

    def h(self):
        return 0
    
    def print(self):
        return str(self.operator)

from datetime import datetime

def main():
    
    #
    # Executando busca em largura
    #
    print('Busca em largura')
    state = KnuthProblem(4, '', 10)
    algorithm = BuscaLargura()
    inicio = datetime.now()
    result = algorithm.search(state)
    fim = datetime.now()
    print(fim - inicio)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')


if __name__ == '__main__':
    main()
