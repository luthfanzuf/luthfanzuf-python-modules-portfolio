import pandas as pd

df = pd.read_csv('./combined_csv.csv')

filtered_df = df[df.isnull()]

print(filtered_df)
print(df.isnull().sum())

#delete blank or empty row
df1 = df.dropna(
   axis=0,
   how='any'
)

df2 = df1[df1.iloc[:, 0] != df1.columns[0]]

df2.to_csv('combined_csv_without_blank.csv', index=False, encoding='utf-8-sig')