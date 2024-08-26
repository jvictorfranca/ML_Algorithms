import pandas as pd
import scipy as sp

class LinearRegressionTrainer:
     def __init__(self, data: pd.DataFrame):
        self.data = data 
        self.beta = 0
        self.alpha = 0
        self.x = ""
        self.y = ""

     def get_yhat(self, alpha, beta):
        return alpha + self.data[self.x]*beta
     
     def get_errors(self, alpha, beta):
        y_hat =  self.get_yhat(alpha, beta)
        return y_hat - self.data[self.y]
     
     def get_square_errors(self, alpha, beta):
        errors = self.get_errors(alpha, beta)
        return errors**2

     def constraint_error_zero(self, params):
        alpha, beta = params
        return self.get_errors(alpha, beta).sum()
     
     def minimizer(self, params):
        alpha, beta = params
        return  self.get_square_errors(alpha, beta).sum()


     def fit(self, x, y):
         self.x = x
         self.y = y
         con1 = {'type': 'eq', 'fun': self.constraint_error_zero }
         answer = sp.optimize.minimize(self.minimizer, (0,0), constraints=[con1])
         self.alpha = answer.x[0]
         self.beta = answer.x[1]
         return answer
     
     def get_r_squared(self):
        errors_square = self.get_square_errors(self.alpha, self.beta)
        sum_of_squares = (self.data[self.y]-self.data[self.y].mean())**2
        total_sum_of_squares = sum_of_squares.sum()
    
        return 1 - (errors_square.sum()/total_sum_of_squares)

     def predict_y(self, x):
        return self.alpha + x*self.beta
     
     def predict_y_list(self, x_array):
        return [self.predict_y(x) for x in x_array]
     
     def get_parameters(self):
        return [self.alpha, self.beta]
