# Exercise 1: Interrogating the user
# def interrogate_user():
#     # Questions to ask the user
#     questions = {
#         "name": "What's your name?",
#         "age": "How old are you?",
#         "favourite_colour": "What is your favourite colour?",
#         "likes_python": "Do you like Python? (yes or no)",
#         "world_flat": "The world is flat: True or False?"
#     }
#
#     # Dictionary to store the user's answers
#     answers = {}
#
#     # Asking each question and storing the answer
#     for key, question in questions.items():
#         answers[key] = input(question + " ")
#
#     # Making comments based on the answers
#     print("\n--- Let's see what we have here... ---")
#
#     # Comment on the user's name
#     print(f"Ah, {answers['name']}, that's a great name!")
#
#     # Comment on age
#     try:
#         age = int(answers["age"])
#         if age < 18:
#             print("You're quite young! Enjoy learning Python.")
#         elif age < 60:
#             print("Good age to get comfortable with coding.")
#         else:
#             print("Never too late to enjoy Python!")
#     except ValueError:
#         print("Couldn't quite catch your age there!")
#
#     # Comment on favourite colour
#     print(f"{answers['favourite_colour'].capitalize()} is a wonderful choice!")
#
#     # Comment on liking Python
#     if answers["likes_python"].lower() == "yes":
#         print("Glad you like Python! It's a powerful language.")
#     else:
#         print("Oh no, maybe Python will grow on you!")
#
#     # Comment on flat world belief
#     if answers["world_flat"].strip().lower() == "true":
#         print("Hmm, you might want to check with a scientist on that one!")
#     else:
#         print("Good answer. The Earth appreciates it!")
#
#
# # Run the interrogation
# interrogate_user()

# Exercise 2: DNA Translation  ################################################################
# Task Breakdown & Goals
# (done)Aim 2.1: Translate DNA sequence to protein:
# Use the gencode dictionary to translate the DNA sequence into amino acids.
# (done)Aim 2.2: Handle undetermined bases (like N):
# Figure out what should happen if an unknown base appears in the sequence.
# Aim 2.3: Translate in all three forward frames:
# Perform translation starting at positions 1, 2, and 3 of the sequence.
# Aim 2.4: Translate in all three reverse frames:
# Translate in reverse by generating the reverse complement and starting at positions 1, 2, and 3 of this reversed sequence.

#################################################################################################
# Aim 2.1: Translate DNA sequence to protein:
# Use the gencode dictionary to translate the DNA sequence into amino acids.

# A dict of list codon
gencode = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

# 2.1 Pseudo codes: (Translate DNA sequence to protein)
# Input: A DNA sequence (string)
# Process:
# Iterate over the sequence in codons (groups of three nucleotides).
# Look up each codon in gencode and translate it to the corresponding amino acid.
# Handle cases where a codon contains an unknown base (N) by adding an X (or some other placeholder) to the protein sequence.
# Output: Protein sequence (string)

# 2.1 Input:
# ask the user to provide sequences
# make a function, that have 1 arg: sequence, and return the confirmation messages
# example: ATGTTCGGT
def get_dna_sequences_user ():
    dict_questions = {
        "name_seq" : "What is the name of your sequence?",
        "dna_seq": "Please input your DNA here"
    }
    # Dictionary to store the user's answers
    dict_answers = {}
    item_dict_questions = dict_questions.items()
    print(item_dict_questions)

    # Asking each question and storing the answer
    for key, question in item_dict_questions:
        dict_answers[key] = input(question + " ")

    # Asking the length of seq_user
    length_DNA_input = len(dict_answers["dna_seq"])

    # Display results
    print("\n--- Let's see what we have here... ---")
    # Comment on the user's name
    result_input_user = print(f'This is your dna_input:\n{dict_answers["dna_seq"]}\nLength of your dna:\n{length_DNA_input} bases')
    return dict_answers, length_DNA_input

# 2.1 Process:
# Iterate over the sequence in codons (groups of three nucleotides).
# In this part, translation to protein, only happens in 1 ORF

# 2.1.1 Get the sequence content from the previous function
# Call the first function and get the results
# this is to automated the input of 2nd function
dict_answers, length_DNA_input = get_dna_sequences_user()
input_dna_seq = dict_answers["dna_seq"]
input_length_DNA = length_DNA_input

# 2.1.2 Make 2nd function. def function to translate into codon
def translate_dna_to_protein (input_dna_seq,input_length_DNA):
    # Initialize empty protein_sequence
    protein_seq = ""
    # Using sliding function. Set parameter of sliding, each of 3 bases
    k_mer_size = 3
    length_dna_seq = length_DNA_input
    for i in range(0,length_dna_seq,k_mer_size):
        codon = input_dna_seq[i:i+k_mer_size]
        if codon in gencode:     # this is because the key in gencode is the three dna seq
            protein_seq += gencode[codon]
        else:
            protein_seq += "X"
            print(f'There is an ambigous amino acid in your sequence')
    result_translate_to_protein = print(f'This is the translated protein of {input_dna_seq}:\n{protein_seq}')
    return protein_seq

# Call the second function. Directly type the argument as the result from the 1st function
protein_seq = translate_dna_to_protein(input_dna_seq,input_length_DNA)
