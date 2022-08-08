from turtle import *
import random

def move_to(x,y):
	penup()
	setx(x)
	sety(y)
	pendown()

def tree(n, a, da, size, lenght):
	if n == 0:
		return
	pensize(size)
	seth(a)
	forward(lenght)
	x,y = pos()
	tree(n - 1, a - da , random.randint(20, 90), size * 0.7, lenght * (random.randint(4, 9)*0.1))
	move_to(x, y)
	tree(n - 1, a + da , random.randint(20, 90), size * 0.7, lenght * (random.randint(4, 9)*0.1))

speed(0)
tracer(False)
move_to(0,-300)
left(90)
tree(15, 90, 10, 10, 200)
tracer(True)
input()