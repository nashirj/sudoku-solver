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
        # validate squares
        for i in range(self.num_squares):
            for j in range(self.num_squares):
                sq_rows = table[self.sq_size*i:self.sq_size*i+self.sq_size]
                sq = [row[self.sq_size*j:self.sq_size*j+self.sq_size] for row in sq_rows]
                if not self.validate_square(sq):
                    print("this square is invalid")
                    print(sq)
                    return False
            
        # validate rows
        for row in table:
            if not self.validate_vector(row):
                print("this row is invalid")
                print(row)
                return False
            
        # validate cols
        for i in range(self.board_size):
            col = [table[j][i] for j in range(self.board_size)]
            if not self.validate_vector(col):
                print("this col is invalid")
                print(col)
                return False
            
        return True

    def reset_nums(self):
        for i in range(1, self.board_size+1):
            self.nums[str(i)] = False

    def solve(self, table):
        '''This is where the magic happens but I'm trying to figure out the right spell!!!
        I can't quite figure out how to backtrack properly.
        '''
        new_table = table.copy()
        for i in range(self.board_size):
            for j in range(self.board_size):
                if new_table[i][j] == '.':
                    for k in range(1, self.board_size+1):
                        new_table[i][j] = str(k)
                        print(new_table)
                        if self.validate(new_table):
                            break
                        # if self.validate(new_table):
                        #     temp = self.solve(new_table)
                        # else:
                        #     new_table[i][j] = '.'
                if not self.validate(table):
                    return None
        if self.validate(new_table):
            return new_table
        else:
            return None


