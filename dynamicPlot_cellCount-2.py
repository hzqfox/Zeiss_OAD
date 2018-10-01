import os
import math
import optparse
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

# configure parsing option for command line usage
parser = optparse.OptionParser()
parser.add_option("-f", "--file",
                  action="store", dest = "dirname",
                  help="query string", default="No filename passed")

# parse command line arguments
options, args = parser.parse_args()
dirname = options.dirname

# check input if data is single or multiple series
filename = dirname + os.sep + 'summary_C1.xls'
numFig = 1;
col = 1;
row = 1;

if (os.path.isfile(filename)):
    multiPlot = False
else:
    multiPlot = True
    #print(dirname)
    dirList = os.listdir(dirname)
    # automatically decomposite column and row for multiple plots
    numFig = len(dirList)
    N = math.ceil(math.sqrt(numFig))    
    while (numFig%N!=0):
        N+=1
    row = N
    col = int(numFig/N)

        
# create figure plot window
fig, axes = plt.subplots(row, col, figsize = (12, 8), dpi = 100)


#print(len(axes))
fig.canvas.set_window_title('Online Plot - Cell Counting')


#for i in range(0:numFig):
while False:
    for d in range(1,len(dirList)+1):
        filepath = dirname + os.sep + dirList[d-1]
        if (os.path.isdir(filepath)):
            ani = animation.FuncAnimation(fig,
                animate(filepath,col,row,d),
                interval = 1000, blit = True)
#ax = fig.add_subplot(1,1,1)
#line, = ax.plot([],[],lw=2)


#def init():
#    line.set_data([],[])
#    return line,

# define animate function
def animate(i):
    global dirname
    global axes
    global row
    global col
    global dirList

    if (col == 1):
        for r in range(0, row):
            i = r
            axes[r].clear()
            title = dirList[i].split(os.sep)[-1]
            file1 = dirname + os.sep + dirList[i] + os.sep + 'summary_C1.xls'
            file2 = dirname + os.sep + dirList[i] + os.sep + 'summary_C2.xls'
            # assign local variables:
            #   t:time; C1:cell count in channel 1;
            #   C2:cell count in channel 2;
            t = []
            C1 = []
            C2 = []
            data_C1 = open(file1,'r').read()
            data_C1_line = data_C1.split('\n')

            data_C2 = open(file2,'r').read()
            data_C2_line = data_C2.split('\n')
            
        
            for rw in data_C1_line[1:]:
                if len(rw)>1:
                    count = rw.split(',')[1]
                    C1.append(float(count))
                
            for rw in data_C2_line[1:]:
                if len(rw)>1:
                    count = rw.split(',')[1]
                    C2.append(float(count))

            lenCompleteFrame = min(len(C1),len(C2))

            for i in range(1,lenCompleteFrame+1):
                t.append(i);
                           
            axes[r].plot(t,C1[0:lenCompleteFrame],color='g',label='C1')
            axes[r].plot(t,C2[0:lenCompleteFrame],color='r',label='C2')
            axes[r].legend(loc="upper left")
            axes[r].set_title(title)
            axes[r].set_xlabel('frame count')
            axes[r].set_ylabel('cell count')
            fig.tight_layout()
        return
            
    for c in range(0, col):
        for r in range(0, row):
    #for i in range(0, len(dirList)):
            i = r + c*row
            axes[r, c].clear()
            title = dirList[i].split(os.sep)[-1]
            file1 = dirname + os.sep + dirList[i] + os.sep + 'summary_C1.xls'
            file2 = dirname + os.sep + dirList[i] + os.sep + 'summary_C2.xls'
            # assign local variables:
            #   t:time; C1:cell count in channel 1;
            #   C2:cell count in channel 2;
            t = []
            C1 = []
            C2 = []
            data_C1 = open(file1,'r').read()
            data_C1_line = data_C1.split('\n')

            data_C2 = open(file2,'r').read()
            data_C2_line = data_C2.split('\n')
            
        
            for rw in data_C1_line[1:]:
                if len(rw)>1:
                    count = rw.split(',')[1]
                    C1.append(float(count))
                
            for rw in data_C2_line[1:]:
                if len(rw)>1:
                    count = rw.split(',')[1]
                    C2.append(float(count))

            lenCompleteFrame = min(len(C1),len(C2))

            for i in range(1,lenCompleteFrame+1):
                t.append(i);
                           
            axes[r, c].plot(t,C1[0:lenCompleteFrame],color='g',label='C1')
            #line1.set_data(t,C1)
            axes[r, c].plot(t,C2[0:lenCompleteFrame],color='r',label='C2')
            #line2.set_data(t,C2)
            axes[r, c].legend(loc="upper left")
            axes[r, c].set_title(title)
            axes[r, c].set_xlabel('frame count')
            axes[r, c].set_ylabel('cell count')
            #extent = ax1.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
            #fig.savefig(imgFile, bbox_inches=extent)
            #fig.savefig(imgFile)
            #ax1.set_ylim(bottom=0)
            #ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
            fig.tight_layout()
            #return line1, line2

ani = animation.FuncAnimation(fig,animate, interval = 1000)
plt.show()


while False:
    if (os.path.isfile(filename)):
        ani = animation.FuncAnimation(fig,animate(dirname,1,1,1),
            interval = 1000, blit = True,)

    else:
        dirList = os.listdir(dirname)

        numFig = len(dirList)
        N = math.ceil(math.sqrt(numFig))

        while (numFig%N!=0):
            N+=1
        col = N;
        row = int(numFig/N)

        for d in range(1,len(dirList)+1):
            filepath = dirname + os.sep + dirList[d-1]
            if (os.path.isdir(filepath)):
                ani = animation.FuncAnimation(fig,
                    animate(filepath,col,row,d),
                    interval = 1000, blit = True)
                
            #continue
            
    plt.show()
