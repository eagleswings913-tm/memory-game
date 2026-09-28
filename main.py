import random
from itertools import product
import os

while True:
    difficulty = input("Choose a difficulty ( e (easy), m (medium), h (hard): \n")
    if difficulty == 'e':
        game_rows = 3
        game_columns = 4
        break
    elif difficulty == 'm':
        game_rows = 4
        game_columns = 6
        break
    elif difficulty == 'h':
        game_rows = 6
        game_columns = 6
        break
    print("Please enter e (easy), m (medium), h (hard): \n")

game_grid = [[['', '', ''] for _ in range(game_columns)] for _ in range(game_rows)]

icons = ['❤️', '❤️', '❄️', '❄️', '🔵', '🔵', '🟪','🟪', '🔴','🔴', '🔶', '🔶']
icons_medium = ['❤️', '❤️', '❄️', '❄️', '🔵', '🔵', '🟪','🟪', '🔴','🔴', '🔶', '🔶'
               ,'💙', '💙', '🟥', '🟥', '🟡', '🟡', '🟨','🟨', '💚','💚', '🔷', '🔷']
icons_hard = ['❤️', '❤️', '❄️', '❄️', '🔵', '🔵', '🟪','🟪', '🔴','🔴', '🔶', '🔶'
             ,'💙', '💙', '🟥', '🟥', '🟡', '🟡', '🟨','🟨', '💚','💚', '🔷', '🔷'
             ,'💛', '💛', '🟦', '🟦', '🟢', '🟢', '🟩','🟩', '🧡','🧡', '♦️', '♦️']
# more icons 🟠🟡🟢🟣🟥🟧🟨🟩🟦♦️🔷🧡💛💚💜💙🤍

def print_game_grid(card_grid):
    grid_rows = len(card_grid)
    grid_columns = len(card_grid[0])
    grid_begin_e = '_____________________________\n|      |      |      |      |\n'
    grid_begin_m_l = '___________________________________________\n|      |      |      |      |      |      |\n'
    grid_middle_e = '\n|      |      |      |      |\n_____________________________\n|      |      |      |      |\n'
    grid_middle_m_l = '\n|      |      |      |      |      |      |\n___________________________________________\n|      |      |      |      |      |      |\n'
    grid_end_e = '\n|      |      |      |      |\n_____________________________\n'
    grid_end_m_l = '\n|      |      |      |      |      |      |\n___________________________________________\n'
    if grid_columns == 6:
        grid = grid_begin_m_l
    else:
        grid = grid_begin_e

    for row in range(grid_rows):
        for column in range(grid_columns):
            if int(card_grid[row][column][0]) <= 9:
                if card_grid[row][column][2] == '1':
                    grid = grid + '|  '
                else:
                    grid = grid + '|   '
            else:
                grid = grid + '|  '

            if card_grid[row][column][2] == '0':
                grid = grid + card_grid[row][column][0]
            elif card_grid[row][column][2] == '1':
                grid = grid + card_grid[row][column][1]
            elif card_grid[row][column][2] == '2' and int(card_grid[row][column][0]) <= 9:
                grid = grid + ' '
            else:
                grid = grid + '  '

            if column == len(card_grid[0]) - 1:
                if int(card_grid[row][column][0]) <= 9 or (int(card_grid[row][column][0]) > 9 and card_grid[row][column][2] == '2'):
                    grid = grid + '  |'
                else:
                    grid = grid + '  |'
            else:
                if int(card_grid[row][column][0]) <= 9 or (int(card_grid[row][column][0]) > 9 and card_grid[row][column][2] == '2'):
                    grid = grid + '  '
                else:
                    grid = grid + '  '
        if row == len(card_grid) - 1:
            if grid_columns == 6:
                grid = grid + grid_end_m_l
            else:
                grid = grid + grid_end_e
        else:
            if grid_columns == 6:
                grid = grid + grid_middle_m_l
            else:
                grid = grid + grid_middle_e

    print(grid)

def initialize_grid(grid, pics):
    random.shuffle(pics)
    random.shuffle(pics)
    random.shuffle(pics)
    grid_rows = len(grid)
    grid_columns = len(grid[0])
    num = 1
    for row in range(grid_rows):
        for column in range(grid_columns):
            grid[row][column][0] = str(num)
            grid[row][column][1] = pics[num - 1]
            grid[row][column][2] = str(0)
            num += 1
    return grid
############################################################################
if difficulty == 'e':
    game_grid = initialize_grid(game_grid, icons)
elif difficulty == 'm':
    game_grid = initialize_grid(game_grid, icons_medium)
else:
    game_grid = initialize_grid(game_grid, icons_hard)
# print(game_grid)
print_game_grid(game_grid)
number_of_turn = 0
game_complete = False
while not game_complete:
    number_of_turn += 1
    choice_2 = ""
    while True:
        choice_1 = input("Choose a square: \n")
        card_1 = int(choice_1) - 1
        card_1_row = card_1 // game_columns
        card_1_column = card_1 % game_columns
        square_1_value = game_grid[card_1_row][card_1_column][0]
        square_1_pic = game_grid[card_1_row][card_1_column][1]
        square_1_flag = game_grid[card_1_row][card_1_column][2]
        if square_1_value == choice_1 and square_1_flag != '2':
            game_grid[card_1_row][card_1_column][2] = '1'
            print_game_grid(game_grid)
            break
        else:
            print(f"Square {choice_1} is not available! Choose another square")

    while True:
        choice_2 = input("Choose a square: \n")
        if choice_2 == choice_1:
            print(f"You already chose {choice_2} square! Please choose another square")
        else:
            card_2 = int(choice_2) - 1
            card_2_row = card_2 // game_columns
            card_2_column = card_2 % game_columns
            square_2_value = game_grid[card_2_row][card_2_column][0]
            square_2_pic = game_grid[card_2_row][card_2_column][1]
            square_2_flag = game_grid[card_2_row][card_2_column][2]
            if square_2_value == choice_2 and square_2_flag != '2':
                game_grid[card_2_row][card_2_column][2] = '1'
                print_game_grid(game_grid)
                break
            else:
                print(f"Square {choice_2} is not available! Choose another square")

    if square_1_pic == square_2_pic:
        print("The cards match!")
        game_grid[card_1_row][card_1_column][2] = '2'
        game_grid[card_2_row][card_2_column][2] = '2'
        # print(game_grid)
        input("Press any key to continue...")
        os.system('cls')
        print_game_grid(game_grid)
    else:
        print("The cards do not match!")
        game_grid[card_1_row][card_1_column][2] = '0'
        game_grid[card_2_row][card_2_column][2] = '0'
        # print(game_grid)
        input("Press any key to continue...")
        os.system('cls')
        print_game_grid(game_grid)

    for row1, column1 in product(range(game_rows), range(game_columns)):
        if game_grid[row1][column1][2] == '2':
            continue
        else:
            # print('All cards are not turned!')
            break
    else:
        print('All cards are turned! Game done')
        game_complete = True

print(f'Game completed in {number_of_turn} turns')