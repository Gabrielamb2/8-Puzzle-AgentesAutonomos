from SearchAlgorithms import AEstrela
from main import inversion
from main import Puzzle

def test_facil():
    facil = [[8,1,3],
            [0,7,2],
            [6,5,4]
            ]
    state = Puzzle(board = facil, operator ='')
    algorithm = AEstrela()
    result = algorithm.search(state)
    assert result.show_path() == " ; right ; right ; down ; left ; left ; up ; up ; right ; down"

def test_dificil0():
    dificil0 = [[7,8,6],   
                [2,3,5],
                [1,4,0]
               ]
    state = Puzzle(board = dificil0, operator ='')
    algorithm = AEstrela()
    result = algorithm.search(state)
    assert result.show_path() == " ; up ; left ; left ; up ; right ; down ; down ; left ; up ; up ; right ; right ; down ; left ; down ; left ; up ; right ; up ; left ; down ; down ; right ; up"

def test_dificil1():
    dificil1 = [[7,8,6],   
                [2,3,5],
                [0,1,4]
               ]
    state = Puzzle(board = dificil1, operator ='')
    algorithm = AEstrela()
    result = algorithm.search(state)
    assert result.show_path() == " ; up ; up ; right ; down ; left ; down ; right ; up ; right ; up ; left ; left ; down ; down ; right ; up ; up ; left ; down ; right ; right ; down ; left ; up"

def test_dificil2():
    dificil2 = [[8,3,6],   
                [7,5,4],
                [2,1,0]
               ]
    state = Puzzle(board = dificil2, operator ='')
    algorithm = AEstrela()
    result = algorithm.search(state)
    assert result.show_path() == " ; up ; up ; left ; left ; down ; right ; down ; left ; up ; up ; right ; down ; down ; left ; up ; up ; right ; down ; right ; down ; left ; up"


def test_impossivel0():
    impossivel0 = [[3,4,8],   
                   [1,2,5],
                   [7,0,6]
                  ]
    state = Puzzle(board = impossivel0, operator ='')
    algorithm = AEstrela()
    solvable = inversion(impossivel0)
    if solvable:
        state = Puzzle(board = impossivel0, operator ='')
        algorithm = AEstrela()
        result = algorithm.search(state)
         
    else:
        result = None
    assert result == None

def test_impossivel1():
    impossivel1 = [[5,4,0],   
                   [6,1,8],
                   [7,3,2]
                  ]
    state = Puzzle(board = impossivel1, operator ='')
    algorithm = AEstrela()
    solvable = inversion(impossivel1)
    if solvable:
        state = Puzzle(board = impossivel1, operator ='')
        algorithm = AEstrela()
        result = algorithm.search(state)
         
    else:
        result = None
    assert result == None
