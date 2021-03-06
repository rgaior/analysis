import matplotlib.pyplot as plt
import matplotlib.pylab as plab
import matplotlib
from matplotlib import gridspec
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
evnr = int(sys.argv[1])

basefolder = '/Users/romain/work/Auger/EASIER/data/txtdata/2015/'
#months = ['03/','04/','05/','06/','07/','08/','09/','10/','11/','12/']
months = ['05/']

idcode = {'nono':340}
rms = np.array([])
maxvem = np.array([])
#idcode = {'vieira':433}
for name in idcode.keys():
    mean = np.array([])
    meanvem = np.array([])
    std = np.array([])
    gpssec = np.array([])
    normedtrace = np.array([])
    gooddate = np.array([])
    for month in months:
        files = glob.glob(basefolder +month+ '*.txt')
        #    time = np.linspace(0,767,768)
#        for file in files[::40]:
        for file in files:
            #    print file
            ev = event.Event(file)
            ev.fill()
            if ev.id !=  evnr:
                continue
            else:
                print 'got it'
            for ant in ev.antenna:
                if ant.id !=idcode[name]:
                    continue
                vem = ant.vemtrace
                maxvem = np.append(maxvem,np.max(vem))
                radio = ant.radiotrace
                date = utils.gpstodate(ev.gpssecond)
                dstr = date.strftime("%d/%m/%y") 
                if np.std(radio) > 30:
                    print ev.id
                    print np.std(radio[400:500])
                    print np.std(radio)
                    fig = plt.figure(figsize=(12,5))
                    fig.suptitle(name + ' ('  + dstr + ' )',fontsize=15,fontweight='bold')
                    gs = gridspec.GridSpec(1, 2, width_ratios=[2, 1])
                    ax1 = plt.subplot(gs[0])
                    ax1.plot(radio)
                    figvem = plt.figure()
                    plt.plot(vem)
#                ax1.plot(radio- np.mean(radio))
 #               ax2 = plt.subplot(gs[1])
                rms = np.append(rms, np.std(radio))
#                print np.std(radio - np.mean(radio)), '  ' , np.std(radio)
  #              ax2.hist(radio - np.mean(radio))
                

#plt.hist(rms)
fig2 = plt.figure()
plt.plot(maxvem,rms,'o')
plt.show()
