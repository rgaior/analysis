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
months ='03/'

fileforEA7 = 'sd_32194925.txt' # st 333
#fileforEA47 = 'sd_32195116.txt' # st 306
#fileforEA47 = 'sd_32196794.txt' # st 328
#fileforEA47 = 'sd_32194254.txt' # st 334
fileforEA47 = 'sd_32194925.txt' # st 403

fileforGD = 'sd_32195223.txt' # st 427

filehelix = 'sd_32017448.txt'

fileforEA7  = basefolder + months + fileforEA7
fileforEA47  = basefolder + months + fileforEA47
fileforGD  = basefolder + months + fileforGD

ev = event.Event(fileforEA7)
ev.fill()
for ant in ev.antenna:
    if ant.id == 333:
        radio = ant.radiotrace
        print np.std(radio)
        plt.plot(radio,label='EASIER7')

ev2 = event.Event(fileforEA47)
ev2.fill()
for ant in ev2.antenna:
    if ant.id == 403:
        radio = ant.radiotrace
        print np.std(radio)
        plt.plot(radio,label='EASIER61')

ev3 = event.Event(fileforGD)
ev3.fill()
for ant in ev3.antenna:
    if ant.id == 427:
        radio = ant.radiotrace
        print np.std(radio)
        plt.plot(radio,label='GIGADUCK')
plt.xlabel('time bin')
plt.ylabel('ADC')
plt.ylim(150,950)
plt.legend()
plt.show()
