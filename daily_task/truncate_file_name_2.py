#!/usr/bin/python3

import os
import sys

rootdir = './'
listing = os.listdir(rootdir)

for file_xlsx in listing:
	if file_xlsx.endswith('.xlsx'):  ##pay attention to the endswith and it affects the next line about truncate [-15:]
            os.rename(file_xlsx,file_xlsx[-15:]) ##the position

