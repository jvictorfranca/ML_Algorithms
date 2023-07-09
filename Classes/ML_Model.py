from abc import ABC, abstractmethod

class ML_Model(ABC):

    @abstractmethod
    def __init__(self, param):
        self.param = param
        pass

    
    @property
    @abstractmethod
    def model(self):
        pass
    

    @abstractmethod
    def train(self, X_train, y_train):
        pass
    
    @abstractmethod
    def predict(self, X_prediction):
        pass

