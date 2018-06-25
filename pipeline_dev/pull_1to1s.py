#! /usr/bin/env python3

import argparse
import Bio.SeqIO

#function to pull members of one-to-one orthogroups from a protein fasta file
def pull():
    try:
        ogs = set()
        ols = {}
        with open("{}".format(args.cluster), "r") as cluster_file:
            with open("{}".format(args.ortho), "r") as ortho_file:
                for line in cluster_file:
                    line = line.split("\t")
                    if line.startswith("OG"):
                        ogs.add(line[0])
                for line in ortho_file:
                    line = line.split("\t")
                    if line[0] in ogs:
                        ols.setdefault(line[0], line[1:])

        prot_seqs = []
        for record in Bio.SeqIO.parse("{}".format(args.prots), "fasta"):
            for item in ols[item]:
                if record.id == ols[item]:
                    cur_prot = Bio.SeqRecord.SeqRecord(id = record.id, seq = record.seq)
                    prot_seqs.append(cur_prot)
        Bio.SeqIO.write(prot_seqs, "{}".format(args.out), "fasta")

    except IOError:
        print("Problem reading files")

parser = argparse.ArgumentParser(description = "arguments for pulling 1-to-1 orthologues from a fasta")
parser.add_argument("-c", "--cluster", required = True, help = "all.all.cluster_1to1s.txt provided by kinfin")
parser.add_argument("-o", "--ortho", required = True, help = "Orthologues.csv provided by orthofinder")
parser.add_argument("-p", "--prots", required = True, help = "fasta file containing all proteins in the orthofinder analysis")
parser.add_argument("-o", "--out", required = True, help = "name of the output fasta file")

pull()
