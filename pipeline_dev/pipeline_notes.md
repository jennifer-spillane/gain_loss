# Input data

Actual data are protein datasets that have already been translated using TransDecoder.
All have .pep names but differ from there.

Code that Dave gave me to convert headers into downstream-appropriate format:

This line changes each fasta header so that it is just ">count" eg >1, >2, >3, etc.
> awk '/^>/{print ">" ++i; next}{print}' < ./fastafile1.fa > genus_species.fa

This line replaces the greater than symbol with the string I provide.
It should be the genus and species separated by an underscore.
> perl -p -i -e 's/>/>genus_species|/g' genus_species.fa

I'll need to write out both of these lines for each dataset we have.
Example:
> awk '/^>/{print ">" ++i; next}{print}' < ./transdecoded_aas//Hormathia_digitata_pep.fa > Hormathia_digitata.fa
> perl -p -i -e 's/>/>Hormathia_digitata|/g' Hormathia_digitata.fa

It would be great to automate this step, but all the formats of the names are currently different.
Matt says he still knows a way to do it, so stay tuned for that update.



# Assumptions of and notes for the scripts

## quality.py

### Assumptions

- it is given an absolute path to a directory containing protein fastas
- it is being run in a directory where there is also a busco file called "config.ini"
- it is being run in a directory where there is a busco database file

### Notes

Right now, the script just uses a threshold that is hard-coded into the program.
If I need to, it would be easy to change this to be user-input, which would make it more flexible.

## ortho.py

### Assumptions

- it is given an absolute path to a directory (probably "above_thresh") that contains protein fasta files that fell above the threshold

### Notes

BLAST is the step that takes forever. There are pretty much two options to make it go faster:
1. run BLAST the way I did it in December (see sponge_sec/initial_blasting)
2. use DIAMOND instead. (with "-S diamond", or "-S diamond_more_sensitive")

There are lots of other options if I want OrthoFinder to use different programs for different parts of the analysis - talk to Matt and Dave about which ones might be best.


# Actually running through the different parts of the workflow

### ORP
### filter_transrate.py
### filter_cdhit.py
### move files to batchx_decoder <- this is a weird one - address.
### transdecoder_batchx.py
### changing headers of fasta files
### orthofinder
### interproscan
### kinfin 

## Example of downloading:
> scp jlh1023@premise.sr.unh.edu:/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/sponge_test/test_data/Results_Feb06/WorkingDirectory/kinfin_results/cluster_size_distribution.pdf ~/Desktop/
