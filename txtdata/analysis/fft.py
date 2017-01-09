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
import constant
import event
from datetime import date
#name = sys.argv[1]

basefolder = '/Users/romain/work/Auger/EASIER/data/txtdata/2015/'
#months = ['03/','04/','05/','06','07/']
months = ['04/']

#colcode = {339:'k',313:'r',340:'b',329:'g',330:'c',334:'m',328:'y'}
idcode = constant.GDstationidbyname
a_fft = np.ndarray(shape=(7,385))
#f = plt.figure(figsize=(10,10))                
f, axarr = plt.subplots(2, 4)
a_count = np.zeros(7)
count = 0
mean = np.array([])
meanvem = np.array([])
std = np.array([])
gpssec = np.array([])
normedtrace = np.array([])
gooddate = np.array([])
for month in months:
    files = glob.glob(basefolder +month+ '*.txt')
    for file in files[::10]:
        #    print file
        ev = event.Event(file)
        ev.fill()
        for name in idcode.keys():
            for ant in ev.antenna:
                if ant.id !=idcode[name]:
                    continue
                index = constant.GDstationindex[name]
#                print 'name = ', name , ' index = ', index
                radio = ant.radiotrace
                fft = np.fft.rfft(radio)
                a_fft[index] = a_fft[index] + np.absolute(fft)
                a_count[index] +=1
                mean = np.append(mean,np.mean(radio))
                normedtrace = np.append(normedtrace, radio-np.mean(radio))
                std = np.append(std,np.std(radio))
                gpssec = np.append(gpssec,ev.gpssecond)
                gooddate = np.append(gooddate,utils.gpstodate(ev.gpssecond))
                vem = ant.vemtrace
                meanvem = np.append(meanvem,np.mean(vem))

for name,i in constant.GDstationindex.items():
    print type(i)
    indices = utils.splitintwocol(i,4)
    axarr[indices[0],indices[1]].plot(a_fft[i][1:]/a_count[i])
    axarr[indices[0],indices[1]].set_title(name)
    
plt.show()
  #  ax1 = plt.subplot(111)
  #  ax1.set_ylabel('ADC',fontsize=15)
  #  ax1.plot(a_fft)
  #  plt.show()
