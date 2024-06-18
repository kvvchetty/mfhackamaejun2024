import pandas as pd

# Replace 'your_file.xlsx' with the path to your actual excel file
file_path = '2022 DHCR Citywide.xlsx'

# Read the data from the excel file
df = pd.read_excel(file_path, dtype=str)

# Specify the column names to combine
column_1 = 'ZIP'  # Replace with your actual column name
column_2 = 'BLOCK'  # Replace with your actual column name
column_3 = 'LOT'  # Replace with your actual column name

# Create a new column by combining the existing columns
df['KEY_COL1'] = df[column_1].astype(str) + df[column_2].astype(str) + df[column_3].astype(str)

# Save the DataFrame back to the excel file (overwrites the existing file)
df.to_excel(file_path, index=False)

print('New column created and added to Excel file!')
