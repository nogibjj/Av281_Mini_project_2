import pandas as pd

def PDdescribe(data):
	df = pd.DataFrame(data)
	return df.describe()