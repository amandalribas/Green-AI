import pandas as pd


dataframe = pd.read_csv('data01.csv')
print(f"{dataframe}\n")


dataframe_averange = dataframe['salary'].mean() #media de salarios

print(f"{dataframe_averange}\n")

dataframe_averange = dataframe.groupby('occ')['salary'].mean()
print(f"{dataframe_averange}\n")

#onde nao tem nada fica NaN
#substituindo Nan por 0

dataframe_nullfill = dataframe.fillna(0)
print(f"{dataframe_nullfill}\n")
