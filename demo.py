# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 20:11:20 2019

@author: sandy
"""

import pandas as pd
data = pd.read_csv(r"C:\Users\sandy\Dropbox\Part 0 - Self_practice\titanic\dataset\train.csv")
data.head(5)
data.info()
sum(data.isnull())