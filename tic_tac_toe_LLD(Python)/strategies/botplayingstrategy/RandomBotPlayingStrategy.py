from strategies.botplayingstrategy import BotPlayingStrategy
from models.Move import Move
from models.Cell import Cell
from models.CellState import CellState
import random

class RandomBotPlayingStrategy(BotPlayingStrategy):
    def decide_move(self, player, board):
        dimension = len(board.get_board())

        empty_cells = []
        for i in range(dimension):
            for j in range(dimension):
                if board.get_board()[i][j].get_cell_state() == CellState.EMPTY:
                    empty_cells.append(Cell(i, j))

        if empty_cells:
            return Move(player, random.choice(empty_cells))
        else:
            return None
