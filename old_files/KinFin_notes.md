# KinFin Papers

## Yoshida et al.
- identified orthologues for phylogenetic analysis
- explored patterns of gene family expansion and contraction
- stats about gene families (% species specific, % aa span from singletons)
- identifying synapomorphies
- mapped gene family presence/absence across 2 contrasting phylogenies
- used different inflation parameters in the markov cluster algorithm in OrthoFinder
- made a graphical representation of the orthofinder clustering

# Kinfin explorations

I'm working in the directory /mnt/lustre/macmaneslab/jlh1023/pipeline_dev/sponge_test/sponge_ref/ and playing with
different things kinfin can do

> echo '#IDX,TAXON' > config.txt
> sed 's/: /,/g' SpeciesIDs.txt | \
	cut -f 1 -d"." \
	>> config.txt

Now my config file looks like this:
IDX,TAXON
0,acar
1,aque
2,hsap
3,ltet
4,ppen
5,ptra

This is the command I'm trying now
> kinfin -g ../Orthogroups.txt -c config.txt -s SequenceIDs.txt -p SpeciesIDs.txt

this generates all the normal kinfin output that I got during the first trial.
directories: all, TAXON
files: cluster_counts_by_taxon.txt, cluster_size_distribution.pdf
and obviously more stuff inside the directories.

It seems like I'll need to run interproscan before I run some of these analyses (maybe even orthofinder?), so this is the command I'm using to do that. (in a slurm called inter.slurm)
> interproscan -d inter_out -i ./sponge_ref/\*.fa -appl Pfam        #don't include the backslash, it was just messing with all the formatting.      




# Kinfining on the real dataset - batch1

I made a directory called batch1_kinfin to do these analyses

Orthofinder finished, so now I need these three files to do the kinfin analysis:
- /mnt/lustre/macmaneslab/jlh1023/metazoa_matrix/batch1_orthofinder/Results_May13/Orthogroups.txt
- /mnt/lustre/macmaneslab/jlh1023/metazoa_matrix/batch1_orthofinder/Results_May13/WorkingDirectory/SpeciesIDs.txt
- /mnt/lustre/macmaneslab/jlh1023/metazoa_matrix/batch1_orthofinder/Results_May13/WorkingDirectory/SequenceIDs.txt

### Prepping the kinfin config file

> echo '#IDX,TAXON' > config.txt
> sed 's/: /,/g' /mnt/lustre/macmaneslab/jlh1023/metazoa_matrix/batch1_orthofinder/Results_May13/WorkingDirectory/SpeciesIDs.txt | \
    cut -f 1 -d"." \
    >> config.txt

Top of the config file:
#IDX,TAXON
0,Adineta_vaga
1,Amphimedon_queenslandica
2,Anolis_carolinensis
3,Bombus_impatiens
4,Caenorhabditis_elegans
5,Capitella_teleta
6,Ciona_savignyi
7,Crassostrea_gigas
8,Danaus_plexippus
9,Danio_rerio
10,Daphnia_pulex


Got stalled out on that one (moved on to other analyses) but have now come back and am doing kinfin on the batch 2 version of the dataset.

### Kinfin analysis

I had all the parts to make a config file, but then realized that I didn't name the files in the way that kinfin prefers, so I changed the names in the SpeciesIDs file before I made the config file so that it would fit better into their formatting. *hopefully this doesn't mess anything up* In the future, I'll rename the files before they go into the orthofinder analysis so that they conform.

I prepped the config file the same way as before, using this file:
/mnt/lustre/macmaneslab/jlh1023/metazoa_matrix/Results_May23/WorkingDirectory/alt_SpeciesIDs.txt

and it is here on premise:
/mnt/lustre/macmaneslab/jlh1023/metazoa_matrix/kinfin/confix.txt

I also made one using the normal file, which I like a lot better, since it still has the intact species name instead of the made-up abbreviation. That one is config2.txt in the same directory. I'm going to try to use it in all subsequent analyses.

