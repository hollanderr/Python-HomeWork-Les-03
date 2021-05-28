"""
Программа запрашивает у пользователя строку чисел, разделённых пробелом. 
При нажатии Enter должна выводиться сумма чисел. 
Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter. 
Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
"""
summ = 0
while True:
  summ += sum([float(i) for i in input().split(" ")])
  print(summ)

# Вариант №2 Функция

def summa():
  summ = 0
  while True:
    try: 
      summ += sum([float(i) for i in input().split(" ")])
    except ValueError:
      return
    print(summ)

summa()
# Вариант №3
def summa():
  summ = 0
  while True:
    try:
      summ += sum([float(i) for i in input().split(" ")])
    except ValueError:
      print("Неправильный ввод! Хотите закончить? Y/N")
      flag = input()
      if flag in ("Y","y"):
        break
    print(summ)
summa()