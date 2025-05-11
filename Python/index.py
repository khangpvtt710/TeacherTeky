import turtle
import pygame
scr = turtle.Screen()
tt = turtle.Turtle()
scr.setup(500,500)
scr.bgpic ('nen.gif')
scr.addshape(r'D:\IT\python\bien.gif')
turtle.color('red')
move = 100
turn = 100
def  foward():
    turtle.forward(move)
def  backward():
    turtle.backward(move)
def left():
    turtle.left(turn)
def right():
    turtle.right(turn)
turtle.penup()
scr.onkey(foward,'Up')
scr.onkey(backward,'Down')
scr.onkey(left,'Left')
scr.onkey(right,'Right')
scr.listen()
turtle.done()
