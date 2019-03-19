'''(*) C2: Посчитать сумму и произведение цифр положительного числа, заданного пользователем '''

chislo = input('Введите положительное число \n' )

ch = ''
summa = 0
proizv = 1 

for symbol in chislo:  # в этом блоке просто избавляемся от точки или запятой - ведь не сказано, что число целое
    if symbol == '.':
        ch = ch
    else:
        ch = ch + symbol
        
for symbol in ch:
    summa = summa + int(symbol)
    proizv = proizv * int (symbol) 

print ('Сумма цифр равна', summa, '\nПроизведение цифр равно', proizv) 
