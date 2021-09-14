import os
import sys
import time
import pandas as pd

windows_platform = ['win32', 'cygwin']

print(sys.platform)
if sys.platform in windows_platform:
    print("Detected Windows. This script will not work for Windows\nMake your own Modification if you would like")
    time.sleep(10)
    sys.exit(1)

os.chdir(os.getcwd())

files = os.listdir()

dataFile = ''

for file in files:
    if file.endswith('.data'):
        dataFile = file

if len(dataFile) == 0:
    print(f"Couldn't find a .data file{'.' * 6}Exiting")
    time.sleep(10)
    sys.exit(1)

data = pd.read_csv(dataFile, sep=",")
print(data)

xlsxFile = f'{dataFile.split(".data")[0]}.xlsx'
data.to_excel(fr'{xlsxFile}', index=None, header=True)
