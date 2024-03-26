def compute_unique_pathes(grid:list[list[int]]) -> int:
    if grid[0][0] == 1 or grid[-1][-1] == 1: 
        return 0 

    for i in range(len(grid[0])):
        if grid[0][i] != 1: grid[0][i] = -1
    for i in range(len(grid)):
        if grid[i][0] != 1: grid[i][0] = -1

    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            if grid[i][j] == 1: continue
            
            grid[i][j] = (
                grid[i - 1][j] * (grid[i - 1][j] != 1) +
                grid[i][j - 1] * (grid[i][j - 1] != 1)
            )

    return abs(grid[-1][-1])

grid = [
    [0, 1],
    [1, 0]
]

ans = compute_unique_pathes(grid)
print(*grid, sep='\n')
assert ans == 0
