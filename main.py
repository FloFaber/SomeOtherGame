import pygame
import sys

FPS = 144

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

GRID_WIDTH = 7
GRID_HEIGHT = 7

BLOCK_SIZE = 50

WINDOW_WIDTH = BLOCK_SIZE * 7
WINDOW_HEIGHT = BLOCK_SIZE * 7

RECTS = []
POINTS = []

MOVING = False
SCREEN = None
CLOCK = None


def main():
    global SCREEN, CLOCK
    pygame.init()
    pygame.display.set_caption("Nonnenspiel")
    SCREEN = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
    CLOCK = pygame.time.Clock()

    draw_grid()

    while True:
        CLOCK.tick(FPS)

        SCREEN.fill(BLACK)

        for r in RECTS:
            r.draw()

        for p in POINTS:
            p.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                clicked_sprite = None
                for r in RECTS:
                    if r.r.collidepoint(pos):
                        clicked_sprite = r

                try:
                    x = clicked_sprite.x
                    y = clicked_sprite.y

                    for p in POINTS:
                        if p.x == x and p.y == y and not MOVING:
                            p.start_move(x, y)
                        elif p.moving:
                            p.stop_move(x, y)

                except AttributeError:
                    pass

        pygame.display.update()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.moving = False
        self.before_moving = None

    def remove(self, x, y):
        for p in POINTS:
            if p.x == x and p.y == y:
                POINTS.remove(p)

    def draw(self):
        if self.moving:
            pos = pygame.mouse.get_pos()
            self.x = pos[0]
            self.y = pos[1]
            pygame.draw.circle(SCREEN, BLUE, (self.x, self.y), 20)
        else:
            pygame.draw.circle(SCREEN, BLUE, (self.x * BLOCK_SIZE + BLOCK_SIZE / 2, self.y * BLOCK_SIZE + BLOCK_SIZE / 2), 20)

    def start_move(self, x, y):
        global MOVING
        MOVING = True
        self.before_moving = { "x": x, "y": y }
        self.moving = True
        print("start move")

    def stop_move(self, x, y):
        print("STOP MOVE:")
        print((x, y))
        global MOVING

        if not self.is_occupied(x, y):
            print("a1")
            if x == self.before_moving["x"] or y == self.before_moving["y"]:
                print("a2")
                if x == self.before_moving["x"] + 2:
                    self.remove(x - 1, y)
                elif x == self.before_moving["x"] - 2:
                    self.remove(x + 1, y)
                elif y == self.before_moving["y"] + 2:
                    self.remove(x, y - 1)
                elif y == self.before_moving["y"] - 2:
                    self.remove(x, y + 1)
                elif x == self.before_moving["x"] and y == self.before_moving["y"]:
                    self.x = x
                    self.y = y
                else:
                    return

                MOVING = False
                self.x = x
                self.y = y
                self.moving = False

    def is_occupied(self, x, y):
        for p in POINTS:
            if p.x == x and p.y == y:
                return True
        return False


class Rect:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = pygame.Rect(self.x * BLOCK_SIZE, self.y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)

    def draw(self):
        pygame.draw.rect(SCREEN, WHITE, self.r, 1)

    def collidepoint(self, pos):
        return self.r.collidepoint(pos)


def draw_grid():
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            if not ((x <= 1 and y <= 1) or (x >= GRID_WIDTH - 2 and y >= GRID_HEIGHT - 2) or (x >= GRID_WIDTH - 2 and y <= 1) or (x <= 1 and y >= GRID_HEIGHT - 2)):

                if not (x == 3 and y == 3):
                    p = Point(x, y)
                    POINTS.append(p)

                RECTS.append(Rect(x, y))


if __name__ == "__main__":
    main()
