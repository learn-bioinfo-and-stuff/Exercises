#!/usr/bin/bash
inputfile="$PWD/blastoutput2.out"
echo -e ${inputfile}
#Initial variable value at start
goodlines=$(grep -v "#" ${inputfile} | wc -l | cut -d ' ' -f1)
unset IFS
unset dataline
shortHSP=0;
hspcounter=0;
echo -e "We have ${goodlines} data lines for processing...\n" 
