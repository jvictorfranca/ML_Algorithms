import pandas as pd

from Classes.LinearRegressionTrainer import LinearRegressionTrainer

sheet = pd.read_excel("Supervised\LinearRegression\sheet.xlsx")

trainer = LinearRegressionTrainer(sheet)

trainer.fit("X", "Y")
print(trainer.alpha, trainer.beta)
print(trainer.get_r_squared())
print(trainer.predict_y([1, 3, 4]))