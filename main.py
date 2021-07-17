import pygame
from Piece import Piece
from Pieces import Pieces
from Node import Node
import Param as P
from game_functions import game_functions
import time
import sys


def main(WIN, WIDTH, game_functions_inst):
    moves = 0
    selected = False
    piece_to_move = []
    grid = game_functions_inst.make_grid(8, WIDTH)
    while 1:
        pygame.time.delay(50)  # stops cpu dying
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                pos = pygame.mouse.get_pos()
                y, x = game_functions_inst.Find_Node(pos, WIDTH)

                if not selected:
                    try:
                        possible = game_functions_inst.select_moves((game_functions_inst.board[x][y]), (x,y), moves)
                        for positions in possible:
                            row, col = positions
                            grid[row][col].colour = P.BLUE
                        piece_to_move = x,y
                        selected = True
                    except:
                        piece_to_move = []
                        print('Can\'t select')
                    #print(piece_to_move)

                else:
                    try:
                        if game_functions_inst.board[x][y].killable:
                            row, col = piece_to_move  # coordinates of original piece
                            game_functions_inst.board[x][y] = game_functions_inst.board[row][col]
                            game_functions_inst.board[row][col] = '  '
                            game_functions_inst.deselect()
                            game_functions_inst.remove_highlight(grid)
                            game_functions_inst.Do_Move((col, row), (y, x), WIN)
                            moves += 1
                            print(game_functions_inst.convert_to_readable(game_functions_inst.board))
                        else:
                            game_functions_inst.deselect()
                            game_functions_inst.remove_highlight(grid)
                            selected = False
                            print("Deselected")
                    except:
                        if game_functions_inst.board[x][y] == 'x ':
                            row, col = piece_to_move
                            game_functions_inst.board[x][y] = game_functions_inst.board[row][col]
                            game_functions_inst.board[row][col] = '  '
                            game_functions_inst.deselect()
                            game_functions_inst.remove_highlight(grid)
                            game_functions_inst.Do_Move((col, row), (y, x), WIN)
                            moves += 1
                            print(game_functions_inst.convert_to_readable(game_functions_inst.board))
                        else:
                            game_functions_inst.deselect()
                            game_functions_inst.remove_highlight(grid)
                            selected = False
                            print("Invalid move")
                    selected = False

            game_functions_inst.update_display(WIN, grid, 8, WIDTH)

if __name__ == '__main__':

    # Setup the window size and display it
    WIN = pygame.display.set_mode((P.WIDTH, P.WIDTH))

    # Set a caption
    pygame.display.set_caption("Chess")

    game_functions_inst = game_functions()

    game_functions_inst.create_board()

    main(WIN, P.WIDTH, game_functions_inst)