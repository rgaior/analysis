import matplotlib.pyplot as plt
import matplotlib.pylab as plab
import numpy as np
import os
import sys
import glob
cwd = os.getcwd()
classpath = cwd + '/../classes/'
#utilspath = cwd + '/../utils/'
#sys.path.append(utilspath)
sys.path.append(classpath)
#import utils
import event

name = sys.argv[1]

basefolder = '/Users/romain/work/Auger/EASIER/data/txtdata/2015/'
month = '05/'
files = glob.glob(basefolder +month+ '*.txt')
#print files
time = np.linspace(0,767,768)
freq = np.fft.rfftfreq(len(time),25e-9)
#{339,313,340,329,330,334,328};
colcode = {339:'k',313:'r',340:'b',329:'g',330:'c',334:'m',328:'y'}
idcode = {'santy':339,'rula':313,'nono':340,'jorge':329,'eva':330,'gilda':334,'gringa':328}
print len(files)
for file in files[:10]:
#    print file
    ev = event.Event(file)
    ev.fill()
    # print ev.antenna[0].radiotrace
    for ant in ev.antenna:
        if ant.id !=idcode[name]:
            continue
        radio = ant.radiotrace
        vem = ant.vemtrace
#        fft = np.fft.rfft(radio)
#        plt.plot(time,radio, label=str(ant.id))
        plt.plot(time,radio,str(colcode.get(ant.id)))
#        spec= np.absolute(fft)
#        plt.plot(freq,spec,str(colcode.get(ant.id)))



#plt.plot(time,vem)
#plt.legend()
plt.show()
