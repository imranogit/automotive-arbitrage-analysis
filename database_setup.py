import sqlite3

def create_database():
    # Connect to a database (or create it if it doesn't exist)
    conn = sqlite3.connect('parts_data.db')
    cursor = conn.cursor()

    # Create a table for specific Car Parts
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS parts (
        id INTEGER PRIMARY KEY,
        part_number TEXT UNIQUE,
        part_name TEXT,
        compatible_cars TEXT
    )
    ''')

    # Create a table for Price Observations
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS prices (
        id INTEGER PRIMARY KEY,
        part_id INTEGER,
        source_country TEXT, -- 'DE' or 'UAE'
        price_eur REAL,      -- Converted to Euro for comparison
        url TEXT,
        date_observed DATE,
        FOREIGN KEY(part_id) REFERENCES parts(id)
    )
    ''')

    conn.commit()
    conn.close()
    print("Database initialized successfully.")

if __name__ == "__main__":
    create_database()