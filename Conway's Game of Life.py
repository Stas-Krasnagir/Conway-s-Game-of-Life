import random
import time


def create_universe(height, length):
    grid = [[1] * length] * height
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j] = random.randrange(2)
        return grid


length = int(input("Lenght: "))
height = int(input("Height: "))

grid = create_universe(height, length)


# grid = [[0, 0, 0, 1, 0, 0],
#        [0, 1, 1, 1, 0, 0],
#        [0, 0, 1, 0, 1, 0],
#        [0, 1, 1, 0, 1, 0],
#        [0, 1, 0, 1, 0, 0],
#        [0, 0, 0, 0, 0, 0]]


def game_step(grid):
    new_grid = grid.copy()
    for i in range(len(new_grid)):
        for j in range(len(new_grid[0])):
            res = validate(i - 1, j - 1, new_grid) + validate(i - 1, j, new_grid) + \
                  validate(i - 1, j, new_grid) + validate(i, j - 1, new_grid) + \
                  validate(i, j + 1, new_grid) + validate(i + 1, j - 1, new_grid) + \
                  validate(i + 1, j, new_grid) + validate(i + 1, j + 1, new_grid)
            if new_grid[i][j] == 0 and res == 3:
                new_grid[i][j] = 1
            if new_grid[i][j] == 1 and res == 2 or res == 3:
                new_grid[i][j] = 1
            else:
                new_grid[i][j] = 0
    return new_grid


def validate(i, j, new_grid):
    if 0 < i < len(new_grid) and 0 < j < len(new_grid[0]):
        return new_grid[i][j]
    else:
        res = 0
        return res


def output_grid(grid):
    while True:
        print('\n'.join(' '.join(str(x) for x in row) for row in reversed(game_step(grid))))
        time.sleep(1)
        grid = game_step(grid)
        from shutil import get_terminal_size
        print("\n" * get_terminal_size().lines, end='')


print(output_grid(grid))
