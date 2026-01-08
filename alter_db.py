import sqlite3

db_path = "weighing_scales.db"  # adjust if your file has another name
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Column to add
column_name = "is_active"
column_type = "INTEGER DEFAULT 1"  # 1 = active, 0 = disabled

# Check existing columns in USER table (not logs)
cursor.execute("PRAGMA table_info(user);")
existing_columns = [col[1] for col in cursor.fetchall()]

# Add only if missing
if column_name not in existing_columns:
    cursor.execute(f"ALTER TABLE users ADD COLUMN {column_name} {column_type};")
    print(f"✅ Added column '{column_name}' to 'user' table with DEFAULT 1 (active)")
else:
    print(f"ℹ️ Column '{column_name}' already exists in 'user' table")

conn.commit()
conn.close()
print("✅ Database update completed successfully!")