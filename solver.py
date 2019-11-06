import board

### FOR DEBUGGING
import time

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
            if val == '.':
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
                if val == '.':
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
                    # print("this square is invalid")
                    # print(sq)
                    return False
            
        # validate rows
        for row in table:
            if not self.validate_vector(row):
                # print("this row is invalid")
                # print(row)
                return False
            
        # validate cols
        for i in range(self.board_size):
            col = [table[j][i] for j in range(self.board_size)]
            if not self.validate_vector(col):
                # print("this col is invalid")
                # print(col)
                return False
            
        return True

    def reset_nums(self):
        for i in range(1, self.board_size+1):
            self.nums[str(i)] = False

    def is_completed(self, table):
        for row in table:
            if '.' in row:
                return False
        return True

    def solve(self, table, i=0, j=0):
        '''This works for 1 row.
        I think it gets weird when backtracking from row i to row i - 1.
        The first row starts out right, and then over time I think it backtracks too far and
        changes the value. Try to figure out why second row skips over the solution, i.e.
        should be 632158947 (see sudokusolver.net).

        '''

        # time.sleep(0.1)
        for t in table:
            print(t)

        # if the current cell isn't solved
        if table[i][j] == '.':
            # try all possible values
            for k in range(1, self.board_size+1):
                table[i][j] = str(k)
                # if this value is valid, recurse
                if self.validate(table):
                    if j < self.board_size - 1:
                        # advance to next column
                        table = self.solve(table, i, j+1)
                    else:
                        # advance to next row
                        table = self.solve(table, i+1, 0)
                    # if self.is_completed(table):
                    #     return table
                # if this value is not valid, try the next value in the loop
            # if we got here, then we tried all numbers up to board size
            # this case is handled in the penultimate conditional, setting table[i][j] = '.' if table is invalid
        else:
            if j < self.board_size - 1:
                # advance to next column
                table = self.solve(table, i, j+1)
            else:
                # advance to next row
                table = self.solve(table, i+1, 0)
            # if self.is_completed(table):
            #     return table
        
        if not self.validate(table):
            table[i][j] = '.'

        return table


