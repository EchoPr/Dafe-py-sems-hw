
# Передалал старт рекурсии, тк могла выходить лажа
# Считаю количество путей в отрицательных числах, чтобы не считать стены за клетку, в которую ведёт один путь

def make_step(grid, i, j):

    up, left = (grid[i - 1][j] if i > 0 and grid[i - 1][j] != 1 else 0), \
                 (grid[i][j - 1] if j > 0 and grid[i][j - 1] != 1 else 0)
    
    grid[i][j] = up + left
    if i == j == 0:
        grid[i][j] = -1

    if i < len(grid) - 1 and grid[i + 1][j] != 1:
        make_step(grid, i + 1, j)

    if j < len(grid[0]) - 1 and grid[i][j + 1] != 1:
        make_step(grid, i, j + 1)
                 

def compute_unique_pathes(grid:list[list[int]]) -> int:
    grid[0][0] = -1

    make_step(grid, 0, 0)

    return abs(grid[-1][-1])

grid = [
 [0, 0, 0],
 [0, 1, 0], 
 [0, 0, 0],
 [0, 1, 0]
]

ans = compute_unique_pathes(grid)
print(*grid, sep='\n')
assert ans == 2
