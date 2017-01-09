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
arrayname = sys.argv[1]
#month = int(sys.argv[2])

if arrayname == 'easier7':
    array = utils.easier7
elif arrayname == 'easier47':
    array = utils.easier47
elif arrayname == 'gigaduck':
    array = utils.gigaduck
elif arrayname == 'helix':
    array = utils.helix
basefolder = '/Users/romain/work/Auger/EASIER/data/txtdata/2015/'
#basefolder = '/Users/romain/work/Auger/EASIER/LPSC/filter/data/txtdata/2015/'
months = ['05/']
stdarray = {}
meanarray = {}
fluctarray = {}
for stid in array:
    stdarray[stid] = np.array([])
    meanarray[stid] = np.array([])
    fluctarray[stid] = np.array([])
    
for month in months:
    files = glob.glob(basefolder +month+ '*.txt')
    for file in files[::10]:
        ev = event.Event(file)
        ev.fill()
        for id in array:
            for ant in ev.antenna:
                if ant.id not in array:
                    continue
                radio = ant.radiotrace
                stdarray[ant.id] = np.append(stdarray[ant.id],np.std(radio))
                meanarray[ant.id] = np.append(meanarray[ant.id],np.mean(radio))
                fluctarray[ant.id] = np.append(fluctarray[ant.id],radio - np.mean(radio))
                
meanstd = np.array([])
ids = np.array([])
if arrayname=='easier47':
    arrayname = 'easier61'
fig = plt.figure()
fig.suptitle(arrayname,fontsize=15,fontweight='bold')

for id in array:
    if arrayname == 'easier61'  and (np.std(fluctarray[id]) < 55  and np.std(fluctarray[id]) > 45) :
        np.savez(arrayname+'_'+str(id),fluctarray[id])
        count, bins, patches = plt.hist(fluctarray[id], 100,histtype='step',normed=True,log=True)        
    elif arrayname == 'gigaduck' and np.std(fluctarray[id]) < 55:
        count, bins, patches = plt.hist(fluctarray[id], 100,histtype='step',normed=True,log=True)
        np.savez(arrayname+'_'+str(id),fluctarray[id])
    elif arrayname == 'easier7' :
        count, bins, patches = plt.hist(fluctarray[id], 100,histtype='step',normed=True,log=True)
        np.savez(arrayname+'_'+str(id),fluctarray[id])

#plt.plot(ids,meanstd,'ro')
plt.xlabel('amplitude - baseline [ADC]')
plt.show()
