import psycopg2
import os

# Get environment variables for database connection
SOURCE_DB_HOST = os.getenv("SOURCE_DB_HOST")
SOURCE_DB_USER = os.getenv("SOURCE_DB_USER")
SOURCE_DB_PASSWORD = os.getenv("SOURCE_DB_PASSWORD")
SOURCE_DB_NAME = os.getenv("SOURCE_DB_NAME")

TARGET_DB_HOST = os.getenv("TARGET_DB_HOST")
TARGET_DB_USER = os.getenv("TARGET_DB_USER")
TARGET_DB_PASSWORD = os.getenv("TARGET_DB_PASSWORD")
TARGET_DB_NAME = os.getenv("TARGET_DB_NAME")

# Connect to source database
source_conn = psycopg2.connect(
    host=SOURCE_DB_HOST,
    user=SOURCE_DB_USER,
    password=SOURCE_DB_PASSWORD,
    dbname=SOURCE_DB_NAME
)
source_cursor = source_conn.cursor()

# Fetch data from the source database
source_cursor.execute("SELECT * FROM claim_table_count WHERE status='active';")
records = source_cursor.fetchall()

#Connect to target database
target_conn = psycopg2.connect(
    host=TARGET_DB_HOST,
    user=TARGET_DB_USER,
    password=TARGET_DB_PASSWORD,
    dbname=TARGET_DB_NAME
)
target_cursor = target_conn.cursor()

# Insert data into the target table
for record in records:
    target_cursor.execute("""
        INSERT INTO claims_table_details (table_name, database_name, loaded_date, record_count)
        VALUES (%s, %s, %s, %s);
    """, (record[0], record[1], record[2], record[3]))

# Commit and close connections
target_conn.commit()
source_cursor.close()
source_conn.close()
target_cursor.close()
target_conn.close()

print(f"Successfully transferred {len(records)} records.")
