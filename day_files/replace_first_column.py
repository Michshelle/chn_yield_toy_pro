import os
import sys
from datetime import datetime
import pandas as pd

rootdir = './'
listing = os.listdir(rootdir)

for file_csv in listing:
    if file_csv.endswith('.csv'):
        replace_str = datetime.strptime(file_csv.split('.')[0],'%Y-%m-%d').strftime('%Y/%m/%d')
        df = pd.read_csv(file_csv,header=None)
        dk = df.replace(to_replace='?????????(??)',value=replace_str,regex=False)
        dk.to_csv(file_csv,index=False,header=False)

