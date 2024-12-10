import pandas as pd
import glob

file_pattern = '*_Keystone_Exam_School_Level_Data_cleaned.csv'
files = glob.glob(file_pattern)

print(files)
dataframes = []
for file in files:
   df = pd.read_csv(file)
   
   df.rename(columns={
      'Student_Group_Name': 'Group',
      'Group': 'Group',  # Ensure consistent naming
      'N Scored': 'Number Scored',
      'Pct. Advanced': 'Percent Advanced',
      'Pct. Proficient': 'Percent Proficient',
      'Pct. Basic': 'Percent Basic',
      'Pct. Below Basic': 'Percent Below Basic',
      '% Advanced': 'Percent Advanced',
      '% Proficient': 'Percent Proficient',
      '% Basic': 'Percent Basic',
      '% Below Basic': 'Percent Below Basic'
   }, inplace=True)
   
   dataframes.append(df)

merged_data = pd.concat(dataframes, ignore_index=True)

merged_data.to_csv('merged_keystone_exam_data_2015_2023.csv', index=False)

print("Merged data saved to 'merged_keystone_exam_data_2015_2023.csv'")