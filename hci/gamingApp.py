import turtle, random

t = turtle.Turtle()
t.speed(0)
t.shape("square")
t.color("blue")
t.penup()

ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(random.randint(-150,150), 150)

score = 0
t.goto(0, -150)

def move_left():
    x = t.xcor() - 20
    t.setx(x)

def move_right():
    x = t.xcor() + 20
    t.setx(x)

turtle.listen()
turtle.onkeypress(move_left, "Left")
turtle.onkeypress(move_right, "Right")

while True:
    y = ball.ycor() - 5
    ball.sety(y)
    if ball.ycor() < -150 and abs(ball.xcor() - t.xcor()) < 20:
        score += 1
        print("Score:", score)
        ball.goto(random.randint(-150,150), 150)
    if ball.ycor() < -200:
        print("Game Over! Final Score:", score)
        break
