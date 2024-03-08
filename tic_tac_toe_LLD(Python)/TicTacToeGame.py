class Player:
    def __init__(self, name, symbol, player_type):
        self.name = name
        self.symbol = symbol
        self.player_type = player_type

class Bot:
    def __init__(self, name, symbol, difficulty):
        self.name = name
        self.symbol = symbol
        self.difficulty = difficulty

class Game:
    def __init__(self, dimension, players):
        self.dimension = dimension
        self.players = players
        self.board = [[' ' for _ in range(dimension)] for _ in range(dimension)]
        self.game_status = 'IN_PROGRESS'

class GameController:
    def create_game(self, dimension, players):
        return Game(dimension, players)

    def get_game_status(self, game):
        return game.game_status

    def display_board(self, game):
        for row in game.board:
            print(' '.join(row))
        print()

    def execute_next_move(self, game):
        # Logic for executing next move goes here
        pass

    def undo(self, game):
        # Logic for undoing last move goes here
        pass

    def get_winner(self, game):
        # Logic for determining the winner goes here
        pass

def main():
    game_controller = GameController()

    print("What should be the dimension of game?")
    dimension = int(input())

    print("Will there be any bot? y/n")
    is_bot_string = input()

    players = []

    to_iterate = dimension - 1

    if is_bot_string == "y":
        to_iterate = dimension - 2

    for i in range(to_iterate):
        print(f"What is the name of player {i}:")
        player_name = input()

        print(f"What is the char of player {i}:")
        player_symbol = input()[0]

        players.append(Player(player_name, player_symbol, "HUMAN"))

    if is_bot_string == "y":
        print("What is the name of bot?")
        bot_name = input()

        print("What is the char of bot?")
        bot_symbol = input()[0]

        players.append(Bot(bot_name, bot_symbol, "EASY"))

    game = game_controller.create_game(dimension, players)

    while game_controller.get_game_status(game) == 'IN_PROGRESS':
        print("This is the current board:")
        game_controller.display_board(game)

        print("Does anyone want to undo? y/n")
        user_input = input()

        if user_input == "y":
            game_controller.undo(game)
        else:
            game_controller.execute_next_move(game)

    print("Game has ended. Result was:")
    if game.game_status != 'DRAW':
        print(f"Winner is: {game_controller.get_winner(game).name}")

if __name__ == "__main__":
    main()
