
import json
import boto3
import io
import pandas as pd
# import psycopg2

s3_client = boto3.client('s3')

def lambda_handler(event, context):
  try:
    s3_Bucket_Name = event["Records"][0]["s3"]["bucket"]["name"]
    s3_File_Name = event["Records"][0]["s3"]["object"]["key"]
    
    print(s3_File_Name)
    print(s3_Bucket_Name)

    s3_client.download_file(s3_Bucket_Name, s3_File_Name, '/tmp/data.xlsx')  # Download to a temporary location
  except Exception as e:
    print(f"Error downloading file: {e}")
    return {
      'statusCode': 500,
      'body': json.dumps('Error downloading file')
    }
  

  try:
    file_path = '/tmp/data.xlsx'
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

    # Upload the modified file back to S3 (optional)
    s3_client.upload_file(file_path, s3_Bucket_Name, s3_File_Name)  # Upload back to S3
    
    
#---------------------    
    # # Connect to PostgreSQL database
    # # Replace placeholders with your actual connection details
    # dbname = "your_database_name"
    # dbuser = "your_username"
    # dbpassword = "your_password"
    # dbhost = "your_host"
    # dbport = "your_port"

    # conn = psycopg2.connect(dbname=dbname, user=dbuser, password=dbpassword, host=dbhost, port=dbport)
    # cur = conn.cursor()

    # # Define the table name and columns for insertion
    # table_name = "your_table_name"
    # columns = ", ".join(df.columns.tolist())

    # # Prepare SQL statement for inserting data using list comprehension
    # insert_stmt = f"""INSERT INTO {table_name} ({columns}) VALUES (%s)"""
    # data = df.values.tolist()
    # cur.executemany(insert_stmt, data)

    # # Commit the changes
    # conn.commit()
    # cur.close()
    # conn.close()

#----------------------    

  except Exception as e:
    print(f"Error processing data: {e}")
    return {
      'statusCode': 500,
      'body': json.dumps('Error processing data')
    }


  # Success message
  return {
    'statusCode': 200,
    'body': json.dumps('New column created and added to Excel file!')
  }
