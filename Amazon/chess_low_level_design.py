# ChessBoard
# ChessGame
# Move 
#    # DiagonalMove
#    # StraightMove
# ChessPiece
#    # King
#    # Knight
#    # Pawn
#    # Queen
#    # Rook
#    # Bishop
# PieceFactory

# class ChessPiece:
#     def __init__(self, color):
#        self.color = color

#     @abstractmethod
#     def get_valid_moves(self, position, board):
#         pass

#     def __str__(self):
#         return f"{self.color[0]}{self.__class__.__name__[0]}"

class StraightMove:
    def can_move(self, board, start_row, start_col, end_row, end_col):
        if start_row != end_row and start_col != end_col:
            return False
            
        # horizontal move + check obstacles
        if start_row == end_row:
            step = 1 if end_col > start_col else -1
            for col in range(start_col + step, end_col, step):
                if board.get_piece(start_row, col) is not None: #inbetweenmovement
                    return False

        # vertically
        if start_col == end_col:
            step = 1 if end_row > start_row else -1
            for row in range(start_row + step, end_row, step):
                if board.get_piece(row, start_col) is Not None: # in between movement
                    return False           
            
        return True

class DiagonalMove:

    def can_move(self, board, start_row, start_col, end_row, end_col):
        # delta must be same for row and col
        if abs(end_row - start_row) != abs(end_col - start_col):
            return False

        row_step = 1 if end_row > start_row else -1
        col_step = 1 if end_col > start_col else -1
        r, c = start_row + row_step, start_col + col_step
        
        while r!=end_row and c!=end_col:
            if board.get_piece(r, c) is not None: #in between some piece is there then also the move is not allowed
                return False 
            r += row_step
            c += col_step

        return True
            

class Rook:
    # what common classes they should have -> move, color
    def __init__(self, color):
        # super().__init__(color)
        self.color = color
        self.straight_move = StraightMove()

    def can_move(self, board, start_row, start_col, end_row, end_col):
        if not self.straight_move.can_move(self, board, start_row, start_col, end_row, end_col):
            return False
        # kill
        target = board.get_piece(end_row, end_col)
        if target is None:
            return True
        elif target.get_color() != self.color:
            return True
        else:
            return False
    

class Bishop:
    # what common classes they should have -> move, color
    def __init__(self, color):
        # super().__init__(color)
        self.color = color
        self.diagonal_move = DiagonalMove()

    def can_move(self, board, start_row, start_col, end_row, end_col):
        if not self.diagonal_move.can_move(self, board, start_row, start_col, end_row, end_col):
            return False
        # kill
        target = board.get_piece(end_row, end_col)
        if target is None:
            return True
        elif target.get_color() != self.color:
            return True
        else:
            return False

class Queen:
    def can_move(self, board, start_row, start_col, end_row, end_col):
        if start_row == end_row:
            rook_move = Rook(self.color).can_move(self, board, start_row, start_col, end_row, end_col)
        elif start_col == end_col:
            rook_move = Rook(self.color).can_move(self, board, start_row, start_col, end_row, end_col)
        elif abs(end_row - start_row) == abs(end_col - start_col):
            bishop_move = Bishop(self.color).can_move(self, board, start_row, start_col, end_row, end_col)
        return rook_move or bishop_move

class King:
    def __init__(self, color):
        # super().__init__(color)
        self.color = color
        self.straight_move = StraightMove()

    def can_move(self, board, start_row, start_col, end_row, end_col):
        row_delta = abs(end_row - start_row)
        col_delta = abs(end_col - start_col)
        if row_delta > 1 or col_delta > 1:
            return False
        # kill
        target = board.get_piece(end_row, end_col)
        if target is None:
            return True
        elif target.get_color() != self.color:
            return True
        else:
            return False

class Knight:
    def __init__(self, color):
        # super().__init__(color)
        self.color = color

    def can_move(self, board, start_row, start_col, end_row, end_col):
        row_delta = abs(end_row - start_row)
        col_delta = abs(end_col - start_col)
        if not ((row_delta == 1 and col_delta == 2) or (row_delta == 2 and col_delta == 1)):
            return False
        # kill
        target = board.get_piece(end_row, end_col)
        if target is None:
            return True
        elif target.get_color() != self.color:
            return True
        else:
            return False

class PieceFactory:
    
    @staticmethod
    def create_piece(piece_type, color):
        pieces = {
            'Rook': Rook,
            'Queen': Queen,
            'Knight': Knight,
            'King': King,
            'Bishop': Bishop,
            'Pawn': Pawn
        }
        if piece_type in pieces:
            return pieces[piece_type](color)
        raise ValueError(f"Unknown Piece Type: {piece_type}")
        
class ChessBoard:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.initialize_board()

    def initialize_board():
        factory = PieceFactory()
        self.board[0] = [
            factory.create_piece('Rook','white'), factory.create_piece('Knight', 'white'), factory.create_piece('Bishop', 'white'), 
            factory.create_piece('Queen', 'white'), factory.create_piece('King', 'white'), factory.create_piece('Bishop', 'white'),
            factory.create_piece('Knight', 'white'), factory.create_piece('Rook','white')
        ]
        self.board[1] = [factory.create_piece('Pawn','white') for _ in range(8)]
        self.board[6] = [factory.create_piece('Pawn','black') for _ in range(8)]
        self.board[7] = [
            factory.create_piece('Rook','black'), factory.create_piece('Knight', 'black'), factory.create_piece('Bishop', 'black'), 
            factory.create_piece('Queen', 'black'), factory.create_piece('King', 'black'), factory.create_piece('Bishop', 'black'),
            factory.create_piece('Knight', 'black'), factory.create_piece('Rook','black')
        ]

    def get_piece(self, row, col):
        if 0<=row<=8 and 0<=col<=8:
            return self.board[row][col]
        return None

    def place_piece(self, piece, row, col):
        return self.board[row][col] = piece

    def move_piece(self, start_row, end_row, start_col, end_col):
        piece = self.get_piece(end_row, end_col)
        if piece is None:
            raise ValueError("No piece at starting position")

        if piece.can_move(self, start_row, end_row, start_col, end_col):
            self.place_piece(self, piece, row, col)
            self.board[start_row][start_col] = None
        else:
            raise ValueError("invalid move")

    def display(self):
        for row in self.board:
            print(['.' if piece is None else f"{piece.color[0]}{piece.__class__.__name__[0] for piece in row} "])

class ChessGame:
    def __init__(self):
        self.board = ChessBoard()
        self.current_turn = 'white'

    def play_turn(self, start_row, start_col, end_row, end_col):
        piece = self.board.get_piece(start_row, start_col)
        if piece is None:
            print("Piece is None")
            return False

        if piece.color != self.current_turn:
            print(f"its {self.current_turn}'s turn")
            return False

        try:
            self.board.move_piece(start_row, start_col, end_row, end_col)
            self.current_turn = "black" if self.current_turn == "white" else "white"
            return True
        except ValueError as e:
            print(e)
            return False
            
            
        


game = ChessGame()
# game.displayBoard()

