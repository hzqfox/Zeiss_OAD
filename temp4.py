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

filename = dirname + os.sep + 'summary_C1.xls'

dirList = os.listdir(dirname)

print(len(dirList))
