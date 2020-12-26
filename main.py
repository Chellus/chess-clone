import pygame

pygame.init()

# window constants
window_h = 800
window_w = 800

# our board
board = []

# board constants
board_size = 8
block_size = 100

# create window and clock
window = pygame.display.set_mode((window_w, window_h))
clock = pygame.time.Clock()

# colors
black = (0, 0, 0)
white = (255, 255, 255)
beige = (245, 245, 220)
brown = (97, 48, 0)

# white pieces images
white_pawn = pygame.image.load("resources/white_pawn.png")
white_rook = pygame.image.load("resources/white_rook.png")
white_knight = pygame.image.load("resources/white_knight.png")
white_bishop = pygame.image.load("resources/white_bishop.png")
white_queen = pygame.image.load("resources/white_queen.png")
white_king = pygame.image.load("resources/white_king.png")

# black pieces images
black_pawn = pygame.image.load("resources/black_pawn.png")
black_rook = pygame.image.load("resources/black_rook.png")
black_knight = pygame.image.load("resources/black_knight.png")
black_bishop = pygame.image.load("resources/black_bishop.png")
black_queen = pygame.image.load("resources/black_queen.png")
black_king = pygame.image.load("resources/black_king.png")

# generating the logic board
# white: pawn = 1, rook = 2, knight = 3, bishop = 4, queen = 5, king = 6
# black: pawn = 7, rook = 8, knight = 9, bishop = 10, queen = 11, king = 12
# 8 - 9 - 10 - 11 - 12 - 10 - 9 - 8
# 7 - 7 - 7  - 7  - 7  - 7  - 7 - 7
# 0 - 0 - 0  - 0  - 0  - 0  - 0 - 0
# 0 - 0 - 0  - 0  - 0  - 0  - 0 - 0
# 0 - 0 - 0  - 0  - 0  - 0  - 0 - 0
# 0 - 0 - 0  - 0  - 0  - 0  - 0 - 0
# 1 - 1 - 1  - 1  - 1  - 1  - 1 - 1
# 2 - 3 - 4  - 5  - 6  - 4  - 3 - 2
def generate_board():
    global board

    # fill the board with the values
    for i in range(board_size):
        if i == 0:
            row = [8, 9, 10, 11, 12, 10, 9, 8]
        elif i == 1:
            row = [7, 7, 7, 7, 7, 7, 7, 7]
        elif i == 6:
            row = [1, 1, 1, 1, 1, 1, 1, 1]
        elif i == 7:
            row = [2, 3, 4, 5, 6, 4, 3, 2]
        else:
            row = []
            for j in range(board_size):
                row.append(0)
        board.append(row)

    print(board)

# this function draws the board
def draw_board():
    global block_size
    for x in range((window_w // block_size)):
        for y in range((window_h // block_size)):
            if (x + y) % 2 != 0:
                rect = pygame.Rect(x * block_size, y * block_size, block_size, block_size)
                pygame.draw.rect(window, brown, rect)
            else:
                rect = pygame.Rect(x * block_size, y * block_size, block_size, block_size)
                pygame.draw.rect(window, beige, rect)

    for x in range(board_size):
        for y in range(board_size):
            if board[x][y] == 1:
                window.blit(white_pawn, ((y * block_size) + 13, (x * block_size) + 13))
            elif board[x][y] == 2:
                window.blit(white_rook, ((y * block_size) + 13, (x * block_size) + 13))
            elif board[x][y] == 3:
                window.blit(white_knight, ((y * block_size) + 13, (x * block_size) + 13))
            elif board[x][y] == 4:
                window.blit(white_bishop, ((y * block_size) + 13, (x * block_size) + 13))
            elif board[x][y] == 5:
                window.blit(white_queen, ((y * block_size) + 13, (x * block_size) + 13))
            elif board[x][y] == 6:
                window.blit(white_king, ((y * block_size) + 13, (x * block_size) + 13))
            elif board[x][y] == 7:
                window.blit(black_pawn, ((y * block_size) + 13, (x * block_size) + 13))
            elif board[x][y] == 8:
                window.blit(black_rook, ((y * block_size) + 13, (x * block_size) + 13))
            elif board[x][y] == 9:
                window.blit(black_knight, ((y * block_size) + 13, (x * block_size) + 13))
            elif board[x][y] == 10:
                window.blit(black_bishop, ((y * block_size) + 13, (x * block_size) + 13))
            elif board[x][y] == 11:
                window.blit(black_queen, ((y * block_size) + 13, (x * block_size) + 13))
            elif board[x][y] == 12:
                window.blit(black_king, ((y * block_size) + 13, (x * block_size) + 13))

# main
if __name__ == "__main__":
    running = True
    generate_board()
    while running:
        draw_board()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()
        clock.tick(30)
