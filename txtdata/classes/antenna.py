#import utils
import numpy as np

class Antenna:
    def __init__(self, id = 0
                 ):
        self.id = id
        self.radiotrace = np.array([])
        self.vemtrace = np.array([])

