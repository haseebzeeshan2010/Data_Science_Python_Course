import pandas as pd
csv_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv'
df = pd.read_csv(csv_path)

#print(df.loc[0, 'Artist']) finding specific element
#print(df.iloc[0:2, 0:3]) slicing dataframe
print(df.loc[0:2, 'Artist':'Released']) 