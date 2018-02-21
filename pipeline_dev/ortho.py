#! /usr/bin/env python3

import argparse
import subprocess

def orthofinder():
    subprocess.run("orthofinder.py -f {0} -t 24 -S diamond".format(args.dir), shell = True, stdout = subprocess.PIPE)

parser = argparse.ArgumentParser(description = "Things that OrthoFinder needs to run")
parser.add_argument("dir", help = "path to a directory of fasta files that passed the busco threshold")
args = parser.parse_args()

orthofinder()
