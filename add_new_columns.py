import sqlite3

DB_PATH = "weighing_scales.db"

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

try:
    cur.execute("ALTER TABLE weighing_scales ADD COLUMN wintec_sdk TEXT;")
    conn.commit()
    print("✅ Columns 'wintec_sdk' added successfully.")
except sqlite3.OperationalError as e:
    print("⚠️", e)
finally:
    conn.close()
