
import os
import pandas as pd
import glob
import openpyxl
import numpy as np
import matplotlib.pyplot as plt
import re

cwd = os.getcwd()
folder_path = cwd
#print(cwd)

directory = os.listdir('.')
#print(directory)

for filename in glob.glob(os.path.join(folder_path, '*.xlsx')):
    df = pd.read_excel(filename)
    a = df.head()
    #print(df.head(0))
    b = list(df.head(0))
    matrix = np.array(b)
    #print(matrix)
    timeseries = []
    for i in matrix:
        row = np.array(pd.Series(df[i]))
        timeseries.append(row)

X = np.array(timeseries)
#print(X)
print(X.shape)

lv = []
for n in range(X.shape[0]):
    last_value = X[n,(X.shape[1]-1)]
    lv.append(last_value)

Y = []
for row in range(X.shape[0]):
    parametrized_row = X[row]-lv[row]
    new_row =np.array(parametrized_row)
    #print(parametrized_row)
    #print(row)
    Y.append(new_row)

Yfinal = np.array(Y)
print(Yfinal)

for l in range(Yfinal.shape[0]):
    plt.plot(Yfinal[l])
    plt.show()
    print(l)



