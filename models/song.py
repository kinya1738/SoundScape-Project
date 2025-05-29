from models.session import get_connection

class Song:
    def __init__(self, title, artist, user_id, duration):
        self.title = title
        self.artist = artist
        self.user_id = user_id
        self.duration = duration

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO songs (title, artist, user_id, duration) VALUES (?, ?, ?, ?)",
            (self.title, self.artist, self.user_id, self.duration)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def get_by_user(user_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT title, artist, duration FROM songs WHERE user_id = ?", (user_id,))
        songs = cursor.fetchall()
        conn.close()
        return songs
