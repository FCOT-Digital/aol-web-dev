from sqlite3 import connect

connection = connect("17_resource_my_database.db")
cursor = connection.cursor()

# Create presentations table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS presentations (
        join_code TEXT PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT
    )
''')

# Create participants table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS participants (
        email TEXT PRIMARY KEY,
        show_name TEXT NOT NULL
    )
''')

# Create comments table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS comments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        lesson TEXT NOT NULL,
        participant TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        comment_text TEXT NOT NULL,
        FOREIGN KEY (lesson) REFERENCES presentations(join_code),
        FOREIGN KEY (participant) REFERENCES participants(email)
    )
''')

connection.commit()
connection.close()
