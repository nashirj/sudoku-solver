class Board:
    def __init__(self, puzzle_str):
        self.table = [[puzzle_str[i+9*j] for i in range(9)] for j in range(9)]
        self.solved = False
        