from Piece import Piece
from Pieces import Pieces
import Param as P
from Node import Node
import pygame


class game_functions():

    def __init__(self):
        self.board = [['  ' for i in range(8)] for i in range(8)]

    def create_board(self):
        print(self)
        self.board[0] = [Piece('b', 'r', 'b_rook.png'), Piece('b', 'kn', 'b_knight.png'), Piece('b', 'b', 'b_bishop.png'), \
                   Piece('b', 'q', 'b_queen.png'), Piece('b', 'k', 'b_king.png'), Piece('b', 'b', 'b_bishop.png'), \
                   Piece('b', 'kn', 'b_knight.png'), Piece('b', 'r', 'b_rook.png')]

        self.board[7] = [Piece('w', 'r', 'w_rook.png'), Piece('w', 'kn', 'w_knight.png'), Piece('w', 'b', 'w_bishop.png'), \
                   Piece('w', 'q', 'w_queen.png'), Piece('w', 'k', 'w_king.png'), Piece('w', 'b', 'w_bishop.png'), \
                   Piece('w', 'kn', 'w_knight.png'), Piece('w', 'r', 'w_rook.png')]

        for i in range(8):
            self.board[1][i] = Piece('b', 'p', 'b_pawn.png')
            self.board[6][i] = Piece('w', 'p', 'w_pawn.png')
        return self.board


    ## returns the input if the input is within the boundaries of the board
    def on_board(self, position):
        if position[0] > -1 and position[1] > -1 and position[0] < 8 and position[1] < 8:
            return True


    ## returns a string that places the rows and columns of the board in a readable manner
    def convert_to_readable(self, dummy):
        output = ''

        for i in self.board:
            for j in i:
                try:
                    output += j.team + j.type + ', '
                except:
                    output += j + ', '
            output += '\n'
        return output


    ## resets "x's" and killable pieces
    def deselect(self):
        for row in range(len(self.board)):
            for column in range(len(self.board[0])):
                if self.board[row][column] == 'x ':
                    self.board[row][column] = '  '
                else:
                    try:
                        self.board[row][column].killable = False
                    except:
                        pass
        return self.convert_to_readable(self.board)


    ## Takes in board as argument then returns 2d array containing positions of valid moves
    def highlight(self, dummy):
        highlighted = []
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 'x ':
                    highlighted.append((i, j))
                else:
                    try:
                        if self.board[i][j].killable:
                            highlighted.append((i, j))
                    except:
                        pass
        return highlighted

    def check_team(self, moves, index):
        row, col = index
        if moves%2 == 0:
            if self.board[row][col].team == 'w':
                return True
            else:
                print('Not your turn.')
                return False
        else:
            if self.board[row][col].team == 'b':
                return True
            else:
                print('Not your turn.')
                return False

    ## This takes in a piece object and its index then runs then checks where that piece can move using separately defined functions for each type of piece.
    def select_moves(self, piece, index, moves):
        if self.check_team(moves, index):
            if piece.type == 'p':
                if piece.team == 'b':
                    return self.highlight(self.pawn_moves_b(index))
                else:

                    return self.highlight(self.pawn_moves_w(index))

            if piece.type == 'k':
                return self.highlight(self.king_moves(index))

            if piece.type == 'r':
                return self.highlight(self.rook_moves(index))

            if piece.type == 'b':
                return self.highlight(self.bishop_moves(index))

            if piece.type == 'q':
                return self.highlight(self.queen_moves(index))

            if piece.type == 'kn':
                return self.highlight(self.knight_moves(index))


    ## Basically, check black and white pawns separately and checks the square above them. If its free that space gets an "x" and if it is occupied by a piece of the opposite team then that piece becomes killable.
    def pawn_moves_b(self, index):
        if index[0] == 1:
            if self.board[index[0] + 2][index[1]] == '  ' and self.board[index[0] + 1][index[1]] == '  ':
                self.board[index[0] + 2][index[1]] = 'x '
        bottom3 = [[index[0] + 1, index[1] + i] for i in range(-1, 2)]

        for positions in bottom3:
            if self.on_board(positions):
                if bottom3.index(positions) % 2 == 0:
                    try:
                        if self.board[positions[0]][positions[1]].team != 'b':
                            self.board[positions[0]][positions[1]].killable = True
                    except:
                        pass
                else:
                    if self.board[positions[0]][positions[1]] == '  ':
                        self.board[positions[0]][positions[1]] = 'x '
        return self.board

    def pawn_moves_w(self, index):
        if index[0] == 6:
            if self.board[index[0] - 2][index[1]] == '  ' and self.board[index[0] - 1][index[1]] == '  ':
                self.board[index[0] - 2][index[1]] = 'x '
        top3 = [[index[0] - 1, index[1] + i] for i in range(-1, 2)]

        for positions in top3:
            if self.on_board(positions):
                if top3.index(positions) % 2 == 0:
                    try:
                        if self.board[positions[0]][positions[1]].team != 'w':
                            self.board[positions[0]][positions[1]].killable = True
                    except:
                        pass
                else:
                    if self.board[positions[0]][positions[1]] == '  ':
                        self.board[positions[0]][positions[1]] = 'x '
        return self.board


    ## This just checks a 3x3 tile surrounding the king. Empty spots get an "x" and pieces of the opposite team become killable.
    def king_moves(self, index):
        for y in range(3):
            for x in range(3):
                if self.on_board((index[0] - 1 + y, index[1] - 1 + x)):
                    if self.board[index[0] - 1 + y][index[1] - 1 + x] == '  ':
                        self.board[index[0] - 1 + y][index[1] - 1 + x] = 'x '
                    else:
                        if self.board[index[0] - 1 + y][index[1] - 1 + x].team != self.board[index[0]][index[1]].team:
                            self.board[index[0] - 1 + y][index[1] - 1 + x].killable = True
        return self.board


    ## This creates 4 lists for up, down, left and right and checks all those spaces for pieces of the opposite team. The list comprehension is pretty long so if you don't get it just msg me.
    def rook_moves(self, index):
        cross = [[[index[0] + i, index[1]] for i in range(1, 8 - index[0])],
                 [[index[0] - i, index[1]] for i in range(1, index[0] + 1)],
                 [[index[0], index[1] + i] for i in range(1, 8 - index[1])],
                 [[index[0], index[1] - i] for i in range(1, index[1] + 1)]]

        for direction in cross:
            for positions in direction:
                if self.on_board(positions):
                    if self.board[positions[0]][positions[1]] == '  ':
                        self.board[positions[0]][positions[1]] = 'x '
                    else:
                        if self.board[positions[0]][positions[1]].team != self.board[index[0]][index[1]].team:
                            self.board[positions[0]][positions[1]].killable = True
                        break
        return self.board


    ## Same as the rook but this time it creates 4 lists for the diagonal directions and so the list comprehension is a little bit trickier.
    def bishop_moves(self, index):
        diagonals = [[[index[0] + i, index[1] + i] for i in range(1, 8)],
                     [[index[0] + i, index[1] - i] for i in range(1, 8)],
                     [[index[0] - i, index[1] + i] for i in range(1, 8)],
                     [[index[0] - i, index[1] - i] for i in range(1, 8)]]

        for direction in diagonals:
            for positions in direction:
                if self.on_board(positions):
                    if self.board[positions[0]][positions[1]] == '  ':
                        self.board[positions[0]][positions[1]] = 'x '
                    else:
                        if self.board[positions[0]][positions[1]].team != self.board[index[0]][index[1]].team:
                            self.board[positions[0]][positions[1]].killable = True
                        break
        return self.board


    ## applies the rook moves to the board then the bishop moves because a queen is basically a rook and bishop in the same position.
    def queen_moves(self, index):
        self.board = self.rook_moves(index)
        self.board = self.bishop_moves(index)
        return self.board


    ## Checks a 5x5 grid around the piece and uses pythagoras to see if if a move is valid. Valid moves will be a distance of sqrt(5) from centre
    def knight_moves(self, index):
        for i in range(-2, 3):
            for j in range(-2, 3):
                if i ** 2 + j ** 2 == 5:
                    if self.on_board((index[0] + i, index[1] + j)):
                        if self.board[index[0] + i][index[1] + j] == '  ':
                            self.board[index[0] + i][index[1] + j] = 'x '
                        else:
                            if self.board[index[0] + i][index[1] + j].team != self.board[index[0]][index[1]].team:
                                self.board[index[0] + i][index[1] + j].killable = True
        return self.board


    def make_grid(self, rows, width):
        grid = []
        gap = P.WIDTH // rows
        print(gap)
        for i in range(rows):
            grid.append([])
            for j in range(rows):
                node = Node(j, i, gap)
                grid[i].append(node)
                if (i+j)%2 ==1:
                    grid[i][j].colour = P.GREY
        return grid


    def draw_grid(self, win, rows, width):
        gap = width // 8
        for i in range(rows):
            pygame.draw.line(win, P.BLACK, (0, i * gap), (width, i * gap))
            for j in range(rows):
                pygame.draw.line(win, P.BLACK, (j * gap, 0), (j * gap, width))

        """
        The nodes are all white so this we need to draw the grey lines that separate all the chess tiles
        from each other and that is what this function does"""


    def update_display(self, win, grid, rows, width):
        for row in grid:
            for spot in row:
                spot.draw(win)
                spot.setup(win)
        self.draw_grid(win, rows, width)
        pygame.display.update()


    def Find_Node(sel, pos, WIDTH):
        interval = WIDTH / 8
        y, x = pos
        rows = y // interval
        columns = x // interval
        return int(rows), int(columns)


    def display_potential_moves(self, positions, grid):
        for i in positions:
            x, y = i
            grid[x][y].colour = P.BLUE
            """
            Displays all the potential moves
            """


    def Do_Move(self, OriginalPos, FinalPosition, WIN):
        Pieces.starting_order[FinalPosition] = Pieces.starting_order[OriginalPos]
        Pieces.starting_order[OriginalPos] = None


    def remove_highlight(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i+j)%2 == 0:
                    grid[i][j].colour = P.WHITE
                else:
                    grid[i][j].colour = P.GREY
        return grid
    """this takes in 2 co-ordinate parameters which you can get as the position of the piece and then the position of the node it is moving to
    you can get those co-ordinates using my old function for swap"""


