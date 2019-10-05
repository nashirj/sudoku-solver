class Solver:
    def __init__(self, board_size):
        self.nums = {}
        self.board_size = board_size
        self.reset_nums()

    @staticmethod
    def validate_row(board, row_num):
        self.reset_nums()
        for val in board[row_num][:]:
            if val != '.':
                if self.nums[val] == False:
                    self.nums[val] == True
                else:
                    return False
        return True

    @staticmethod
    def validate_col(board, col_num):
        self.reset_nums()
        for val in board[:][col_num]:
            if val != '.':
                if self.nums[val] == False:
                    self.nums[val] == True
                else:
                    return False
        return True

    @staticmethod
    def validate_square(board, start_row):
        self.reset_nums()
        for val in board[:][col_num]:
            if val != '.':
                if self.nums[val] == False:
                    self.nums[val] == True
                else:
                    return False
        return True

    @staticmethod
    def reset_nums():
        for i in range(self.board_size):
            self.nums[str(i)] = False