#import utils
import antenna
import numpy as np
class Event:
    def __init__(self, fname = ''
                 ):
        self.fname = fname
        self.id = 0
        self.gpssecond = 0
        self.energy = 0
        self.zenith = 0
        self.azimuth = 0
        self.antenna = []
        
    def fill(self):
        f = open(self.fname,'r')
        file = f.read()
        filesplit = file.split('\n')
        size = len(filesplit)
        for i in range(size):
            l = filesplit[i]
            if 'SDId:' in l:
                self.id = int(l.split()[1])
            if 'energy:' in l:
                self.energy = float(l.split()[1])
            if 'zenith:' in l:
                self.zenith = float(l.split()[1])
            if 'azimuth:' in l:
                self.azimuth = float(l.split()[1])
            if 'GPSSeconc:' in l:
                self.gpssecond = float(l.split()[1])
            if 'stid:' in l:
                ant = antenna.Antenna(int(l.split()[1]))
                ant.spdistance = float(filesplit[i+1].split()[1])
                radio = filesplit[i+3].split()
                vem = filesplit[i+5].split()
                if len(vem) < 768:
                    ant.vemtrace = np.zeros(768) 
                else:
                    ant.vemtrace = np.asarray(vem,dtype=float)
                ant.radiotrace = np.asarray(radio,dtype=int)
                self.antenna.append(ant)
                
