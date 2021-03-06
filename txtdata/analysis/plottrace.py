import matplotlib.pyplot as plt
import matplotlib.pylab as plab
import matplotlib
matplotlib.rc('xtick', labelsize=15) 
matplotlib.rc('ytick', labelsize=15) 
import numpy as np
import os
import sys
import glob
cwd = os.getcwd()
classpath = cwd + '/../classes/'
sys.path.append(classpath)
utilspath = cwd + '/../utils/'
sys.path.append(utilspath)
import utils
import event
from datetime import date
#month = int(sys.argv[2])

arrays = ['easier7','easier47','gigaduck']

basefolder = '/Users/romain/work/Auger/EASIER/data/txtdata/2015/'
months ='04/'


#filehelix = 'sd_32017448.txt'
#filehelix = 'sd_32189905.txt'
filehelix = 'sd_32559147.txt'
file  = basefolder + months + filehelix

ev = event.Event(file)
ev.fill()
for ant in ev.antenna:
    if ant.id == 340:
        radio = ant.radiotrace
        print np.std(radio)
        plt.plot(radio)


plt.xlabel('time bin')
plt.ylabel('ADC')
plt.ylim(150,950)
plt.legend()
plt.show()
