import pandas as pd

def PDdescribe(filename):
    '''function which returns descriptive stats about input data'''
    df = pd.read_csv(filename)
    return df.describe()

print(PDescribe('nba.csv'))

nba = pd.read_csv('nba.csv')
nba.plot(kind = 'scatter', x = 'Height', y = 'Weight')
plt.show()
