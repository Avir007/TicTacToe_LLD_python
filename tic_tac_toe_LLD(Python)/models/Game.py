from models.Board import Board
from models.Move import Move
from models.Player import Player
from models.CellState import CellState
from strategies.gamewinningstrategy import OrderOneGameWinningStrategy
from models.GameStatus import GameStatus
from exceptions import InvalidGameConstructionParametersException

class Game:
    def __init__(self):
        self.board = None
        self.players = []
        self.moves = []
        self.game_status = GameStatus.IN_PROGRESS
        self.next_player_index = 0
        self.game_winning_strategy = None
        self.winner = None

    def get_winner(self):
        return self.winner

    def set_winner(self, winner):
        self.winner = winner

    def get_game_winning_strategy(self):
        return self.game_winning_strategy

    def set_game_winning_strategy(self, game_winning_strategy):
        self.game_winning_strategy = game_winning_strategy

    def undo(self):
        pass

    def make_next_move(self):
        to_move_player = self.players[self.next_player_index]
        print("It is", to_move_player.get_name(), "'s turn.")

        move = to_move_player.decide_move(self.board)

        row = move.get_cell().get_row()
        col = move.get_cell().get_col()

        print("Move happened at:", row, ",", col)

        self.board.get_board()[row][col].set_cell_state(CellState.FILLED)
        self.board.get_board()[row][col].set_player(self.players[self.next_player_index])

        final_move = Move(self.players[self.next_player_index], self.board.get_board()[row][col])
        self.moves.append(final_move)

        if self.game_winning_strategy.check_winner(self.board, self.players[self.next_player_index], final_move.get_cell()):
            self.game_status = GameStatus.ENDED
            self.winner = self.players[self.next_player_index]

        self.next_player_index += 1
        self.next_player_index %= len(self.players)

    def display_board(self):
        self.board.display()

    def get_board(self):
        return self.board

    def set_board(self, board):
        self.board = board

    def get_players(self):
        return self.players

    def set_players(self, players):
        self.players = players

    def get_moves(self):
        return self.moves

    def set_moves(self, moves):
        self.moves = moves

    def get_game_status(self):
        return self.game_status

    def set_game_status(self, game_status):
        self.game_status = game_status

    def get_next_player_index(self):
        return self.next_player_index

    def set_next_player_index(self, next_player_index):
        self.next_player_index = next_player_index

    class Builder:
        def __init__(self):
            self.dimension = None
            self.players = None

        def set_dimension(self, dimension):
            self.dimension = dimension
            return self

        def set_players(self, players):
            self.players = players
            return self

        def valid(self):
            if self.dimension < 3:
                raise InvalidGameConstructionParametersException("Dimension of game can't be less than 3")

            if len(self.players) != self.dimension - 1:
                raise InvalidGameConstructionParametersException("Number of Players must be Dimension - 1")

            # Validate no 2 people with the same char
            # Validate all 1 bot

            return True

        def build(self):
            try:
                self.valid()
            except Exception as e:
                raise InvalidGameConstructionParametersException(str(e))

            game = Game()
            game.set_game_status(GameStatus.IN_PROGRESS)
            game.set_players(self.players)
            game.set_moves([])
            game.set_board(Board(self.dimension))
            game.set_next_player_index(0)
            game.set_game_winning_strategy(OrderOneGameWinningStrategy(self.dimension))

            return game
