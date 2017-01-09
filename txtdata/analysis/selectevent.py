import matplotlib.pyplot as plt
import matplotlib.pylab as plab
import matplotlib
matplotlib.rc('xtick', labelsize=15) 
matplotlib.rc('ytick', labelsize=15) 
import numpy as np
import os
import sys
import math
import glob
cwd = os.getcwd()
classpath = cwd + '/../classes/'
sys.path.append(classpath)
utilspath = cwd + '/../utils/'
sys.path.append(utilspath)
import utils
import event
from datetime import date
#name = sys.argv[1]

basefolder = '/Users/romain/work/Auger/EASIER/data/txtdata/2015/'
months = ['03/','04/','05/','06/','07/','08/','09/','10/','11/','12/']
#months = ['03/','04']

colcode = {339:'k',313:'r',340:'b',329:'g',330:'c',334:'m',328:'y'}
idcode = {'santy':339,'rula':313,'nono':340,'jorge':329,'eva':330,'gilda':334,'gringa':328}
#idcode = {'nono':340}
time = np.linspace(0,767,768)
for name in idcode.keys():
    for month in months:
        files = glob.glob(basefolder +month+ '*.txt')
        for file in files:
            #    print file
            ev = event.Event(file)
            ev.fill()
            if ev.energy < math.pow(10,19):
                continue
            for ant in ev.antenna:
                if ant.id !=idcode[name]:
                    continue
                if ant.spdistance > 1000:
                    continue
                radio = ant.radiotrace
                if np.std(radio) < 5:
                    continue
#                radio = utils.adctopwatt(radio)
                radiofilt = utils.lowpasshard(radio,40e6,1e6)
                fig1 = plt.figure(figsize=(10,5))
                plt.plot(time,radio)
                plt.plot(time,radiofilt,'r',lw=2)
plt.show()
