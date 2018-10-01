import os
import math
import optparse
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

# configure parsing option for command line usage
parser = optparse.OptionParser()
parser.add_option("-f", "--file",
                  action="store", dest = "filename",
                  help="query string", default="No filename passed")

# read command line arguments
options, args = parser.parse_args()
#folderName = options.filename
file1 = options.filename+'\summary_C1.xls'
file2 = options.filename+'\summary_C2.xls'
imgFile = options.filename+'\cell_count_plot.png'


fig = plt.figure()
fig.canvas.set_window_title('Dynamic Cell Counting Plot - ZH')
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    t = []
    C1 = []
    C2 = []
    
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
    ax1.set_title('Fucci Cell Count')
    ax1.set_xlabel('frame count')
    ax1.set_ylabel('cell count')
    #extent = ax1.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    #fig.savefig(imgFile, bbox_inches=extent)
    #fig.savefig(imgFile)
    #ax1.set_ylim(bottom=0)
    #ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
print(1)    
ani = animation.FuncAnimation(fig,animate, interval = 1000)
#print(2)
#fig.savefig(imgFile)
print(3)
plt.show()
print(4)
