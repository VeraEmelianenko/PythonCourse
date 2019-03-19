'''(*) C1: Пользователь задаёт список чисел, выведите все элементы списка,
которые больше предыдущего элемента'''

stroka = input('Введите список чисел через пробел. Десятичные дроби вводите через точку \n' )
spisok = list(stroka.split())
for i in range (len(spisok) - 1):
    if float(spisok[i+1]) > float(spisok[i]):
        print (spisok[i+1])
