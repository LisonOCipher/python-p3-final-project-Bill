import sqlite3

# Establish a connection to the SQLite database
conn = sqlite3.connect('art_gallery.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''CREATE TABLE IF NOT EXISTS customers (
                    name TEXT PRIMARY KEY,
                    age INTEGER,
                    email TEXT,
                    address TEXT
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS pieces (
                    piece_name TEXT PRIMARY KEY,
                    company_id INTEGER,
                    category_of_piece TEXT,
                    price INTEGER,
                    FOREIGN KEY(company_id) REFERENCES companies(id)
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS companies (
                    id INTEGER PRIMARY KEY,
                    company_name TEXT,
                    location TEXT,
                    established_year INTEGER
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS comments (
                    comment_text TEXT PRIMARY KEY,
                    piece_name TEXT,
                    FOREIGN KEY(piece_name) REFERENCES pieces(piece_name)
                )''')

# Commit changes and close connection
conn.commit()
conn.close()
