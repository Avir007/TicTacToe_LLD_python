from abc import ABC, abstractmethod
from models.Board import Board
from models.Cell import Cell
from models.Player import Player

class GameWinningStrategy(ABC):
    @abstractmethod
    def check_winner(self, board, last_move_player, move_cell):
        pass
