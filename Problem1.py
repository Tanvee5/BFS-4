# Problem 1 : Minesweeper
# Time Complexity : 
'''
BFS - O(m * n) where m is the number of row in board and n is the number of column in board
DFS - O(m * n) where m is the number of row in board and n is the number of column in board
'''
# Space Complexity : 
'''
BFS - O(m * n) where m is the number of row in board and n is the number of column in board
DFS - O(m * n) where m is the number of row in board and n is the number of column in board
'''
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this :
'''
None
'''

# Your code here along with comments explaining your approach

# BFS
from typing import List
from collections import deque
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        # directions array for neighbours in the board ie vertically, horizontally and diagonally
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        # get the length of the rows and columns for the board
        m = len(board)
        n = len(board[0])

        # function countMines to calculat the surrounding mines
        def countMines(board: List[List[str]], i: int, j:int) -> int:
            # directions array for neighbours in the board ie vertically, horizontally and diagonally
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
            # get the length of the rows and columns for the board
            m = len(board)
            n = len(board[0])
            # variable to count the mines, set to 0
            count = 0
            # loop through directions
            for dr, dc in directions:
                # get the new row and column position
                nr = i + dr
                nc = j + dc
                # check if the new row and column is in bounds and the value of the cell is M
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'M':
                    # if it is then increment the count
                    count += 1
            # return the value of count
            return count
        
        # check if the start position has mine
        if board[click[0]][click[1]] == 'M':
            # if it is then set the value as X and return board
            board[click[0]][click[1]] = 'X'
            return board
    
        # define queue to add the index position
        q = deque()
        # append the position of click to queue
        q.append(click)
        # set the position as B ie mark as visited
        board[click[0]][click[1]] = 'B'

        # loop until queue is not empty
        while q:
            # pop the current index pair from the queue
            current = q.popleft()
            # calculate the mines for the current position
            count = countMines(board, current[0], current[1])
            # if the count is 0 ie no mines around
            if count == 0:
                # loop through every direction
                for dr, dc in directions:
                    # get the new row and column 
                    nr = current[0] + dr
                    nc = current[1] + dc
                    # check if the new row and column index is in bounds and the value of the position is 'E'
                    if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'E':
                        # set the position as B ie mark as visited
                        board[nr][nc] = 'B'
                        # append the new row and new column to queue
                        q.append((nr, nc))
            # else it means there are mines around the board
            else:
                # set the value as count for the position
                board[current[0]][current[1]] = str(count)
        # return board
        return board
            

# DFS

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        # directions array for neighbours in the board ie vertically, horizontally and diagonally
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        # get the length of the rows and columns for the board
        m = len(board)
        n = len(board[0])
        # function countMines to calculat the surrounding mines
        def countMines(board: List[List[str]], i: int, j:int) -> int:
            # directions array for neighbours in the board ie vertically, horizontally and diagonally
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
            # get the length of the rows and columns for the board
            m = len(board)
            n = len(board[0])
            # variable to count the mines, set to 0
            count = 0
            # loop through directions
            for dr, dc in directions:
                # get the new row and column 
                nr = i + dr
                nc = j + dc
                # check if the new row and column is in bounds and the value of the cell is M
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'M':
                    # if it is then increment the count
                    count += 1
            # return the value of count
            return count
        
        # dfs function for traversing the board in dfs manner
        def dfs(board: List[List[str]], i: int, j:int, directions) -> None:
            # base
            # check the boundary condition or the value of position is not E then return
            if(i < 0 or i == len(board) or j < 0 or j == len(board[0]) or board[i][j] != 'E'):
                return

            # logic
            # set the position as B ie mark as visited
            board[i][j] = 'B'
            # calculate the mines for the current position
            count = countMines(board, i, j)
            # if the count is 0 ie no mines around
            if count == 0:
                # loop through every direction
                for dr, dc in directions:
                    # get the new row and column 
                    nr = dr + i
                    nc = dc + j
                    # call dfs function for each neighbour
                    dfs(board, nr, nc, directions)
            # else it means there are mines around the board
            else:
                # set the value as count for the position
                board[i][j] = str(count)
        
        # check if the start position has mine
        if board[click[0]][click[1]] == 'M':
            # if it is then set the value as X and return board
            board[click[0]][click[1]] = 'X'
            return board
        # call dfs function with start position
        dfs(board, click[0], click[1], directions)
        # return board
        return board
