#! /usr/bin/env python3

import subprocess
import argparse
import pandas
import os
import shutil
from multiprocessing import Pool
import threading


def model(og):
    #getting the current thread id
    cur_id = threading.get_ident()

    try:
        master_list = []
        #making the command to use later
        command = "/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/r_dollo.r {0}".format(cur_id)
        #split the lines of the matrix and discard the cluster from the first one
        #then write the first line to the new file
        stripped = og[1].rstrip()
        new_stripped = stripped.split("\t")
        og_name = new_stripped[0]
        print("Now working on: {0}".format(og_name))
        #making a set out of the values of the matrix
        #the set will collapse all repeat values
        #so if the length is different from 2, it's universally present or messed up
        #if the line passes, it gets written to the temp file
        sub_stripped = set(new_stripped[1:])
        if len(sub_stripped) == 2:
            with open("{0}_for_r.csv".format(cur_id), "w") as tmp_og:
                tmp_og.write(og[0])
                tmp_og.write(og[1])
            #run the R subprocess, which should print info about the tree to stdout
            rscript = subprocess.run(command, shell = True)
            #once r is finished, opening the output
            with open("{0}_from_r.csv".format(cur_id), "r") as r_file:
                master_list = []
                for row in r_file:
                    master_list.append(row)
                #append to a master variable
                #master_list.append(ind_list)
                master_tuple = (og_name, master_list)
                return(master_tuple)

    except IOError:
        print("Issue reading file")



#arguments for the whole thing
parser = argparse.ArgumentParser(description = "arguments for applying the dollo model")
parser.add_argument("-t", "--tree", required = True, help = "Path to a phylogenetic tree file")
parser.add_argument("-m", "--matrix", required = True, help = "Path to a presense/absense matrix")
parser.add_argument("-o", "--output", required = True, help = "Path to the output file")
args = parser.parse_args()

#copying the files I need into the working directory so that R can access them
working = os.getcwd()
shutil.copyfile(args.tree, "{0}/tree.new".format(working))
shutil.copyfile(args.matrix, "{0}/matrix.csv".format(working))

#setting up the pooling and reading in the matrix file
pool = Pool(24)
file = open("matrix.csv", "r")
all_lines = file.readlines()
file.close()
#extract out headers - save as variable
first = all_lines[0]
newfirst = first.split("\t")
woclust = newfirst.remove("#cluster_id")
taxa_line = "\t".join(newfirst)
header = "\t{0}\n".format(taxa_line)
headers = [header] * (len(all_lines)-1)
for_pool = zip(headers, all_lines[1:])

results = pool.map(model, for_pool)

results_dict = {}
group_num = ""
#"content" is a tuple with the OG as the first thing and a list of lines from
#the r output file as the second thing.
for content in results:
    print(content)
    #checking to see if the og is one that was all present
    if content is not None:
        #"group_num" is the OG element of the tuple, while "presabs" is the list element
        group_num = content[0]
        presabs = content[1]
        all_nodes = []
        #skipping the first row, which is just a 0 and a 1
        for item in presabs[1:]:
            #stripping off the linefeeds and splitting on tabs
            #also taking off the quotation marks from the node names
            #"first_line" is there to be written to a file later
            stripped_item = item.rstrip()
            fields = stripped_item.split("\t")
            stripped_fields = fields[0].strip('"')
            all_nodes.append(stripped_fields)
            #key = OG number, value = empty list, later presense scores
            results_dict.setdefault(group_num, [])
            results_dict[group_num].append(fields[2])

try:
    with open("{0}".format(args.output), "w") as final:
        first_line = "\t".join(all_nodes)
        print(first_line)
        final.write("\t{0}\n".format(first_line))
        for og_num in results_dict:
            all_scores = "\t".join(results_dict[og_num])
            #print("printing results[0]")
            #print(results[0])
            whole_line = "{0}\t{1}\n".format(og_num, all_scores)
            print(whole_line)
            final.write(whole_line)
except IOError:
    print("Problem writing outfile")



#/mnt/lustre/macmaneslab/jlh1023/pipeline_dev/pipeline_scripts/dollo_model.py
#/mnt/lustre/plachetzki/shared/reciprocator/RECIPROCATOR/rax2/RAxML_bestTree.met_67_test
#/mnt/lustre/macmaneslab/jlh1023/metazoa_matrix/Results_Jul17/top_cor_pres_abs.csv
