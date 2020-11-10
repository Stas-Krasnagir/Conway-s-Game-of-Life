def game_of_life(height, length):
    grid = [[0] * length] * height
    for i in range(len(length)):
        for j in range(len(height)):
            if grid[i][j] == 0:
                res_for_dead = grid[i-1][j-1] + grid[i-1][j-1] + grid[i-1][j+1] + \
                      grid[i][j-1] + grid[i][j+1] + \
                      grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1]
                if res_for_dead == 3:
                    grid[i][j] = 1
            if grid[i][j] == 1:
                res_for_life = grid[i-1][j-1] + grid[i-1][j-1] + grid[i-1][j+1] + \
                      grid[i][j-1] + grid[i][j+1] + \
                      grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1]
                if res_for_life == 2 or res_for_life == 3:
                    grid[i][j] = 1
                else:
                    grid[i][j] = 0
    return grid


length = 5
height = 10
print(game_of_life(height, length))
