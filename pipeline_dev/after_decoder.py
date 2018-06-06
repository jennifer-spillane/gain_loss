#! /usr/bin/env python3

import shutil
import os
import subprocess
import argparse

#function that 
def after_decoder():
    #removing directories that will be created later in the function
    shutil.rmtree("decode_out", ignore_errors = True)
    shutil.rmtree("for_orthofinder", ignore_errors = True)
    #storing the original directory name, then making one to hold the output of TransDecoder
    orig_dir = os.getcwd()
    os.mkdir("decode_out")
    os.mkdir("for_orthofinder")
    os.chdir("decode_out")

    #looking inside the larger directory to all the phylum directories to find the assemblies
    species_db = {}
    for directory in os.scandir("{0}".format(args.transcripts)):
        for fasta in os.scandir("{0}/assemblies".format(args.transcripts)):
            if fasta.name.endswith(".orthomerged.fasta"):
                #using TransDecoder to extract the long open reading frames and predict the coding regions
                subprocess.run("TransDecoder.LongOrfs -t {0}".format(fasta.path), shell = True)
                subprocess.run("TransDecoder.Predict -t {0}".format(fasta.path), shell = True)

                #pulling the files orthofinder will need into a different directory and renaming them
                os.rename("{0}/decode_out/{1}.transdecoder.pep".format(orig_dir, fasta.name), "{0}/for_orthofinder/{1}".format(orig_dir, fasta.name))

    #changing directories back to where we started
    os.chdir(orig_dir)

#ends with a directory called for_orthofinder that contains all the .pep files renamed to have their original names.

#arguments for the function
parser = argparse.ArgumentParser(description = "Arguments for TransDecoder")
parser.add_argument("transcripts", help = "path to a directory containing the directories containing the transcriptomic datasets")
args = parser.parse_args()

after_decoder()
