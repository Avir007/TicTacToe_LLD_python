from strategies.gamewinningstrategy import GameWinningStrategy

class OrderOneGameWinningStrategy(GameWinningStrategy):
    def __init__(self, dimension):
        self.row_symbol_counts = [{} for _ in range(dimension)]
        self.col_symbol_counts = [{} for _ in range(dimension)]
        self.top_left_diag_symbol_counts = {}
        self.top_right_diag_symbol_counts = {}

    def is_cell_on_top_left_diag(self, row, col):
        return row == col

    def is_cell_on_top_right_diag(self, row, col, dimension):
        return row + col == dimension - 1

    def check_winner(self, board, last_move_player, move_cell):
        symbol = move_cell.get_player().get_symbol()
        row = move_cell.get_row()
        col = move_cell.get_col()
        dimension = len(board.get_board())

        self.row_symbol_counts[row][symbol] = self.row_symbol_counts[row].get(symbol, 0) + 1
        self.col_symbol_counts[col][symbol] = self.col_symbol_counts[col].get(symbol, 0) + 1

        if self.is_cell_on_top_left_diag(row, col):
            self.top_left_diag_symbol_counts[symbol] = self.top_left_diag_symbol_counts.get(symbol, 0) + 1

        if self.is_cell_on_top_right_diag(row, col, dimension):
            self.top_right_diag_symbol_counts[symbol] = self.top_right_diag_symbol_counts.get(symbol, 0) + 1

        if (
            self.row_symbol_counts[row][symbol] == dimension or
            self.col_symbol_counts[col][symbol] == dimension
        ):
            return True

        if (
            self.is_cell_on_top_right_diag(row, col, dimension) and
            self.top_right_diag_symbol_counts[symbol] == dimension
        ):
            return True

        if (
            self.is_cell_on_top_left_diag(row, col) and
            self.top_left_diag_symbol_counts[symbol] == dimension
        ):
            return True

        return False
