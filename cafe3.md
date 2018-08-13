# Running cafe3

Files needed:
-tree in nexus format (ultrametric)
-Gene Counts file from Orthofinder

First I have to edit the GeneCounts file because mine still contains species that aren't in the tree.
> cut -f 1-47,49-68,72- Orthogroups_4.GeneCount.csv > cor_orthogroups.GeneCount.csv

This gets rid of the duplicates at the end as well as Acropora and eudiplozoon_nipponicum, which I forgot to get rid of earlier. I also changed the hydra label to be lowercase, as it is in the tree.

I put the tree (/mnt/lustre/plachetzki/shared/reciprocator/RECIPROCATOR/rax2/RAxML_bestTree.met_67_test) into figtree and exported it as a nexus tree to be compatible with r8s.

Cannot get r8s to work, so I forced a janky ultrametric tree in R instead. That process is in the file "crappy_ultrametric_tree.R" in the dropbox.

So now the tree file is ult_met67.nex and the data file is orthogroups.GeneCount.tab (I deleted the)
