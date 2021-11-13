# Chesss

# Import and initialize the pygame library
import pygame as p
import objects
import engine

p.init()
display_width = 400
display_height = 600
screen = p.display.set_mode((display_width, display_height))
piece_size = display_width // 8
images = {}
game = engine.GameState()


def loadImages():
    pieces = ['wP', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bP', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        images[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (piece_size, piece_size))


def createBoard():
    screen.fill((255, 255, 255))
    x = 0
    y = 200
    for c in range(8):
        for r in range(8):
            if (r+c) % 2 == 0:
                color = (65,189,82)
            else:
                color = (22,98,137)
            p.draw.polygon(screen, color, [(x, y), (x+50, y), (x+50, y+50), (x, y+50)])
            x += 50
        y += 50
        x = 0

    for r in range(8):
        p.draw.line(screen, (0, 0, 0), (0, 200 + 50 * r), (400, 200 + 50 * r))
    for c in range(8):
        p.draw.line(screen, (0, 0, 0), (50 * c, 200), (50 * c, 600))


def createPieces(gamestate):
    return True


def main():
    # loadImages()
    createBoard()
    createPieces()

    running = True
    while running:

        # Did the user click the window close button?
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False

        # Flip the display
        p.display.flip()

    p.quit()


main()
