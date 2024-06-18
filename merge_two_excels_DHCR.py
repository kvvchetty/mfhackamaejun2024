import pandas as pd

# Replace file paths with your actual file paths
file1_path = '2022 DHCR Citywide.xlsx'
file2_path = 'renstab_counts_from_doffer_2021_upd.xlsx'

# Read the data from both excel files
df1 = pd.read_excel(file1_path, dtype=str)
df2 = pd.read_excel(file2_path, dtype=str)
left_on = 'KEY_COL1'  # Column in file_one (df1)
right_on = 'ucbbl'  # Column in file_two (df2)

# Select the two desired columns from the second file
df2_selected = df2[['ucbbl', 'uc2021']]  # Replace 'col1' and 'col2' with desired column names

# Perform the merge operation based on the common column
merged_df = df1.merge(df2_selected, left_on=left_on, right_on=right_on, how='left')

# Save the merged DataFrame to a new excel file (optional)
merged_df.to_excel('merged_data.xlsx', index=False)

print('Files merged successfully!')
