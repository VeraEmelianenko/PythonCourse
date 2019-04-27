with open('rosalind_subs.txt', 'r') as file:
    s, t = file.read().split()
a=[]
a.append(s.find(t)+1)

while True:
    if s.find(t, int(a[-1]), -1) == -1:
        break
    else:
        a.append(s.find(t, int(a[-1]), -1) +1)
print(*a, sep = ' ')
