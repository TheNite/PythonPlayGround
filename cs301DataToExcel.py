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

try:
    with open(dataFile, 'r+') as f:
        allLines = f.readlines()
        f.seek(0)
        f.write(str(allLines[0].lstrip(',')))
        f.write(''.join(allLines[1:]))
        f.truncate()
except:
    print("Couldn't find any file ending with .data")
    time.sleep(10)
    sys.exit(1)

data = pd.read_csv(dataFile, sep=",")
print(data)

xlsxFile = f'{dataFile.split(".data")[0]}.xlsx'
data.to_excel(fr'{xlsxFile}', index=None, header=True)