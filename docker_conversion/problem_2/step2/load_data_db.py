import pandas as pd
import psycopg2

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="mftestdb",
    user="admin",
    password="root"
)

# Create a cursor object to interact with the database
cur = conn.cursor()

# Read the Excel file into a pandas DataFrame
file_path = "docker_conversion\problem_2\step2\data\outputfile.xlsx"
df = pd.read_excel(file_path)

# Convert DataFrame column names to a list
columns = list(df.columns)

# Create a placeholder query template
placeholder_query = ", ".join(["%s"] * len(columns))

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    values = tuple(row[columns].values)
    insert_query = f"INSERT INTO mf_sec8_integrated ({', '.join(columns)}) VALUES ({placeholder_query});"
    cur.execute(insert_query, values)

# Commit the changes and close the connection
conn.commit()
conn.close()
