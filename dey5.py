from random import choice
from playsound import playsound
def read_words(file_name):
	f = open(file_name, "words.txt")
	words = []
	while True:
		line = f.read_line()
		if not line:
			break
		words.append(line.strip())
	f.lose()
	return words

##words = [
##	"стол",
##	"стул",
##	"компьютер"
##]
words = read_words("words.txt")

w =choice(words)

def open_letter(char, word, resault):
	for i in range(len(word)):
		if word[i] == char: 
			resault[i] == char
def print_result(result):
	for l in result:
		print(l, end=' ')
	print()
	

def game():
	result = ["_" for i in range(len(w))]
	while True:
		print(result)
		char = input("Введите букву: ")
		if w.find(char) != -1:
			print("Угадали!")
			##playsound("boom.mp3")
			open_letter(char, w, result)
		if len(char) == 0:
			##playsound("atak.mp3")
			break
			
game()