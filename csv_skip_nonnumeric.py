import csv

# Replace 'data.txt' with the path to your actual CSV file
def process_csv_skip_non_numeric(file_path):
  try:
    # Open the CSV file in read mode
    with open(file_path, 'r') as csvfile:
      reader = csv.reader(csvfile)

      # Skip header row (if present)
      next(reader, None)  # Discard header if it exists

      # Process valid rows (replace with your desired processing logic)
      for row in reader:
        if row[0].isdigit():  # Check if first element is a digit
          # Example: Print the row
          print(', '.join(row))

  except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")

# Example usage
process_csv_skip_non_numeric('output.csv')
