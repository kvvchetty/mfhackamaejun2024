import pandas as pd

# Define file paths and the common column name
file1 = "property_file.xlsx"
file2 = "section8.xlsx"
common_column = "property_id"  # Replace with the actual column name

# Read excel files into DataFrames
df1 = pd.read_excel(file1)
df2 = pd.read_excel(file2)

# Perform the merge based on the common column
merged_df = df1.merge(df2, on=common_column, how="outer")

# Save the merged DataFrame to a new excel file (optional)
merged_df.to_excel("merged_property_data.xlsx", index=False)

print("Excel files merged successfully!")