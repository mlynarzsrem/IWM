from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

import numpy as np
from sklearn.model_selection import KFold, cross_val_score
class Classifier:
    def __init__(self,dataSets):
        self.dataSets =dataSets
        #self.model = DecisionTreeClassifier(max_depth=5)
        self.model =RandomForestClassifier()
        self.trainModel()

    def trainModel(self):
        print("ok")
        data = self.convertData([s.getData() for s in self.dataSets])
        labels = np.asarray([s.getDecisiom() for s in self.dataSets])
        k_fold = KFold(n_splits=5)
        scores = [self.model.fit(data[train], labels[train]).score(data[test], labels[test]) for train, test in k_fold.split(data)]
        print(scores)
    def convertData(self,data):
        xShape =len(data)
        yShape = data[0].shape[0]
        zeros =np.zeros((xShape,yShape))
        for i in range(xShape):
            part = data[i]
            for j in range(yShape):
                zeros[i,j]= part[j]
        return zeros



