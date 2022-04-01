#
# Implements a solution for N-queens problem, where N could 
# be any number between 4 and 10.
#


from SearchAlgorithms import AEstrela
from Graph import State
from random import randrange
# import numpy as np
# import random
# import time
from copy import deepcopy

def printa_board(board):
    for b in board:
        print(b)
def acha_buraco(board):
    for i in range(0,3): #linhas
        for j in range(0,3): #colunas
            if(board[i][j] == 0):
                return i,j
def printa_caminho(string,board):
    output=string.split(';')
    for c in output:               
        i,j = acha_buraco(board)
        if c == ' right ':
            print("right")
            board[i][j] = board[i][j+1]
            board[i][j+1] = 0
            printa_board(board)
            print()
        elif c == ' down ':
            print("down")
            board[i][j] = board[i+1][j]
            board[i+1][j] = 0
            printa_board(board)
            print()
        elif c == ' up ':
            print("up")
            board[i][j] = board[i-1][j]
            board[i-1][j] = 0
            printa_board(board)
            print()
        elif c == ' left ':
            print("left")
            board[i][j] = board[i][j-1]
            board[i][j-1] = 0
            printa_board(board)
            print()
        else:
            pass
        
def inversion(board):
    contador = 0
    for i in range(0,3): #linhas
        for j in range(0,3): #colunas
            if board[i][j] != 0:
                valor_atual = board[i][j] 
                for l in range(0,3): #linhas
                    for c in range(0,3): #colunas
                        if(l>i or l==i and c>j):
                            if(board[l][c] < valor_atual and board[l][c] != 0):
                                contador+=1
    # print("inversao {0}".format(contador))
    if(contador % 2 == 1):
        print("tem solucao")
        return True
    else:
        print("nao tem solucao")
        return False
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
                    #move down
                    if(i != 2):
                        temp = deepcopy(self.board)
                        temp[i][j] = temp[i+1][j]
                        temp[i+1][j] = 0
                        sucessores.append(Puzzle(temp,'down'))
                    #move left
                    if(j != 0):
                        temp = deepcopy(self.board)
                        temp[i][j] = temp[i][j-1]
                        temp[i][j-1] = 0
                        sucessores.append(Puzzle(temp,'left'))
                    #move right
                    if(j != 2):
                        temp = deepcopy(self.board)
                        temp[i][j] = temp[i][j+1]
                        temp[i][j+1] = 0
                        sucessores.append(Puzzle(temp,'right'))
        return sucessores
                      
    def is_goal(self):
        goal=[[1,2,3],
              [8,0,4],
              [7,6,5]
                ]
        return self.board == goal
    
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
                num = str(self.board[i][j])
                for l in range(0,3):
                    for c in range(0,3):
                        if(str(goal[l][c]) == num):
                            distancia = abs(i - l) + abs(j-c)
                            h += distancia
       


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
    impossivel0 = [[3,4,8],   
                   [1,2,5],
                   [7,0,6]
                  ]
    impossivel1 = [[5,4,0],   
                   [6,1,8],
                   [7,3,2]
                  ]
    print("Estado inicial:")
    printa_board(facil)
    print()
    solvable = inversion(facil)
    if solvable:
        state = Puzzle(board = facil, operator ='')
        algorithm = AEstrela()
        result = algorithm.search(state)
         
    else:
        result = None

    if result != None:
        print('Achou!')
        print()
        caminho = result.show_path()
        printa_caminho(caminho,facil)
        # print(result.show_path())
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()