import turtle
import time
#画表盘
t = turtle.Turtle()
t.hideturtle()
#画时针
s = turtle.Turtle()
s.hideturtle()
s.left(90)
s.speed(0)
#画分针
f = turtle.Turtle()
f.hideturtle()
f.left(90)
f.speed(0)
#画秒针
m = turtle.Turtle()
m.hideturtle()
m.left(90)
m.speed(0)


def drwa_table():
    turtle.tracer(12)
    t.left(90)
    t.penup()
    i = 1
    while i < 13:
        t.right(360/12)
        if i % 3 == 0:
            t.color("red")
        else:
            if i % 2 == 0:
                t.color("green")
            else:
                t.color("blue")
        t.fd(200)
        t.write(i, align="center", font=("微软雅黑", 18, 'normal'))
        t.fd(-200)
        i = i + 1
    turtle.update()


def draw_time():
    #初始化获取时间
    localtime = time.localtime(time.time())
    global __hh
    __hh = localtime[3] % 12
    global __ff
    __ff = localtime[4]
    global __mm
    __mm = localtime[5]
    #print(__hh, __ff, __mm)

    s.clear()
    s.seth(90)
    s.right((__hh+(__ff/60))*30)
    s.pensize(15)
    s.fd(60)
    s.fd(-60)
    turtle.update()
    f.clear()
    f.seth(90)
    f.right(__ff*6)
    f.pensize(7)
    f.fd(100)
    f.fd(-100)
    turtle.update()

    m.clear()
    m.seth(90)
    m.right(__mm*6)
    m.pensize(3)
    m.fd(170)
    m.fd(-170)
    turtle.update()

#画出表盘
drwa_table()

while True:
    time.sleep(0.99)
    draw_time()
    turtle.update()
