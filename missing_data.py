# Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Taking care of missing data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'median', axis = 0)
imputer = imputer.fit(X[:, 1:3])
imputer.statistics_
X[:, 1:3] = imputer.transform(X[:, 1:3])

dataset.isnull().any(axis=1)
nullDF = dataset[dataset.isnull().any(axis=1)]

dataset['Age'] = dataset['Age'].fillna(dataset['Age'].mean())

dataset.isnull().any(axis=1)


