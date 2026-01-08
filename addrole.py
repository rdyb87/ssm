import sqlite3
import os

DB_PATH = "weighing_scales.db"  # <-- change to your actual database path if different

def update_user_table():
    if not os.path.exists(DB_PATH):
        print(f"❌ Database file not found: {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        # ✅ Step 1: Detect existing columns safely
        cursor.execute("PRAGMA table_info(users);")
        columns = cursor.fetchall()
        if not columns:
            print("❌ No 'users' table found in the database.")
            return

        col_names = [col[1] for col in columns]
        print("🔍 Existing columns:", col_names)

        # ✅ Step 2: Backup old table
        cursor.execute("ALTER TABLE users RENAME TO users_old;")

        # ✅ Step 3: Create new table (with new CHECK constraint)
        cursor.execute("""
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                role TEXT CHECK(role IN ('admin', 'technician', 'support')) NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            );
        """)

        # ✅ Step 4: Copy only matching columns
        # (ignore missing ones to prevent mismatch errors)
        old_cols = [col for col in col_names if col in ('id', 'username', 'password', 'role', 'created_at')]
        col_list = ", ".join(old_cols)

        cursor.execute(f"INSERT INTO users ({col_list}) SELECT {col_list} FROM users_old;")

        # ✅ Step 5: Drop old table
        cursor.execute("DROP TABLE users_old;")

        conn.commit()
        print("✅ Table updated successfully. Role 'support' is now allowed.")
    except sqlite3.Error as e:
        print(f"❌ SQLite error: {e}")
        conn.rollback()
    except Exception as e:
        print(f"❌ Python error: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    update_user_table()
