# Problem 2 : Snakes and Ladders
# Time Complexity :  O(n^2) where n is the size of the board
# Space Complexity : O(n^2) where n is the size of the board
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this :
'''
None
'''

# Your code here along with comments explaining your approach
from typing import List
from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # get the length of the board
        n = len(board)
        # define the 1-d arrayBoard with size (n*n) and fill with -1
        array_board = [-1] * (n * n)
        # define direction boolean variable with True
        direction = True
        # row and column index for the position (start position is (n-1), 0)
        r, c = n - 1, 0
        # index variable for 1-d array
        index = 0

        # Flatten the 2D board into 1D array
        while index < n * n:
            # check if the value is -1 and if it is then set value -1 at index position
            if board[r][c] == -1:
                array_board[index] = -1
            else:
                # else set the value as (board[r][c] - 1) at index position
                array_board[index] = board[r][c] - 1
            # incrememt index
            index += 1
            # check if direction value as True
            if direction:
                # if it is then increment the column
                c += 1
                # if the column reach near right boundary
                if c == n:
                    # set the direction to False and decrement the column and row
                    direction = False
                    c -= 1
                    r -= 1
            else:
                # else decrement the column
                c -= 1
                 # if the column reach near left boundary
                if c == -1:
                    # set the direction to True, decrement the row and increment the column
                    direction = True
                    c += 1
                    r -= 1

        # BFS 
        # defince the queue and append 0 index
        q = deque([0])
        # set the value as -2 to mark as visited
        array_board[0] = -2
        # define moves variable to count the moves
        moves = 0

        # loop till queue is not empty
        while q:
            # get the length of the current queue
            size = len(q)
            # loop for the length of the queue
            for _ in range(size):
                # pop the index from the queue
                current = q.popleft()
                # check if the index is the destination then return moves
                if current == n * n - 1:
                    return moves
                # loop from 1 to 6 which are die values
                for j in range(1, 7):
                    # get newIndex by adding j to current index
                    new_index = current + j
                    # check if index value is greater or equal to (n*n) then break
                    if new_index >= n * n:
                        break
                    # check the value at index and if it is -1 then append the new index
                    if array_board[new_index] == -1:
                        q.append(new_index)
                    # check the value at index and if it is not -2 then append the value of the array_board at new index position 
                    elif array_board[new_index] != -2:
                        q.append(array_board[new_index])
                    # set the value as -2 to mark as visited
                    array_board[new_index] = -2  # mark as visited
            # increment the moves
            moves += 1
        # else return -1
        return -1
