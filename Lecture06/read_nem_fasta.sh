#!/bin/bash

cat "/home/s2762031/Exercises/Lecture06/nem.fasta" | awk '{
if(substr($1,1,1)==">")     
 {
print "this is a header line: " $0;
hline=FNR ; # FNR is file number record (i.e. which line of the file)
 }
# Identify the first line of the actual sequence
# ...and then the first character of that line

if(FNR==hline+1)
 {
print "First line is:" $0;
first_seq_character=substr($0,1,1)
print "First character is: " first_seq_character
print first_seq_character > "first_seq_character.txt" 
 }
}'
