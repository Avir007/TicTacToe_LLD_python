from abc import ABC, abstractmethod
from models.Move import Move
from models.Board import Board
from models.Player import Player

class BotPlayingStrategy(ABC):
    @abstractmethod
    def decide_move(self, player, board):
        pass
