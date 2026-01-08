import sqlite3
from datetime import datetime

DB_PATH = "weighing_scales.db"

def clear_renewal_history():
    """Delete all records from logs table safely."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Check if logs table exists
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='renewal_history';")
    if not c.fetchone():
        print("❌ 'Renewal History' table does not exist in the database.")
        conn.close()
        return

    # Count existing logs before deletion
    c.execute("SELECT COUNT(*) FROM renewal_history;")
    count = c.fetchone()[0]

    if count == 0:
        print("✅ No history to clear. The table is already empty.")
        conn.close()
        return

    # Delete all logs
    c.execute("DELETE FROM renewal_history;")
    conn.commit()
    conn.close()

    print(f"🗑️  Successfully cleared {count} history entries at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    clear_renewal_history()
