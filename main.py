import pygame
import random
import copy
import time

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)

BLOCK_SIZE = 32

#위드하이트, 마진등등... 블록사이즈로 대체합니다. 아직안했으니까 누군가 할듯 .

WIDTH = 30
HEIGHT = 30
MARGIN = 2
# Call this function so the Pygame library can initialize itself
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()

# Create an 800x600 sized screen
screen = pygame.display.set_mode([520, 640])

# This sets the name of the window
pygame.display.set_caption('TETRIS')

clock = pygame.time.Clock()

# 0 ~ 6 색깔 있는 블럭 7 아직 저장안된 블럭 8 블럭이 없음

# Make a board (it originally 40x10, but I use 24x10 board, 4 is buffer)
board = [[8 for x in range(10)] for y in range(24)]

# 데이터들을 준비합니다.
pc_i = [[[0,1],[1,1],[2,1],[3,1]],[[2,0],[2,1],[2,2],[2,3]],[[0,2],[1,2],[2,2],[3,2]],[[1,0],[1,1],[1,2],[1,3]]]
pc_j = [[[0,1],[1,1],[2,1],[2,2]],[[2,0],[2,1],[2,2],[1,2]],[[0,1],[0,2],[1,2],[2,2]],[[2,0],[1,0],[1,1],[1,2]]]
pc_l = [[[0,1],[0,2],[1,1],[2,1]],[[0,0],[1,0],[1,1],[1,2]],[[2,0],[2,1],[1,1],[0,1]],[[0,0],[0,1],[0,2],[1,2]]]
pc_o = [[[0,1],[1,1],[0,2],[1,2]],[[0,1],[1,1],[0,2],[1,2]],[[0,1],[1,1],[0,2],[1,2]],[[0,1],[1,1],[0,2],[1,2]]]
pc_s = [[[1,1],[2,1],[0,2],[1,2]],[[1,0],[1,1],[2,1],[2,2]],[[1,1],[2,1],[0,2],[1,2]],[[0,0],[0,1],[1,1],[1,2]]]
pc_t = [[[0,1],[1,1],[2,1],[1,2]],[[1,0],[0,1],[1,1],[1,2]],[[1,0],[0,1],[1,1],[2,1]],[[1,0],[1,1],[2,1],[1,2]]]
pc_z = [[[0,1],[1,1],[1,2],[2,2]],[[2,0],[1,1],[2,1],[1,2]],[[0,0],[1,0],[1,1],[2,1]],[[2,0],[1,1],[2,1],[1,2]]]
pc_name = [pc_i, pc_j, pc_l, pc_o, pc_s, pc_t, pc_z]

block_i = pygame.image.load("block_i.png")
block_j = pygame.image.load("block_j.png")
block_l = pygame.image.load("block_l.png")
block_o = pygame.image.load("block_o.png")
block_s = pygame.image.load("block_s.png")
block_t = pygame.image.load("block_t.png")
block_z = pygame.image.load("block_z.png")
block_name = [block_i, block_j, block_l, block_o, block_s, block_t, block_z]

ghostblock = pygame.image.load("ghostblock.png")

pygame.display.set_icon(pygame.image.load("logo.png"))

done = False

make_piece = True

effect = False
TIME = 0
MOVE_TIME = 0
block_wait_time = 0
x_move = 0
y_move = 0
speed = 15
score = 0
block_down = 1
hold_block = 8
block_wait = False
speed_temp = speed

back_img = pygame.image.load("back_img.png")
pygame.mixer.Sound("Korobeiniki.ogg").play(loops=-1)
click_sound = pygame.mixer.Sound("click.ogg")
effect_sound = pygame.mixer.Sound("jump-bump.ogg")
tak_stroke = pygame.mixer.Sound("takstroke.ogg")

