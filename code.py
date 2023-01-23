import pygame
import random
import time

pygame.init()
name = input('введите имя на английском: ')
dis = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Snake')

#сообщение
font_style = pygame.font.SysFont(None, 50)
def message(msg,collor):
    mesg = font_style.render(msg, True, collor)
    dis.blit(mesg, [235, 140])

def sscore(msg , collor):
    mesg = font_style.render(msg, True, collor)
    dis.blit(mesg, [335, 150])
def records(msg, collor, x):
    mesg = font_style.render(msg, True, collor)
    dis.blit(mesg, [235, x])

def beat(msg , collor):
    mesg = font_style.render(msg, True, collor)
    dis.blit(mesg, [235, 75])

#фпс
clock = pygame.time.Clock()

#переменные

game_end=False
while not game_end:
    q = 4
    maxofalll = 0
    zam = 0

    napravlenie = 'up'
    fonend = pygame.image.load('fonend.jpg')
    fon = pygame.image.load('fongame.jpg')
    gift = pygame.image.load('gift.png')
    telogift = pygame.image.load('telozmeie.png')
    cathead = pygame.image.load('cat.png')
    eaten = True
    co = [0, 0]
    telo = []
    score = 1
    xy = [300, 300]
    x1_change = 0
    y1_change = 0
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                game_end=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    y1_change = 25
                    x1_change = 0
                    napravlenie= 'down'
                if event.key == pygame.K_UP:
                    y1_change = -25
                    x1_change = 0
                    napravlenie= 'up'
                if event.key == pygame.K_LEFT:
                    x1_change = -25
                    y1_change = 0
                    napravlenie= 'left'
                if event.key == pygame.K_RIGHT:
                    x1_change = 25
                    y1_change = 0
                    napravlenie = 'right'

        dis.blit(fon, (0,0))
        #dis.blit(fon, (0,0))
        lastcoord = [xy[0],xy[1]]
        xy[0] += x1_change
        xy[1] += y1_change
        if xy[0]>775:
            game_over=True
        if xy[0]<0:
            game_over=True
        if xy[1]>575:
            game_over=True
        if xy[1]<0:
            game_over=True


        #модуль яблока

        if co == xy:
            eaten=True
            score=score+1

        if eaten==True:
            applesX = random.randint(1, 31)*25
            applesY = random.randint(1, 23)*25
            co=[applesX, applesY]

            eaten = False
        dis.blit(gift, (co[0], co[1]))


        rotimg = cathead
        rotimgtelo = telogift
        #модуль для змейки
        if napravlenie == 'right':
            rotimg = pygame.transform.rotate(cathead, -90)
        if napravlenie == 'left':
            rotimg = pygame.transform.rotate(cathead, 90)
        if napravlenie == 'down':
            rotimg = pygame.transform.rotate(cathead, 180)
        if len(telo) != 1:
            for i in range(len(telo)):
                if telo[i][2] == 1:
                    rotimgtelo = pygame.transform.rotate(telogift, -90)
                if telo[i][2] == 2:
                    rotimgtelo = pygame.transform.rotate(telogift, 90)
                if telo[i][2] == 3:
                    rotimgtelo = pygame.transform.rotate(telogift, 180)
                if telo[i][2] == 4:
                    rotimgtelo = telogift

                dis.blit(rotimgtelo, (telo[i][0], telo[i][1]))
                if xy[0] == telo[i][0] and xy[1]==telo[i][1]:
                    game_over=True
        else:
            if len(telo)!=0:
                if telo[0][2] == 1:
                    rotimgtelo = pygame.transform.rotate(telogift, -90)
                if telo[0][2] == 2:
                    rotimgtelo = pygame.transform.rotate(telogift, 90)
                if telo[0][2] == 3:
                    rotimgtelo = pygame.transform.rotate(telogift, 180)
                if telo[0][2] == 4:
                    rotimgtelo = telogift

                dis.blit(rotimgtelo, (telo[0][0], telo[0][1]))
        dis.blit(rotimg, (xy[0], xy[1], 25, 25))


        if len(telo)==score:
            telo.pop(0)

        if napravlenie == 'right':
            q = 1
        if napravlenie == 'left':
            q = 2
        if napravlenie == 'down':
            q = 3
        if napravlenie == 'up':
            q=4
        telo.append([xy[0],xy[1],q])
        sscore(f'score: {score}','darkgreen')


        pygame.display.update()
        clock.tick(10)
    if game_over == True and game_end == False:
            print('1')
            record = 'unbeat'
            dockread = open('maxx.txt', 'r')
            apt = []
            number = 0
            datadwa = []
            data = dockread.readlines()
            data = [line.rstrip() for line in data]
            print(data)
            dockread.close()
            print(data[1])
            if int(data[1])<score:
                record = 'beat'
            if record == 'beat':
                data.pop(1)
                data.pop(0)
                data.append(f'{name}')
                data.append(score)
                writefile = open('maxx.txt', 'w')
                print('побит')
                for i in [1,3,5,7,9]:
                    datadwa.append([int(data[i]), f'{data[i-1]}'])
                print(f'datadwa={datadwa}')
                datadwa.sort(key=lambda student: student[0])

                for i in range(len(datadwa)):
                    writefile.write(f'{datadwa[i][1]}\n')
                    writefile.write(f'{datadwa[i][0]}\n')
                writefile.close()
            else:
                for i in [1,3,5,7,9]:
                    datadwa.append([int(data[i]), f'{data[i-1]}'])
                print(f'datadwa={datadwa}')
                datadwa.sort(key=lambda student: student[0])

            dis.blit(fonend, (0,0))
            message(f'you lose with score: {score}', 'black')
            if record == 'beat':
                beat('u beat one of the max records', 'red')
            records('top','black', 200)
            records(f'{datadwa[4][1]}  {datadwa[4][0]}', 'red', 270)
            records(f'{datadwa[3][1]}  {datadwa[3][0]}', 'pink', 310)
            records(f'{datadwa[2][1]}  {datadwa[2][0]}', 'yellow', 350)
            records(f'{datadwa[1][1]}  {datadwa[1][0]}', 'brown', 390)
            records(f'{datadwa[0][1]}  {datadwa[0][0]}', 'black', 430)
            pygame.display.update()
            time.sleep(2)
            game_over = False
pygame.quit()
quit()
