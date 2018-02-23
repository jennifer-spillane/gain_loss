#! /usr/bin/env python3

#a scipt to take a transcriptome assembly and discard all those transcripts below
#a threshold equal to some fraction of a standard deviation from the median score

import argparse
import statistics

def filter():
    try:
        #opening both a file to read from and one to write to
        with open("{0}".format(args.in_file), "r") as con_file:
            print("opened in_file")
            with open("{0}".format(args.out_file), "w") as filtered_csv:
                print("opened out_file")
                score_list = []
                filtered_lines = {}
                for line in con_file:
                    line = line.split(",")
                    if line[8] != "score":
                        score_list.append(float(line[8]))
                #calculating all necessary scores to filter
                med_score = statistics.median(score_list)
                dev_score = statistics.stdev(score_list)
                low_bound = med_score - (args.prop * dev_score)
                               print(med_score)
                print(dev_score)
                print(low_bound)
                #iterating through each line, and adding the ones that pass
                for line in con_file:
                    line = line.split(",")
                    if line[8] != "score":
                        if float(line[8]) >= low_bound:
                            filtered_lines += line
                print(filtered_names)
    except IOError:
        print("Issue reading file")
    return(filtered_names)

parser = argparse.ArgumentParser(description = "Arguments for filtering transctiptomes")
parser.add_argument("in_file", help = "path to the transrate contigs.csv file")
parser.add_argument("prop", type = float, help = "proportion of a standard deviation below the medi$
parser.add_argument("out_file", help = "the name of the new filtered output file")
args = parser.parse_args()

filter()
