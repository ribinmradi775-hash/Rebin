class Piece:
    def __init__(self, color):
        self.color = color

class Pawn(Piece):
    def move(self, start, end):
        pass  # Implement pawn movement logic

class Rook(Piece):
    def move(self, start, end):
        pass  # Implement rook movement logic

# Add other piece classes

class ChessBoard:
    def __init__(self):
        self.board = self.setup_board()

    def setup_board(self):
        board = [[None] * 8 for _ in range(8)]
        # Initialize pieces on the board
        return board

    def is_in_check(self, color):
        # Logic to detect check
        return False

    def can_promote(self, pawn_position):
        # Logic to check for pawn promotion
        return False

    def display(self):
        # Simple UI to display the board
        for row in self.board:
            print(' '.join([str(piece) if piece else '.' for piece in row]))

    def move_piece(self, start, end):
        # Move piece logic with validation
        pass

# Example usage
if __name__ == '__main__':
    game = ChessBoard()
    game.display()