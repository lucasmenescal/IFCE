import pandas as pd
iris = pd.read_csv("iris.csv")
iris.head()

X = iris.iloc[:, 0:4].values