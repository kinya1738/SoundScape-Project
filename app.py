from models.user import User
from models.song import Song
from report import show_user_report

def main():
    print(" Welcome to SoundScape ")
    print("1. Create a user")
    print("2. View all users")
    print("3. Add a song")
    print("4. View weekly report")
    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter your username: ")
        user = User(name)
        user.save()
        print("User created!")
 
    elif choice == "2":
        users = User.get_all()
        for user in users:
            print(f"{user[0]}: {user[1]}")

    elif choice == "3":
        user_id = int(input("Enter your user ID: "))
        title = input("Song title: ")
        artist = input("Artist name: ")
        duration = int(input("Duration in minutes: "))
        song = Song(title, artist, user_id, duration)
        song.save()
        print("Song added!")

    elif choice == "4":
        user_id = int(input("Enter your user ID: "))
        show_user_report(user_id)

if __name__ == "__main__":
    main()


