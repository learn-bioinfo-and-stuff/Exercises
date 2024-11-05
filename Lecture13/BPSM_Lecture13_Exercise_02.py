#!/usr/bin/env python3
# Question number 2. Multiple exons from genom
# extract the exon segment, concatenate them and write them into a new file

# Input data
# open genomic_dna2.txt
genomic_dna = open("genomic_dna2.txt")
# open exons.txt
exon_ref = open("exons.txt")

# Process
# Preview exons.txt and make it into a list, as a ref position
with exon_ref as file:
    print("1. This is the content of exons.txt versi 1")
    # convert each line into list.
    exon_ref_content = file.readlines()  # the exon position. this is already a list.
    print(exon_ref_content)  # output: item in list still 'X,Y\n'
    # using loop, clean up item in list and replace delimeter
    # define the output list
    exon_ref_content_clean = []
    for item in exon_ref_content:
        # syntax to remove \n and change delimiter
        clean_item = item.rstrip('\n').replace(",",":")
        # append each output of looping into output list (make it into single list)
        exon_ref_content_clean.append(clean_item)
    print(f'2. This is the content of exons.txt versi 2 or clean\n{exon_ref_content_clean}')

# Preview the genomic data
with genomic_dna as file:
        print("3. This is the original content of genomic_dna2.txt")
        genomic_dna_content = genomic_dna.read().replace("\n","")   #not only read, but also remove space between lines
        print(genomic_dna_content)
        # Transform into a list, where each item represents a single letter.
        print("4. list of genomic_dna2:")
        list_genomic_dna2 = list(genomic_dna_content)
        print(list_genomic_dna2)        # our genomic data is now one list @item = single letter

# Get exon sequence
# Define the output txt
exon_seq_only = "output_exon_seq_only.txt"
with open(exon_seq_only,"a") as outputfile:
    for item in exon_ref_content_clean:         # taking the output of process 2 into this process
        # convert item as start and stop number
        start_str, stop_str = item.split(":")    #split by delimite
        start = int(start_str)                   #convert into int
        stop = int(stop_str)                     #convert into int
        # take item from list exon ref with reference start and stop position
        sub_exon = list_genomic_dna2[start:stop]
        print(f'This is the fragment {item} of exon-only:\n{sub_exon}')
        # concatenate sub_exon (list of list) into one long str
        outputfile.write(''.join(sub_exon))

# Output
# Preview the results
with open(exon_seq_only) as file:
    file_content = file.read()
    print(f'The content of Exon_only_seq:\n{file_content}')
