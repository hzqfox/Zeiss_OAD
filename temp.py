import os.path
import math
from tkinter import Tk
from tkinter.filedialog import askdirectory


Tk().withdraw()
dirname = askdirectory()
filename = dirname + os.sep + 'summary_C1.xls'
numFig = col = row = 0;

if (os.path.isfile(filename)):
    multiPlot = False
    numFig = col = row = 1;
else:
    multiPlot = True
    print(dirname)
    dirList = os.listdir(dirname)
    for file in dirList:
        print(file)
    # automatically decomposite column and row for multiple plots
    numFig = len(dirList)
    print(numFig)
    N = math.ceil(math.sqrt(numFig))    
    while (numFig%N!=0):
        N+=1
    col = N;
    row = int(numFig/N)

    print(N)        
if (multiPlot):
    print("correct")
else:
    print("wrong")
print("row: ", row)
print("col: ", col)
