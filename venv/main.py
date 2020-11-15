import pygame
import sys

FPS = 30

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
BLUE = (0, 0, 255)

GRID_WIDTH = 7
GRID_HEIGHT = 7

BLOCK_SIZE = 50

WINDOW_WIDTH = BLOCK_SIZE * 7
WINDOW_HEIGHT = BLOCK_SIZE * 7

RECTS = []

def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    drawGrid()

    while True:
        CLOCK.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                clicked_sprites = [s for s in RECTS if s["rect"].collidepoint(pos)]
                print(pos)
                print(clicked_sprites)
                print("----------------")
                drawPoint(clicked_sprites[0]["x"], clicked_sprites[0]["y"])

        pygame.display.update()


def drawPoint(x, y):
    print("Drawing point at " + str(x) + "x" + str(y))
    pygame.draw.circle(SCREEN, BLUE, (x * BLOCK_SIZE + BLOCK_SIZE / 2, y * BLOCK_SIZE + BLOCK_SIZE / 2), 20)


def drawGrid():
    for x in range(WINDOW_WIDTH):
        for y in range(WINDOW_HEIGHT):

            if not ((x <= 1 and y <= 1) or (x >= GRID_WIDTH - 2 and y >= GRID_HEIGHT - 2) or (x >= GRID_WIDTH - 2 and y <= 1) or (x <= 1 and y >= GRID_HEIGHT - 2)):

                r = {
                    "x": x,
                    "y": y,
                    "rect": pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                }

                RECTS.append(r)
                pygame.draw.rect(SCREEN, WHITE, r["rect"], 1)




if __name__ == "__main__":
    main()
