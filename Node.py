from Pieces import Pieces
import pygame
import Param as P

class Node:
    def __init__(self, row, col, width):
        self.row = row
        self.col = col
        self.x = int(row * width)
        self.y = int(col * width)
        self.colour = P.WHITE
        self.occupied = None

    def draw(self, WIN):
        pygame.draw.rect(WIN, self.colour, (self.x, self.y, P.WIDTH / 8, P.WIDTH / 8))

    def setup(self, WIN):
        if Pieces.starting_order[(self.row, self.col)]:
            if Pieces.starting_order[(self.row, self.col)] == None:
                pass
            else:
                WIN.blit(Pieces.starting_order[(self.row, self.col)], (self.x, self.y))

        """
        For now it is drawing a rectangle but eventually we are going to need it
        to use blit to draw the chess pieces instead
        """

