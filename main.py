import random

rows = 3
columns = 4
game_grid = [[['', '', ''] for _ in range(columns)] for _ in range(rows)]

icons = ['❤️', '❤️', '❄️', '❄️', '🔵', '🔵', '🟪','🟪', '⭐','⭐', '🔶', '🔶']

def print_game_grid(game_grid):
    grid = '_____________________________\n|      |      |      |      |\n'
    for j in range(rows):
        for i in range(columns):
            if int(game_grid[j][i][0]) <= 9:
                grid = grid + '|   '
            else:
                grid = grid + '|  '
            # print(f'square {game_grid[j][i][0]} flag = {game_grid[j][i][2]}')
            if game_grid[j][i][2] == '0':
                grid = grid + game_grid[j][i][0]
            elif game_grid[j][i][2] == '1':
                # print(f'Square number = {game_grid[j][i][0]}')
                grid = grid + game_grid[j][i][1]
            else:
                grid = grid + ' '

            if i == len(game_grid[0]) - 1:
                if int(game_grid[j][i][0]) <= 9 or (int(game_grid[j][i][0]) > 9 and game_grid[j][i][2] == '2'):
                    grid = grid + '  |'
                else:
                    grid = grid + '  |'
            else:
                if int(game_grid[j][i][0]) <= 9 or (int(game_grid[j][i][0]) > 9 and game_grid[j][i][2] == '2'):
                    grid = grid + '  '
                else:
                    grid = grid + '  '
        if j == len(game_grid) - 1:
            grid = grid + '\n|      |      |      |      |\n_____________________________\n'
        else:
            grid = grid + '\n|      |      |      |      |\n_____________________________\n|      |      |      |      |\n'
    print(grid)

def initialize_grid(grid, pics):
    random.shuffle(pics)
    random.shuffle(pics)
    random.shuffle(pics)
    num = 1
    for i in range(3):
        for j in range(4):
            grid[i][j][0] = str(num)
            grid[i][j][1] = pics[num - 1]
            grid[i][j][2] = str(0)
            num += 1
    return grid

game_grid = initialize_grid(game_grid, icons)
print(game_grid)
print_game_grid(game_grid)
turns = 1
choice_2 = ""
choice_1 = input("Choose a square: \n")
card_1 = int(choice_1) - 1
card_1_row = card_1 // columns
card_1_column = card_1 % columns
square_1_value = game_grid[card_1_row][card_1_column][0]
square_1_pic = game_grid[card_1_row][card_1_column][1]
square_1_flag = game_grid[card_1_row][card_1_column][2]
if square_1_value == choice_1 and square_1_flag != 2:
    game_grid[card_1_row][card_1_column][2] = '1'
    print_game_grid(game_grid)
else:
    print(f"Square {choice_1} is not available! Choose another square")

choice_2 = input("Choose a square: \n")
card_2 = int(choice_2) - 1
card_2_row = card_2 // columns
card_2_column = card_2 % columns
square_2_value = game_grid[card_2_row][card_2_column][0]
square_2_pic = game_grid[card_2_row][card_2_column][1]
square_2_flag = game_grid[card_2_row][card_2_column][2]
if square_2_value == choice_2 and square_2_flag != 2:
    game_grid[card_2_row][card_2_column][2] = '1'
    print_game_grid(game_grid)
else:
    print(f"Square {choice_2} is not available! Choose another square")

if square_1_pic == square_2_pic:
    print("The cards match!")
    game_grid[card_1_row][card_1_column][2] = '2'
    game_grid[card_2_row][card_2_column][2] = '2'
    print(game_grid)
    input("Press any key to continue...")
    # print('Now print grid')
    print_game_grid(game_grid)
else:
    print("The cards do not match!")
    game_grid[card_1_row][card_1_column][2] = '0'
    game_grid[card_2_row][card_2_column][2] = '0'
    input("Press any key to continue...")
    print(game_grid)
    print('Now print grid')
    print_game_grid(game_grid)
