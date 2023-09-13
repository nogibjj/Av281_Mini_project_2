import pandas as pd
import matplotlib.pyplot as plt

def PDdescribe(filename):
    '''function which returns descriptive stats about input data'''
    df = pd.read_csv(filename)
    return df.describe()

results = PDdescribe('nba.csv')

print(results)

nba = pd.read_csv('nba.csv')
nba.plot(kind = 'scatter', x = 'Height', y = 'Weight')
plt.show()
