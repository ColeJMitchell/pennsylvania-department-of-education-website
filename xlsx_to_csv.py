import os
import pandas as pd

output_folder = "../csv_data"

if not os.path.exists(output_folder):
      os.makedirs(output_folder)
      
os.chdir("data")

# Collect all xlsx files
xlsx_files = [f for f in os.listdir('.') if f.endswith('.xlsx')]

# Convert
for xlsx_file in xlsx_files:
    df = pd.read_excel(xlsx_file)
    
    csv_file = f"{output_folder}/{os.path.splitext(xlsx_file)[0]}.csv"
    
    df.to_csv(csv_file, index=False)
    
# Lots of warnings are generated. I believe due to formatting issues...