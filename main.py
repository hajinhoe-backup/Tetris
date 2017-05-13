import pygame
import random
import copy

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

WIDTH = 30
HEIGHT = 30
MARGIN = 2
# Call this function so the Pygame library can initialize itself
pygame.init()

# Create an 800x600 sized screen
screen = pygame.display.set_mode([320, 640])

# This sets the name of the window
pygame.display.set_caption('TETRIS')

clock = pygame.time.Clock()

# Make a board (it originally 40x10, but I use 25x10 board, 4 is buffer, 1 is ground)
board = [[0 for x in range(10)] for y in range(25)]
for x in range(10) :
    board[24][x] = 3

# Make piece, pc_i[포즈][조각번호][x, y값(0또는 1)]
pc_i = [[[0,2],[1,2],[2,2],[3,2]],[[3,1],[3,2],[3,3],[3,4]],[[0,3],[1,3],[2,3],[3,3]],[[2,1],[2,2],[2,3],[2,4]]]
pc_j = [[[0,1],[1,1],[2,1],[2,2]],[[2,0],[2,1],[2,2],[1,2]],[[0,1],[0,2],[1,2],[2,2]],[[0,0],[1,0],[1,1],[1,2]]]
pc_l = [[[0,1],[0,2],[1,1],[2,1]],[[0,0],[1,0],[1,1],[1,2]],[[2,0],[2,1],[1,1],[0,1]],[[0,0],[0,1],[0,2],[1,2]]]
pc_o = [[[0,1],[1,1],[0,2],[1,2]],[[0,1],[1,1],[0,2],[1,2]],[[0,1],[1,1],[0,2],[1,2]],[[0,1],[1,1],[0,2],[1,2]]]
pc_s = [[[1,1],[2,1],[0,2],[1,2]],[[1,0],[1,1],[2,1],[2,2]],[[1,1],[2,1],[0,2],[1,2]],[[0,0],[0,1],[1,1],[1,2]]]
pc_t = [[[0,1],[1,1],[2,1],[1,2]],[[1,0],[0,1],[1,1],[1,2]],[[1,0],[0,1],[1,1],[2,1]],[[1,0],[1,1],[2,1],[1,2]]]
pc_z = [[[0,1],[1,1],[1,2],[2,2]],[[2,0],[1,1],[2,1],[1,2]],[[0,0],[1,0],[1,1],[2,1]],[[2,0],[1,1],[2,1],[1,2]]]
pc_name = [pc_i, pc_j, pc_l, pc_o, pc_s, pc_t, pc_z]

done = False

make_piece = True

TIME = 0
MOVE_TIME = 0
x_move = 0
y_move = 0
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                a = 0
            elif event.key == pygame.K_LEFT:
                x_move = -1
                MOVE_TIME += 1
            elif event.key == pygame.K_RIGHT:
                x_move = 1
                MOVE_TIME += 1
            elif event.key == pygame.K_UP:
                if change != 3 :
                    change += 1
                else :
                    change = 0
            elif event.key == pygame.K_DOWN:
                y_move = 1
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_move = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_move = 0

    #make a piece
    if make_piece == True :
        change = 0
        x = 3
        y = 0
        random_number = random.randrange(0,7)
        now_piece = pc_name[random_number]
        make_piece = False

    display_board = copy.deepcopy(board)

    #display_board의 칸 값을 지금 조각이 위치한 경우라면 임시값인 2로 하자
    for i in range(4) :
        display_board[now_piece[change][i][1] + y][now_piece[change][i][0] + x] = 2

    #그리자
    for row in range(4, 24) :
        for col in range(10) :
            color = WHITE
            if display_board[row][col] == 1 or display_board[row][col] == 2 :
                color = GREEN
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * col + MARGIN, (MARGIN + HEIGHT) * (row - 4 ) + MARGIN,
                              WIDTH, HEIGHT])

#현재까지 알려진 문제점
#블럭이 옆에 있을 때, 그 옆으로 이동하면 겹쳐버린다.
#가끔씩 그냥 플레이하는데 아웃오프 레인지가 나온다.
#벽 끝에서 변환하면 변환이안되게 하던가 해야하는데, 옆으로 나와버린다.


    if TIME != 10 :
        TIME += 1
    else :
        TIME = 0
        y += 1

    if MOVE_TIME == 1:
        for i in range(4):
            if now_piece[change][i][0] + x == 0 and x_move == -1:
                x_move = 0
            elif now_piece[change][i][0] + x == 9 and x_move == 1:
                x_move = 0
        x += x_move
        MOVE_TIME = 0

    #다른 블럭과 닿는 경우, 3인 경우는 땅
    for i in range(4):
        if board[now_piece[change][i][1] + y + 1][now_piece[change][i][0] + x] == 1 or board[now_piece[change][i][1] + y + 1][now_piece[change][i][0] + x] == 3:
            for i in range(4):
                board[now_piece[change][i][1] + y][now_piece[change][i][0] + x] = 1
            make_piece = True




    pygame.display.flip()

    clock.tick(60)

pygame.quit()