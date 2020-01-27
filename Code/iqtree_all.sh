#!/bin/bash

for afa_file in /home/adhock/Projects/Tree_rooting_analysis_NEWDATA/Data/OMA_orthologs/5204_4890_33511_33317_33090/*.afa; do
	prot_name=$(basename "$afa_file" .afa)
	echo $prot_name
	iqtree -s $afa_file -m LG+I+R8+F -nt 8 -redo -quiet
	wait
done
