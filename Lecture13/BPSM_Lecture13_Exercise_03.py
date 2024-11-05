#!/usr/bin/env python3
# Question number 3: Sliding windows

# Input
input_file = "AJ223353_exon.fasta"

# Prosess
# Step 1: Open and read files
with open(input_file) as file:
    input_file_content = file.readlines()
    header =""
    seq =""
    for item in input_file_content:
        item_data = item.strip()
        if item_data.startswith(">"):
            header = item_data
        else:
            seq += item_data.replace("\n","")

# Define the window ize and offset
window_size = 30
offset = 3

# Initialize a list to hold all segments
segments = []

# Generate segment with sliding wndow
for start in range(0,len(seq) - window_size + 1, offset):
    segment =seq[start:start +window_size]
    segments.append(segment)

    # count gc in each segment
    gc_count =segment.count("G") + segment.count("C")
    gc_content_percentage = (gc_count /window_size)

    # print the segment and its content
    print(f'Segment: {segment}, GC Content: {gc_content_percentage}')

# write all segment to separate files
for i, segment in enumerate(segments):
    segment_length = len(segment)
    header = f'>segment_{i+1}_length_{segment_length}'

    with open(f'segment_{i+1}.fasta','w') as output_file:
        output_file.write(f'{header}\n{segment}\n')

# write all segments to a single fasta file
with open('all_segments.fasta','w') as all_output_file:
    for i,segment in enumerate(segments):
        segment_length =len(segment)
        header =f'>segment_{i+1}_length{segment_length}'
        all_output_file.write(f'{header}\n{segment}\n')