#Rosalind HAMM   given two strings of the same length,  count missmatches

with open('rosalind_hamm.txt', 'r') as file:
    dna = file.read()
a = dna.splitlines()
first = a[0]
second = a[1]

g = 0
for i in range (len(first)):
    if first[i] == second [i]:
        g = g + 0
    else:
        g = g + 1
print (g) 
