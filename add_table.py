import sqlite3

# Connect to your existing SQLite database
conn = sqlite3.connect('weighing_scales.db')
cursor = conn.cursor()

# Create the renewal_history table
cursor.execute('''
CREATE TABLE IF NOT EXISTS renewal_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    scale_id INTEGER NOT NULL,
    old_expiry_date DATE NOT NULL,
    new_expiry_date DATE NOT NULL,
    renewed_by TEXT,
    renewal_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    FOREIGN KEY (scale_id) REFERENCES scales(id) ON DELETE CASCADE
)
''')

# Create indexes
cursor.execute('CREATE INDEX IF NOT EXISTS idx_scale_id ON renewal_history(scale_id)')
cursor.execute('CREATE INDEX IF NOT EXISTS idx_renewal_date ON renewal_history(renewal_date)')

# Commit changes and close connection
conn.commit()
conn.close()

print("Table 'renewal_history' created successfully with indexes.")
