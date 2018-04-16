from SampleExtracter import SampleExtracter
from FileLoader import FileLoader
from Preprocessor import Preprocessor
from Classifier import Classifier
fileLoader = FileLoader("data/orginal", "data/result")
if __name__ =="__main__":
    files = []
    for f in fileLoader.getFilePairs():
        files+=f
    sampleExtracter = SampleExtracter(f[0],f[1],10)
    samples =  sampleExtracter.getSamples()
    p = Preprocessor(samples)
    samples = p.getTrainingData()
    c =Classifier(samples[:7000])
