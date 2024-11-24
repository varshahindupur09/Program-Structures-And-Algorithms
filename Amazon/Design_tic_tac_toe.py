# Low level design : https://leetcode.com/problems/design-tic-tac-toe/
# Board: # 2D matrix - square[n][n] -> int[n][n] -> {0,1,2} # winner -> first, second, draw, undecided -> 0 to 4 # functions: initialize, getBoard, getWinner, getCurrentPlayer, makeMove(Move m)
# Move: row, col {highly unlikely of asking to implement};;;; int Player, int i, int j
# Elo is a rating system used in competitive gaming to calculate the relative skill levels of players.
# User Object: UserId, Statistics [wins, losses, ELO, best opponent played against,etc ;;; feature based], updateStatistics {Profile -later}
# Game Object: Game_Id, UserID1, UserID2, List<Moves> [later user can download or undo function implement]: initialize, undo
# interviewer can ask you to make move in O(1) time; 
# to say to find winner for tic-tac-toe the diagonal, vertical, horizontal everything 3 has to be same and declared winner but that ends in O(n**3) 
# to decide a winner the grid's x,y moves touching that last move is to be observed and only that person making the move can win after making their move - important observation

from collections import defaultdict

class TicTacToe:

    def __init__(self, n: int):
        self.rows = defaultdict(int)
        self.columns = defaultdict(int)
        self.leftdiag = 0
        self.rightdiag = 0
        self.n = n

    def move(self, row: int, col: int, player: int) -> int: #0,0,1
        if player == 1:
            movementcount = -1  
        else:
            movementcount = 1
        # initialize all
        self.rows[row] += movementcount
        self.columns[col] += movementcount
        if row == col:
            self.leftdiag += movementcount
        if abs(row + col) == self.n - 1:
            self.rightdiag += movementcount
        # moves calculater to check winner
        if max(abs(self.rows[row]), abs(self.columns[col]), abs(self.leftdiag), abs(self.rightdiag)) == self.n:
            return player
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)

# 0|0|0 = 0 #  [0,1=1]==0 exceeds 0 
# 1|1|1 = 3

# -1|-1|-1 = -3
# 1|1|1 = 3

# 00 11 22 = row,col = same. [-1,1=0]
# 02 11 20 = row,col = same. [n-1]




