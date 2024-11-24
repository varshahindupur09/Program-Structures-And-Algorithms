# Low level design : 
# Board: # 2D matrix - square[n][n] -> int[n][n] -> {0,1,2} # winner -> first, second, draw, undecided -> 0 to 4 # functions: initialize, getBoard, getWinner, getCurrentPlayer, makeMove(Move m)
# Move: row, col {highly unlikely of asking to implement};;;; int Player, int i, int j
# Elo is a rating system used in competitive gaming to calculate the relative skill levels of players.
# User Object: UserId, Statistics [wins, losses, ELO, best opponent played against,etc ;;; feature based], updateStatistics {Profile -later}
# Game Object: Game_Id, UserID1, UserID2, List<Moves> [later user can download or undo function implement]: initialize, undo
# interviewer can ask you to make move in O(1) time; 
# to say to find winner for tic-tac-toe the diagonal, vertical, horizontal everything 3 has to be same and declared winner but that ends in O(n**3) 
# to decide a winner the grid's x,y moves touching that last move is to be observed and only that person making the move can win after making their move - important observation

class Board:
  pass