The command I used to run the basic kinfin analysis:
>kinfin -g ../Results_May23/Orthogroups.txt -c config2.txt -s ../Results_May23/WorkingDirectory/SequenceIDs.txt

### Analysis based on taxonomy

I can add things to the config file that will give kinfin more info, so now the top of my config2.txt file looks like this:

\#IDX,TAXON,OUT,TAXID
0,Adineta_vaga,0,Rotifera
1,Amphimedon_queenslandica,0,Porifera
2,Anolis_carolinensis,0,Chordata
3,Bombus_impatiens,0,Arthropoda
4,Caenorhabditis_elegans,0,Nematoda
5,Capitella_teleta,0,Annelida
6,Capsaspora_owczarzaki,1,Filasterea
7,Ciona_savignyi,0,Chordata
8,Crassostrea_gigas,0,Mollusca
9,Danaus_plexippus,0,Arthropoda

This one got hung up on Brachiopoda, and I'm not sure why, so I switched back to the unfancy one for now, which still yields great info.

### Playing with results.

I explored some of the results that kinfin spit out, and it seems like the stuff in the TAXON directory is the most interesting. One file, the TAXON.cluster_summary.txt is great. I used the following command to extract the parts that I needed from it:
> cut -f 1,9-89 TAXON.cluster_summary.txt > just_taxa.txt

I wrote a program that takes the edited table and makes a presence/absence matrix from it. The orthogroups that are there are represented by 1s and the ones that are not are represented by 0s.
The file is matrix_maker.py

I'm also playing with the 1 to 1 orthologues that kinfin can extract.
I altered the number that would come out with the x flag:
> kinfin -g ../Results_May23/Orthogroups.txt \
-c config3.txt \
-s ../Results_May23/WorkingDirectory/SequenceIDs.txt \
-o onetoone \
-x 0.60

Then I can extract the actual orthologues using this script:
> /mnt/lustre/software/linuxbrew/colsa/Cellar/kinfin/1.0.3/libexec/scripts/get_protein_ids_from_cluster.py \
-g /mnt/lustre/macmaneslab/jlh1023/metazoa_matrix/Results_May23/Orthogroups.txt \
--protein_ids /mnt/lustre/macmaneslab/jlh1023/metazoa_matrix/Results_May23/WorkingDirectory/SequenceIDs.txt \
--cluster_ids /mnt/lustre/macmaneslab/jlh1023/metazoa_matrix/kinfin/onetoone.kinfin_results/all/all.all.cluster_1to1s.txt



-fg orthogroup_results_dir, --from-groups orthogroup_results_dir
    Infer gene trees and orthologues starting from OrthoFinder orthogroups in orthogroup_results_dir/.






Also using orthomatic in Reciprocator to make the tree things I need.
> /mnt/lustre/macmaneslab/jlh1023/metazoa_matrix/RECIPROCATOR/orthomatic.sh \
-T 24 -i OGs -r Nematostella -e 1e-20 \
-t /mnt/lustre/macmaneslab/jlh1023/metazoa_matrix/RECIPROCATOR/taxa_blastdatabase \
-g /mnt/lustre/macmaneslab/jlh1023/metazoa_matrix/RECIPROCATOR/ref_genome_blastdatabase



### using the script I wrote to pull out the one-to-one orthologs.

/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/pull_seqs.py -c onetoone.kinfin_results/all/all.all.cluster_1to1s.txt -r /mnt/lustre/macmaneslab/jlh1023/metazoa_matrix/Results_May23/Orthogroups.csv -p /mnt/lustre/macmaneslab/jlh1023/metazoa_matrix/batch2_all.fa -o pull_seqs_out.fa


### script Dave used to run IQtree on the data (without the problematic lophotrocozoans, and with hydra and acropora genomes)

> iqtree -s met_67.phylip -m "GTR20+C20" -alrt 1000 -nt 24
