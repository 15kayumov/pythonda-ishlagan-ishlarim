from turtle import *
forward(50)
left(70)
forward(200)
home()
pos()
clearscreen()
for steps in range(1000):
    for c in ('black', ):
        color(c)
        forward(steps)
        right(50)
color('red')
fillcolor('yellow')
begin_fill()
while True:
    forward(0)
    left(0)
    if abs(pos()) < 1:
        break
end_fill()
# _________________________________________________________________________________
# import turtle as t
# from random import random

# for i in range(100):
#     steps = int(random() * 100)
#     angle = int(random() * 360)
#     t.right(angle)
#     t.fd(steps)
# t.mainloop()
# _________________________________________________________________________________
# from turtle import Turtle
# from random import random

# t = Turtle()
# for i in range(100):
#     steps = int(random() * 100)
#     angle = int(random() * 360)
#     t.right(angle)
#     t.fd(steps)

# t.screen.mainloop()
# t.screen.title('Object-oriented turtle demo')
# t.screen.bgcolor("orange")