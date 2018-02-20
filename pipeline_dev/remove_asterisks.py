#! usr/bin/env python3

import re
import os

def asterisk():
    for entry in os.scandir("{0}".format(args.directory)):
        try:
            with open("{0}".format(entry.path)) as fasta_file:
                for line in fasta_file:
                    stop = re.search("\*", line)
                    rem_stop = stop.replace("\*", "")
        except FileNotFoundError:
            print("file could not be found")
