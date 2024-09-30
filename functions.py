import pygame as pg
from sudoku_solver import solve_sudoku


pg.font.init()
font = pg.font.SysFont("Consolas", 30)
bold_font = pg.font.SysFont("Consolas", 30, True)

def convert_to_matrix(grid):
    return [grid[i : i + 9]for i in range(0, 81, 9)]

def draw_grid_lines(window):
    for i in range(0, 451, 50):
        if i not in [150, 300]:
            pg.draw.line(window, (0, 0, 0),(0, i),(450, i),1)
    for j in range(0, 451, 50):
        if j not in [150, 300]:
            pg.draw.line(window, (0, 0, 0), (j, 0), (j, 450),1)
    for i in [150, 300]:
        pg.draw.line(window, (0, 0, 0),(0, i), (450, i), 2)
    for j in [150, 300]:
        pg.draw.line(window, (0, 0, 0), (j, 0), (j, 450),2)

def draw_hit_box(window, hit_box):
    pg.draw.rect(window, (200, 200, 200), hit_box)

def highlight_cell(window, hit_box_grid, grid=None):
    if grid is None:
        grid = []
    pos = pg.mouse.get_pos()
    for i in range(9):
        for j in range(9):
            if hit_box_grid[i][j].collidepoint(pos):
                if (i, j) not in grid:
                    draw_hit_box(window, hit_box_grid[i][j])

def highlight_selected_cell(window, hit_box_grid, cell):
    i, j = cell
    draw_hit_box(window, hit_box_grid[i][j])

def click_cell(hit_box_grid):
    pos = pg.mouse.get_pos()
    for i in range(9):
        for j in range(9):
            if hit_box_grid[i][j].collidepoint(pos):
                return i, j

def assign_num(grid, ind, user_input):
    if ind is not None:
        i, j = ind
        grid[i][j]=user_input

def get_predefined_numbers_ind(grid):
    indexes=[]
    for i in range(9):
        for j in range(9):
            if grid[i][j]:
                indexes.append((i, j))
    return indexes

def draw_initial_grid_numbers(window, grid, hit_box_grid, indexes):
    global font
    for ind in indexes:
        i, j = ind
        hit_box = hit_box_grid[i][j]
        num = str(grid[i][j])
        text_width, text_height = font.size(num)
        text_surf = bold_font.render(str(grid[i][j]), True, (0, 0, 0))
        window.blit(text_surf, ((hit_box.left + hit_box.right) / 2- text_width / 2, (hit_box.top + hit_box.bottom) / 2 - text_height / 2))

def draw_player_numbers(window, grid, hit_box_grid, indexes):
    for i in range(9):
        for j in range(9):
            if (i, j) not in indexes:
                if grid[i][j] != 0:
                    hit_box = hit_box_grid[i][j]
                    num = str(grid[i][j])
                    text_width, text_height = font.size(num)
                    text_surf = font.render(str(grid[i][j]), True, (50, 30, 150))
                    window.blit(text_surf, ((hit_box.left + hit_box.right) / 2 - text_width / 2, (hit_box.top + hit_box.bottom) / 2 - text_height / 2))

def auto_solve(window, grid, hit_box_grid, indexes):
    for i in range(9):
        for j in range(9):
            if (i, j) not in indexes:
                grid[i][j] = 0
    solve_sudoku(window, grid, hit_box_grid, indexes)

def draw_all(window, grid, hit_box_grid, indexes, selected_cell = None):
    window.fill((255, 255, 255))
    draw_grid_lines(window)
    highlight_cell(window, hit_box_grid, indexes)
    if selected_cell is not None:
        highlight_selected_cell(window, hit_box_grid, selected_cell)
    draw_initial_grid_numbers(window, grid, hit_box_grid, indexes)
    draw_player_numbers(window, grid, hit_box_grid, indexes)
