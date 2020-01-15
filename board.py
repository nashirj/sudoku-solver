'''Board module, contains board class.
'''
import tkinter
import solver

class Board:
    '''Class used to represent a puzzle as a 2D array of rows and columns.
    '''
    def __init__(self, puzzle_str):
        '''Parse the input string, and initialize a boolean flag.
        self.solved is used to indicate whether or not the Board has been solved.
        '''

        self.table = [[puzzle_str[i+9*j] for i in range(9)] for j in range(9)]
        self.solved = False

    def __init__(self, puzzle_str):
        self.puzzle_str = puzzle_str
        self.root_window = tkinter.Tk()
        self.root_window.title("Sudoku")

        self.label = tkinter.Label(master=self.root_window,
                            text="Unsolved puzzle",
                            width="12",
                            height="1")
        self.label.pack(side=tkinter.TOP)
        self.label_state = True

        self.button = tkinter.Button(master=self.root_window, 
                        text="Solve puzzle",
                        fg="red",
                        command=self.solve_puzzle)
        self.button.pack(side=tkinter.TOP)

        self.grid = tkinter.Frame(self.root_window)
        self.grid.pack(side=tkinter.BOTTOM)

        self.size = 9
        self.table = [[puzzle_str[i+self.size*j] for i in range(self.size)] for j in range(self.size)]
        
        for row in range(self.size):
            for col in range(self.size):
                label = tkinter.Label(self.grid,
                    relief=tkinter.RAISED, # raised border
                    padx=10, # make label wide
                    width=2,
                    height=2,
                    text=self.table[row][col]) # label text
                # place label in row r and column c
                label.grid(row=row, column=col)

        self.sol = solver.Solver(9, 3)
        self.solved_table = None

        self.root_window.mainloop()

    def reset_board(self):
        # pass
        self.table = [[self.puzzle_str[i+9*j] for i in range(9)] for j in range(9)]
        for row in range(self.size):
            for col in range(self.size):
                label = tkinter.Label(self.grid,
                    relief=tkinter.RAISED, # raised border
                    padx=10, # make label wide
                    width=2,
                    height=2,
                    text=self.table[row][col]) # label text
                # place label in row r and column c
                label.grid(row=row, column=col)

        self.solved = False

    def solve_puzzle(self):
        if self.label_state:
            self.label["text"] = "Solved puzzle"
            self.button["text"] = "Reset puzzle"
            if self.solved_table:
                self.table = self.solved_table
            else:
                self.sol.solve(self)
                self.solved_table = self.table
        else:
            self.label["text"] = "Unsolved puzzle"
            self.button["text"] = "Solve puzzle"
            self.reset_board()
        self.label_state = not self.label_state
        if self.solved:
            for row in range(self.size):
                for col in range(self.size):
                    label = tkinter.Label(self.grid,
                        relief=tkinter.RAISED, # raised border
                        padx=10, # make label wide
                        width=2,
                        height=2,
                        text=self.table[row][col]) # label text
                    # place label in row r and column c
                    label.grid(row=row, column=col)
        else:
            print("no solution to this puzzle")

    def is_solved(self):
        '''Getter for self.solved.
        '''
        return self.solved

    def get_table(self):
        '''Getter for self.table.
        '''
        return self.table
