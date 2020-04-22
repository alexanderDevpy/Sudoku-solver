import numpy as np
import random
import json

# create initial board
board = np.zeros((9, 3, 3), dtype=np.int16)


def draw_table(board):
    for y, z in enumerate(board, 1):
        if y % 3 == 0:

            for a, b, c in zip(board[y - 3], board[y - 2], board[y - 1]):
                print("|", *a, "|", *b, "|", *c, "|")
            print('-------------------------')
    print("################## New ##################")


def poptable(numbers):
    '''Populate the board with number from game.json'''
    for key, value in numbers.items():
        table, row, column = key.split(',')
        board[int(table), int(row), int(column)] = value
    return board


def solution_bord(initial_board):
    '''
    Solve the puzzel

    '''
    board = initial_board.copy()
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    pozition = []
    table, row, column = 0, 0, 0
    while True:

        if initial_board[table][row][column] != 0:
            if column == 2:
                if row < 2:
                    row += 1
                    column = 0
                    continue
                else:
                    if table < 8:
                        table += 1
                        row = 0
                        column = 0
                        continue

                    elif table == 8 and row == 2 and column == 2:

                        break
            else:
                column += 1
                continue

        elif board[table][row][column] == 0:

            a = [[table, row, column], [0]]

            pozition.append(a)

            if column == 2:
                if row < 2:
                    row += 1
                    column = 0
                    continue
                else:
                    if table < 8:
                        table += 1
                        row = 0
                        column = 0
                        continue

                    elif table == 8 and row == 2 and column == 2:
                        print('final')
                        break
            else:
                column += 1
                continue

    conter = 0
    steep = 0
    while True:

        steep += 1
        if steep > 100000:
            return False

        if conter == len(pozition):
            wining = win(board)
            if wining:
                draw_table(board)

                break
            else:
                continue

        table, row, column = pozition[conter][0]

        if 0 in pozition[conter][1]:
            for nums in numbers:
                if board[table][row][column] == 0:
                    if nums == 10:
                        if conter > 0:

                            pozition[conter - 1][1][0] = 0
                            conter -= 1

                            break
                        elif conter == 0:
                            break

                        break
                    if nums in board[table]:
                        continue
                    else:

                        che = check_table(board, table, row, column, nums)
                        if che:
                            continue
                        else:

                            board[table][row][column] = nums
                            pozition[conter][1][0] = nums
                            conter += 1
                            break
                else:

                    if nums == 10:
                        board[table][row][column] = 0
                        if conter > 0:

                            pozition[conter - 1][1][0] = 0
                            conter -= 1
                            break
                        elif conter == 0:
                            break

                    if nums <= board[table][row][column]:
                        continue
                    if nums in board[table]:
                        continue
                    else:

                        che = check_table(board, table, row, column, nums)
                        if che:
                            continue
                        else:

                            board[table][row][column] = nums
                            pozition[conter][1][0] = nums
                            conter += 1
                            break
        else:
            wining = win(board)
            if wining:
                break
            else:
                continue
    return True


def check_table(board, table, row, column, number):
    '''
    check if a number is unique in row and column
    '''
    # if number in board[table]:
    # return True
    board = board.copy()
    board[table][row][column] = 0
    if table <= 2:
        if number in board[0][row] or number in board[1][row] or number in board[2][row]:
            return True
    elif table <= 5:
        if number in board[3][row] or number in board[4][row] or number in board[5][row]:
            return True
    elif table <= 8:
        if number in board[6][row] or number in board[7][row] or number in board[8][row]:
            return True
    for x in range(2):
        for y in range(3):
            if table in [0, 1, 2]:
                if x == 0:
                    if number == board[table + 3][y][column]:
                        return True
                elif x == 1:
                    if number == board[table + 6][y][column]:
                        return True
            if table in [3, 4, 5]:
                if x == 0:
                    if number == board[table - 3][y][column]:
                        return True
                elif x == 1:
                    if number == board[table + 3][y][column]:
                        return True
            if table in [6, 7, 8]:
                if x == 0:
                    if number == board[table - 3][y][column]:
                        return True
                elif x == 1:
                    if number == board[table - 6][y][column]:
                        return True

    return False


def win(board):
    '''
    Check board to see if player win.
    '''
    for table in range(9):
        for row in range(3):
            for colmn in range(3):
                if 0 in board:

                    return False
                else:
                    chhh = check_table(board, table, row, colmn, board[table][row][colmn])
                    if chhh:
                        return False
                    else:
                        continue
    return True


def populate_table(pozition):
    '''
    Generate a random sudoku puzzel. Not valid 100 % of time
    '''
    for x in range(pozition):

        while True:
            table = random.randint(0, 8)
            row = random.randint(0, 2)
            column = random.randint(0, 2)
            nums = random.randint(1, 9)
            checkIfExist = check_table(board, table, row, column, nums)
            if nums in board[table]:
                continue
            if checkIfExist:
                continue
            else:

                board[table][row][column] = nums
                break
    return board

with open('games.json') as f:
  data = json.load(f)

draw_table(board)
b = poptable(data["puzzels"][random.randint(0,len(data["puzzels"])-1)])
draw_table(b)
solution_bord(b)