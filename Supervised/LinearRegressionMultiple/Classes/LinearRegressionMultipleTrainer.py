import pandas as pd
import scipy as sp

class LinearRegressionMultipleTrainer:
     def __init__(self, data: pd.DataFrame):
        self.data = data 
        self.betas = []
        self.alpha = 0
        self.xs = []
        self.y = ""

     def get_yhat(self, alpha, betas):
        value = alpha
        for index, beta in enumerate(betas):
            property = self.xs[index]
            value += self.data[property]*beta
        return value
         
     
     def get_errors(self, alpha, betas):
        y_hat =  self.get_yhat(alpha, betas)
        return y_hat - self.data[self.y]
     
     def get_square_errors(self, alpha, betas):
        errors = self.get_errors(alpha, betas)
        return errors**2

     def constraint_error_zero(self, params):
        alpha = params[0]

        betas = [params[index+1] for index, value in enumerate(self.xs)]
        return self.get_errors(alpha, betas).sum()
     
     def minimizer(self, params):
        alpha = params[0]
        betas = [params[index+1] for index, value in enumerate(self.xs)]
        return  self.get_square_errors(alpha, betas).sum()


     def fit(self, y, xs):
         self.xs = xs
         self.y = y
         con1 = {'type': 'eq', 'fun': self.constraint_error_zero }
         answer = sp.optimize.minimize(self.minimizer, (0, 0, 0), constraints=[con1])
         self.alpha = answer.x[0]
         self.betas = [answer.x[index + 1] for index, value in enumerate(self.xs)]
         return answer
     
     def get_r_squared(self):
        errors_square = self.get_square_errors(self.alpha, self.betas)
        sum_of_squares = (self.data[self.y]-self.data[self.y].mean())**2
        total_sum_of_squares = sum_of_squares.sum()
    
        return 1 - (errors_square.sum()/total_sum_of_squares)

     def predict_y(self, xs):
        value = self.alpha
        for index, beta in enumerate(self.betas):
            x = xs[index]
            value += x*beta
        return value
     
     def predict_y_list(self, xs_array):
        return [self.predict_y(xs) for xs in xs_array]
     
     def get_parameters(self):
        return [self.alpha, self.betas]
