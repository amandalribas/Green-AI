import pandas as pd

dataframe = pd.read_csv('data02.csv')
print(f"{dataframe}\n")

dataframe['profit'] = dataframe['profit'].apply(lambda x:x>0)
print(f"{dataframe}\n")

#merge 2 dataframes
dt0 = pd.read_csv('data03.csv')
dt1 = pd.read_csv('data04.csv')
print(f"{dt0}\n")
print(f"{dt1}\n")
dt = pd.merge(dt0,dt1)
print(f"{dt}\n")

#dt = pd.merge(dt0,dt1, how='inner', on= 'eid')
#print(f"{dt}\n")
print(dt.info())
print()
print(dt.describe())