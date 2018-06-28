import os
import pandas as pd

data = pd.read_table('tennis.txt', header=None)
data = data.drop(0)
print(data)
