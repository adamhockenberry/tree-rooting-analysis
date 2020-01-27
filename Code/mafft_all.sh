#!/bin/bash

#for fasta_file in /home/adhock/Projects/Tree_rooting_analysis_NEWDATA/Data/OMA_orthologs/5204_4890/*.fasta; do
#	prot_name=$(basename "$fasta_file" .fasta)
#	echo $prot_name
#	afa_file="/home/adhock/Projects/Tree_rooting_analysis_NEWDATA/Data/OMA_orthologs/5204_4890/${prot_name}.afa"
#	mafft --thread 4 --localpair --quiet --maxiterate 1000 $fasta_file > $afa_file
#	wait
#done
#
#
#
#for fasta_file in /home/adhock/Projects/Tree_rooting_analysis_NEWDATA/Data/OMA_orthologs/5204_4890_33511_33317/*.fasta; do
#	prot_name=$(basename "$fasta_file" .fasta)
#	echo $prot_name
#	afa_file="/home/adhock/Projects/Tree_rooting_analysis_NEWDATA/Data/OMA_orthologs/5204_4890_33511_33317/${prot_name}.afa"
#	mafft --thread 8 --localpair --quiet --maxiterate 1000 $fasta_file > $afa_file
#	wait
#done
#
#
#
#for fasta_file in /home/adhock/Projects/Tree_rooting_analysis_NEWDATA/Data/OMA_orthologs/5204_4890_33511_33317_33090/*.fasta; do
#	prot_name=$(basename "$fasta_file" .fasta)
#	echo $prot_name
#	afa_file="/home/adhock/Projects/Tree_rooting_analysis_NEWDATA/Data/OMA_orthologs/5204_4890_33511_33317_33090/${prot_name}.afa"
#	mafft --thread 8 --localpair --quiet --maxiterate 1000 $fasta_file > $afa_file
#	wait
#done
