# Procedure for processing data for gain/loss study

# to download:
curl -LO link/to/fastq_1.gz
curl -LO link/to/fastq_2.gz

# unzipping and changing the headers to remove the space:
gzip -cd fastq_1.gz | sed  's_ __' > genus_species_1.fastq
gzip -cd fastq_2.gz | sed  's_ __' > genus_species_2.fastq

# subsampling if necessary:
module purge
module load linuxbrew/colsa

seqtk sample -s 51 genus_species_1.fastq 35000000 > genus_species_sub_1.fastq
seqtk sample -s 51 genus_species_2.fastq 35000000 > genus_species_sub_2.fastq

# example of a script to assemble:
#! /bin/bash
#SBATCH --partition=macmanes,shared
#SBATCH -J species
#SBATCH --output genus_species.log
#SBATCH --mem 500Gb

module purge
module load anaconda/colsa
source activate orp

cd /mnt/lustre/macmaneslab/jlh1023/gainloss_data/porifera

oyster.mk main MEM=450 CPU=24 \
READ1=genus_species_1.fastq \
READ2=genus_species_2.fastq \
RUNOUT=genus_species
