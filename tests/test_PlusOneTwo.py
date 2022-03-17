from utils.SearchAlgorithms import BuscaLargura
from utils.SearchAlgorithms import BuscaProfundidade
from utils.SearchAlgorithms import BuscaProfundidadeIterativa
from utils.SearchAlgorithms import BuscaCustoUniforme
from utils.SearchAlgorithms import BuscaGananciosa
from utils.SearchAlgorithms import AEstrela
from scripts.PlusOneTwo import PlusOneTwo
from datetime import date, datetime

def test_largura():
    state = PlusOneTwo(1, '', 10)
    algorithm = BuscaLargura()
    inicio = datetime.now()
    result = algorithm.search(state)
    fim = datetime.now()
    print(fim - inicio)
    assert result.show_path() == " ; 2 ; 2 ; 2 ; 2 ; 1"

def test_profundidade():
    state = PlusOneTwo(1, '', 10)
    algorithm = BuscaProfundidade()
    inicio = datetime.now()
    result = algorithm.search(state, 50)
    fim = datetime.now()
    print(fim - inicio)
    assert result.show_path() == " ; 1 ; 1 ; 1 ; 1 ; 1 ; 1 ; 1 ; 1 ; 1"

def test_BPI():
    state = PlusOneTwo(1, '', 10)
    inicio = datetime.now()
    algorithm = BuscaProfundidadeIterativa()
    fim = datetime.now()
    print(fim - inicio)
    result = algorithm.search(state)
    assert result.show_path() == " ; 1 ; 2 ; 2 ; 2 ; 2"

def test_custoUniforme():
    state = PlusOneTwo(1, '', 10)
    inicio = datetime.now()
    algorithm = BuscaCustoUniforme()
    fim = datetime.now()
    print(fim - inicio)
    result = algorithm.search(state)
    assert result.show_path() == " ; 1 ; 2 ; 2 ; 2 ; 2"

def test_largura_bigger():
    state = PlusOneTwo(1, '', 40)
    algorithm = BuscaLargura()
    inicio = datetime.now()
    result = algorithm.search(state)
    fim = datetime.now()
    print(fim - inicio)


