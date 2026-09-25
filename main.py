import random

rows = 3
cols = 4
game_grid = [[['', ''] for _ in range(cols)] for _ in range(rows)]

icons = ['❤️', '❤️', '❄️', '❄️', '🔵', '🔵', '🟪','🟪', '⭐','⭐', '🔶', '🔶']

def print_game_grid(game_grid):
    grid = '_____________________________\n|      |      |      |      |\n'
    for j in range(rows):
        for i in range(cols):
            if int(game_grid[j][i][0]) <= 9:
                grid = grid + '|   '
            else:
                grid = grid + '|  '
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

print_game_grid(game_grid)
