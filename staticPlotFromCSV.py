import os
import math
import matplotlib.pyplot as plt
import numpy as np
import csv
from tkinter import Tk
from tkinter.filedialog import askdirectory


fig = plt.figure()
fig.canvas.set_window_title('Offline Plot - Cell Counting')
# plot two summary
def plot(filename,x,y,z):

    title = filename.split(os.sep)[-1]
    file1 = filename+'\summary_C1.xls'
    file2 = filename+'\summary_C2.xls'
    #imgFile = filename+'\cell_count_plot.png'

    
    #ax1 = fig.add_subplot(x,y,z)
    ax1 = plt.subplot(x,y,z)
    t= []
    C1 =[]
    C2 =[]

    pullData1 = open(file1,'r').read()
    dataArray1 = pullData1.split('\n')

    pullData2 = open(file2,'r').read()
    dataArray2 = pullData2.split('\n')
    
    for row in dataArray1[1:]:
        if len(row)>1:
            count = row.split(',')[1]
            C1.append(float(count))
        
    for row in dataArray2[1:]:
        if len(row)>1:
            count = row.split(',')[1]
            C2.append(float(count))

    lenCompleteFrame = min(len(C1),len(C2))
    
    for i in range(1,lenCompleteFrame+1):
        t.append(i);

    ax1.clear()        
    ax1.plot(t,C1[0:lenCompleteFrame],color='g',label='C1')
    ax1.plot(t,C2[0:lenCompleteFrame],color='r',label='C2')
    ax1.legend(loc="upper left")
    ax1.set_title(title)
    ax1.set_xlabel('frame count')
    ax1.set_ylabel('cell count')

    fig.tight_layout()


    
Tk().withdraw()
dirname = askdirectory()

filename = dirname + os.sep + 'summary_C1.xls'
if (os.path.isfile(filename)):
    plot(dirname,1,1,1)
else:
    dirList = os.listdir(dirname)

    numFig = len(dirList)
    N = math.ceil(math.sqrt(numFig))

    while (numFig%N!=0):
        N+=1
    row = N;
    col = int(numFig/N)
    
    for d in range(1,len(dirList)+1):
        filepath = dirname + os.sep + dirList[d-1]
        if (os.path.isdir(filepath)):
            plot(filepath,row,col,d)


#fig.savefig(imgFile)
#print(imgFile)

plt.show()

#print("saved!")
