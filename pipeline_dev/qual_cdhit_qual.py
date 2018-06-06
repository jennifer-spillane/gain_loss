#! /usr/bin/env python3

#A program to run datasets through busco, then filter them with cdhit,
#and then run them through busco again

import argparse
import subprocess
import os

def qual_cdhit_qual():
    #recording the original directory and changing to one where the busco files will go
    orig_dir = os.getcwd()
    os.chdir("{0}".format(args.new_busco))
    #running busco a file that has gone through filter_transrate.py, before it is filtered again.
    busco1 = ("run_BUSCO.py -m tran -l /mnt/lustre/hcgs/shared/databases/busco/eukaryota_odb9 -i {0} -o {1}_trans".format(args.infile, args.prefix))
    subprocess.run(busco1, shell = True)

    #running cdhit on a file that has previously been filtered using filter_transrate.py
    print("Running cdhit")
    subprocess.run("cdhit -c {0} -T 24 -i {1} -o {2}".format(args.similarity, args.infile, args.outfile), shell = True)

    os.chdir("{0}".format(args.final_busco))
    #running busco once more on the filtered (now twice) files
    busco2 = ("run_BUSCO.py -m tran -l /mnt/lustre/hcgs/shared/databases/busco/eukaryota_odb9 -i {0} -o {1}_cdhit".format(args.outfile, args.prefix))
    subprocess.run(busco2, shell = True)


def calc_busco():
    #looping through all the busco scores for each species
    for entry in os.scandir("{0}".format(args.orig_busco)):
        score1 = None
        score2 = None
        score3 = None
        whole = entry.name.split(".")
        front = suffix[0].split("_")
        #storing just the genus_species names for later
        specname = "{0}_{1}".format(front[2], front[3])
        print(specname)

        #extracting the score from the original busco files
        try:
            with open("{0}".format(entry.name)) as first:
                for line in first:
                    line = line.strip()
                    if line[0] == "C":
                        score1 += float(line[2:6])

            #extracting the score from the second busco run
            with open("{0}/run_{1}_trans/short_summary_{1}_trans.txt".format(args.new_busco, specname)) as second:
                for line in second:
                    line = line.strip()
                    if line[0] == "C":
                        score2 += float(line[2:6])

            #extracting the score from the third busco run
            with open("{0}/run_{1}_cdhit/short_summary_{1}_cdhit.txt".format(args.final_busco, specname)) as third:
                for line in third:
                    line = line.strip()
                    if line[0] == "C":
                        score3 += float(line[2:6])

            with open("{0}/specname.scores.txt", "w") as new_file:
                

parser = argparse.ArgumentParser(description = "Arguments for quality checking and filtering with cdhit")
parser.add_argument("-i", "--infile", required = True, help = "absolute path to file to be filtered and buscoed")
parser.add_argument("-s", "--similarity", type = float, default = 1.0, help = "similarity threshold for cdhit")
parser.add_argument("-n", "--new_busco", required = True, help = "path to directory where busco scores should be stored")
parser.add_argument("-f", "--final_busco", required = True, help = "path to directory where busco scores should be stored")
parser.add_argument("-b", "--orig_busco", required = True, help = "path to the directory where original busco score is")
parser.add_argument("-p", "--prefix", required = True, help = "prefix to go into the name of the busco output")
parser.add_argument("-o", "--outfile", required = True, help = "path to the filtered assembly file")
parser.add_argument("-bs", "--busco_scores", required = True, help = "path to where the busco score calculations should go")
args = parser.parse_args()

qual_cdhit_qual()

#submitted at 1:50 or so.



def busco():
    orig_dir = os.getcwd()
    os.chdir("{0}".format(args.busco_out))
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
