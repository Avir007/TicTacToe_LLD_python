from models import GameStatus

class GameController:
    def undo(self, game):
        game.undo()

    def create_game(self, dimension, players):
        try:
            return Game.builder() \
                .set_dimension(dimension) \
                .set_players(players) \
                .build()
        except Exception as e:
            return None

    def display_board(self, game):
        game.display_board()

    def get_game_status(self, game):
        return game.get_game_status()

    def execute_next_move(self, game):
        game.make_next_move()

    def get_winner(self, game):
        return game.get_winner()
