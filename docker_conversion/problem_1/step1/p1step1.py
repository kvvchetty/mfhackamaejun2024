import pandas as pd
import sys
import os

if __name__ == "__main__":

  # Check if two arguments are provided
  if len(sys.argv) != 3:
    print("Error: Please provide the Excel file name and output file name as arguments.")
    sys.exit(1)

  # Access arguments
  filein_path = sys.argv[1]
  fileout_path = sys.argv[2]
  excel_file_path = os.path.join("/app/input", filein_path)  # Replace with actual filename
  # Get the output file path (if needed)
  output_file_path = os.path.join("/app/output", fileout_path)  # Replace with desired filename

  print('Reading data from:', excel_file_path)
  print('Writing data to:', output_file_path)
  

  # Read the data from the excel file
  df = pd.read_excel(excel_file_path, dtype=str)

  # ... rest of your code remains the same ...

  # Specify the column names to combine
  column_1 = 'ZIP'  # Replace with your actual column name
  column_2 = 'BLOCK'  # Replace with your actual column name
  column_3 = 'LOT'  # Replace with your actual column name

  # Create a new column by combining the existing columns
  df['KEY_COL1'] = df[column_1].astype(str) + df[column_2].astype(str) + df[column_3].astype(str)

  # Save the DataFrame to the output file (specify desired format)
  df.to_excel(output_file_path, index=False)

  print('New column created and saved to:', output_file_path)
