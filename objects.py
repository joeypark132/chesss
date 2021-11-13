class Pieces:
    def __init__(self, x, y, color, piece):
        """ Chess pieces constructor """
        self.x = x
        self.y = y
        self.width = 10
        self.height = 10
        self.color = color
        self.piece = piece

    def move(self, color, piece, r, c):
        """ Method for the piece to move """


class Board:
    """ Chess board constructor """

    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 80
        self.height = 80
        self.fill = [[]]
        for r in range(8):
            for c in range(8):
                self.fill[r][c] = 0

    def fill(self, prev_r, prev_c, post_r, post_c):
        """ If the piece moves then proper row and
            column are filled and unfilled
        """
        self.fill[prev_r][prev_c] = 0
        self.fill[post_r][post_c] = 0



