"""
Выполнить функцию, которая принимает несколько параметров, 
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон. 
Функция должна принимать параметры как именованные аргументы. 
Осуществить вывод данных о пользователе одной строкой.

"""
def data_input():
	name = input("Введите Ваше Имя: ")
	family = input("Введите Вашу Фамилию: ")
	birth_year = input("Введите Ваш Год Рождения: ")
	city = input("Введите Ваш  Город Проживания: ")
	email = input("Введите Ваш Еmail: ")
	tel = input("Введите Ваш Телефон: ")

	print(f" Имя: {name}, Фамилия: {family}, Год Рождения: {birth_year}, Город: {city},  Email: {email}, Телефон: {tel}")

data_input()