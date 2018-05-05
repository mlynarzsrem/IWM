import math
from random import shuffle,sample
import numpy as np
class Preprocessor:
    def __init__(self,samples):
        self.samples =samples
        self.positive =[s for s in samples if s.getDecisiom()==1]
        self.negative = [s for s in samples if s.getDecisiom() == 0]
        if(len(self.positive)==0 or  len(self.negative)==0):
            raise "Wrong data"
    def getTrainingData(self):
        minSet = min(len(self.positive),len(self.negative))
        positive = sample(self.positive,minSet)
        negative =sample(self.negative,minSet)
        allData =positive + negative
        return sample(allData,len(allData))
