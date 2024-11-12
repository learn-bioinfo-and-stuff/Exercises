#!/usr/bin/python3
## v1, 12 Nov 2024, written by s2762031
## Script for exercising dataframe using panda.
## We use eukaryotes.txt as input file

## Inputs modules
import os, sys, subprocess
import numpy as np
import pandas as pd


## 1.  Create dataframe from files = reading the files and preview the key info about it.

## 1.A Get the data from NCBI
#subprocess.call('wget -qO eukaryotes.txt "ftp://ftp.ncbi.nlm.nih.gov/genomes/GENOME_REPORTS/eukaryotes.txt" ', shell=True)
#print("Data downloaded successfully!")

## 1.B Import the eukaryotes.txt data into a dataframe. Using read_csv()
df = pd.read_csv('eukaryotes.txt', sep="\t")
#print(df)
# Preview all about our data
# How big is our data?
size_df = df.shape
print(f'The eukaryotes.txt file is now a dataframe: df')
print(f'The size of df:\nnumber of rows:{size_df[0]}\nnumber of columns:{size_df[1]}')
# What are the column headings?
list_header = list(df.columns)
print(f'This is the list header of our data:\n{list_header}')


## 2.   How many Fungal species have genomes bigger than 100MB? What are the names?
## Fungi information is in Group coloumn
filter = df[(df['Group'] == 'Fungi') & (df['Size (Mb)'] > 100)]
filter_expression = "df[(df['Group'] == 'Fungi') & (df['Size (Mb)'] > 100)]"
print(f'The result of {filter_expression}\n')
print(filter)

#filter_2 = df[(df['Group'] == 'Fungi') & (df['Size (Mb)'] > 100)].value_counts()   #value count is showing unique data
#filter_2_expression = "df[(df['Group'] == 'Fungi') & (df['Size (Mb)'] > 100)].value_counts()"
#print(f'The result of {filter_2_expression}\n')
#print(filter_2)

filter_3 = df[(df['Group'] == 'Fungi') & (df['Size (Mb)'] > 100)].shape()
filter_3_expression = "df[(df['Group'] == 'Fungi') & (df['Size (Mb)'] > 100)].shape()"
print(f'The result of {filter_3_expression}\n')
print(filter_3)
