import sys
sys.path.append('C:/Users/Joao/Desktop/Remote/ML_Algorithms')

from Classes.ML_Model import ML_Model


class K_Nearest_Neighbors(ML_Model):

    model = None

    def __init__(self, K):
        self.K = K

    def train(self, X_train, y_train):
        self.model = "oii"

        return (X_train, y_train)
    
    def predict(self, X_prediction):
        print(self.model)
        return X_prediction
    

alou = K_Nearest_Neighbors(K=5)
alou.predict(2)
alou.train(2, 3)
isso = alou.predict(5)
        