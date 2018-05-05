from SampleExtracter import SampleExtracter
from FileLoader import FileLoader
from Preprocessor import Preprocessor
from Classifier import Classifier

import cv2
fileLoader = FileLoader("data/orginal", "data/result")
if __name__ =="__main__":
    files = []
    for f in fileLoader.getFilePairs():
        files+=f
    sampleExtracter = SampleExtracter(files[0],files[1],10)
    samples =  sampleExtracter.getSamples()
    p = Preprocessor(samples)
    samples = p.getTrainingData()
    c =Classifier(samples[:10000],10)


    image = cv2.imread("data/orginal/im0001.jpg",0)
    output = c.extractBloodVessels2(image,True)
    print(output)
    cv2.imshow("input", image)
    cv2.imshow("output",output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
