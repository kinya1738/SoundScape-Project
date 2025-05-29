from models.song import Song
from collections import Counter

def show_user_report(user_id):
    songs = Song.get_by_user(user_id)
    if not songs:
        print("No songs found.")
        return

    print("\nYour Songs This Week:")
    total_time = 0
    artist_list = []

    for title, artist, duration in songs:
        print(f"{title} by {artist} - {duration} min")
        total_time += duration
        artist_list.append(artist)

    print(f"\nTotal Listening Time: {total_time} minutes")

    if artist_list:
        most_common = Counter(artist_list).most_common(1)[0]
        print(f"Favorite Artist of the Week: {most_common[0]} ({most_common[1]} songs)")
