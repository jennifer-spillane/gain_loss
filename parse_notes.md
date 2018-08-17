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

OGs that sponges don't have, but choanos and cnidarians do:
OG0000050
OG0000324
OG0000385
OG0000513
OG0000743
OG0000772
OG0000806

I can go into the original orthofinder file "Orthogroups_4.csv" to find the ids of the seqs that are in this OG, then into the genomes/transcriptomes themselves to find the seqs.

grep "OG0000050" Orthogroups_4.csv > choano_sponge.txt
grep "OG0000324" Orthogroups_4.csv >> choano_sponge.txt
grep "OG0000385" Orthogroups_4.csv >> choano_sponge.txt
grep "OG0000513" Orthogroups_4.csv >> choano_sponge.txt
grep "OG0000743" Orthogroups_4.csv >> choano_sponge.txt
grep "OG0000772" Orthogroups_4.csv >> choano_sponge.txt
grep "OG0000806" Orthogroups_4.csv >> choano_sponge.txt

batch1_orthofinder]$ grep -A 1 "Homo_sapiens_70219" Homo_sapiens.prot.fa

####OG0000050

grep -A 1 "Homo_sapiens_56350" Homo_sapiens.prot.fa
>Homo_sapiens_56350
MLIGKGSLVMEGQKHLNSKKKGLKASFSLSLTFTSRLAPDPSLVIYAIFPSGGVVADKIQ

####OG0000324

grep -A 1 "Homo_sapiens_70219" Homo_sapiens.prot.fa
>Homo_sapiens_70219
MQTKGGQTWARRALLLGILWATAHLPLSGTSLPQRLPRATALGLSQDVAGTTFMAAGSSA

####OG0000385

grep -A 1 "Homo_sapiens_20799" Homo_sapiens.prot.fa
>Homo_sapiens_20799
MSDRPTARRWGKCGPLCTRENIMVAFKGVWTQAFWKAVTAEFLAMLIFVLLSLGSTINWG

####OG0000513

grep -A 1 "Homo_sapiens_73628" Homo_sapiens.prot.fa
>Homo_sapiens_73628
MSRSPLNPSQLRSVGSQDALAPLPPPAPQNPSTHSWDPLCGSLPWGLSCLLALQHVLVMA

####OG0000743

grep -A 1 "Homo_sapiens_41094" Homo_sapiens.prot.fa
>Homo_sapiens_41094
MFFTCGPNEAMVVSGFCRSPPVMVAGGRVFVLPCIQQIQRISLNTLTLNVKSEKVYTRHG

####OG0000772

grep -A 1 "Homo_sapiens_36069" Homo_sapiens.prot.fa
>Homo_sapiens_36069
MPRHHAGGEEGGAAGLWVKSGAAAAAAGGGRLGSGMKDVESGRGRVLLNSAAARGDGLLL

####OG0000806

grep -A 1 "Homo_sapiens_56069" Homo_sapiens.prot.fa
>Homo_sapiens_56069
MTEGARAADEVRVPLGAPPPGPAALVGASPESPGAPGREAERGSELGVSPSESPAAERGA
