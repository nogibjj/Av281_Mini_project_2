import pandas as pd

def PDdescribe(filename):
    '''function which returns descriptive stats about input data'''
    df = pd.read_csv(filename)
    return df.describe()
