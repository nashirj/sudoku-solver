'''
 A1 A2 A3| A4 A5 A6| A7 A8 A9    4 . . |. . . |8 . 5     4 1 7 |3 6 9 |8 2 5 
 B1 B2 B3| B4 B5 B6| B7 B8 B9    . 3 . |. . . |. . .     6 3 2 |1 5 8 |9 4 7
 C1 C2 C3| C4 C5 C6| C7 C8 C9    . . . |7 . . |. . .     9 5 8 |7 2 4 |3 1 6 
---------+---------+---------    ------+------+------    ------+------+------
 D1 D2 D3| D4 D5 D6| D7 D8 D9    . 2 . |. . . |. 6 .     8 2 5 |4 3 7 |1 6 9 
 E1 E2 E3| E4 E5 E6| E7 E8 E9    . . . |. 8 . |4 . .     7 9 1 |5 8 6 |4 3 2 
 F1 F2 F3| F4 F5 F6| F7 F8 F9    . . . |. 1 . |. . .     3 4 6 |9 1 2 |7 5 8 
---------+---------+---------    ------+------+------    ------+------+------
 G1 G2 G3| G4 G5 G6| G7 G8 G9    . . . |6 . 3 |. 7 .     2 8 9 |6 4 3 |5 7 1 
 H1 H2 H3| H4 H5 H6| H7 H8 H9    5 . . |2 . . |. . .     5 7 3 |2 9 1 |6 8 4 
 I1 I2 I3| I4 I5 I6| I7 I8 I9    1 . 4 |. . . |. . .     1 6 4 |8 7 5 |2 9 3 
'''

# row = ['.']*9
# table = [row.copy() for i in row]
# table[0][0] = '4'
# table[0][6] = '8'
# table[0][8] = '5'
# table[1][1] = '3'
# table[2][3] = '7'
# table[3][1] = '2'
# table[3][7] = '6'
# table[4][4] = '8'
# table[4][6] = '4'
# table[4][6] = '4'
puzzle = "4 . . . . . 8 . 5 . 3 . . . . . . . . . . 7 . . . . . . 2 . . . . . 6 . . . . . 8 . 4 . . . . . . 1 . . . . . . . 6 . 3 . 7 .  5 . . 2 . . . . . 1 . 4 . . . . . ."
row = puzzle.split()
table = [None]*9
for i in range(len(row) // 9):
    table[i] = [row[i*9:(i+1)*9]]
for t in table:
    print(t)