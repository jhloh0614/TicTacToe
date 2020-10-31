# write your code here
# write your code here
cells = input()

print("-" * 9)
print("|", " " * 5, "|")
print("|", " " * 5, "|")
print("|", " " * 5, "|")
print("-" * 9)

win_condition = [[[0, 0], [1, 0], [2, 0]], [[0, 1], [1, 1], [2, 1]], [[0, 2], [1, 2], [2, 2]],
                 [[0, 0], [0, 1], [0, 2]], [[1, 0], [1, 1], [1, 2]], [[2, 0], [2, 1], [2, 2]],
                 [[0, 0], [1, 1], [2, 2]], [[0, 2], [1, 1], [2, 0]]]
x_coord = []
o_coord = []
empty_coord = []
x = 0
o = 0
empty = 0
state = 0

n = 0
for i in range(9):
    if i != 0 and i % 3 == 0:
        n += 1
    empty_coord.append([n, i % 3])
    empty += 1

'''
def win(list1):
    for coords in win_condition:
        intersect = [value for value in coords if value in list1]
        if intersect == coords:
            return True
        return any([[value for value in coords if value in list1] == coords for coords in win_condition])
    return False
'''


def win(list1):
    return any([[value for value in coords if value in list1] == coords for coords in win_condition])
    # find intersection between list1 coords with win_condition
    # if any is true means win


while True:
    while True:
        move_col, move_row = input("Enter the coordinates: ").split()
        if move_col.isdigit() and move_row.isdigit():
            if (1 <= int(move_col) <= 3) and (1 <= int(move_row) <= 3):
                move_col = int(move_col) - 1
                move_row = 3 - int(move_row)
                move = [move_row, move_col]
                if move in empty_coord:
                    empty_coord.remove(move)
                    if state == 0:
                        x_coord.append(move)
                        state = 1
                    else:
                        o_coord.append(move)
                        state = 0
                    break
                else:
                    print("This cell is occupied! Choose another one!")
            else:
                print("Coordinates should be from 1 to 3!")
        else:
            print("You should enter numbers!")

    print("-" * 9)
    for row in range(3):
        print("|", end=" ")
        for col in range(3):
            pos = [row, col]
            if pos in x_coord:
                print("X", end=" ")
            elif pos in o_coord:
                print("O", end=" ")
            else:
                print(" ", end=" ")
        print("|")
    print("-" * 9)

    if win(x_coord):
        print("X wins")
        break
    elif win(o_coord):
        print("O wins")
        break
    elif not bool(empty_coord):
        print("Draw")
        break








