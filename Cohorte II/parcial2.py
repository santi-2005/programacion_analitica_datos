import pandas as pd
import matplotlib as plt
import numpy as np

df = pd.read_csv("C:\winequality-red.csv")

df.head()

missing_data = df.isnull()
missing_data.head()
