#!/bin/bash

#for tree_file in /home/adhock/Projects/Tree_rooting_analysis/Data/OMA_orthologs/5204_4890/*.True.newick; do
for tree_file in /home/adhock/Projects/Tree_rooting_analysis/Data/OMA_orthologs/5204_4890_33511_33317/*.True.newick; do
#for tree_file in /home/adhock/Projects/Tree_rooting_analysis/Data/OMA_orthologs/5204_4890_33511_33317_33090/*.True.newick; do
	prot_name=$(basename "$tree_file" .True.newick)
	echo $prot_name
	/home/adhock/Workspace/mad/mad $tree_file
    wait
done
