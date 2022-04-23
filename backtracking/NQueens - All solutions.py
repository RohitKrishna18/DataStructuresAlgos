# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 00:17:53 2022

@author: rohit
"""

class NQueensSolution:
    
    solutions = []
    
    def addSolution(self, board, size):
        sol = []
        for col in range(size):
            sol.append(board[col].index(1)+1)
        self.solutions.append(sol)
    
    def printSolution(self, board, size):
        for i in range(size):
            for j in range(size):
                print (board[i][j], end = " ")
            print()
    
    def isValid(self, board, row, col, size):
        for i in range(col):
            if board[row][i]==1:
                return False
        for i,j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j]==1:
                return False
        for i,j in zip(range(row, size, 1), range(col, -1, -1)):
            if board[i][j]==1:
                return False
        return True
    
    def solveUtil(self, board, col, size):
        if col>=size:
            self.addSolution(board, size)
        for i in range(size):
            if self.isValid(board, i, col, size):
                board[i][col] = 1
                self.solveUtil(board, col+1, size)
                board[i][col]=0
    
    def solve(self, board, size):
        self.solveUtil(board, 0, size)

    def nQueen(self, n):
        # code here
        #board = [[0,0,0,0], [0,0,0,0],[0,0,0,0],[0,0,0,0]]
        board = [[0 for col in range(n)] for row in range(n)]
        self.solve(board, n)
        self.solutions.sort()
        return self.solutions
		
solution = NQueensSolution()
solution.nQueen(4)