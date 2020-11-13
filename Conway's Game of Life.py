import random, time


def create_universe(height, length):
    grid = [[0] * length] * height
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j] = random.randrange(2)
    return grid


length = 5
height = 5
#grid = create_universe(height, length)

grid = [[0, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 1, 0],
        [0, 0, 1, 1, 1, 1],
        [0, 1, 1, 1, 0, 0],
        [1, 1, 0, 1, 1, 0],
        [0, 0, 0, 1, 0, 1]]


def game_step(grid):
    new_grid = grid.copy()
    for i in range(len(new_grid)):
        for j in range(len(new_grid[0])):
            a = validate(i - 1, j - 1, new_grid)
            b = validate(i - 1, j, new_grid)
            c = validate(i - 1, j, new_grid)

            d = validate(i, j - 1, new_grid)
            e = validate(i, j + 1, new_grid)

            f = validate(i + 1, j - 1, new_grid)
            g = validate(i + 1, j, new_grid)
            h = validate(i + 1, j + 1, new_grid)

            if new_grid[i][j] == 0:
                res_for_dead = a + b + c + d + e + f + g + h
                if res_for_dead == 3:
                    new_grid[i][j] = 1
            if new_grid[i][j] == 1:
                res_for_life = a + b + c + d + e + f + g + h
                if res_for_life == 2 or res_for_life == 3:
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


print(grid)
time.sleep(1)
count = 0
while count < 5:
    print(game_step(grid))
    time.sleep(1)
    grid = game_step(grid)
    count += 1
