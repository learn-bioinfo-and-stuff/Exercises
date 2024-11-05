#!/usr/bin/env python3
# Question one: Make some fasta sequences
import os
import subprocess
import shutil

# Aim:
# One. Make fasta files, with header name containing length of sequence, header name is the sama of the files
# Two. Fasta files from input file is being splited into two files; intron and exon. fasta files


# Input
# There is 2 files: local and remote. local data already in txt, without header
local_input = "plain_genomic_seq.txt"
remote_input = "AJ223353.fasta"

# Process
# Process: Fase One
# Since remote data already in fasta and the header name containing space, we need to delete the header and transform into .txt
# Define output .txt
remote_input_fin = f'{remote_input.rstrip(".fasta")}.txt'

# Open the remote input file, get the header and seq part
with open(remote_input) as file:
    remote_input_content = file.readlines()   # readlines function use '\n' as separator and output as list
    print(f'list of remote_input_content:\n{remote_input_content}')
    header=""
    seq_str=""
    for line in remote_input_content:
        if line.startswith(">"):
            header = line
        else:
            seq_str += line.replace("\n","")  # append, and replace the \n. because thats the separator for list function before
    # check the ouput now
    print(f'header:\n{header}')
    print(f'seq_str:\n{seq_str}')

# populate the outputfile or our txt
with open(remote_input_fin,"w") as outputfile:   #make sure we are in write mode, because is still empty
    new_content = f'{seq_str}'
    outputfile.write(new_content)
print(f'This is the remote_input_final as .txt content\n{remote_input_fin}\n{new_content}')

# Process: Fase Two
# Process all .txt files into fasta. only consist DNA seq (ATGC), have a header name that same like the filename and in upper case
# Define the path of the directory containing the .txt files
path = "/home/s2762031/Exercises/Lecture12/"

# Loop through each txt files in the directory
for file in os.listdir(path):
    if file.endswith(".txt"):
        # Get the full path of each file
        file_path = os.path.join(path, file)
        # Define the output fasta
        basename = os.path.basename(file_path.rstrip(".txt"))   #basement function, will automatically take the last part of path as the basename
        outputfile_fasta = f'{basename}.fasta'
        # Edit each .txt into .fasta and removing non ATGC and make the letter capital
        with open(file_path) as file:
            file_content = file.read()
        with open(outputfile_fasta,"w") as outputfile:
            seq_str_DNA_only = file_content.replace("X", "").replace("S", "").replace("K", "").replace("L", ""). upper()
            length_seq_str_DNA_only = len(seq_str_DNA_only)
            header = f'>{outputfile_fasta.rstrip(".fasta")}_length_{length_seq_str_DNA_only}'
            new_content_DNA_only = f'{header}\n{seq_str_DNA_only}\n'
            outputfile.write(new_content_DNA_only)
        print(f'The content of only DNA seq or {outputfile_fasta}\n')
        os.system(f"cat {outputfile_fasta}")

# Process: Fase Three
# Process all .fasta file (which is already uppercase and only ATGC): Split intron and exon, and give length in header too

# Split intron-exon in local_fasta first
# Define target file
local_fasta = f'plain_genomic_seq.fasta'

# Define the output local fasta
outputfile_local_fasta_exon = f'{local_fasta.rstrip(".fasta")}_exon.fasta'
outputfile_local_fasta_intron = f'{local_fasta.rstrip(".fasta")}_intron.fasta'

# Open the local fasta and split exon-intron
with open(local_fasta) as file:
    file_content = file.readlines()  #make it into list, to separate header and seq_content
    header=""
    seq_content=""
    for line in file_content:
        if line.startswith(">"):
            header = line
        else:
            seq_content += line.rstrip("\n")

# local_fasta: write intron only
with open(outputfile_local_fasta_intron,"w") as outputfile:
    # split header and seq_str content
    local_fasta_intron_seq = seq_content[63:90]
    local_fasta_intron_seq_length = len(local_fasta_intron_seq)
    local_fasta_intron_header = f'>{outputfile_local_fasta_intron.rstrip(".fasta")}_length_{local_fasta_intron_seq_length}'
    # define how to write the final intron fasta
    local_fasta_intron_combine = f'{local_fasta_intron_header}\n{local_fasta_intron_seq}'
    # write to output file
    outputfile.write(local_fasta_intron_combine)
    print(f'This is the intron of {local_fasta}\n{local_fasta_intron_combine}')

# local_fasta: write exon only
with open(outputfile_local_fasta_exon,"a") as outputfile:
    # split header and seq_str content
    local_fasta_exon_01 = seq_content[:63]
    local_fasta_exon_02 = seq_content[90:]
    local_fasta_exon = local_fasta_exon_01 + local_fasta_exon_02
    local_fasta_exon_length = len(local_fasta_exon)
    local_fasta_exon_header = f'>{outputfile_local_fasta_exon.rstrip(".fasta")}_length_{local_fasta_exon_length}'
    # define how to write the final exon fasta
    local_fasta_exon_combine = f'{local_fasta_exon_header}\n{local_fasta_exon}'
    # write to output file
    outputfile.write(local_fasta_exon_combine)
    print(f'This is the exon of {local_fasta}\n{local_fasta_exon_combine}')


# Open the remote fasta and split exon-intron
# Define target file
remote_fasta = f'AJ223353.fasta'

# Open the remote fasta and split exon-intron
with open(remote_fasta) as file:
    file_content = file.readlines()  #make it into list, to separate header and seq_content
    header_remote=""
    seq_content_remote=""
    for line in file_content:
        if line.startswith(">"):
            header_remote = line
        else:
            seq_content_remote += line.rstrip("\n")

# Define the output local fasta
outputfile_remote_fasta_exon = f'{basename}_exon.fasta'
outputfile_remote_fasta_intron = f'{basename}_intron.fasta'

# Remote_fasta: write exon only
with open(outputfile_remote_fasta_exon,"a") as outputfile:
    # split header and seq_str content
    remote_fasta_exon_seq = seq_content_remote[28:409]
    remote_fasta_exon_seq_length = len(remote_fasta_exon_seq)
    remote_fasta_exon_header = f'>{outputfile_local_fasta_exon.rstrip(".fasta")}_length_{remote_fasta_exon_seq_length}'
    # define how to write the final exon fasta
    remote_fasta_exon_combine = f'{remote_fasta_exon_header}\n{remote_fasta_exon_seq}\n'
    # write to output file
    outputfile.write(remote_fasta_exon_combine)
    print(f'This is the exon of {remote_fasta}\n{remote_fasta_exon_combine}')

# Remote_fasta: write intron only
with open(outputfile_remote_fasta_intron,"a") as outputfile:
    # split header and seq_str content
    remote_fasta_intron_seq_01 = seq_content_remote[:28]
    remote_fasta_intron_seq_02 = seq_content_remote[409:]
    remote_fasta_intron_seq = remote_fasta_intron_seq_01 + remote_fasta_intron_seq_02
    remote_fasta_intron_seq_length = len(remote_fasta_intron_seq)
    remote_fasta_intron_header = f'>{outputfile_remote_fasta_intron.rstrip(".fasta")}_length_{remote_fasta_intron_seq_length}'
    # define how to write the final intron fasta
    remote_fasta_intron_combine = f'{remote_fasta_intron_header}\n{remote_fasta_intron_seq}'
    # write to output file
    outputfile.write(remote_fasta_intron_combine)
    print(f'This is the intron of {remote_fasta}\n{remote_fasta_intron_combine}')