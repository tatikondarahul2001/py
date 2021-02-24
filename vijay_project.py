import pandas as pd

csv_file = pd.read_csv('tmdb-movies.csv')

#print(csv_file)

#1
pivot = df_all.groupby(['Shift']).mean()
shift_productivity = pivot.loc[:,"budget":"original_title"]
print(shift_productivity)