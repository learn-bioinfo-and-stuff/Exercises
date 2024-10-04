#!/bin/bash

# A. set path to fastqc executable
fastqc_path="/usr/bin/fastqc"

# B. set path to the output directory for fastqc
fastqc_output="/home/s2762031/Exercises/Myfirstpipeline/output_fastqc"

# C. set path to seq.files
fastqc_input="/localdisk/data/BPSM/MyFirstPipeline/fastq"

# C.1 get the name of pair sequence of each sample from name list Tco2.fq.files
name_list="/localdisk/data/BPSM/MyFirstPipeline/fastq/Tco2.fqfiles"
generate_name=$(grep -v "SampleName" ${name_list}| awk 'BEGIN {FS="\t";}{print$1}')
echo "$generate_name"

# C.2 get the name of pair sequence of each sample from name list Tco2.fq.files and run in fastqc
name_list="/localdisk/data/BPSM/MyFirstPipeline/fastq/Tco2.fqfiles"
generate_name=$(grep -v "SampleName" ${name_list}| awk 'BEGIN {FS="\t";}{print$1}')
echo "$generate_name"

for name in ${generate_name};do
        forward_fq=$(grep -v "SampleName" "${name_list}" | awk -v sample="$name" 'BEGIN{FS="\t";}{if($1==sample){print$6}}')
        path_forward="${fastqc_input}/${forward_fq}"
	reverse_fq=$(grep -v "SampleName" "${name_list}" | awk -v sample="$name" 'BEGIN{FS="\t";}{if($1==sample){print$7}}')
	path_reverse="${fastqc_input}/${reverse_fq}"
	echo "Forward output path: $path_forward"
	echo "reverse output path: $path_reverse"
	#run fastqc
	${fastqc_path} -t 2 ${path_forward} ${path_reverse} --outdir=${fastqc_output}
	#print status running
	echo "fastqc analysis for ${name} is completed"
done 
