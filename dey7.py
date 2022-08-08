from turtle import *

def fratal(level, lenght):
	if level == 0:
		forward(lenght)
		return
	fratal(level-1, lenght/3)
	left(90)
	fratal(level-1, lenght/3)
	right(90)
	fratal(level-1, lenght/3)
	right(90)
	fratal(level-1, lenght/3)
	left(90)
	fratal(level-1, lenght/3)

tracer(False)
penup()
setpos(-500,0)
pendown()
fratal(8,600)
tracer(True)
input()