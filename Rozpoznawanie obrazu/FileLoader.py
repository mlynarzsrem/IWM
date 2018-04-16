from os import listdir
from os.path import isfile, join

class FileLoader:
    def __init__(self,orgImgPath,resImgPath):
        self.orgImgPath = orgImgPath
        self.resImgPath =resImgPath
        self.orgImgs = [f for f in listdir(orgImgPath) if isfile(join(orgImgPath, f))]
        self.resImgs = [f for f in listdir(resImgPath) if isfile(join(resImgPath, f))]
        self.filePairs = []
        self.prepareFiles()
    def prepareFiles(self):
        for i in range(len(self.orgImgs)):
            oImg= self.orgImgs[i]
            try:
                rImgIdx = self.resImgs.index(oImg)
                rImg = self.resImgs[rImgIdx]
                pair = (join(self.orgImgPath, oImg),join(self.resImgPath, rImg))
                self.filePairs.append(pair)
            except:
                pass
    def getFilePairs(self):
        return self.filePairs