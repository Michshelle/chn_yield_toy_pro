#!/usr/bin/python3

import os
import sys
import csv

rootdir = './'
listing = os.listdir(rootdir)

for i_t in listing:
    if i_t.endswith('.csv') and not i_t.startswith('updated'):
        with open(i_t,'r') as f:
            with open('updated_' + i_t,'w' ) as f1:
                next(f)
                for line in f:
                    f1.write(line)
for i_t in listing:
    os.system("rm i_t")
