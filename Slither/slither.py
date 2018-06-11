import pygame
import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
mintgreen = (170,255,128)
green = (0, 204, 102)

display_width = 800
display_height = 600

bg = pygame.image.load("images/resizedimage.jpg")
intro_bg = pygame.image.load("images/slitherintro.png")
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Slither')

icon = pygame.image.load("images/131-512.png")
pygame.display.set_icon(icon)

img = pygame.image.load('images/rsz_1snakehead.png')
img_apple = pygame.image.load('images/rsz_apple.png')
img_rock = pygame.image.load('images/rsz_rock.png')

clock = pygame.time.Clock()

block_size = 10
rect_size = 10
barrier_size = 20
#FPS = 8

direction = "right"

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.blit(bg,(0,0))
        message_to_screen("Paused",
                            black,-100,size="large")
        message_to_screen("Press C to continue or Q to quit",
                            black, 25)
        pygame.display.update()
        clock.tick(5)

def scores(score):
    text = smallfont.render("Score: " + str(score), True, black)
    gameDisplay.blit(text, [0,0])

def game_intro():

    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        #gameDisplay.blit(bg,(0,0))
        gameDisplay.blit(intro_bg, (20, 15))
        #message_to_screen("Welcome to Slither",green,-100,
        #                    size="large")
        #message_to_screen("How to play: Arrow keys to move", black, -30)
        #message_to_screen("Objective is to eat the apples", black, 10)
        #message_to_screen("Avoid running into yourself, the rocks, and the edges", black, 50)
        #message_to_screen("Press C to play or Q to exit", black, 180)
        pygame.display.update()
        clock.tick(15)


def snake(block_size, snakelist):

    if direction == "right":
        head = pygame.transform.rotate(img, 270)

    if direction == "left":
        head = pygame.transform.rotate(img, 90)

    if direction == "up":
        head = img

    if direction == "down":
        head = pygame.transform.rotate(img, 180)

    gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))
    for XnY in snakelist[:-1]:
        pygame.draw.rect(gameDisplay, green, [XnY[0],XnY[1],block_size,block_size])

def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_to_screen(msg,color, y_displace=0, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width/2), (display_height/2) + y_displace
    gameDisplay.blit(textSurf, textRect)

def gameLoop():
    global direction
    gameExit = False
    gameOver = False
    FPS = 8

    lead_x = display_width / 2
    lead_y = display_height / 2
    lead_x_change = 10
    lead_y_change = 0

    snakelist = []
    snakelength = 1
    score = 0
    blocks = 0
    blockX2 = -500
    blockY2 = -500
    blockX3 = -600
    blockY3 = -600
    blockslistX = []
    blockslistY = []

    randAppleX = round(random.randrange(0, display_width - block_size)/10.0)*10.0
    randAppleY = round(random.randrange(0, display_height - block_size)/10.0)*10.0

    if randAppleX in blockslistX and randAppleY in blockslistY:
        randAppleX = round(random.randrange(0, display_width - block_size)/10.0)*10.0
        randAppleY = round(random.randrange(0, display_height - block_size)/10.0)*10.0

    blockX = round(random.randrange(0, display_width - barrier_size)/20.0)*20.0
    blockY = round(random.randrange(0, display_height - barrier_size)/20.0)*20.0

    blockslistX.append(blockX)
    blockslistY.append(blockY)

    if blockX == randAppleX and blockY == randAppleY:
        randAppleX = round(random.randrange(0, display_width - block_size)/10.0)*10.0
        randAppleY = round(random.randrange(0, display_height - block_size)/10.0)*10.0

    while not gameExit:

        while gameOver == True:
            gameDisplay.blit(bg, (0, 0))
            message_to_screen("Game Over", red, -50, size="large")
            message_to_screen("Your final score: " + str(score), black, 50, size="small")
            message_to_screen("Press C to play again or Q to quit", black, 100, size="small")
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():

            #exit game with exit button
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = block_size
                    lead_x_change = 0
                elif event.key == pygame.K_p:
                    pause()

            #use this if you want to stop moving after the key is up
            #if event.type == pygame.KEYUP:
            #    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            #        lead_x_change = 0

        if lead_x >= display_width or lead_x <= 0 or lead_y >= display_height or lead_y <= 0:
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        #gameDisplay.fill(mintgreen)
        gameDisplay.blit(bg, (0, 0))
        #draw apple
        gameDisplay.blit(img_apple,(randAppleX, randAppleY))
        gameDisplay.blit(img_rock,(blockX, blockY))

        if blocks == 1:
            blockX2 = 350
            blockY2 = 400
            blockslistX.append(350)
            blockslistY.append(400)
            gameDisplay.blit(img_rock,(blockX2, blockY2))

        if blocks == 2:
            blockX3 = 200
            blockY3 = 250
            blockX2 = 350
            blockY2 = 400
            blockslistX.append(200)
            blockslistY.append(250)
            gameDisplay.blit(img_rock,(blockX2, blockY2))
            gameDisplay.blit(img_rock,(blockX3, blockY3))

        snakehead = []
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snakelist.append(snakehead)

        if len(snakelist) > snakelength:
            del snakelist[0]

        #gameover if collision
        for eachSegment in snakelist[:-1]:
            if eachSegment == snakehead:
                gameOver = True

        snake(block_size, snakelist)

        #use this command once all the background has been finished

        scores(score)
        pygame.display.update()

        if lead_x == randAppleX and lead_y == randAppleY:
            randAppleX = round(random.randrange(0, display_width - block_size)/10.0)*10.0
            randAppleY = round(random.randrange(0, display_height - block_size)/10.0)*10.0
            snakelength += 1
            score += 1
            FPS += 0.1

            if score > 0 and score % 6 == 0:
                FPS += 1
                blocks += 1

        #if lead_x > blockX and lead_x < blockX - barrier_size and lead_y > blockY and lead_y < blockY + barrier_size:
        if blockX <= lead_x <= barrier_size + blockX  and blockY <= lead_y <= blockY + barrier_size:
            gameOver = True

        if blockX2 <= lead_x <= barrier_size + blockX2  and blockY2 <= lead_y <= blockY2 + barrier_size:
            gameOver = True

        if blockX3 <= lead_x <= barrier_size + blockX3  and blockY3 <= lead_y <= blockY3 + barrier_size:
            gameOver = True

        clock.tick(FPS)

    pygame.quit()
    quit()

game_intro()
gameLoop()
