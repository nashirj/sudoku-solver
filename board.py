class Board:
    def __init__(self, puzzle_str):
        self.table = [None]*9
        for i in range(len(puzzle_str) // 9):
            self.table[i] = [puzzle_str[i*9:(i+1)*9]]
        # for t in self.table:
        #     print(t)
