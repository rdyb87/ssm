import sqlite3
import os

conn = sqlite3.connect(r'C:\Users\RCS\Desktop\ssm\weighing_scale.db')
print("Using DB file:", os.path.abspath('weighing_scales.db'))

cursor = conn.cursor()

# List all tables in main schema
cursor.execute("SELECT name, type FROM sqlite_master WHERE type IN ('table','view');")
tables = cursor.fetchall()
print("Tables in main schema:", tables)

# List temporary tables
cursor.execute("SELECT name, type FROM sqlite_temp_master WHERE type IN ('table','view');")
temp_tables = cursor.fetchall()
print("Temporary tables:", temp_tables)

conn.close()
