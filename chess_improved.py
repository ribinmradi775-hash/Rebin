class ChessGame:
    def __init__(self):
        self.board = self.create_board()
        self.current_turn = 'white'
        self.move_history = []
        self.game_over = False
        self.check_status = {'white': False, 'black': False}

    def create_board(self):
        board = [[' ' for _ in range(8)] for _ in range(8)]
        # Placing pawns
        for i in range(8):
            board[1][i] = 'P'  # White pawns
            board[6][i] = 'p'  # Black pawns
        # Other pieces can be placed here as well
        return board

    def display_board(self):
        for row in self.board:
            print(' '.join(row))

    def is_check(self, color):
        # Implement check detection logic here
        pass

    def move_piece(self, start_pos, end_pos):
        # Implement piece movement logic including
        # castling, en passant, and promotion
        pass

    def update_game_status(self):
        # Display current game status
        self.display_board()
        if self.check_status[self.current_turn]:
            print(f'{self.current_turn.capitalize()} is in check!')
        if self.game_over:
            print(f'{self.current_turn.capitalize()} has lost the game!')

    # Additional methods for pawn promotion, castling, en passant, etc.

if __name__ == '__main__':
    game = ChessGame()
    while not game.game_over:
        game.update_game_status()
        # Here, implement user input and game loop logic
