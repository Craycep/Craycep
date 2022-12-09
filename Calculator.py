# Turtle Graphic Game
import time
import turtle
import math
import random
import os
import simpleaudio as sa
import wave

# Sounds
bounce_sound = sa.WaveObject.from_wave_file('Bounce.wav')
collision_sound = sa.WaveObject.from_wave_file('Collision.wav')

# Set up screen
wn = turtle.getscreen()
wn.clear()
wn.bgcolor('lightgreen')
#wn.bgpic('TGGame.gif')
wn.tracer(3)

# Draw border
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-330, -330)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(660)
    mypen.left(90)
mypen.hideturtle()

# Create player Turtle
player = turtle.Turtle()
player.color('blue')
player.shape('circle')
player.shapesize(2, 2, 1)
player.penup()  # delete trace
player.speed(0)

# Create multiple goals
max_goals = 25
goals = []
for count in range(max_goals):
    goals.append(turtle.Turtle())
    goals[count].color('dark red')
    goals[count].shape('circle')
    goals[count].penup()  # delete trace
    goals[count].speed(2)
    goals[count].setposition(random.randint(-300, 300), random.randint(-300, 300))

# Set speed variable
speed = 1


# Create the score of the game
game_score = 0


# Define functions
def turn_left():
    player.left(30)


def turn_right():
    player.right(30)


def increase_speed():
    global speed
    speed += 1


def decrease_speed():
    global speed
    speed -= 1


def is_collision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 20:
        return True
    else:
        return False


# Set keyboard binding
turtle.listen()
turtle.onkey(turn_left, "Left")
turtle.onkey(turn_right, "Right")
turtle.onkey(increase_speed, "Up")
turtle.onkey(decrease_speed, "Down")

while True:
    player.forward(speed)

    # Boundary Checking for player
    if player.xcor() > 330 or player.xcor() < -330:
        player.right(random.randint(160, 200))
        play_bounce = bounce_sound.play()
        play_bounce.stop()

    if player.ycor() > 330 or player.ycor() < -330:
        player.right(random.randint(160, 200))
        play_bounce = bounce_sound.play()
        play_bounce.stop()

    # Move the goal
    for count in range(max_goals):
        goals[count].forward(0.3)

        # Collision checking
        if is_collision(player, goals[count]):
            goals[count].setposition(random.randint(-300, 300), random.randint(-300, 300))
            goals[count].right(random.randint(0, 360))
            game_score += 1
            # Draw  the score on the screen
            mypen.undo()
            mypen.penup()
            mypen.hideturtle()
            mypen.setposition (-300, 330)
            score_string = 'Score: %s' %game_score
            mypen.write(score_string, False, align='left', font=('Arial', 14, 'normal'))
            play_collision = collision_sound.play()
            play_collision.stop()

        # Boundary Checking for goal
        if goals[count].xcor() > 320 or goals[count].xcor() < -320:
            goals[count].right(random.randint(110, 250))


        if goals[count].ycor() > 320 or goals[count].ycor() < -320:
            goals[count].right(random.randint(110, 250))

