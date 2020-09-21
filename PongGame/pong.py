import turtle

wn = turtle.Screen()
wn.title("Pong by @Shyamashrita")
wn.bgcolor("#000080")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
sa = 0
sb = 0

# Paddle 1
p1 = turtle.Turtle()
p1.speed(0)
p1.shape("square")
p1.color("#ff66b3")
p1.shapesize(stretch_wid=4, stretch_len=1)
p1.penup()
p1.goto(-370, 0)

# Paddle 2
p2 = turtle.Turtle()
p2.speed(0)
p2.shape("square")
p2.color("#ff5c33")
p2.shapesize(stretch_wid=4, stretch_len=1)
p2.penup()
p2.goto(370, 0)

# Ball
b1 = turtle.Turtle()
b1.speed(0)
b1.shape("circle")
b1.color("#99ff99")
b1.penup()
b1.goto(0, 0)
b1.dx = 0.2
b1.dy = 0.2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("White")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0     Player B: 0", align="center", font=("Courier",24,"normal"))


def p1_up():
    y = p1.ycor()
    y += 20
    p1.sety(y)


def p1_down():
    y = p1.ycor()
    y -= 20
    p1.sety(y)


def p2_up():
    y = p2.ycor()
    y += 20
    p2.sety(y)


def p2_down():
    y = p2.ycor()
    y -= 20
    p2.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(p1_up, "w")
wn.onkeypress(p1_down, "s")
wn.onkeypress(p2_up, "Up")
wn.onkeypress(p2_down, "Down")

# Main game loop
while True:
    wn.update()

    # Move the ball
    b1.setx(b1.xcor() + b1.dx)
    b1.sety(b1.ycor() + b1.dy)

    # Border checking
    if (b1.ycor() > 290):
        b1.sety(290)
        b1.dy *= -1
    if (b1.ycor() < -290):
        b1.sety(-290)
        b1.dy *= -1
    if (b1.xcor() > 390):
        b1.goto(0, 0)
        b1.dx *= -1
        sa +=1
        pen.clear()
        pen.write("Player A: {}     Player B: {}".format(sa,sb), align="center", font=("Courier", 24, "normal"))
    if (b1.xcor() < - 390):
        b1.goto(0, 0)
        b1.dx *= -1
        sb +=1
        pen.clear()
        pen.write("Player A: {}     Player B: {}".format(sa,sb), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if (b1.xcor() > 340 and b1.xcor()<350 and (b1.ycor() < p2.ycor() + 30 and b1.ycor() > p2.ycor() - 30)):
        b1.setx(340)
        b1.dx *= -1
    if (b1.xcor() < -340 and b1.xcor() > -350 and (b1.ycor() < p1.ycor() + 40 and b1.ycor() > p1.ycor() - 40)):
        b1.setx(-340)
        b1.dx *= -1