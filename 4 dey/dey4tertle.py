from turtle import *
colormode(255)


for r in range (255):
	for g in range (255):
		for b in range (255):
			if r == 255:
				r=0
			elif g == 255:
				g=0
			elif b == 255:
				b=0
			else:
				color((r,g,b))
				for i in range (360):
					forward(100)
					right(i+90)
					forward(100)
					right(i+90)
					forward(100)
					right(i+90)
					forward(100)
					right(i+90)
input()