#
# Implements a solution for N-queens problem, where N could 
# be any number between 4 and 10.
#


from SearchAlgorithms import AEstrela
from Graph import State
from random import randrange
import numpy as np
import random
import time
from copy import deepcopy

def printa_board(board):
    for b in board:
        print(b)

class Puzzle(State):

    def __init__(self, board, operator):
        self.board = board
        self.operator = operator

    def env(self):
        return self.board
    
    def sucessors(self):
        sucessores = []
        for i in range(0,3): #linhas
            for j in range(0,3): #colunas
                if(self.board[i][j] == 0):
                    #move up
                    if(i != 0):
                        temp = deepcopy(self.board)
                        temp[i][j] = temp[i-1][j]
                        temp[i-1][j] = 0
                        sucessores.append(Puzzle(temp,'up'))
                        printa_board(temp)
                        print()
                    #move down
                    if(i != 2):
                        temp = deepcopy(self.board)
                        temp[i][j] = temp[i+1][j]
                        temp[i+1][j] = 0
                        sucessores.append(Puzzle(temp,'down'))
                        printa_board(temp)
                        print()
                    #move left
                    if(j != 0):
                        temp = deepcopy(self.board)
                        temp[i][j] = temp[i][j-1]
                        temp[i][j-1] = 0
                        sucessores.append(Puzzle(temp,'left'))
                        printa_board(temp)
                        print()
                    #move right
                    if(j != 2):
                        temp = deepcopy(self.board)
                        temp[i][j] = temp[i][j+1]
                        temp[i][j+1] = 0
                        sucessores.append(Puzzle(temp,'right'))
                        printa_board(temp)
                        print()
        return sucessores
                      
    def is_goal(self):
        if self.h() == 0:
            return True
        return False
    
    def description(self):
        return "Queens Problem"
    
    def cost(self):
        return 1

    def print(self):
        pass
    
    def h(self):
        h= 0
        goal=[[1,2,3],
              [8,0,4],
              [7,6,5]
                ]
        for i in range(0,3): #linhas
            for j in range(0,3): #colunas
                if(self.board[i][j] != goal[i][j]):
                    h+=1
        
        return h

   

def main():
    facil = [[8,1,3],
            [0,7,2],
            [6,5,4]
            ]
    dificil0 = [[7,8,6],   
            [2,3,5],
            [1,4,0]
            ]
    dificil1 = [[7,8,6],   
            [2,3,5],
            [0,1,4]
            ]
    dificil2 = [[8,3,6],   
            [7,5,4],
            [2,1,0]
            ]
    printa_board(dificil1)
    print()
    state = Puzzle(board = dificil1, operator ='')
    algorithm = AEstrela()
    
    result = algorithm.search(state)
    
    
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()
