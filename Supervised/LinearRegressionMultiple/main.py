import pandas as pd

from Classes.LinearRegressionMultipleTrainer import LinearRegressionMultipleTrainer

sheet = pd.read_excel("Supervised\LinearRegressionMultiple\sheet D3.xlsx")

trainer = LinearRegressionMultipleTrainer(sheet)

trainer.fit("Y", ["X1", "X2"])
print(trainer.alpha, trainer.betas)
print(trainer.get_errors(trainer.alpha, trainer.betas).sum())
print(trainer.get_r_squared())
print(trainer.predict_y([5,1]))
print(trainer.predict_y_list([[1,1], [3,6], [4,2]]))  

