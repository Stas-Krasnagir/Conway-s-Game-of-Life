import random
import time


def create_universe(height, length):
    zero_grid = []
    for i in range(length):
        zero_grid.append([0] * height)
    return zero_grid

length = int(input("Length: "))
height = int(input("Height: "))
living_cells = int(input("Number of living cells: "))

zero_grid = create_universe(height, length)

def set_living_cells(zero_grid, living_cells):
    life_grid = zero_grid.copy()
    count = 0
    while count < living_cells:
        i = random.randint(0, height - 1)
        j = random.randint(0, length - 1)
        if life_grid[i][j] == 0:
            life_grid[i][j] = 1
            count += 1
    return life_grid
life_grid = set_living_cells(zero_grid, living_cells)

def validate(i, j, new_grid):
    if 0 < i < len(new_grid) and 0 < j < len(new_grid[0]):
        return new_grid[i][j]
    else:
        res = 0
        return res

def game_step(life_grid):
    new_grid = life_grid.copy()
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


new_grid = game_step(life_grid)


def output_grid(new_grid):
    while True:
        print('\n'.join(' '.join(str(x) for x in row) for row in reversed(game_step(new_grid))))
        time.sleep(1)
        new_grid = game_step(new_grid)
        import os
        os.system("clear")

output_grid(new_grid)