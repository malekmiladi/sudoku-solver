if __name__ == "__main__":
    from os import environ
    from sys import exit
    from functions import *
    import pygame as pg

    environ["SDL_VIDEO_CENTERED"] = "1"
    pg.init()

    wn = pg.display.set_mode((451, 451))
    pg.display.set_caption("Sudoku!")

    #TODO: build sudoku pyzzle generator
    #TODO: check puzzle when user finishes filling the numbers, and display a text if it's correct

    # GAME CONSTANTS
    grid_hardest = [
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 6, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 9, 0, 2, 0, 0],

        [0, 5, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 4, 5, 7, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 3, 0],

        [0, 0, 1, 0, 0, 0, 0, 6, 8],
        [0, 0, 8, 5, 0, 0, 0, 1, 0],
        [0, 9, 0, 0, 0, 0, 4, 0, 0]
    ]
    grid2 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],

        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],

        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    grid = [
        [0,0,0,0,0,1,2,0,0],
        [0,0,0,0,0,0,3,4,0],
        [0,0,0,0,0,0,0,5,6],
        [0,0,0,0,0,0,0,0,7],
        [0,0,0,0,0,0,0,0,0],
        [1,0,0,0,0,0,0,0,0],
        [7,2,0,0,0,0,0,0,0],
        [0,4,8,0,0,0,0,0,0],
        [0,0,6,3,0,0,0,0,0]
    ]

    hit_box_grid = convert_to_matrix(
        [pg.Rect(i - 1, j - 1, 49, 49) for j in range(2, 451, 50) for i in range(2, 451, 50)]
    )
    predefined_number_ind = get_predefined_numbers_ind(grid)
    click = False
    user_input = None
    selected_cell = None
    solve = False

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if pg.mouse.get_pressed()[0]:
                    selected_cell = click_cell(hit_box_grid)
                    click = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    selected_cell = None
                    solve = True
                    click = False
                if click:
                    if event.key == pg.K_KP1 or event.key == pg.K_1:
                        user_input = 1
                    elif event.key == pg.K_KP2 or event.key == pg.K_2:
                        user_input = 2
                    elif event.key == pg.K_KP3 or event.key == pg.K_3:
                        user_input = 3
                    elif event.key == pg.K_KP4 or event.key == pg.K_4:
                        user_input = 4
                    elif event.key == pg.K_KP5 or event.key == pg.K_5:
                        user_input = 5
                    elif event.key == pg.K_KP6 or event.key == pg.K_6:
                        user_input = 6
                    elif event.key == pg.K_KP7 or event.key == pg.K_7:
                        user_input = 7
                    elif event.key == pg.K_KP8 or event.key == pg.K_8:
                        user_input = 8
                    elif event.key == pg.K_KP9 or event.key == pg.K_9:
                        user_input = 9

        draw_all(wn, grid, hit_box_grid, predefined_number_ind, selected_cell)
        if solve:
            auto_solve(wn, grid, hit_box_grid, predefined_number_ind)
        if click:
            if selected_cell is not None and selected_cell not in predefined_number_ind and user_input is not None:
                assign_num(grid, selected_cell, user_input)
                user_input = None
                click = False
                selected_cell = None

        solve = False
        pg.display.update()
