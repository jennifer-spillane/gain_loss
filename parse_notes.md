#Notes on analyzing the presence/absence spreadsheet from kinfin and my presabs script.

I can run the program "dollo_model.py" on the tree from RAxML, and the spreadsheet with the 1s and 0s.

head -n 1 ten_k_pres_abs.csv > sec_random_pres_abs.csv
grep -v "#cluster_id" ten_k_pres_abs.csv | shuf -n 1000 >> sec_random_pres_abs.csv



OGs that sponges don't have, but ctenophores and cnidarians do:
OG0000403
OG0000414
OG0000743
OG0000856
OG0000862

I can go into the original orthofinder file "Orthogroups_4.csv" to find the ids of the seqs that are in this
