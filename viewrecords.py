import sqlite3

db_path = "weighing_scales.db"
conn = sqlite3.connect(db_path)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

# Check all scales with their supermarket_id and branch_id
cursor.execute("SELECT id, serial_number, supermarket_id, branch_id FROM weighing_scales")
rows = cursor.fetchall()

for row in rows:
    print(f"Scale ID: {row['id']}, Serial: {row['serial_number']}, Supermarket ID: {row['supermarket_id']}, Branch ID: {row['branch_id']}")

conn.close()
