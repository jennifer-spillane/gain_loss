#! bin/bash
echo "Type the path to the directory containing the fasta files"
read dir_name
#echo ""
cd $dir_name
for file_name in *.pep
do
    awk '/^>/{print ">" ++i; next}{print}' < ./$file_name > genus_species.fa
done

#! /usr/bin/env python3

import os
import subprocess

for fasta in os. scandir("/mnt/lustre/macmaneslab/jlh1023/metazoa_matrix/batch1_filtered/"):
    filename = fasta.name.split(".")
    genespec = filename[0]


awk '/^>/{$0=">Genus_species_"++i}1' input.fasta > output.fasta





OG0381225: Gene.27787__lucernariopsis_campanulata_54495__g.27787__m.27787
OG0356027: Gene.36946__hirondellea_gigas_87406__g.36946__m.36946
OG0426389: Gene.53874__pleraplysilla_spinifera_103554__g.53874__m.53874
OG0440104: Gene.23036__proasellus_beticus_110697__g.23036__m.23036
OG0339498: Gene.14041__hemithiris_psittacea_16303__g.14041__m.14041
OG0144664: Homo_sapiens_47396
OG0033621: Caenorhabditis_elegans_12948 Caenorhabditis_elegans_12949 Meloidogyne_incognita_12895
OG0129370: Drosophila_melanogaster_22009
OG0276587: Gene.11977__clione_antarctica_24043__g.11977__m.11977
OG0025577: Capitella_teleta_20342 Gene.1889__convolutriloba_macropyga_2780__g.1889__m.1889 Gene.60737__pleraplysilla_spinifera_114915__g.60737__m.60737 Ixodes_scapularis_13782 Nematostella_vectensis_14569

#! /usr/bin/env python3

try:
    with open("{0}".format(args.in) "r") as infile:
        for line in infile:
            line = line.split("\t")
            


import argparse
import re
import Bio.SeqIO

parser = argparse.ArgumentParser(description = "arguments for changing headers")
parser.add_argument("-p", "--pasta", required = True, help = "input ali file to change names of")
parser.add_argument("-o", "--out", required = True, help = "name of out file")
args = parser.parse_args()

try:
    all_lines = []
    for record in Bio.SeqIO.parse("{0}".format(args.pasta), "fasta"):
        header = re.search("([a-z]+)([0-9]*)", record.id)
        species = header.group(1)
        acc = header.group(2)
        cap_species = species.capitalize()
        new_hydra = ""
        if cap_species.startswith("Hydra"):
            hydra_cap_species = cap_species[0:5]
            remaining = cap_species[5:]
            new_hydra = "{0}_{1}".format(hydra_cap_species, remaining)
        new_header = "{0}_{1}".format(new_hydra, acc) if len(new_hydra) > 0 else "{0}_{1}".format(cap_species, acc)
        current_record = Bio.SeqRecord.SeqRecord(id = new_header, seq = record.seq, description = "")
        all_lines.append(current_record)
    Bio.SeqIO.write(all_lines, "{0}".format(args.out), "fasta")
except IOError:
print("Ya dumb!")
