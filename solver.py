import board

class Solver:
    def __init__(self, board_size, sq_size):
        self.nums = {}
        self.board_size = board_size
        self.sq_size = sq_size
        self.num_squares = self.board_size//self.sq_size
        self.reset_nums()

    def validate_vector(self, vector):
        self.reset_nums()
        for val in vector:
            if val == '0':
                continue
            if self.nums[val]:
                return False
            else:
                self.nums[val] = True
        return True

    def validate_square(self, square):
        self.reset_nums()
        for row in square:
            for val in row:
                if val == '0':
                    continue
                if self.nums[val]:
                    return False
                else:
                    self.nums[val] = True
        return True

    def validate(self, table):
        if table is None:
            return False

        # validate squares
        for i in range(self.num_squares):
            for j in range(self.num_squares):
                sq_rows = table[self.sq_size*i:self.sq_size*i+self.sq_size]
                sq = [row[self.sq_size*j:self.sq_size*j+self.sq_size] for row in sq_rows]
                if not self.validate_square(sq):
                    return False
            
        # validate rows
        for row in table:
            if not self.validate_vector(row):
                return False
            
        # validate cols
        for i in range(self.board_size):
            col = [table[j][i] for j in range(self.board_size)]
            if not self.validate_vector(col):
                return False
            
        return True

    def reset_nums(self):
        for i in range(1, self.board_size+1):
            self.nums[str(i)] = False

    def find_unsolved(self, b):
        for row in range(self.board_size):
            for col in range(self.board_size):
                if b.table[row][col] == '0':
                    return row, col

        return -1, -1

    def solve(self, b):
        if not self.validate(b.table):
            b.solved = False
            return

        row, col = self.find_unsolved(b)
        if row == -1 and col == -1: # we solved it!
            b.solved = True
            return

        for k in range(1, self.board_size+1):
            b.table[row][col] = str(k)
            # if this value is valid, recurse
            self.solve(b)
            if b.solved:
                return
            b.table[row][col] = '0' # reset val if it isn't valid

        return

