import os
import sys
import pandas as pd
  
def merge_excel_files(input_file1, input_file2, output_file, common_column = "property_id"):
    """
    Merges data from two Excel files based on a common column.

    Args:
        input_file1 (str): Path to the first Excel file.
        input_file2 (str): Path to the second Excel file.
        output_file (str): Path to save the merged data as an Excel file.
        left_on (str, optional): Column name in the first file for merging. Defaults to 'property_id'.
        right_on (str, optional): Column name in the second file for merging. Defaults to 'property_id'.
    """

    # Read the data from both Excel files
    df1 = pd.read_excel(input_file1, dtype=str)
    df2 = pd.read_excel(input_file2, dtype=str)

    # Perform the merge operation
    merged_df = df1.merge(df2, on=common_column, how="outer")

    # Save the merged DataFrame to a new excel file
    merged_df.to_excel(output_file, index=False)

    print(f'Files merged successfully! Output saved to: {output_file}')  
    

if __name__ == "__main__":
  # Check if two arguments are provided
  if len(sys.argv) != 4:
    print("Error: Please provide the Excel file name and output file name as arguments.")
    sys.exit(1)

  # Access arguments
  in_file1 = sys.argv[1]
  in_file2 = sys.argv[2]
  out_file = sys.argv[3]
   
  input_file1 = os.path.join("/app/input", in_file1)  # Replace with actual filename
  input_file2 = os.path.join("/app/input", in_file2)  # Replace with actual filename
  # Get the output file path
  output_file = os.path.join("/app/output", out_file)  # Replace with desired filename

  print('Reading data from:', input_file1)
  print('Reading data from:', input_file2)
  print('Writing data to:', output_file)
  
  # Call the function with arguments (modify these during runtime)
  merge_excel_files(input_file1, input_file2, output_file)
