import random
a = random.randint(0, 100)

#Я слегка расширила задачуб но так веселее
variants = ('Oк', 'Хорошо', 'Уговорил', 'Да', 'да', 'ок', 'хорошо', 'ok', 'уговорил', 'согласен', 'согласна', 'добра', 'Согласен', 'Согласна', 'Можно', 'может быть')
otricanie = ('нет', 'Нет', 'Отстань', 'No', 'no')
otkas = ('Нуууу так неинтересно', 'Скучно с тобой', 'Вот и предлагай таким поиграть', 'Вот значит как?!', 'Ну эээээййй...', 'Эхххх...')
inv = input('Давай сыграем с тобой в игру. Я загадал число, а ты попробуй угадать. Согласен?  \n' )

while True:
    
    if variants.count(inv) == 1:
        print ('Правильный выбор')
        break
    if variants.count(inv) == 0:
        print (otkas[random.randint(0, 5)])
        inv = input('Давай всё же сыграем, а? \n')

b = ('Неправильно, ', 'Ха, на самом деле ', 'Ну нееееет, ', 'Не расстраивайся, но ',  'Попытайся ещё раз, ')
i = int(input('Введи любое число от 0 до 100 \n'))
while True: 
    if i > a:
        print ( b[random.randint(0, 4)],  "твоё число больше искомого")
        i = int(input())
    elif i < a :    
        print (b[random.randint(0, 4)],  "твоё число меньше искомого")
        i = int(input())
    elif i == a:
        print ('Поздравляю, ты угадал! Ну, неужели тебе не понравилось?)')
        
        while True:
            konec = input('Хочешь ещё?...\n' )
            if variants.count(konec) == 1:
                print ('А вот фигушки тебе!')
                break
            elif otricanie.count(konec) ==1:
                print ('Я так и знал! *уходит в закат*')
                break
            else:
                print ('Переформулируй, пожалуйста, я не понял')
        break 
