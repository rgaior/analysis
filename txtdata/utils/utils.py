import numpy as np
##################################
### conversion function ##########
##################################
from datetime import date
def gpstodate(gpssecond):
    return  date.fromtimestamp(gpssecond+315964800)
import datetime
def gpstodatetime(gpssecond):
    return  datetime.datetime.fromtimestamp(gpssecond+315964800)

def getmean(data):
    mean = 0
    for el in data:
        mean+=el
    mean = mean/len(data)
    print 'mean = ', mean
    return mean/len(data)

def getstddev(data):
    mean = 0
    elsquare = 0
    for el in data:
        elsquare += float(el)**2
        mean += float(el)
    mean = mean/len(data)
    elsquare = elsquare/len(data)
    stddev = np.sqrt(elsquare - mean**2)
    return stddev

def lowpasshard(amp, sampling, fcut):                                                                       
    fft = np.fft.rfft(amp)                                                                                  
    freq = np.fft.rfftfreq(len(fft),float(1./sampling))                                                     
    Nyfreq = sampling/2                                                                                     
    min = np.min(np.absolute(fft))                                                                          
    ratiofcut = float(fcut)/Nyfreq                                                                          
    size = len(fft)                                                                                         
    newpass = fft[:int(ratiofcut*size)]                                                                     
    sizeofzeros = size - len(newpass)                                                                       
    newcut = np.zeros(sizeofzeros)                                                                          
    newfft = np.append(newpass,newcut)                                                                      
    out = np.fft.irfft(newfft)                                                                              
    return out.real                                                                                         

###############################################
#### conversion function (voltage to adc, #####
#### voltage FE to voltage board etc... ) #####
###############################################

#adc counts to volt at the FE input (between 0-1V)
def adctov_fe(adc):
    return float(adc)/1024
def npadctov_fe(adc):
    return np.asarray(adc,dtype=float)/1024

def v_fetoadc(vfe):
    return float(vfe)*1024
def npv_fetoadc(vfe):
    return np.asarray(vfe,dtype=float)*1024

#voltage at front end to voltage at GIGAS/EASIER board
def v_fetov_board(vfe):
    return vfe*(-2)
def v_boardtov_fe(vboard):
    return vboard*(-1/2)

#adc to v board (between -2 and 0 V)
def adctov_board(adc):
    return v_fetov_board(adctov_fe(adc))
def npadctov_board(adc):
    return v_fetov_board(npadctov_fe(adc))
def v_boardtoadc(vboard):
    return v_fetoadc(v_boardtov_fe(vboard))

#vboard to power
def vboardtopdbm(vboard):
    const = -30 
    pdbm = const -10.4*(2+vboard)
    return pdbm

def pdbmtopwatt(pdbm):
    return np.power(10,pdbm/10)

def adctopwatt(adc):
    vboard = npadctov_board(adc)
    pdbm = vboardtopdbm(vboard)
    pwatt = pdbmtopwatt(pdbm)
    return pwatt


################################
### easier array definition  ###
################################
easier7 = [332,333,341,342,343,344,419]
easier47 = [306, 308, 315, 328, 334, 403, 408, 425, 434, 354, 125, 199, 300, 307, 310, 311, 356, 375, 394, 405, 410, 121, 196, 197, 201, 296, 305, 312, 319, 325, 329, 337, 340, 376, 386, 387, 390, 396, 412, 429, 438, 441, 1802]
gigaduck = [433, 422, 431, 385, 384, 427, 432]
helix = [339, 313, 340, 329, 330, 334, 328]

#######
# special function to make an index a double index for plotting reason
def splitintwocol(i,col):
    index1 = int(i/col)
    index2 = i%col
    return [index1,index2]
