#!/usr/bin/env python3

#define sequences
dna_seq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
print(dna_seq)
length_dna_seq = len(dna_seq)
print(f"Length of dna_seq: {length_dna_seq}")

#1.A count A nucleotides
a_count = dna_seq.count("A")
print(f"The number of A nucleotides in {dna_seq}: {a_count}")

#1.B count T nucleotides
t_count = dna_seq.count("T")
print(f"The number of T nucleotides in {dna_seq}: {t_count}")

#1.C add them and divide by length_dna_seq
total_AT = a_count + t_count
print(f"Total 'A' and 'T' nucleotides is {total_AT}")
divide_AT = total_AT/length_dna_seq
print(divide_AT)
print(f"The average 'A' and 'T': {divide_AT}")

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
replacement_4 = replacement_3.replace("C","g")
print(replacement_4)
#making it all upper case
complememt_seq = replacement_4.upper()
print(complememt_seq)

#3. Restriction fragment lengths
fragment_dna = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
motif = "GAATTC"

#3.1 find the position of the motif
motif_location = fragment_dna.find(motif)
print(f"Fragment DNA: {fragment_dna}")
if motif_location == -1:
  print(f"the {motif} motif is not found in our fragment dna")
else:
  print(f"the {motif} motif is found in the position: {motif_location} of our fragment dna")

#3.2 find the position of the cut. (G*AATTC)
position_cut = motif_location+1
print(f"Position to cut: {position_cut}")

#3.3 calculate the length of the second fragment of the cut
second_fragment = len(fragment_dna[position_cut:])
print(f"Second fragment dna or after split: {fragment_dna[position_cut:]}")
print(f"Length of fragment_dna: {len(fragment_dna)}")
print(f"Length of second fragment_dna based on the cut position: {second_fragment}")

#4 splicing out introns
genomic_dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCT\nACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCT\nATCATCGATCGATATCGATGCATCGACTACTAT"
print(genomic_dna)

#4.1 extract first and secon exon
exon_1 = genomic_dna[:65].lower()  #start until 63 real charac
exon_2 = genomic_dna[92:].lower()
print(f"First Exon:\n{exon_1}")
print(f"Second Exon:\n{exon_2}")

#4.2 join all exon to be coding sequence
coding_seq = exon_1 + exon_2
print(f"The coding Seq:\n{coding_seq}")

#4.3 length of coding sequence
print(f"Length of Coding Sequence: {len(coding_seq)}")

#4.4 divide by the length of original and multiply by 100
math_opertion = (len(coding_seq)/len(genomic_dna))*100
print(f"math operations: {math_opertion}")

#5. print original genomic_data with coding bases (Upper case) and non-coding (lower)
intron = genomic_dna[65:92].lower()
exon_1 = exon_1.upper()
exon_2 = exon_2.upper()
genomic_dna_fin = exon_1+intron+exon_2
print(f"Original Sequence:\n{genomic_dna}")
print(f"Genomic Sequence Final:\n{genomic_dna_fin}")
