from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pickle
import os.path
import cv2
from sklearn.model_selection import KFold, cross_val_score
class Classifier:
    def __init__(self,dataSets,size):
        self.size = size
        self.dataSets =dataSets
        #self.model = DecisionTreeClassifier(max_depth=5)
        self.model =RandomForestClassifier()
        if(os.path.isfile("model.dat")):
            self.model =pickle.load(open("model.dat", 'rb'))
        else:
            self.trainModel()

    def trainModel(self):
        print("ok")
        data = self.convertData([s.getData() for s in self.dataSets])
        labels = np.asarray([s.getDecisiom() for s in self.dataSets])
        k_fold = KFold(n_splits=5)
        scores = [self.model.fit(data[train], labels[train]).score(data[test], labels[test]) for train, test in k_fold.split(data)]
        print(scores)
        pickle.dump(self.model, open("model.dat", 'wb'))
    def extractBloodVessels(self,inputImage,online=False):
        x,y =inputImage.shape
        s = 2 * self.size + 1
        outputImage = np.zeros((x,y))
        for i in range(x):
            for j in range(y):
                data = np.zeros((s,s))
                try:
                    frame=inputImage[i-self.size:i+self.size+1,j-self.size:j+self.size+1]
                    if(frame.shape==data.shape):
                        data =frame
                    else:
                        x1,y1 =frame.shape
                        for i1 in range(x1):
                            for j1 in range(y1):
                                data[i1,j1] =frame[i1,j1]
                except:
                   pass
                data =data.flatten()
                data=data.reshape(1,-1)
                score = self.model.predict(data)
                outputImage[i,j]=score*255
                if(online==True):
                    cv2.imshow("output", outputImage)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
        return outputImage

    def getScore(self,cord):
        x = int(cord[0])
        y = int(cord[1])
        sizeOst = (2 * self.size + 1) * (2 * self.size + 1)
        try:
            frame = self.inputImage[x - self.size:x + self.size + 1, y - self.size:y + self.size + 1].flatten()
            if (frame.shape[0] == sizeOst):
                data = frame
            else:
                lenght = frame.shape[0]
                diff = sizeOst - lenght
                data = np.append(np.zeros(diff), frame).flatten()
        except:
            return 0
        data = data.reshape(1, -1)
        score = self.model.predict(data)
        #print(data)
        #print(score)
        return score * 255
    def extractBloodVessels2(self, inputImage, online=False):
        print("Start ")
        self.inputImage = inputImage
        x, y = inputImage.shape
        cords =np.empty(shape=(x,y),dtype='2f')
        for i in range(x):
            for j in range(y):
                cords[i,j]=tuple((i,j))
        listOfRows = []
        for row in cords:
            listOfRows.append(np.array(list(map(self.getScore,row))))
        return np.array(listOfRows)
    def convertData(self,data):
        xShape =len(data)
        yShape = data[0].shape[0]
        zeros =np.zeros((xShape,yShape))
        for i in range(xShape):
            part = data[i]
            for j in range(yShape):
                zeros[i,j]= part[j]
        return zeros



