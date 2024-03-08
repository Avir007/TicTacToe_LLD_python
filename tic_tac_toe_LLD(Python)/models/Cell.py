class Cell:
    def __init__(self, row, col):
        self.player = None
        self.row = row
        self.col = col
        self.cell_state = CellState.EMPTY

    def get_player(self):
        return self.player

    def set_player(self, player):
        self.player = player

    def get_row(self):
        return self.row

    def set_row(self, row):
        self.row = row

    def get_col(self):
        return self.col

    def set_col(self, col):
        self.col = col

    def get_cell_state(self):
        return self.cell_state

    def set_cell_state(self, cell_state):
        self.cell_state = cell_state
