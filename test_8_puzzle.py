import SearchAlgorithms as sa
from Puzzle import Puzzle

def test_facil():
    state = [
            [8, 1, 3],
            [0, 7, 2],
            [6, 5, 4]
        ]
    alg = sa.AEstrela()
    state = Puzzle(state, '')
    result = alg.search(state)

    assert result.show_path() == " ; RIGHT ; RIGHT ; DOWN ; LEFT ; LEFT ; UP ; UP ; RIGHT ; DOWN"