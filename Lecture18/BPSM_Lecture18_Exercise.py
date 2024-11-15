#!/usr/bin/python3
## v1, 15 Nov 2024, written by s2762031
## Script for exercising regex module in Phyton.

## Inputs modules
import re

##  1. Accession numbers
accession_numbers = ["xkn59438", "yhdck2", "eihd39d9", "chdsye847", "hedle3455", "xjhd53e", "45da", "de37dp"]
print(f'List accession numbers: {accession_numbers}\n')

## empty list to store result
num_5_list = []
name_DorE = []
name_dANDe = []
name_d_any1_e = []
name_dANDe_2 = []
name_start_xy = []
name_start_xy_end_e = []
name_three_num = []
name_three_diff_num = []
name_three_num_in_a_row = []
name_ending_filter = []

## List of filter
for accession_number in accession_numbers:
   # 1.A print only "contain number 5"
   if re.search(r'5', accession_number):
      num_5_list.append(accession_number)
   # 1.B contain the letter d or e
   if re.search(r'[de]', accession_number):
      name_DorE.append(accession_number)
   # 1.C contain the letter d AND e in that order
   if re.search(r'(de)', accession_number):
      name_dANDe.append(accession_number)
   # 1.D Contain the letters d and e in that order with a single letter between them
   if re.search(r'(d.e)', accession_number):
      name_d_any1_e.append(accession_number)
   # 1.E Contain the letter d and e in any order
   if re.search(r'd', accession_number) and re.search(r'e',accession_number):
      name_dANDe_2.append(accession_number)
   # 1.F Start with x or y
   if re.search(r'^[xy]',accession_number):
      name_start_xy.append(accession_number)
   # 1.G Start with x or y and end with e
   if re.search(r'^[xy]',accession_number) and re.search(r'e$',accession_number):
      name_start_xy_end_e.append(accession_number)
   # 1.H Contain only  3 numbers in any order
   if len(re.findall(r'\d',accession_number)) == 3:
      name_three_num.append(accession_number)
   # 1.I Contains 3 different numbers in the accession
   if len(set(re.findall(r'\d',accession_number))) == 3:
      name_three_diff_num.append(accession_number)
   # 1.J Contains 3 or more numbers in a row
   if re.findall(r'\d{3,}',accession_number):
      name_three_num_in_a_row.append(accession_number)
   # 1.K end with d followed by either a, r or p
   if re.search(r'de$|da$|dr$|dp$',accession_number):
      name_ending_filter.append(accession_number)


#print all the results
print(f'Contain number 5: {num_5_list}')
print(f'Contain the letter d or E: {name_DorE}')
print(f'Contain the letter d and E in that order: {name_dANDe}')
print(f'Contain the letters d and e in that order with a single letter between them: {name_d_any1_e}')
print(f'Contain the letter d and e in any order: {name_dANDe_2}')
print(f'Start with x or y: {name_start_xy}')
print(f'Start with x or y and end with e: {name_start_xy_end_e}')
print(f'Contain only 3 numbers in any order: {name_three_num}')
print(f'Contain 3 different numbers in any order: {name_three_diff_num}')
print(f'Contain three or more numbers in a row: {name_three_num_in_a_row}')
print(f'end with d followed by either a, r or p:{name_ending_filter}')
