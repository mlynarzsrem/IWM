import cv2
from Sample import Sample
import numpy as np
class SampleExtracter:
    def __init__(self,orginalImageFilename,resultImageFilename,maskSize):
        self.orginalImage =cv2.imread(orginalImageFilename,0)#llast param 0
        self.resultImage = cv2.imread(resultImageFilename,-1)
        self.resultImage[self.resultImage>50]=255
        self.resultImage[self.resultImage <= 50] = 0
        self.resultImage=self.resultImage//255
        if(self.orginalImage is None or self.resultImage is None):
            raise "Non existing files error!"
        self.maskSize = maskSize
        self.samples = []
        self.makeSamples()

    def makeSamples(self):
        height,width = self.orginalImage.shape
        sizeOst= (2*self.maskSize +1)*(2*self.maskSize +1)
        for i in range(height):
            for j in range(width):

                data = self.orginalImage[i-self.maskSize:i+self.maskSize+1,j-self.maskSize:j+self.maskSize+1]
                data = data.flatten()
                decision = self.resultImage[i,j]
                if(data.shape[0]==sizeOst):
                    self.samples.append(Sample(data,decision))
                else:
                    lenght =  data.shape[0]
                    diff = sizeOst - lenght
                    data =np.append(np.zeros(diff) ,data)
                    if (data.shape[0] == sizeOst):
                        self.samples.append(Sample(data, decision))

    def getSamples(self):
        return self.samples