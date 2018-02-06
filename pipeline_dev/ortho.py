#! /usr/bin/env python3

import argparse
import subprocess
import os
import shutil

def orthofinder():
    shutil.rmtree("orthofinder_out", ignore_errors = True)

    orig_dir = os.getcwd()
    os.mkdir("orthofinder_out")
    os.chdir("orthofinder_out")
    trees = subprocess.run("orthofinder.py -f {0} -t 24".format(args.dir), shell = True, stdout = subprocess.PIPE)
    os.chdir("{0}".format(orig_dir))
    return trees.stdout.decode('ascii')

parser = argparse.ArgumentParser(description = "Things that OrthoFinder needs to run")
parser.add_argument("dir", help = "path to a directory of fasta files that passed the busco threshold")
args = parser.parse_args()

orthofinder()
