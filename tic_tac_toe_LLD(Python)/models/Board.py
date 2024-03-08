from Cell import Cell

class Board:
    def __init__(self, dimension):
        self.board = [[Cell(i, j) for j in range(dimension)] for i in range(dimension)]

    def display(self):
        for row in self.board:
            for cell in row:
                if cell.get_cell_state() == "EMPTY":
                    print("|   |", end="")
                else:
                    print(f"| {cell.get_player().get_symbol()} |", end="")
            print("\n")

    def get_board(self):
        return self.board

    def set_board(self, board):
        self.board = board
