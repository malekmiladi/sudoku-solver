import functions as fn


def find_empty_cell(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j]==0:
                return i, j
    return None

def solve_sudoku(wn, grid,hit_box_grid, indexes):
    fn.draw_all(wn, grid,hit_box_grid, indexes)
    fn.pg.display.update()
    empty_cell = find_empty_cell(grid)
    if not empty_cell:
        return True
    else:
        i, j = empty_cell
        for n in range(1,10):
            if is_valid(grid, i, j, n):
                grid[i][j] = n
                if solve_sudoku(wn, grid, hit_box_grid, indexes):
                    return True
                grid[i][j] = 0
    return None

def get_row(grid, r):
    return grid[r]

def get_column(grid, c):
    return [grid[i][c] for i in range(9)]

def is_valid(grid, r, c, number):
    for i in range(9):
        if grid[i][c] == number:
            return False
    
    for j in range(9):
        if grid[r][j] == number:
            return False
    
    rs, cs = (r // 3) * 3, (c // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[rs + i][cs + j] == number:
                return False
    return True

def solve_row(grid, r, c = 0):
    for j in range(9):
        if grid[r][j] == 0:
            for n in range(1,10):
                if is_valid(grid, r, j, n):
                    grid[r][j] = n
                    if solve_row(grid, r, j):
                        return True
                    grid[r][j] = 0
    return True

def solve_column(grid, c, r=0):
    for i in range(9):
        if grid[r][c] == 0:
            for n in range(1, 10):
                if is_valid(grid, i, c, n):
                    grid[i][c] = n
                    if solve_column(grid, c, i):
                        return True
                    grid[i][c] = 0
    return True