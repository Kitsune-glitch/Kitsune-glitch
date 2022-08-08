from random import choice
words = [
	"Желание", 
	"Семнадцать",
	"Ржавый",
	"Рассвет", 
	"Печь", 
	"Девять", 
	"Добросердечный",
	"Возвращение на родину",
	"Один", 
	"Товарный вагон"
]

w = choice(words)
##resault = ["_" for i in range(len(w)) ]
##while True:
	##pass
	##print ("_ " * len(w))
##	input("введие букву")
##	if len(char) == 0:
##		break
def open_letter( char, word, resault):
	for i in range(len(word)):
		if word[i] == char:
			resault[i] = char
	
def game ():
	resault = ["_" for i in range (len(w)) ]
	while True:
		print(resault)
		char = input("введие букву: ")
		if w.find(char) != -1:
			print ("Угадали!")
			open_letter(char, w, resault)
		if len(char) == 0:
			break

		
##def zapol ()
##	a = [input('_') for i in range(len(w)]
##	for t in range(len(w)
 ##		a[t::] = w[t::]
 	##print a

