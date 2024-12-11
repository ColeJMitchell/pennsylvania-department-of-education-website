import pandas as pd
import glob

input_directory = "*.csv"
output_file = "school_fiscal_merged.csv"

dataframes = []

for file_path in glob.glob(input_directory):
    print(f"Processing file: {file_path}")
    
    data = pd.read_csv(file_path)

    wide_data = data.pivot_table(
        index=["SchoolName", "AcademicYearId"],
        columns="DataElement",
        values="DisplayValue",
        aggfunc="first"
    )
    
    wide_data = wide_data.reset_index()
    
    wide_data = wide_data.fillna(0)
    
    wide_data.columns.name = None
    wide_data = wide_data.rename(columns={
        "Federal - Personnel": "Federal-Personnel",
        "Federal - Non-Personnel": "Federal-Non-Personnel",
        "State - Personnel": "State-Personnel",
        "State - Non-Personnel": "State-Non-Personnel",
        "Local - Personnel": "Local-Personnel",
        "Local - Non-Personnel": "Local-Non-Personnel",
    })
    
    dataframes.append(wide_data)

final_data = pd.concat(dataframes, ignore_index=True)

final_data.to_csv(output_file, index=False)

print(f"Consolidated data saved to {output_file}")
