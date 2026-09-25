import random

rows = 3
cols = 4
game_grid = [[['', ''] for _ in range(cols)] for _ in range(rows)]

icons = ['❤️', '❤️', '❄️', '❄️', '🔵', '🔵', '🟪','🟪', '⭐','⭐', '🔶', '🔶']

def print_game_grid(game_grid):
    grid = f"""
 {game_grid[0][0][0]}   | {game_grid[0][1][0]}   | {game_grid[0][2][0]}   | {game_grid[0][3][0]}\n_____|_____|_____|_____
 {game_grid[1][0][0]}   | {game_grid[1][1][0]}   | {game_grid[1][2][0]}   | {game_grid[1][3][0]}\n_____|_____|_____|_____
 {game_grid[2][0][0]}   | {game_grid[2][1][0]}  | {game_grid[2][2][0]}  | {game_grid[2][3][0]}\n     |     |     |"""
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
