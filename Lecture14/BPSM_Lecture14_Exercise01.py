#!/usr/bin/env python3
# Exercise 14. Drossopila data

# Aim
# Aim 1: print out the gene names for all genes drosopilla melanogaster or simulans
# Aim 2: print out all genes names for all genes, that 90-110 bases long
# Aim 3: print out all genes names for all genes, that AT content < 0.5 and expression >200
# Aim 4: print out all genes names for all genes, whose names begins with "K" or "H" except from d. melanogaster
# Aim 5: for each genes names, print out the messeages: names, AT content (high (>0.65), low(<0.45), medium(0.45-0.65))

# Input
# Load and read data.csv
input_file = "data.csv"

# Set the empty output
output_file = "data.tsv"

# Process
# Step 1: Preprocess: Make into tabular and set header to it
with open(input_file, "r") as csv_file, open(output_file, "w") as tsv_file:
    # write header to output files
    header = "species\tseq\tgene\texpression"
    tsv_file.write(header + "\n")
    # edit the content of input_files
    csv_file_content = csv_file.readlines()
    for line in csv_file_content:
        columns = line.strip().split(",")
        # Join all columns
        tabular_line = "\t".join(columns)
        # populate our output
        tsv_file.write(tabular_line + "\n")
print(f"Finished transforming csv into tsv")

# preview tsv_files
with open(output_file) as file:
    file_content = file.read()
    print(f'The content of {output_file}:\n{file_content}')

# Step 2: set specific condition to get our data
# Open the tsv files
with open(output_file, "r") as tsv_file:
    # Read the content
    output_file_content = tsv_file.readlines()  # ini outputnya 1 buah list besar, yang @itemnya adalah data per baris.
    print(output_file_content)
    # Get the header
    header = output_file_content[0].strip().split("\t")             # header value in list. ambil data dari baris 0 atau pertama
    # Get position of species and gene data (to filter it)          # to access the data, need position in list
    species_index = header.index("species")
    gene_index = header.index("gene")
    seq_index = header.index("seq")
    expression_index = header.index("expression")
    # Make an empty list to store our output process
    gene_data = []                      # for output aim 1
    gene_data_specific_length = []      # for output aim 2
    gene_data_3 = []                    # for output aim 3
    gene_data_4 = []                    # for output aim 4
    # Populate empty list
    for item in output_file_content[1:]:     #iterasi data, skip header.
        columns = item.strip().split("\t")   # pisahkan data didalam satu item, ini kita indexing.. get data from list kan harus ada angka posisinya
        species = columns[species_index]     # akses tiap data berdasarkan posisi di list itu, makanya perlu index
        gene = columns[gene_index]
        gene_K = gene.startswith("k")
        gene_H = gene.startswith("h")
        seq = columns[seq_index]
        expression = int(columns[expression_index])
        seq_length = len(seq)
        sum_AT = seq.count("a") + seq.count("t")
        AT_content = sum_AT/seq_length
        # Check before if condition.
        print(f'Species {species}, Gene: {gene}, Length: {seq_length}, AT content: {AT_content}, expression: {expression}')
        # Aim 1: print out the gene names for all genes drosopilla melanogaster or simulans
        if species == "Drosophila melanogaster" or species == "Drosophila simulans":
            selected_genes_1 = gene_data.append(gene)
        # Aim 2: Get all gene names for seq length between 90 and 110 bases
        if seq_length > 90 and seq_length < 110:
            selected_genes_2 = gene_data_specific_length.append(gene)
        # Aim 3: Get all gene names for AT <0.5 and expression > 200
        if AT_content < 0.5 and expression > 200:
            selected_genes_3 = gene_data_3.append(gene)
        # Aim 4: Get all gene names start from K or H and not from d.melano
        if species != "Drosophila melanogaster" and (gene_K is True or gene_H is True):
            selected_genes_4 = gene_data_4.append(gene)
        # Aim 5: labeling each gene from expression level
        if AT_content > 0.65:
            print(f'The AT content of the gene: {gene} is High: {AT_content}')
        elif AT_content < 0.65 and AT_content > 0.45:
            print(f'The AT content of the gene: {gene} is Medium: {AT_content}')
        else:
            print(f'The AT content of the gene: {gene} is Low: {AT_content}')

# Output
# view output 1
print(f'Gene names from Drosophila melanogaster or Drosophila simulans:')
for item in gene_data:
    print(item)
# view output 2
print(f'Gene names for seq length between 90 and 110:')
for item in gene_data_specific_length:
    print(item)
# view output 3
print(f'Get all gene names for AT <0.5 and expression > 200')
for item in gene_data_3:
    print(item)
# view output 4
print(f'Get all gene names start from K or H and not from d.melano')
for item in gene_data_4:
    print(item)
