from Player import Player
from factories import BotPlayingStrategyFactory

class Bot(Player):
    def __init__(self, name, symbol, difficulty_level):
        super().__init__(name, symbol, "BOT")
        self.bot_difficulty_level = difficulty_level
        self.bot_playing_strategy = BotPlayingStrategyFactory.get_strategy_for_difficulty_level(difficulty_level)

    def get_bot_difficulty_level(self):
        return self.bot_difficulty_level

    def set_bot_difficulty_level(self, bot_difficulty_level):
        self.bot_difficulty_level = bot_difficulty_level

    def decide_move(self, board):
        return self.bot_playing_strategy.decide_move(self, board)
