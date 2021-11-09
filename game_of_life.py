'''
Conway's game of life
'''

def game_of_life(board):
    '''
    Function that implements the Game of Life
    '''
    if board is None or len(board) == 0:
        return board
    rows = len(board)
    cols = len(board[0])
    new_board = [[0 for _ in range(cols)] for _ in range(rows)]
    for row in range(rows):
        for col in range(cols):
            count = 0
            for i in range(row - 1, row + 2):
                for j in range(col - 1, col + 2):
                    if i >= 0 and i < rows and j >= 0 and j < cols:
                        if board[i][j] == 1:
                            count += 1
            if board[row][col] == 1:
                if count < 2 or count > 3:
                    new_board[row][col] = 0
                else:
                    new_board[row][col] = 1
            else:
                if count == 3:
                    new_board[row][col] = 1
    return new_board
    

if __name__=="__main__":
    # random board of 0s and 1s of size 50x50
    import random
    board = [[random.randint(0, 1) for _ in range(50)] for _ in range(50)]

    # visualize and run the game with Pygame
    import pygame
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Game of Life")
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        for row in range(len(board)):
            for cell in range(len(board[row])):
                if board[row][cell] == 1:
                    pygame.draw.rect(screen, (255, 255, 255), (cell * 10, row * 10, 10, 10))
        board = game_of_life(board)
        pygame.display.flip()
        clock.tick(10)
    pygame.quit()
    quit()

