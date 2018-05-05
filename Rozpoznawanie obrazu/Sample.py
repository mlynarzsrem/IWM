import numpy as np
class Sample:
    def __init__(self,data,decision):
        self.data = data
        self.decision = decision
    def getData(self):
        return self.data
    def getDecisiom(self):
        return self.decision
    def __str__(self):
        return str((self.data,self.decision))