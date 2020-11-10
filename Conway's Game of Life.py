def create_universe(height, length):
    grid = [[0] * length] * height
    return grid


length = 5
height = 10


def game_step(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                res_for_dead = validate(grid[i - 1][j - 1]) + validate(grid[i - 1][j]) + validate(grid[i - 1][j + 1]) + \
                               validate(grid[i][j - 1]) + validate(grid[i][j + 1]) + \
                               validate(grid[i + 1][j - 1]) + validate(grid[i + 1][j]) + validate(grid[i + 1][j + 1])
                if res_for_dead == 3:
                    grid[i][j] = 1
            if grid[i][j] == 1:
                res_for_life = validate(grid[i - 1][j - 1]) + validate(grid[i - 1][j]) + validate(grid[i - 1][j + 1]) + \
                               validate(grid[i][j - 1]) + validate(grid[i][j + 1]) + \
                               validate(grid[i + 1][j - 1]) + validate(grid[i + 1][j]) + validate(grid[i + 1][j + 1])
                if res_for_life == 2 or res_for_life == 3:
                    grid[i][j] = 1
                else:
                    grid[i][j] = 0
    return grid


grid = [[0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0]]
row = len(grid)
column = len(grid[0])

def validate(grid):
    if grid < 0:
        res = 0
        return res
    else:
        return grid

print(game_step(grid))


#and i > 0 and i < len(grid) and j > 0 and j < len(grid[0])
#grid[i - 1][j - 1] + grid[i - 1][j] + grid[i - 1][j + 1] + grid[i][j - 1] + grid[i][j + 1] + grid[i + 1][j - 1] + grid[i + 1][j] + grid[i + 1][j + 1]