#!/usr/bin/env python3

# Part One: Amino acid percentage  ##################################################
# define a new function that will get the percentage of protein
# we decide to give the function a name: get_aa_percent
# the function needs 2 arguments: protein_seq and amino_acid_residu
# the only thing that comes out of a function is what we tell it to return

# Our aa_percent function
def get_aa_percent (protein_seq, amino_acid_residu):
    length_protein = len(protein_seq)
    aa_count = protein_seq.count(amino_acid_residu)
    percentage = aa_count*100/length_protein
    return percentage

# test our funtion
test = get_aa_percent("MSRSLLLRFLLFLLLLPPLP","M")
print(test)

# test again using assert
try:
    assert round(get_aa_percent("MSRSLLLRFLLFLLLLPPLP", "M")) == round(5)
    print("Result assert 1: success")
except AssertionError:
    print("Result assert 1: failed")


# Part Two: Amino acid percentage  ##################################################
# define a new func that needs 2 argument:
# one: protein seq
# and two: amino acid residu (as an object and list)

# define a new func that will get:
# one: count of percentage of custom amino acid residu (in the list), if the aa is a list
# two: percentage of hydrophobic aa residu (A,I,L,M,F,W,Y,V), if aa is a single object

# we decide to give the function a name: get_aa_percent_2
# the only thing that comes out of a function is what we tell it to return

# Our get_aa_percent_2 function
def get_aa_percent_2 (protein_seq, aa_residu):
    # length protein_seq
    length_protein = len(protein_seq)
    # Define the results variables:
    result_percentage_custom_aa = []
    result_percentage_hydro = []
    # condition one for str input
    if type(aa_residu) == str:
        hydro_aminos = ["A", "I", "L", "M", "F", "W", "Y", "V"]
        for hydro_amino in hydro_aminos:
            count_hydro_amino = protein_seq.count(hydro_amino)
            percent_hydro_amino = (count_hydro_amino * 100) / length_protein
            # use append to save result of each iteration as an item in our result list
            result_percentage_hydro.append(f'The percentage of hydro amino "{hydro_amino}": {percent_hydro_amino}')
    elif type(aa_residu) == list:
        for aa_residu_item in aa_residu:
            count_custom_aa = protein_seq.count(aa_residu_item)
            percent_custom_aa = (count_custom_aa * 100) / length_protein
            result_percentage_custom_aa.append(f'The percentage of custom aa "{aa_residu_item}":{percent_custom_aa}')
    return result_percentage_custom_aa, result_percentage_hydro

# test funtion_2_if argument aa_residu is single object
print("Test using single object")
test_2 = get_aa_percent_2("MSRSLLLRFLLFLLLLPPLP","M")
print(test_2)

# test funtion_2_if argument aa_residu is list
print("Test using a List")
list_aa = ["L","P"]
test_2_A = get_aa_percent_2("MSRSLLLRFLLFLLLLPPLP",list_aa)
print(test_2_A)

# test again using assert
try:
    test_result = get_aa_percent_2("MSRSLLLRFLLFLLLLPPLP", "M")
    # need to specify this, because we have two output from this function
    assert round(test_result[1]) == round(5)
    print("Result assert 1: success")
except AssertionError:
    print("Result assert 1: failed")
