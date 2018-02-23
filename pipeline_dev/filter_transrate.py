#! /usr/bin/env python3

#a scipt to take a transcriptome assembly and discard all those transcripts below
#a threshold equal to some fraction of a standard deviation from the median score

import argparse
import statistics

def filter():
    try:
        with open("args.in_file", "r", newline = "") as con_file:
            with open("args.out_file", "w") as filtered_csv:
                score_list = []
                filtered_lines = ""
                    for line in con_file:
                        score_list.append(line[8])
                    med_score = statistics.median(score_list)
                    dev_score = statistics.stdev(score_list)
                    low_bound = med_score - (args.prop * dev_score)
                    print(med_score)
                    print(dev_score)
                    print(low_bound)
                    for line in con_file:
                        if line[8] >= low_bound:
                            filtered_lines += line
                    filtered_csv.write(filtered_lines)


parser = argparse.ArgumentParser(description = "Arguments for filtering transctiptomes")
parser.add_argument("in_file", help = "path to the transrate contigs.csv file")
parser.add_argument("prop", help = "proportion of a standard deviation below the median that defines the lowest allowed score")
parser.add_argument("out_file", help = "the name of the new filtered output file")
args = parser.parse_args()
