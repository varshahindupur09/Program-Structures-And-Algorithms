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


#############################
CLASS IMPLEMENTATIONS: BOARD, MOVE
#############################

from collections import defaultdict

class TicTacToe:
    
    class Board:
        def __init__(self, n: int):
            self.n = n
            self.grid = [[0 for _ in range(n)] for _ in range(n)]
            print(self.grid)
            self.rows = defaultdict(int)
            self.columns = defaultdict(int)
            self.leftDiagonal = 0
            self.rightDiagonal = 0
            
        def getBoard(self): # gives current state of the board
            return grid
            
        def getWinner(self, player, row, col):
            if abs(self.leftDiagonal) == self.n:
                return player
            elif abs(self.rightDiagonal) == self.n:
                return player
            elif abs(self.rows[row]) == self.n:
                return player
            elif abs(self.columns[col]) == self.n:
                return player
            return 0 #no winner yet

        def getCurrentPlayer(self):
            totalMoves = sum(sum(1 for cell in row if cell != 0) for row in self.grid)
            return 1 if totalMoves % 2 == 0 else 2
            
        def makeMove(self, move):
            player, row, col = move.player, move.row, move.col
            movement = -1 if player == 1 else 1
            
            # update the board
            self.grid[row][col] = player
            self.rows[row] += movement
            self.columns[col] += movement
            if row == col:
                self.leftDiagonal += movement
            if row + col == self.n - 1:
                self.rightDiagonal += movement

            return self.getWinner(player, row, col)
    
    class User:
        pass
    
    class Move:
        def __init__(self, player: int, row: int, col: int):
            self.player = player
            self.row = row
            self.col = col
    
    class Game:
        pass


tictactoe = TicTacToe()
board = tictactoe.Board(3)
# direct moves
move1 = tictactoe.Move(1,0,0)
winner = board.makeMove(move1)
print("Winner after Move 1:", winner)

move2 = tictactoe.Move(2, 1, 1)  # Player 2 places on (1, 1)
winner = board.makeMove(move2)  # No winner yet
print("Winner after Move 2:", winner)

move3 = tictactoe.Move(1, 0, 1)  # Player 1 places on (0, 1)
winner = board.makeMove(move3)  # No winner yet
print("Winner after Move 3:", winner)

move4 = tictactoe.Move(2, 2, 2)  # Player 2 places on (2, 2)
winner = board.makeMove(move4)  # No winner yet
print("Winner after Move 4:", winner)

move5 = tictactoe.Move(1, 0, 2)  # Player 1 places on (0, 2), completing a row
winner = board.makeMove(move5)  # Player 1 wins
print("Winner after Move 5:", winner)
