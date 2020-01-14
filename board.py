'''Board module, contains board class.
'''
class Board:
    '''Class used to represent a puzzle as a 2D array of rows and columns.
    '''
    def __init__(self, puzzle_str):
        '''Parse the input string, and initialize a boolean flag.
        self.solved is used to indicate whether or not the Board has been solved.
        '''

        self.table = [[puzzle_str[i+9*j] for i in range(9)] for j in range(9)]
        self.solved = False

    def is_solved(self):
        '''Getter for self.solved.
        '''
        return self.solved

    def get_table(self):
        '''Getter for self.table.
        '''
        return self.table
