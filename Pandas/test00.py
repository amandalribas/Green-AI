import pandas as pd

#print(pd.__version__)
given_list = [2, 4, 5, 6, 9]
#series = pd.Series(given_list)
#print(series) #index   elemento

series = pd.Series(given_list, index = [1,2,6,7,8])
print(series)


#date_series = pd.date_range(start="07-20-2025", end="07-31-2025") #mes-dia-ano
#print(date_series) #output: ano-mes-dia
"""
series = pd.Series([2,4,5,6,9])
print(f"{series}\n")

modified_series = series.apply(lambda x:x/2)
print(f"{modified_series}\n")
"""
"""
dict = {'name': ['Amanda', 'Lais'], 'age':[20,19]}
dict_dataframe = pd.DataFrame(dict)
print(dict)
print(dict_dataframe)"""


lists = [[2,"Amanda", 20], [1,"Madu",19], [3,"Lais",18]]
lists_dataframe = pd.DataFrame(lists, columns=['id', 'name', 'age'])
print(lists_dataframe)

