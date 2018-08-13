#! /usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description = "arguments for finding interesting OGs")
parser.add_argument("-i", "--input", required = True, help = "Path to the spreadsheet to be analyzed")
args = parser.parse_args()

try:
    with open("args.input", "r") as og_file:
        for line in og_file:
            if line.startswith("OG"):
                nodes = line.split("\t")
                if float(nodes[3]) <= 0.025:
                    if float(nodes[8]) >= 0.075:
                        if float(nodes[16]) >= 0.075:
                            loss = "\t".join(nodes)
                            print(loss)
