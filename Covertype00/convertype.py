import pandas as pd
import numpy as np



names = ["Elevation", "Aspect", "Slope", "Horizontal_Distance_To_Hydrology", "Vertical_Distance_To_Hydrology", "Horizontal_Distance_To_Roadways", "Hillshade_9am", "Hillshade_Noon", "Hillshade_3pm", "Horizontal_Distance_To_Fire_Points"]
names += [f"Wilderness_Area_{i}" for i in range(4)]
names += [f"Soil_Type_{i}" for i in range(40)]
names += ["Cover_Type"]


dataframe = pd.read_csv("covtype.data", header=None, names=names)

wilderness_columns = [col for col in dataframe.columns if col.startswith('Wilderness_Area')]
wilderness_classes = []
for _, row in dataframe.iterrows():
    for col in wilderness_columns:
        if row[col] == 1:
            wilderness_classes.append(int(col.split('_')[-1]))
            break
dataframe.drop(columns=wilderness_columns, inplace=True)
dataframe.insert(len(dataframe.columns)-1, 'Wilderness_Area', wilderness_classes)


soil_type_columns = [col for col in dataframe.columns if col.startswith('Soil_Type')]
soil_type_classes = []
for _, row in dataframe.iterrows():
    for col in soil_type_columns:
        if row[col] == 1:
            soil_type_classes.append(int(col.split('_')[-1]))
            break
dataframe.drop(columns=soil_type_columns, inplace=True)
dataframe.insert(len(dataframe.columns)-1, 'Soil_Type', soil_type_classes)

#Printando 10 primeiros e 10 ultimos
#print(dataframe.head(10))
#print(dataframe.iloc[:10,:])

#print(dataframe.iloc[-10:,:])
#print(dataframe.tail(10))

#print(dataframe) #Printando dataframe total

#print(dataframe.describe())
x = dataframe.drop(columns="Cover_Type")
y = dataframe["Cover_Type"]


cover_types =  ["Spruce/Fir", "Lodgepole Pine", "Ponderosa Pine", "Cottonwood/Willow", "Aspen", "Douglas-fir", "Krummholz"]

y_named = y.apply(lambda v: cover_types[v - 1])
print(y_named)
#print(y_named.value_counts())

#print(np.unique(dataframe["Cover_Type"], return_counts=True))

print(x)