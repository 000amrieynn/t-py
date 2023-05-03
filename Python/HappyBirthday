import turtle

happy = turtle.Screen()
happy.bgcolor("black")
sjsj = turtle.Turtle()
sjsj.width(7)
colors = ["#f5ac2f", "#279cf5", "#d820f5", "#a2f52f", "#f527c1"]


def draw_ankita(i, x, y):
    sjsj.pencolor("linen")
    sjsj.color(colors[i % 7])
    sjsj.lt(70)
    sjsj.penup()
    sjsj.goto(x, y)
    sjsj.pendown()
    sjsj.circle(22)
    sjsj.end_fill()


def ballon(x, y):
    sjsj.pensize(4)
    for i in range(5):
        draw_ankita(i, x, y)


def f1():
    for i in range(7):
        sjsj.pensize(5)
        sjsj.pencolor('light blue')
        sjsj.color(colors[i % 19])
        sjsj.begin_fill()
        sjsj.left(330)
        sjsj.forward(55)
        sjsj.begin_fill()
        sjsj.rt(110)
        sjsj.circle(33)
        sjsj.end_fill()
        sjsj.rt(11)
        sjsj.backward(33)
        sjsj.end_fill()


def cake(x, y):
    sjsj.fd(x)
    sjsj.rt(90)
    sjsj.fd(y)
    sjsj.rt(90)
    sjsj.fd(x)
    sjsj.rt(90)
    sjsj.fd(y)


def move(x, y):
    sjsj.up()
    sjsj.setposition(0, 0)
    sjsj.setheading(90)
    sjsj.rt(90)
    sjsj.fd(x)
    sjsj.lt(90)
    sjsj.fd(y)
    sjsj.pendown()


def mov(x, y):
    sjsj.up()
    sjsj.setposition(0, 0)
    sjsj.setheading(90)
    sjsj.lt(90)
    sjsj.fd(x)
    sjsj.rt(90)
    sjsj.fd(y)
    sjsj.pendown()


def A(size):
    sjsj.rt(19)
    sjsj.forward(size)
    sjsj.rt(141)
    sjsj.fd(size)
    sjsj.backward(size / 2)
    sjsj.rt(105)
    sjsj.fd(int(size / 3))


def B(size):
    sjsj.forward(size)
    sjsj.rt(90)
    for i in range(18):
        sjsj.rt(9)
        sjsj.fd(size // 20)
    for i in range(18):
        sjsj.rt(size // 5)
        sjsj.backward(size // 20)


def D(size):
    sjsj.fd(size)
    sjsj.rt(90)
    sjsj.fd(size // 10)
    for i in range(13):
        sjsj.rt(13)
        sjsj.fd(size // 8)


def E(size):
    sjsj.rt(90)
    sjsj.fd(int(size / 3))
    sjsj.back(int(size / 3))
    sjsj.left(90)
    sjsj.fd(size / 2)
    sjsj.rt(90)
    sjsj.fd(int(size / 3))
    sjsj.back(int(size / 3))
    sjsj.lt(90)
    sjsj.fd(size / 2)
    sjsj.rt(90)
    sjsj.fd(int(size / 3))


def H(size):
    sjsj.fd(size)
    sjsj.backward(size // 2)
    sjsj.rt(90)
    sjsj.fd(size // 2)
    sjsj.lt(90)
    sjsj.fd(size // 2)
    sjsj.backward(size)


def I(size):
    sjsj.fd(size)
    sjsj.rt(90)
    sjsj.circle(size // 8)

def L(size):
    sjsj.rt(90)
    sjsj.fd(int(size / 2))
    sjsj.back(int(size / 2))
    sjsj.lt(90)
    sjsj.fd(size)

def N(size):
    sjsj.fd(size)
    sjsj.rt(150)
    sjsj.fd(size + int(size / 6))
    sjsj.lt(150)
    sjsj.fd(size)


def P(size):
    sjsj.fd(size)
    sjsj.rt(90)
    sjsj.fd(size // 8)
    for i in range(8):
        sjsj.rt(20)
        sjsj.fd(size // 9)

def R():
    sjsj.fd(60)
    sjsj.rt(90)
    sjsj.fd(7)
    for i in range(15):
        sjsj.rt(12)
        sjsj.fd(3)
    sjsj.lt(120)
    sjsj.fd(40)


def S(size):
    sjsj.rt(90)
    for i in range(0, 5):
        if i < 3:
            sjsj.fd(size / 2)
            sjsj.lt(90)
            if i == 2:
                sjsj.rt(90)
        else:
            sjsj.right(90)
            sjsj.fd(size / 2)


def T(size):
    sjsj.fd(size)
    sjsj.rt(90)
    sjsj.fd(size // 2)
    sjsj.backward(size // 2)


def Y(size):
    sjsj.fd(size)
    sjsj.left(60)
    sjsj.fd(size // 2)
    sjsj.backward(size // 2)
    sjsj.rt(90)
    sjsj.fd(size // 1.5)

sjsj.speed(19)


mov(120, 30)
sjsj.begin_fill()
sjsj.color("#f7b543")
cake(40, 180)
sjsj.end_fill()
mov(110, 75)
sjsj.color("#d152f7")
sjsj.begin_fill()
cake(40, 160)
sjsj.end_fill()
mov(100, 120)
sjsj.color("#f54eb8")
sjsj.begin_fill()
cake(40, 140)
sjsj.end_fill()
mov(30, 170)
sjsj.width(11)
sjsj.pencolor("red")
sjsj.circle(7)
move(180, 307)
mov(0, 0)
ballon(-490, 200)
ballon(490, 200)
ballon(183, -150)
ballon(-133, -150)

sjsj.speed(7)
sjsj.width(9)
sjsj.pencolor("#319df5")
mov(260, 205)



sjsj.pencolor("red")
style = ('Arial', 50, 'italic')
sjsj.write("Chinara Teacher", font=style)

sjsj.pencolor("cyan")
sjsj.width(13)
mov(260, -80)
H(100)
sjsj.width(7)
mov(190, -80)
A(65)
mov(135, -80)
P(60)
mov(100, -80)
P(60)
mov(52, -80)
Y(60)
mov(28, -80)
B(60)
move(12, -80)
I(60)
move(36, -80)
R()
move(80, -80)
T(100)
move(102, -80)
H(60)
move(150, -80)
sjsj.pencolor('hotpink')
D(200)
move(160, -80)
A(60)
move(220, -80)
Y(60)
happy.exitonclick()
