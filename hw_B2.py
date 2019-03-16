 #Reverse complement

with open('rosalind_revc.txt', 'r') as file:
    dna = file.read()
s = dna
def reverse(s): 
  inv = "" 
  for i in s: 
    inv = i + inv
  return inv
a = reverse (s)

trans = str.maketrans('ATGC', 'TACG')
c = a.translate(trans)  #знаю, мы этого не у4или, но оно нагуглилось

print(c)
