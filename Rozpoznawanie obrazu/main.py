from SampleExtracter import SampleExtracter
from FileLoader import FileLoader
from Preprocessor import Preprocessor
from Classifier import Classifier
import cv2
from os import listdir
from KCK import KCK
from os import listdir
from os.path import isfile, join
from sklearn.metrics import confusion_matrix
import pandas as pd
import numpy as np

def train():
    fileLoader = FileLoader("data/orginal", "data/result")
    files =  fileLoader.getFilePairs()
    samples = []
    print("Sample extracting")
    for file in files:
        sampleExtracter = SampleExtracter(file[0],file[1],10)
        samples+=sampleExtracter.getSamples()
    print("Preprocessing")
    p = Preprocessor(samples)
    samples = p.getTrainingData()
    c =Classifier(samples[:100000],10)


def test():
    c = Classifier(None, 10)
    image = cv2.imread("data/orginal/im0002.jpg",0)
    output = c.extractBloodVessels2(image,True)
    cv2.imshow("input", image)
    cv2.imshow("output",output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def compareToModel(prediction, model):
    conf = confusion_matrix(prediction.flatten(), model.flatten())
    #print(conf)
    #print(pd.crosstab(prediction.flatten(),model.flatten(),  rownames=['Predicted'], colnames=['True'], margins=True))
    sensitivity = conf[1][1] / (conf[1][1] + conf[0][1])
    precision = conf[1][1] / (conf[1][1] + conf[1][0])
    accuracy = (conf[1][1] + conf[0][0]) / np.sum(conf)
    print("sensitivity: " + str(sensitivity))
    print("precision: " + str(precision))
    print("accuracy: " + str(accuracy))
    return conf, sensitivity, precision, accuracy
    pass

def calculate(resultPaths, labeledPaths):
    sensitivity, precision, accuracy, i = 0, 0, 0, 0

    for result, label in zip(resultPaths, labeledPaths):
        resultImage = cv2.imread(result, cv2.IMREAD_GRAYSCALE)
        labeledImage =cv2.imread(label, cv2.IMREAD_GRAYSCALE)
        resultImage[resultImage >= 150] = 255
        resultImage[resultImage < 150] = 0
        labeledImage[labeledImage >= 150] = 255
        labeledImage[labeledImage < 150] = 0
        _, sen, pre, acc = compareToModel(resultImage, labeledImage)
        sensitivity += sen
        precision += pre
        accuracy += acc
        i += 1

    print(i)

    print("sensitivity: " + str(sensitivity/i))
    print("precision: " + str(precision/i))
    print("accuracy: " + str(accuracy/i))

def drawOnOriginal(resultPath, KCKPath):
    samplePath = "data/orginal"
    outputKCK = "onKCK"
    outputResults = "onResults"
    for result, kck, f in zip(resultPath, KCKPath, listdir(samplePath)):
        if isfile(join(samplePath, f)):
            resultImg = cv2.imread(result, cv2.IMREAD_GRAYSCALE)
            KCKImg = cv2.imread(kck, cv2.IMREAD_GRAYSCALE)
            image = cv2.imread(samplePath + "/" + f)
            image2 = np.copy(image)
            image[resultImg==255] = [255, 255, 255]
            image2[KCKImg == 255] = [255, 255, 255]
            cv2.imwrite(outputKCK + "/" + f, image2)
            cv2.imwrite(outputResults + "/" + f, image)


def calculations():
    #c = Classifier(None, 10)
    #dir = "data/orginal"
    #for f in listdir(dir):
    #    image = cv2.imread(dir+"/"+f, 0)
    #    output = c.extractBloodVessels2(image, True)
    #    cv2.imwrite("results/"+f,output)

    resultPath = "results"
    labeledPath = "data/result"
    KCKPath  = "KCK"

    #KCK().writeImagesToFile(KCKPath)

    resultPaths = [resultPath + "/" +f for f in listdir(resultPath) if isfile(join(resultPath, f))]
    KCKPaths = [KCKPath + "/" +f for f in listdir(KCKPath) if isfile(join(KCKPath, f))]
    labeledPaths = [labeledPath + "/" +f for f in listdir(labeledPath) if isfile(join(labeledPath, f))]

    #calculate(resultPaths, labeledPaths)
    #calculate(KCKPaths, labeledPaths)

    drawOnOriginal(resultPaths, KCKPaths)

if __name__ =="__main__":
    calculations()