pre_block = random.randrange(0,7)
gameover = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                y = gy
                block_down = 0
                score += gy * 2
            elif event.key == pygame.K_LEFT:
                x_move = -1
                MOVE_TIME += 1
            elif event.key == pygame.K_RIGHT:
                x_move = 1
                MOVE_TIME += 1
            elif event.key == pygame.K_UP:
                click_sound.play()
                if not block_wait :
                    if change != 3 :
                        change += 1
                    else :
                        change = 0
            elif event.key == pygame.K_DOWN:
                speed_temp = speed
                if speed > 5 :
                    speed = 3
                else :
                    speed = 1
            elif event.key == pygame.K_u :
                if speed > 4 :
                    speed -= 3
            elif event.key == pygame.K_d :
                if speed < 21 :
                    speed += 3
            elif event.key == pygame.K_t :
                if block_down == 1 :
                    block_down = 0
                else :
                    block_down = 1
            elif event.key == pygame.K_h :
                if hold_block == 8 :
                    hold_block = now_block
                    make_piece = True
                else :
                    temp = now_block
                    now_block = hold_block
                    now_piece = pc_name[now_block]
                    hold_block = temp
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_move = 0
            elif event.key == pygame.K_DOWN :
                speed = speed_temp

    if not speed == speed_temp :
        if TIME == 0 :
            if block_down == 1 :
                score += 1

    if gameover:
        while gameover :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameover = False
                    done = True

    if effect == True :
        effect_sound.play()
        pygame.time.wait(100)
        effect = False
    #make a piece
    if make_piece == True :
        change = 0
        x = 3
        y = 2
        now_block = pre_block
        pre_block = random.randrange(0,7)
        now_piece = pc_name[now_block]
        make_piece = False

    display_board = copy.deepcopy(board)

    for i in range(4) :
        if now_piece[change][i][0] + x > 9 :
            x -= 1
        elif now_piece[change][i][0] + x < 0 :
            x += 1

    #display_board의 칸 값을 지금 조각이 위치한 경우라면 임시값인 2로 하자
    for i in range(4) :
        display_board[now_piece[change][i][1] + y][now_piece[change][i][0] + x] = 7

    #ghostblock 구현
    gy = y
    ghostloop = True
    while ghostloop :
            for i in range(4) :
                if now_piece[change][i][1] + gy == 23 or board[now_piece[change][i][1] + gy + 1][now_piece[change][i][0] + x] < 7 :
                    ghostloop = False
            if ghostloop :
                gy += 1

    #그리자
    screen.blit(back_img, [0,0])

    for i in range(4) :
        screen.blit(ghostblock, [(MARGIN + WIDTH) * (now_piece[change][i][0] + x) + MARGIN, (MARGIN + HEIGHT) * (now_piece[change][i][1] + gy - 4) + MARGIN - 4])

    for row in range(4, 24) :
        for col in range(10) :
            color = BLACK
            if display_board[row][col] < 7 :
                screen.blit(block_name[display_board[row][col]], [(MARGIN + WIDTH) * col + MARGIN, (MARGIN + HEIGHT) * (row - 4) + MARGIN - 4])
            elif display_board[row][col] == 7 :
                screen.blit(block_name[now_block], [(MARGIN + WIDTH) * col + MARGIN, (MARGIN + HEIGHT) * (row - 4 ) + MARGIN - 4])
    for i in range(4) :
        screen.blit(block_name[pre_block], [32 * pc_name[pre_block][0][i][0] + 360, 32 * (pc_name[pre_block][0][i][1] - 4) + 265])

    font = pygame.font.SysFont('Calibri', 48, True, False)
    text = font.render(str(score), False, WHITE)
    screen.blit(text, [350, 65])

    if hold_block != 8 :
        for i in range(4) :
            screen.blit(block_name[hold_block],
                        [32 * pc_name[hold_block][0][i][0] + 360, 32 * (pc_name[hold_block][0][i][1] - 4) + 420])
    if TIME < speed :
        TIME += 1
    else :
        TIME = 0
        y += block_down

    if MOVE_TIME == 1 :
        if x_move != 0:
            for i in range(4):
                if x_move == -1 :
                    if now_piece[change][i][0] + x == 0 :
                        x_move = 0
                    elif now_piece[change][i][0] + x - 1 != 0:
                        if board[now_piece[change][i][1] + y][now_piece[change][i][0] + x - 1] < 7:
                            x_move = 0
                elif x_move == 1 :
                    if now_piece[change][i][0] + x == 9 :
                        x_move = 0
                    elif now_piece[change][i][0] + x + 1 != 9 :
                        if board[now_piece[change][i][1] + y][now_piece[change][i][0] + x + 1] < 7:
                            x_move = 0
        x += x_move
        MOVE_TIME = 0



    #하단이 다른 블럭과 닿는 경우또는 땅에 닿는 경우와 옆에 닿는 경우를 처리
    for i in range(4):
        if now_piece[change][i][1] + y == 23 or board[now_piece[change][i][1] + y + 1][now_piece[change][i][0] + x] < 7:
            block_wait = True
            block_down = 0
            if block_wait_time > 15 :
                for i in range(4):
                    if now_piece[change][i][1] + y < 4 :
                        gameover = True
                    board[now_piece[change][i][1] + y][now_piece[change][i][0] + x] = now_block
                make_piece = True
                tak_stroke.play()
                block_down = 1
                block_wait = False
                block_wait_time = 0

    if block_wait :
        block_wait_time += 1
        if block_wait_time > 16 :
            block_wait = False
            block_down = 1
            block_wait_time = 0

    if make_piece == True :
        delblocknumber = 0
        for i in range(4):
            if y + i < 24 :
                delthis = True
                for j in board[y + i]:
                    if j > 6:
                        delthis = False
                if delthis :
                    del board[y + i]
                    board = [[8, 8, 8, 8, 8, 8, 8, 8, 8, 8]] + board
                    delblocknumber += 1
                    pygame.draw.rect(screen,
                                     BLACK,
                                     [0,
                                      32 * (y + i - 4),
                                      322,
                                      32])
                    effect = True
        if delblocknumber == 1 :
            score += 100
        elif delblocknumber == 2 :
            score += 300
        elif delblocknumber == 3 :
            score += 600
        elif delblocknumber == 4 :
            score += 1000

    if gameover == True :
        pygame.mixer.pause()
        pygame.mixer.Sound("gameover.ogg").play()
        screen.fill(BLUE)
        text = font.render("GAME OVER", False, WHITE)
        screen.blit(text, [160, 280])

    pygame.display.flip()

    clock.tick(60)

pygame.quit()