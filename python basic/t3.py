'''

Imagine a square chessboard. 
The queen (or queen) can move vertically, horizontally and diagonally any number of cells. 
Based on the coordinates of the two squares, 
determine whether the queen can move from the first to the second in one move. 
If it can, print YES. Otherwise, print NO. The program gets 4 whole numbers from 1 to 8. 
The first and the second one give the column and the row for the first square, the third and the fourth for the second square.   
 
Entry example #1
1
1
2
2
Example result #1
YES
Entry example #2
1
1
8
2
Example result #2
NO

'''

column = int(input())
row = int(input())
next_column = int(input())
next_row = int(input())

if column == next_column or row == next_row or abs(column - next_column) == abs(row - next_row):
	result = 'YES'
else:
	result = 'NO'
print(result)
