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


### Kinfin analysis
