with open('rosalind_rna.txt', 'r') as file:
    dna = file.read() 

print(dna.replace('T', 'U')) 
