import csv
import os
import re
import pdfplumber
import pandas as pd

from pdfplumber.utils import extract_text, get_bbox_overlap, obj_to_bbox

pdf = pdfplumber.open("2022-DHCR-Manhattan.pdf")

page = pdf.pages[0]

filtered_page = page
chars = filtered_page.chars

for table in page.find_tables():
    first_table_char = page.crop(table.bbox).chars[0]

    filtered_page = filtered_page.filter(lambda obj: 
        get_bbox_overlap(obj_to_bbox(obj), table.bbox) is None
    )

    chars = filtered_page.chars

    df = pd.DataFrame(table.extract())
    df.columns = df.iloc[0]

    markdown = df.drop(0).to_markdown(index=False)

    for i, markdown_line in enumerate(markdown.split("\n")):
        new_attrs = {
            "text": markdown_line,
            "doctop": first_table_char["doctop"] + first_table_char["height"] * i,
        }
        chars.append(first_table_char | new_attrs)

#================================================

if os.path.exists('output.csv'):
    os.remove('output.csv')
    print("Existing 'output.csv' removed.")

table_content = extract_text(chars, layout=True)
# Define a regular expression to capture all columns (modify if needed)
pattern = r"[-;,.\s]\s*"
all_columns = [re.split(pattern, row) for row in table_content.splitlines()]


try:
# Open the CSV file in write mode with 'newline='' for proper handling
    with open('output.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        for row in all_columns:
            # Combine first and last two columns using list indexing
            bbl = f"{row[0]}{row[-2]}{row[-1]}"
            row.append(bbl)
            writer.writerow(row)
    print(f"CSV data written to output.csv.")
except IOError as e:
    print(f"Error writing to file: {e}")
  
#===================End of file ==========================