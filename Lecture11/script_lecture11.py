#!/usr/bin/env python3

#define sequences
dna_seq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
print(dna_seq)
length_dna_seq = len(dna_seq)
print("Length of" $dna_seq" : " + str(length_dna_seq))

#1.A count A nucleotides
a_count = dna_seq.count("A")
print("The number of A nucleotides in " $dna_seq" : "+ str(a_count))

#1.B count T nucleotides
t_count = dna_seq.count("T")
print("The number of T nucleotides in " $dna_seq" : "+ str(t_count))

#1.C add them and divide by length_dna_seq
total_AT = a_count + t_count
print("Total 'A' and 'T' nucleotides is " + str(total_AT))
divide_AT = total_AT/length_dna_seq
print(divide_AT)
print("The average 'A' and 'T': " + str(divide_AT))

#2. complementing DNA
#replace A with T
replacement_1 = dna_seq.replace("A","t")
print(replacement_1)
#replace T with A
replacement_2 = replacement_1.replace("T","a")
print(replacement_2)
#replace G with C
replacement_3 = replacement_2.replace("G","c")
print(replacement_3)
#replace C with G
replacement_4 = replaceme
