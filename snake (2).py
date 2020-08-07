import pygame
import random

pygame.init()

FPS = 10
u = 0
height = 300
width = 300
cord_x = 10
cord_y = 10
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
right_flug = True
left_flug = False
up_flug = False
down_flug = False
flag = False
score = 0
range_x = [cord_x]
range_y = [cord_y]
clock = pygame.time.Clock()
sc = pygame.display.set_mode((height, width))
sc.fill((0, 0, 0))
segment = 1
x = 0
y = 0
c_x = [cord_x]
c_y = [cord_y]
step = 13
for i in range(height // step + 1):
    pygame.draw.line(sc, (255, 255, 255), (x, 0), (x, height))
    pygame.draw.line(sc, (255, 255, 255), (0, y), (width, y))
    x = x + step
    y = y + step
pygame.display.update()
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
    rand_x = random.randint(0, height // step - 1)
    rand_y = random.randint(0, height // step - 1)
    if rand_y != cord_y and rand_x != cord_x and flag == False:
        pygame.draw.rect(sc, RED, (rand_x * 13 + 1, rand_y * 13 + 1, step - 1, step - 1))
        flag = True
        fruit_x = rand_x
        fruit_y = rand_y
    p_cord_x = cord_x * 13 + 1
    p_cord_y = cord_y * 13 + 1
    # ------------------
    pygame.draw.rect(sc, GREEN, (p_cord_x, p_cord_y, step - 1, step - 1))
    # ------------------
    # p_cord_x += 14
    pygame.display.update()
    c_x.append(cord_x)
    c_y.append(cord_y)
    if len(c_x) > segment and len(c_y) > segment:
        c_x.pop(0)
        c_y.pop(0)
    len_x = len(c_x)
    len_y = len(c_y)
    u += 1
    if u >= segment:
        for n in range(1, segment - 1):
            if c_x[len_x - 1] == c_x[n] and c_y[len_y - 1] == c_y[n]:
                print("You score:", segment)
                exit()
    # pygame.draw.rect(sc, BLACK, (c_x[len_x-1]*13+1, c_y[len_y-1]*13+1, step-1, step-1))
    pygame.draw.rect(sc, BLACK, (c_x[0] * 13 + 1, c_y[0] * 13 + 1, step - 1, step - 1))
    # pygame.draw.rect(sc, BLACK, (p_cord_x, p_cord_y, step-1, step-1))
    # p_cord_x + (segment*13+1)
    if cord_x == fruit_x and cord_y == fruit_y:
        flag = False
        score += 1
        segment += 1

        print(score)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        if right_flug == True:
            left_flug = False
            down_flug = False
            right_flug = True
            up_flug = False
        else:
            # cord_x -= 1
            left_flug = True
            down_flug = False
            right_flug = False
            up_flug = False
    elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
    	if left_flug == True:
    	    left_flug = True
    	    down_flug = False
    	    right_flug = False
    	    up_flug = False
    	else:
            right_flug = True
            down_flug = False
            left_flug = False
            up_flug = False
    elif keys[pygame.K_w] or keys[pygame.K_UP]:
    	if down_flug == True:
    	    right_flug = False
    	    down_flug = True
    	    left_flug = False
    	    up_flug = False
    	else:
	    # cord_y -= 1
            down_flug = False
            left_flug = False
            right_flug = False
            up_flug = True
    elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
        if up_flug == True:
            up_flug = True
        else:
            # cord_y += 1
            down_flug = True
            left_flug = False
            right_flug = False
            up_flug = False
    if right_flug == True:
        cord_x += 1
    elif left_flug == True:
        cord_x -= 1
    elif up_flug == True:
        cord_y -= 1
    elif down_flug == True:
        cord_y += 1

    if cord_y > 22:
        print("You score:", segment)
        exit()
    if cord_x > 22:
        print("You score:", segment)
        exit()
    if cord_x < 0:
        print("You score:", segment)
        exit()
    if cord_y < 0:
        print("You score:", segment)
        exit()
    x = 0
    y = 0

    for i in range(height // step + 1):
        pygame.draw.line(sc, (255, 255, 255), (x, 0), (x, height))
        pygame.draw.line(sc, (255, 255, 255), (0, y), (width, y))
        x = x + step
        y = y + step

    # cord_y = cord_y + 1
    # cord_x = cord_x + 1

    clock.tick(FPS)
