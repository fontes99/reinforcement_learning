from utils.SearchAlgorithms import BuscaLargura
from utils.SearchAlgorithms import BuscaProfundidade
from utils.SearchAlgorithms import BuscaProfundidadeIterativa
from scripts.VacuumWorld import VacuumWorld

def test_largura():
    state = VacuumWorld('left', True, False, '')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    assert result.show_path() == " ; Move Right ; clean ; Move Left"

def test_profundidade():
    state = VacuumWorld('left', True, False, '')
    algorithm = BuscaProfundidade()
    result = algorithm.search(state, 10)
    assert result.show_path() == " ; clean ; clean ; clean ; clean ; clean ; clean ; clean ; Move Right ; clean ; Move Left"

def test_BPI():
    state = VacuumWorld('left', True, False, '')
    algorithm = BuscaProfundidadeIterativa()
    result = algorithm.search(state)
    assert result.show_path() == " ; Move Right ; clean ; Move Left"