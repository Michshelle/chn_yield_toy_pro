#!/usr/bin/python3

import os
import sys

rootdir = './'
listing = os.listdir(rootdir)

for file_xlsx in listing:
	if file_xlsx.endswith('.xlsx'):
            print(file_xlsx)
            os.system("libreoffice --headless --convert-to csv {}".format(file_xlsx))
            os.system("rm {}".format(file_xlsx))

