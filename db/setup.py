import sqlite3

def setup():
    conn = sqlite3.connect("soundscape.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS songs (
            id INTEGER PRIMARY KEY,
            title TEXT,
            artist TEXT,
            user_id INTEGER,
            duration INTEGER,
            FOREIGN KEY(user_id) REFERENCES users(id)
        );
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup()
