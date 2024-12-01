import pandas as pd


file_path = "/home/cole/github/pennsylvania-department-of-education-app/district_relation_data/district.csv"  # Replace with the actual path to your CSV file
df = pd.read_csv(file_path, sep="\t", header=None)


df.columns = ['School District', 'Attribute', 'Value']

df = df.drop_duplicates(subset=['School District', 'Attribute'])
df_pivoted = df.pivot(index='School District', columns='Attribute', values='Value').reset_index()


df_pivoted = df_pivoted.sort_values(by='School District')
output_file = "district_transformed_sorted.csv"
df_pivoted.to_csv(output_file, index=False)
print(df_pivoted.head())

