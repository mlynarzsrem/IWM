import numpy as np
import pickle
import os.path
import cv2
from keras.models import Sequential
from keras.layers import Dense,Flatten,Conv2D,MaxPooling2D,Conv1D,MaxPooling1D,Dropout
from sklearn.model_selection import KFold, cross_val_score
class Classifier:
    def __init__(self,dataSets,size):
        self.size = size
        self.dataSets =dataSets
        self.createModel()
        self.trainModel()
    def createModel(self):
        dShape = self.size*2+1
        self.model = Sequential()
        self.model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(dShape, dShape, 3)))
        self.model.add(Conv2D(32, (3, 3), activation='relu'))
        self.model.add(MaxPooling2D(pool_size=(2, 2)))
        self.model.add(Dropout(0.25))

        self.model.add(Conv2D(64, (3, 3), activation='relu'))
        self.model.add(Conv2D(64, (3, 3), activation='relu'))
        self.model.add(MaxPooling2D(pool_size=(2, 2)))
        self.model.add(Dropout(0.25))

        self.model.add(Flatten())
        self.model.add(Dense(256, activation='relu'))
        self.model.add(Dropout(0.5))

        self.model.add(Dense(1, activation='softmax'))
        self.model.compile(loss="binary_crossentropy",optimizer="sgd",metrics=['accuracy'])
    def trainModel(self):
        print("ok")
        data = self.convertData([s.getData() for s in self.dataSets])
        labels = np.asarray([s.getDecisiom() for s in self.dataSets])
        k_fold = KFold(n_splits=5)
        scores= []
        for train, test in k_fold.split(data):
            self.model.fit(data[train],labels[train],batch_size=len(train),epochs=1)
            score =self.model.evaluate(data[test],labels[test],batch_size=len(test))
            scores.append(scores)
            pass
        print(scores)
    def extractBloodVessels(self,inputImage,online=False):
        x,y =inputImage.shape
        s = 2 * self.size + 1
        outputImage = np.zeros((x,y))
        for i in range(x):
            for j in range(y):
                data = np.zeros((s,s,3))
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
                data =self.convertData([data])
                score = self.model.predict(data)
                outputImage[i,j]=score*255
        return outputImage
    def convertData(self,data):
        dShape = self.size * 2 + 1
        score =[]
        for img in data:
            if(img.shape==(dShape,dShape,3)):
                score.append(img)
        return np.array(score)


