import pandas as pd
import matplotlib as plt
import numpy as np

df1 = pd.read_csv("C:\winequality-red.csv")
df2 = pd.read_csv("C:\winequality-white.csv")

df.head()

missing_data = df.isnull()
missing_data.head()
