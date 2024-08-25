import pandas as pd
import scipy as sp



class linearRegressionTrainer:
     def __init__(self, data: pd.DataFrame):
        self.data = data 
        self.beta = 0
        self.alpha = 0
        self.x = ""
        self.y = ""

     def get_yhat(self, alpha, beta):
        return alpha + self.df[self.x]*beta
     
     def get_errors(self, alpha, beta):
        y_hat =  self.get_yhat(self.df,self.x, self.y, alpha, beta)
        return y_hat - self.df[self.y]
     
     def get_square_errors(self, alpha, beta):
        errors = self.get_errors(alpha, beta)
        return errors**2

     def constraint_error_zero(self, params):
        alpha, beta = params
        return self.get_errors(alpha, beta).sum()
     
     def minimizer(self, params):
        alpha, beta = params
        return  self, self.get_square_errors(alpha, beta).sum()


     def fit(self, x, y):
         self.x = x
         self.y = y
         con1 = {'type': 'eq', 'fun': self.constraint_error_zero }
         answer = sp.optimize.minimize(self.minimizer, (0,0), constraints=[con1])
         return answer
     
     def get_r_squared(self):
        errors_square = self.get_square_errors(self.alpha, self.beta)
        sum_of_squares = (self.df[self.y]-self.df[self.y].mean())**2
        total_sum_of_squares = sum_of_squares.sum()
    
        return 1 - (errors_square.sum()/total_sum_of_squares)

     def predict_yhat(self):
        return self.alpha + self.df[self.x]*self.beta
