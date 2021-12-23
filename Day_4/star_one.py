class board_element:

    def __init__(self, value):
        self.value = value
        self.called = False

    def __str__(self):
        return str(self.value) + " :: "  + str(self.called)


file = open("input.txt")
lines = file.readlines()

draws = lines[0].split(",")

board_input = [lines[i] for i in range(1, len(lines))]

board_num = len(board_input) / 6

boards = []

# for each board input given
# 1. create a new board
# 2. add the rows to the board
# 3. add the completed board to the list of boards
for i in range(1, len(lines)-1, 6):

    board = []

    #print(f"------------ board :: {(i-1)/6} ------------")

    for j in range(0, 5):
        print(f"i :: {i}  j :: {j}")
        row_raw = board_input[i + j]
        #print(row_raw)
        row_parsed = []
        for k in range(0,13,3):
            newEntry = board_element(int(row_raw[k]+row_raw[k+1]))
            #print(newEntry)
            row_parsed.append(newEntry)
        #print(row_parsed)
        board.append(row_parsed)

    boards.append(board)

i = 0
breaker = True
while i < len(boards) and breaker:



