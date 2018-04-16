import numpy as np
class Sample:
    def __init__(self,data,dectison):
        self.data = data
        self.decysion = dectison
    def getData(self):
        return self.data
    def getDecisiom(self):
        return self.decysion
    def __str__(self):
        return str((self.data,self.decysion))