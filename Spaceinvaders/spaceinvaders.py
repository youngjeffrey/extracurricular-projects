import turtle
import os
import math
import random


wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("images/ezgif-2-4c1bd379c9.gif")

#register the shapes
turtle.register_shape("images/invader.gif")
turtle.register_shape("images/player.gif")

#Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()


#set the score to 0
score = 0

#draw the score on screen
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial",14,"normal"))

#player is controlled by user
player = turtle.Turtle()
player.color("blue")
player.shape("images/player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 18

#choose number of enemies
number_of_enemies = 6
#create list
enemies = []

#add enemies to the list
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("images/invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x,y)

enemyspeed = 4

#create weapon
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.hideturtle()
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)


bulletspeed = 20

#Define bullet state
#ready to fire
#fire- bullet is moving
bulletstate = "ready"
gamestate = True

def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    global bulletstate
    #checks if bulletstate is ready to prevent spamming
    if bulletstate == "ready":
        bulletstate = "fire"
        #when bullet is fired, it is fired at the x and y position of player
        x = player.xcor()
        y = player.ycor()
        bullet.setposition(x,y + 10)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False

def play_again():
    gamestate = True

#Create keyboard bindings
turtle.listen()

#when left key is pushed the player is moved left
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")
turtle.onkey(play_again, "c")

#main game loop
while gamestate:

    for enemy in enemies:
        #move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        #move all of the enemies back and down
        if enemy.xcor() > 280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1

        if enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1

        if isCollision(bullet, enemy):
            #reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            #reset enemy to random spot
            x = random.randint(-200, 200)
            y = random.randint(50, 250)
            enemy.setposition(x,y)
            #update the score
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial",14,"normal"))

        if isCollision(player, enemy) or enemy.ycor() < -280:
            player.hideturtle()
            enemy.hideturtle()

            game_over = turtle.Turtle()
            game_over.speed(0)
            game_over.color("white")
            game_over.penup()
            game_over.setposition(-170, 0)
            gameoverstring = "GAME OVER. Press C to play again"
            game_over.write(gameoverstring, False, align="left", font=("Arial",20,"normal"))
            break

    #move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    #check to see if bullet has reached top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"


turtle.mainloop()
#delay = raw_input("Press enter to finish.")
