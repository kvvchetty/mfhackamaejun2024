
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
    ref_File_Name = "ref_p1s2.xlsx"
    
    print(s3_File_Name)
    print(ref_File_Name)
    print(s3_Bucket_Name)

    s3_client.download_file(s3_Bucket_Name, s3_File_Name, '/tmp/data.xlsx')  # Download to a temporary location
    s3_client.download_file(s3_Bucket_Name, ref_File_Name, '/tmp/ref.xlsx')  # Download to a temporary location
  except Exception as e:
    print(f"Error downloading file: {e}")
    return {
      'statusCode': 500,
      'body': json.dumps('Error downloading file')
    }
  

  try:
    file1_path = '/tmp/data.xlsx'
    file2_path = '/tmp/ref.xlsx'
    
    merged_file_name = 'merged_data.xlsx'

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
    merged_df.to_excel('/tmp/merged_data.xlsx', index=False)
    
    print('Files merged successfully!')


    # # Upload the modified file back to S3 (optional)
    # s3_client.upload_file(file_path, s3_Bucket_Name, merged_file_name)  # Upload back to S3
    
    
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
