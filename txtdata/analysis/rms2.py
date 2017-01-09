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
# arrayname = sys.argv[1]

# if arrayname == 'easier7':
#     array = utils.easier7
# elif arrayname == 'easier47':
#     array = utils.easier47
# elif arrayname == 'gigaduck':
#     array = utils.gigaduck
# elif arrayname == 'helix':
#     array = utils.helix

#arrays = ['easier7','gigaduck']
arrays = ['easier7','easier47','gigaduck']
basefolder = '/Users/romain/work/Auger/EASIER/data/txtdata/2015/'
#basefolder = '/Users/romain/work/Auger/EASIER/LPSC/filter/data/txtdata/2015/'
months = ['04/']
stdarray = {}
meanarray = {}
rmss = []
for arrayname in arrays:
    if arrayname == 'easier7':
        array = utils.easier7
    elif arrayname == 'easier47':
        array = utils.easier47
    elif arrayname == 'gigaduck':
        array = utils.gigaduck
    elif arrayname == 'helix':
        array = utils.helix

    for stid in array:
        stdarray[stid] = np.array([])
        meanarray[stid] = np.array([])

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
                
    meanstd = np.array([])
    ids = np.array([])
    for id in array:
        meanstd = np.append(meanstd,np.mean(stdarray[id]))
        ids = np.append(ids,id)
    rmss.append(meanstd)

fig = plt.figure()
ax = plt.subplot(111)
for rms,arr in zip(rmss,arrays):
    if arr == 'easier47':
        arr = 'easier61'    
    bins = np.linspace(0,120,120)
    #selection of the good detectors
    if arr == 'easier61':
        c1,b1,p1 = plt.hist(rms[ (rms >45) & (rms <55) ],bins=bins,histtype='step',color='g', lw=3, normed=False,alpha=0.75,log=False,label=arr+ ' data')
    if arr == 'gigaduck':
        c1,b1,p1 = plt.hist(rms[ rms <55 ],bins=bins,histtype='step', color='r',lw=3, normed=False,alpha=0.75,log=False,label=arr+ ' data')
    if arr == 'easier7':
        c1,b1,p1 = plt.hist(rms,bins=bins,histtype='step', lw=3,color='b', normed=False,alpha=0.75,log=False,label=arr+ ' data')


##method 1 convolution
#rmsEA7 = 33.42
#rmsEA61 = 45.4
#rmsGD = 41.1
##method 2: filter
# rmsEA7 = 40.2
# rmsEA61 = 57.8
# rmsGD = 52.7
##method 3: convolution with fixed caracteristics
rmsEA7 = 34.8
rmsEA61 = 58
rmsGD = 52.2

plt.plot(np.array([rmsEA7,rmsEA7]),np.array([0,8]),'b--',lw=2,label='easier7 sim.')
plt.plot(np.array([rmsEA61,rmsEA61]),np.array([0,8]),'g--',lw=2,label='easier61 sim.')
plt.plot(np.array([rmsGD,rmsGD]),np.array([0,8]),'r--',lw=2,label='gigaduck sim.')
    

ax.set_xlabel('RMS [ADC]')
ax.set_xlim(20,80)

plt.legend()


    #    count, bins, patches = plt.hist(stdarray[id], 100)
#     if arrayname == 'easier7':
#         y1 = np.ones(len(meanstd))
#         name1 = np.chararray((len(y1),1),itemsize=7)
#         name1[:] = 'EASIER7'
# #        plt.xticks(y1, name1)
#         plt.plot(y1,meanstd,'bo')
#     if arrayname == 'easier47':
#         y3 = 3*np.ones(len(meanstd))
#         name3 = np.chararray((len(y3),1),itemsize=8)
#         name3[:] = 'EASIER61'
# #        plt.xticks(y3, name3)
#         plt.plot(y3,meanstd,'go')
#     if arrayname == 'gigaduck':
#         y2 = 2*np.ones(len(meanstd))
#         name2 = np.chararray((len(y2),1),itemsize=8)
#         name2[:] = 'GIGADUCK'
#         plt.plot(y2,meanstd,'ro')

# plt.xticks(np.array([1,2,3]), np.array(['EASIER7','EASIER61','GIGADUCK']))

# plt.xlim(-0.5,3.5)    
# plt.ylabel('RMS [ADC]')




#     ax.text(0.01, 0.95, 'mean = ' + str("%.3f" % np.mean(deltav1))+ '\n std = ' + str("%.3f" % np.std(deltav1)),
#         verticalalignment='top', horizontalalignment='left',
#         transform=ax.transAxes,
#         color='blue', fontsize=15)

plt.show()
