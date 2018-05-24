from matplotlib import pyplot as plt
import cv2
import math
import numpy as np
import random
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix
from os.path import isfile, join
from os import listdir

class KCK:
    def __init__(self, dataSets):
        #self.dataSets = dataSets
        #self.samples = np.copy(self.__convertData([s.getData() for s in dataSets]))
        pass

    def __init__(self):
        pass

    def process(self):
        myLabels = self.__predict()
        labels = []
        for sample in self.dataSets:
            labels.append(sample.getDecisiom())
        print(confusion_matrix(labels, myLabels))

    def __predict(self):
        sample = self.samples
        color = np.copy(self.samples)
        #for sample in self.samples:
        #plt.imshow(sample, cmap='gray', interpolation='bicubic')
        #plt.show()
        bloodVessels = []
        bloodVessels = self.__contours(bloodVessels, sample)
        for i in range(len(bloodVessels)):
            bloodVessels[i] = cv2.morphologyEx(bloodVessels[i], cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))
            sth1, contour, sth2 = cv2.findContours(bloodVessels[i], cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for j in range(len(contour)):
                cv2.drawContours(bloodVessels[i], contour, j, (255, 255, 255), cv2.FILLED)
        betterEdges = []
        betterEdges = self.__contours(betterEdges, bloodVessels)

        coords = [0, 0, 0]

        for i in range(len(betterEdges)):
            betterEdges[i] = cv2.morphologyEx(betterEdges[i], cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))
            sth1, contour, sth2 = cv2.findContours(betterEdges[i], cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for j in range(len(contour)):
                if (contour[j].size < 200):
                    continue
                M = cv2.moments(contour[j])
                randomColor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255));
                cv2.drawContours(color[i], contour, j, randomColor, thickness=3)
                cv2.circle(color[i], (int(M['m10'] / M['m00']), int(M['m01'] / M['m00'])), 5, randomColor, -1)

        resultLabels = []

        for col, sample in zip(color, self.samples):
            plt.imshow(sample, cmap='gray', interpolation='bicubic')
            plt.show()
            kmeans = KMeans(n_clusters=2, random_state=0).fit(col.flatten().reshape(-1, 1))
            labels = kmeans.labels_.reshape(col.shape)
            if(np.mean(col[labels==0]) > np.mean(col[labels == 1])):
                col[labels==0] = 0
                col[labels == 1] = 255
            else:
                col[labels==0] = 255
                col[labels == 1] = 0
            plt.imshow(col, cmap='gray', interpolation='bicubic')
            plt.show()
            label = col[int(col.shape[0]/2)][int(col.shape[1]/2)]
            resultLabels.append(label/255)
        return resultLabels

    def __convertData(self,data):
        xShape =len(data)
        yShape = data[0].shape[0]
        zeros =np.zeros((xShape,int(math.sqrt(yShape)), int(math.sqrt(yShape))), dtype = np.uint8)
        for i in range(xShape):
            part = data[i]
            zeros[i] = part.reshape(int(math.sqrt(yShape)), int(math.sqrt(yShape)))
        return zeros

    def __contours(self, bloodVessels, vessels):
        for i in range(len(vessels)):
            std = np.std(vessels[i])
            maskSize = 30
            for row in range(len(vessels[i])):
                for col in range(len(vessels[i][row])):
                    if(vessels[i][row][col] > 150):
                        try:
                            vessels[i][row][col] = np.mean(vessels[i][row-maskSize:row+maskSize+1,col-maskSize:col+maskSize+1])
                        except:
                            pass
            maskSize = 15
            for row in range(len(vessels[i])):
                for col in range(len(vessels[i][row])):
                    if(vessels[i][row][col] > 130):
                        try:
                            vessels[i][row][col] = np.mean(vessels[i][row-maskSize:row+maskSize+1,col-maskSize:col+maskSize+1])
                        except:
                            pass
            v = np.median(vessels[i])
            bloodVessels.append(cv2.Canny(vessels[i], 10, 60))
        return bloodVessels

    def oneFullImage(self, image):
        sample = [image]
        color = np.copy(sample)

        bloodVessels = []
        bloodVessels = self.__contours(bloodVessels, sample)


        for i in range(len(bloodVessels)):
            kernel = np.ones((3, 3), np.uint8)
            bloodVessels[i] = cv2.morphologyEx(bloodVessels[i], cv2.MORPH_CLOSE, np.ones((5,5), np.uint8))
            bloodVessels[i] = cv2.dilate(bloodVessels[i], kernel, iterations=2)

        return bloodVessels[i]

    def writeImagesToFile(self, outputPath):
        samplePath = "data/orginal"
        for f in listdir(samplePath):
            if isfile(join(samplePath, f)):
                image = cv2.imread(samplePath + "/" + f)[:, :, 1]
                processedImage = self.oneFullImage(image)
                cv2.imwrite(outputPath + "/" + f, processedImage)
