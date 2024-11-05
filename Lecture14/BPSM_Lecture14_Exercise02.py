#!/usr/bin/env python3
# Exercise 14. Question 2. K-mer counting
# Write a programme/script that, given any DNA sequence, will print all
# the k-mers (e.g. 4-mers) that occur more than n times.

# Input sequence ~ dummy
sequence_dummy ="atatatatatcgcgtatatatacgactatatgcattaattatagcatatcgatatatatatcgatattatatcgcattatacgcgcgtaattatat"

# Process
# Set parameter for sliding
k_mer_sizes =list(range(2,7))    # k_mer = window sizes, ini contoh aja untuk latihan
kmer_found_min = 3                 # kan mau cari yg occus 4 kali

# Process sliding for kmer size 2-6 with for loop
for item in k_mer_sizes:
    kmers_found = []               # empty list
    kmerrange = list(range(0,len(sequence_dummy)))       # kan mau cari tau berapa kali kita iterasi.  from 0 -end seq
    for starting_base in kmerrange:
        if (starting_base+item)<len(sequence_dummy)+1:    #oh ini mastiin kalau di iterasi ke-n, kita masih ada didalam seq itu
            seqout = sequence_dummy[starting_base:starting_base+item]
            kmers_found =kmers_found + [seqout]
    nonredundantset = list(set(kmers_found))   # ini untuk apa ya?
    for kmersfrequencies in nonredundantset:
        if kmers_found.count(kmersfrequencies) > kmer_found_min:
            print("Lots !" + str(kmersfrequencies) + " " + str(kmers_found.count(kmersfrequencies)))
        else:
            print(str(kmersfrequencies) + " " + str(kmers_found.count(kmersfrequencies)))
