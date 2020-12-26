import pygame

pygame.init()

# window constants
window_h = 800
window_w = 800

# board constants
board_h = 8
board_w = 8
block_size = 100

# create window and clock
window = pygame.display.set_mode((window_w, window_h))
clock = pygame.time.Clock()

# colors
black = (0, 0, 0)
white = (255, 255, 255)
beige = (245, 245, 220)
brown = (97, 48, 0)

# this function draws the board without the pieces
def draw_grid():
    global block_size
    for x in range((window_w // block_size)):
        for y in range((window_h // block_size)):
            if (x + y) % 2 != 0:
                rect = pygame.Rect(x * block_size, y * block_size, block_size, block_size)
                pygame.draw.rect(window, brown, rect)
            else:
                rect = pygame.Rect(x * block_size, y * block_size, block_size, block_size)
                pygame.draw.rect(window, beige, rect)

# main
if __name__ == "__main__":
    running = True

    while running:
        draw_grid()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()
        clock.tick(30)
