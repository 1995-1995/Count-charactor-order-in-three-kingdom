#sevenDigitDraw.py
import turtle as t
def drawLine(Bool):
    t.pd() if Bool else t.pu()
    t.fd(40)
    t.right(90)
def drawDig(digit):
    drawLine(True) if digit in [0,1,2,6,8] else drawLine(False)
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    t.pu()
    t.fd(40)
    t.left(90)
    t.pd()
    drawLine(True) if digit in [0,1,4,5,6,8] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,4,7,8,9] else drawLine(False)
    t.left(90)
    t.pu()
    t.fd(20)
def drawDate(date):
    for i in date:
        drawDig(eval(i))
def main():
    t.setup(800,400,200,200)
    t.pensize(5)
    t.color('black')
    drawDate('20181219')
    t.hideturtle()
    t.down()
main()

    
