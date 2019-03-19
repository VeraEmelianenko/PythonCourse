''' C3: Определить длину самого короткого слова в строке, заданной пользователем '''

a = input()
a_w = ''

for symbol in a:  # в этом блоке избавляемся от знаков препинания - всех, кроме тире, ибо тире ещё и дефис может обозначать
    if symbol == '.' or symbol ==  ',' or symbol ==  '?' or symbol ==  '!' or symbol ==  ':' or symbol == ';' or symbol == '(' or symbol ==   ')':
        a_w = a_w
    else:
        a_w = a_w + symbol
#тут полу4или строку a_w без знаков препинания
        
slova = a_w.split() 
for slovo in slova: #тут удаляем тире 
    if slovo == '-':
        slova.remove(slovo)
        
slova_unic = [] # ну а вдруг строка - это "война и мир" , и там стопятьсот разных слов? удобнее иметь list с уникальными словами
for slovo in slova:
    if slova_unic.count(slovo) == 0:
        slova_unic.append(slovo)
#итого у нас есть list с уникальными словами, повторяются только слова с большой и маленькой буквы (но это on purpose)
# и только тут я дошла до осмысленного блока 

short_word = len(slova_unic[0])

for i in range (len(slova_unic)):
    if len(slova_unic[i]) < short_word:
           short_word = len(slova_unic[i])
        
print('Длина самого короткого слова -', short_word, 'знака')
