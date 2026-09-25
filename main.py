import random

rows = 3
cols = 4
game_grid = [[['', ''] for _ in range(cols)] for _ in range(rows)]

icons = ['❤️', '❤️', '❄️', '❄️', '🔵', '🔵', '🟪','🟪', '⭐','⭐', '🔶', '🔶']

def print_game_grid(game_grid, card1, card2, match_flag):
    grid = '_____________________________\n|      |      |      |      |\n'
    for j in range(rows):
        for i in range(cols):
            if int(game_grid[j][i][0]) <= 9:
                grid = grid + '|   '
            else:
                grid = grid + '|  '
            if card1 == 0:
               grid = grid + game_grid[j][i][0]
            else:
                if card1 == game_grid[j][i][0] or card2 == game_grid[j][i][0]:
                    if match_flag == 1:
                        if game_grid[j][i][1] == "-":
                            if int(game_grid[j][i][0]) > 9:
                                grid = grid + '--'
                            else:
                                grid = grid + game_grid[j][i][1]
                    else:
                        grid = grid + game_grid[j][i][1]
                else:
                    grid = grid + game_grid[j][i][0]
            if i == len(game_grid[0]) - 1:
                if int(game_grid[j][i][0]) <= 9:
                    grid = grid + '  |'
                else:
                    grid = grid + '  |'
            else:
                if int(game_grid[j][i][0]) <= 9:
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
            num += 1
    return grid

game_grid = initialize_grid(game_grid, icons)

print_game_grid(game_grid, card1 = 0, card2 = 0, match_flag=0)
print(game_grid)
turns = 1
choice_2 = ""
choice_1 = input("Choose a square: \n")
card_1 = int(choice_1) - 1
card_1_row = card_1 // cols
card_1_col = card_1 % cols
square1_value = game_grid[card_1 // cols][card_1 % cols][0]
square1_pic = game_grid[card_1 // cols][card_1 % cols][1]
if square1_value == str(card_1 + 1):
    print_game_grid(game_grid, choice_1, choice_2, 0)

choice_2 = input("Choose a square: \n")
card_2 = int(choice_2) - 1
card_2_row = card_2 // cols
card_2_col = card_2 % cols
square2_value = game_grid[card_2 // cols][card_2 % cols][0]
square2_pic = game_grid[card_2 // cols][card_2 % cols][1]
if square2_value == str(card_2 + 1):
    print_game_grid(game_grid, choice_1, choice_2, 0)

if square1_pic == square2_pic:
    print("The cards match!")
    game_grid[card_1 // cols][card_1 % cols][1] = "-"
    game_grid[card_2 // cols][card_2 % cols][1] = "-"
    print(game_grid)
    input("Press any key to continue...")
    print_game_grid(game_grid, choice_1, choice_2, 1)
else:
    print("The cards do not match!")
    input("Press any key to continue...")
    print_game_grid(game_grid, card1 = 0, card2 = 0, match_flag=0)
