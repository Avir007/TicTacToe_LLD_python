from strategies.botplayingstrategy import RandomBotPlayingStrategy

class BotPlayingStrategyFactory:
    @staticmethod
    def get_strategy_for_difficulty_level(difficulty_level):
        return RandomBotPlayingStrategy()
