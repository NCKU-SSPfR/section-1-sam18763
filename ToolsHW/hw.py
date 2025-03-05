import webbrowser

def play_video():
    """Opens the specified video link."""
    video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    webbrowser.open(video_url)

def main():
    """Asks the user a math question and plays a video if answered correctly."""
    while True:
        user_input = input("1 times 1 = ? ")
        if user_input.strip() == "1":
            play_video()
            break
        elif user_input.lower() == "exit":
            print("Exiting program.")
            break
        else:
            print("Wrong! Try again.")

if __name__ == "__main__":
    main()
