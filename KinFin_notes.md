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
> interproscan -d inter_out -i ./sponge_ref/*.fa -appl Pfam
