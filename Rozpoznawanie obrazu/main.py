from SampleExtracter import SampleExtracter
from FileLoader import FileLoader
from Preprocessor import Preprocessor
from Classifier import Classifier
import cv2
from os import listdir
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
def calculations():
    c = Classifier(None, 10)
    dir = "data/orginal"
    for f in listdir(dir):
        image = cv2.imread(dir+"/"+f, 0)
        output = c.extractBloodVessels2(image, True)
        cv2.imwrite("results/"+f,output)

if __name__ =="__main__":
    calculations()
