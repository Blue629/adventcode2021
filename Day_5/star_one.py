file = open("input.txt")
lines = file.readlines()

#init our board
board = []

for i in range(1000):
    column = []
    for j in range(1000):
        column.append(0)
    board.append(column)

#if we have a common value then make a line
for line in lines:

    parsed = line.split(" ")

    initialVals = parsed[0].split(",")

    endVals = parsed[2].split(",")

    x1 = int(initialVals[0])
    y1 = int(initialVals[1])

    x2 = int(endVals[0])
    y2 = int(endVals[1])

    if x1 == x2:
        for i in range(y1, y2 + 1):
            board[x1][i] = board[x1][i] + 1

    if y1 == y2:
        for i in range(x1, x2 + 1):
            board[i][y1] = board[i][y1] + 1

count = 0
for i in range(1000):
    for j in range(1000):
        if board[i][j] > 1:
            count = count + 1

print(count)







    

