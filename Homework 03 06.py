"""
Задания 6 и 7!!!
Реализовать  функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же, 
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
"""
def int_func():
	text = input("Введите текст: ")
	text = str.title(text)
	print(text)
int_func()

# Вариант 2-й, без использования встроенной ф-ции title
def int_func():
	text = input("Введите текст: ")
	text = [str(i) for i in text]
	text[0] = chr(ord(text[0]) - 32)
	for i in range(len(text)):
	  if text[i] == " ":
	    text[i+1] = chr(ord(text[i+1]) - 32)
	text = "".join(text)
	print(text)
int_func()

# Вар-т №3 через upper
def int_func():
	text = input("Введите текст: ")
	text = [str(i) for i in text]
	text[0] = str.upper(text[0])
	for i in range(len(text)):
	  if text[i] == " ":
	    text[i+1] = str.upper(text[i+1])
	text = "".join(text)
	print(text)
int_func()

# Вар-т №4 С защитой от ввода пустой строки и символов " " в начале и/или конце строки, 
# а также неправильных изменений при вводе иных символов, кроме алфавита
def int_func():
	alphabet = "абвгдеёжзийклмнопрстуфхцшщъьэюяabcdefghijklmnopqrstuvwxyz"
	alphabet2 = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦШЩЪЬЭЮЯABCDTFGHIJKLMNOPQRSTUVWXYZ"
	text = [i for i in input()]  # строку преобразуем в список
	if text[0] in alphabet:
	  text[0] = alphabet2[alphabet.index(text[0])]  # Находим индекс 1-й буквы в строке alphabet и присваиваем
# text[0] значение аналогичной буквы из списка верхнего регистра alphabet2
	for i in range(len(text)):
	  if text[i] == " " and i+1 < len(text) and text[i+1] in alphabet:
	    text[i+1] = alphabet2[alphabet.index(text[i+1])]
	print("".join(text))  # Преобразуем text из списка обратно в строку и печатаем ее
#	print(*text) - Вывод списка на экран в виде строки, вместо "".join(text)
int_func()
