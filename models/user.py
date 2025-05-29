from models.session import get_connection

class User:
    def __init__(self, username):
        self.username = username

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username) VALUES (?)", (self.username,))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, username FROM users")
        users = cursor.fetchall()
        conn.close()
        return users
