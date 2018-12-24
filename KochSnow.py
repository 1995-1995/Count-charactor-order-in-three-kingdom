#KochSnow.py
import turtle as t
def koch(side,level):
    if level == 0:
        t.fd(side)
    else:
       for angle in [0,60,-120,60]:
           t.left(angle)
           koch(side/3,level-1)
def main(side):
    t.setup(1200,900,200,200)
    t.pu()
    t.bk(200)
    t.left(90)
    t.fd(100)
    t.seth(0)
    t.pd()
    t.pensize(5)
    t.color('red')
    for i in range(3):
        koch(450,side)
        t.right(120)
        t.down()
        t.hideturtle()
main(3)

