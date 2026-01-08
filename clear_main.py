import sqlite3
from datetime import datetime

DB_PATH = "weighing_scales.db"

def clear_maintenance_records():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Check if logs table exists
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='maintenance_records';")
    if not c.fetchone():
        print("❌ 'maintenance_records' table does not exist in the database.")
        conn.close()
        return

    # Count existing logs before deletion
    c.execute("SELECT COUNT(*) FROM maintenance_records;")
    count = c.fetchone()[0]

    if count == 0:
        print("✅ No record to clear. The table is already empty.")
        conn.close()
        return

    # Delete all logs
    c.execute("DELETE FROM maintenance_records;")
    conn.commit()
    conn.close()

    print(f"🗑️  Successfully cleared {count} maintenance_records entries at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    clear_maintenance_records()
