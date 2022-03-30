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

def test_dificil1():
    state = [
        [7, 8, 6],
        [2, 3, 5],
        [1, 4, 0]
    ]
    alg = sa.AEstrela()
    state = Puzzle(state, '')
    result = alg.search(state)

    assert result.show_path() == " ; UP ; LEFT ; LEFT ; UP ; RIGHT ; DOWN ; DOWN ; LEFT ; UP ; UP ; RIGHT ; RIGHT ; DOWN ; LEFT ; DOWN ; LEFT ; UP ; RIGHT ; UP ; LEFT ; DOWN ; DOWN ; RIGHT ; UP"

def test_dificil2():
    state = [
        [7, 8, 6],
        [2, 3, 5],
        [0, 1, 4]
    ]
    alg = sa.AEstrela()
    state = Puzzle(state, '')
    result = alg.search(state)

    assert result.show_path() == " ; UP ; UP ; RIGHT ; DOWN ; LEFT ; DOWN ; RIGHT ; UP ; RIGHT ; UP ; LEFT ; LEFT ; DOWN ; DOWN ; RIGHT ; UP ; UP ; LEFT ; DOWN ; RIGHT ; RIGHT ; DOWN ; LEFT ; UP"

def test_dificil3():
    state = [
        [8, 3, 6],
        [7, 5, 4],
        [2, 1, 0]
    ]
    alg = sa.AEstrela()
    state = Puzzle(state, '')
    result = alg.search(state)

    assert result.show_path() == " ; UP ; UP ; LEFT ; LEFT ; DOWN ; RIGHT ; DOWN ; LEFT ; UP ; UP ; RIGHT ; DOWN ; DOWN ; LEFT ; UP ; UP ; RIGHT ; DOWN ; RIGHT ; DOWN ; LEFT ; UP"

def test_impossivel():
    state = [
        [3, 4, 8],
        [1, 2, 5],
        [7, 0, 6]
    ]
    alg = sa.AEstrela()
    state = Puzzle(state, '')
    result = alg.search(state)

    assert result == None