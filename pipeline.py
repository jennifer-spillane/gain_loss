#! /usr/bin/env python3

#Script assumes the user has two directories, one containing transcriptome datasets, and one containing proteome datasets.
#Also assumes that the user has downloaded the appropriate busco database and decompressed it.

import shutil
import os
import re
import subprocess
import argparse

#function to store the names of the species, run all files in a given directory through TransDecoder,
#and then organize the result files for analysis by busco
def decoder():
    #removing directories that will be created later in the function
    shutil.rmtree("decode_out")
    shutil.rmtree("for_busco")
    #storing the original directory name, then making one to hold the output of TransDecoder
    orig_dir = os.getcwd()
    os.mkdir("decode_out")
    os.mkdir("for_busco")
    os.chdir("decode_out")

    #storing the accession numbers and species names in a dictionary
    species_db = {}
    for entry in os.scandir("{0}".format(args.transcripts)):
        try:
            with open("{0}".format(entry.path)) as fasta_file:
                first_line = fasta_file.readline()
                #isolate species name without the rest of the header
                species = re.search("TSA:.([A-Z][a-z]+.[a-z]+)", first_line)
                species_name = species.group(1)
                species_name = species_name.replace(" ", "_")
                #add these to the dictionary
                species_db[entry.name] = species_name
                print(species_db)
        except IOError:
            print("Problem reading file")

        #using TransDecoder to extract the long open reading frames and predict the coding regions
        subprocess.run("TransDecoder.LongOrfs -t {0}".format(entry.path), shell = True)
        subprocess.run("TransDecoder.Predict -t {0}".format(entry.path), shell = True)

        #pulling the files busco will need into a different directory and renaming them
        os.rename("{0}/decode_out/{1}.transdecoder.pep".format(orig_dir, entry.name), "{0}/for_busco/{1}.fasta".format(orig_dir, species_db[entry.name]))

    #changing directories back to where we started
    os.chdir(orig_dir)

#ends with a directory called busco_out that contains all the .pep files renames to be .fasta and to have their species names


#function to run the protein sets through BUSCO
def busco():
    shutil.rmtree("busco_out")
    orig_dir = os.getcwd()
    os.mkdir("busco_out")
    os.chdir("busco_out")
    for entry in os.scandir("/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/for_busco"):
        subprocess.run("busco -i {0} -o {1}_qual -l {2}/metazoa_odb9 -m prot".format(entry.path, entry.name, orig_dir), shell = True)
        try:
            with open("run_{0}_qual/short_summary_{0}_qual_out.txt".format(entry.path)) as qual_file:
                score = ""
                for line in qual_file:
                    line = line.strip()
                    if line[0] == "C":
                        score += line[2:6]
                print(score)
        except IOError:
            print("Issue reading file")

    #changing directories back to where we started
    os.chdir(orig_dir)





#function to run orthofinder
def orthofinder():
    trees = ("orthofinder.py -f *_dir", shell = True, stdout = subprocess.PIPE)
    return trees.stdout.decode('ascii')


predicted_prots = []
for fasta in os.scandir("matrix/transcriptome_assemblies"):
    species_prots = decoder(fasta)
    predicted_prots.append(species_prots)


parser = argparse.ArgumentParser(description = "Arguments for the final project pipeline")
parser.add_argument("transcripts", help = "path to a directory containing the transcriptomic datasets")
parser.add_argument("threshold", help = "minimum acceptable BUSCO score to continue to OrthoFinder")
args = parser.parse_args()




import csv

try:
    with open("/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/prots/peps/Results_Dec03/Orthogroups.csv", "r", newline = "") as handle:
        reader = csv.reader(handle, delimiter = "\t")
        for row in reader:
            row = row.split("\t")
