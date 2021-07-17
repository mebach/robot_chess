from Piece import Piece
import pygame


class Pieces():
    ## Creates instances of chess pieces, so far we got: pawn, king, rook and bishop
    ## The first parameter defines what team its on and the second, what type of piece it is
    bp = Piece('b', 'p', 'images/pawn_black.png')
    wp = Piece('w', 'p', 'images/pawn_white.png')
    bkn = Piece('b', 'k', 'images/knight_black.png')
    wkn = Piece('w', 'k', 'images/knight_white.png')
    br = Piece('b', 'r', 'images/rook_black.png')
    wr = Piece('w', 'r', 'images/rook_white.png')
    bb = Piece('b', 'b', 'images/bishop_black.png')
    wb = Piece('w', 'b', 'images/bishop_white.png')
    bq = Piece('b', 'q', 'images/queen_black.png')
    wq = Piece('w', 'q', 'images/queen_white.png')
    bk = Piece('b', 'kn', 'images/king_black.png')
    wk = Piece('w', 'kn', 'images/king_white.png')

    starting_order = {(0, 0): pygame.image.load(br.image), (1, 0): pygame.image.load(bkn.image),
                      (2, 0): pygame.image.load(bb.image), (3, 0): pygame.image.load(bq.image),
                      (4, 0): pygame.image.load(bk.image), (5, 0): pygame.image.load(bb.image),
                      (6, 0): pygame.image.load(bkn.image), (7, 0): pygame.image.load(br.image),
                      (0, 1): pygame.image.load(bp.image), (1, 1): pygame.image.load(bp.image),
                      (2, 1): pygame.image.load(bp.image), (3, 1): pygame.image.load(bp.image),
                      (4, 1): pygame.image.load(bp.image), (5, 1): pygame.image.load(bp.image),
                      (6, 1): pygame.image.load(bp.image), (7, 1): pygame.image.load(bp.image),

                      (0, 2): None, (1, 2): None, (2, 2): None, (3, 2): None,
                      (4, 2): None, (5, 2): None, (6, 2): None, (7, 2): None,
                      (0, 3): None, (1, 3): None, (2, 3): None, (3, 3): None,
                      (4, 3): None, (5, 3): None, (6, 3): None, (7, 3): None,
                      (0, 4): None, (1, 4): None, (2, 4): None, (3, 4): None,
                      (4, 4): None, (5, 4): None, (6, 4): None, (7, 4): None,
                      (0, 5): None, (1, 5): None, (2, 5): None, (3, 5): None,
                      (4, 5): None, (5, 5): None, (6, 5): None, (7, 5): None,

                      (0, 6): pygame.image.load(wp.image), (1, 6): pygame.image.load(wp.image),
                      (2, 6): pygame.image.load(wp.image), (3, 6): pygame.image.load(wp.image),
                      (4, 6): pygame.image.load(wp.image), (5, 6): pygame.image.load(wp.image),
                      (6, 6): pygame.image.load(wp.image), (7, 6): pygame.image.load(wp.image),
                      (0, 7): pygame.image.load(wr.image), (1, 7): pygame.image.load(wkn.image),
                      (2, 7): pygame.image.load(wb.image), (3, 7): pygame.image.load(wq.image),
                      (4, 7): pygame.image.load(wk.image), (5, 7): pygame.image.load(wb.image),
                      (6, 7): pygame.image.load(wkn.image), (7, 7): pygame.image.load(wr.image), }