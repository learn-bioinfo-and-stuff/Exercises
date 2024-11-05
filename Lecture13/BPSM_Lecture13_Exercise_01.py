#!/usr/bin/env python3
# Question number 1. processing dna
# trim adapter (first 14 characters) and count length sequence


# Input
# open input.txt
raw_seq = open("input.txt")
with raw_seq as file:
    # convert each line into list
    raw_seq_content = file.readlines()   #readlines ini tuh jadi list lho outputnya
print(f'This is our raw sequences:\n{"".join(raw_seq_content)}') #makanya ini musti di ubah jadi str lagi dan digabung

# Process: To remove adapter and count the remaining length
# Give information of initial length of each sequences
print('Initial length of each sequence:')
# 2 arguments (i and line: x time looping and line as element in list)
for i, line in enumerate(raw_seq_content, start=1):
    # count the length of each element of list
    length_each_line = len(line.strip())  # using strip because converting each line to list, still including \n
    # show on screen initial length of sequence
    print(f'Length sequence-{i}: {length_each_line}')

# determine how many sequences or lines in our input data
# because out txt content already a list, then use this
print('Sequence after remove adapter:')
total_lines = len(raw_seq_content)
print(f'Total seq in input.txt: {total_lines}')

open("output_no_adapter.txt", "w").close()
# make one new file that doesn't contain adapter
# define output file, that still empty
seq_no_adapter = "output_no_adapter.txt"

# use looping to remove adapter and count length
with open(seq_no_adapter, "a") as output_file:
    # loop as much as total number of sequence aka the number of line
    for i, line in enumerate(raw_seq_content, start=1):
        # remove the adapter
        nth_line_edited = line[14:].strip()    # this is list
        # write seq-no-adapter to the output.txt
        output_file.write(nth_line_edited+"\n")
        # print the length of seq-no-adapter to screen
        nth_line_edited_length = len(nth_line_edited)
        print(f'The length of seq {i} after removing adapter:{nth_line_edited_length}')

# Preview the result to the screen
print("\nThis is our final sequences: Sequence without adapter")
with open(seq_no_adapter) as file:
    content = file.read()  # Read the entire content of the file
    print(content)  # Print the content to the screen