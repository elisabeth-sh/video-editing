import moviepy.editor as mp


# This is a mini-project that allows you to experiment with video files

# The first function allows the user to turn videos into mp3 files

def video_to_audio():
    # Entering the path
    url = input("Enter the path of the video\n")

    # Extracting the name of the file from the path
    words = url.split("\\")
    name = words[-1].split(".")

    # Converting the file
    clip = mp.VideoFileClip(url)
    audio = clip.audio.write_audiofile(f"{name[0]}.mp3")
    return audio


# The second function allows the user to create mini-clips from existing videos
def subclip():
    # Entering the path
    url = input("Enter the path of the video\n")

    # Identifying the video using the path
    clip = mp.VideoFileClip(url)

    # Extracting the name of the file from the path
    words = url.split("\\")
    name = words[-1].split(".")

    # Setting the duration of the subclip
    start = input("When does the subclip start? Enter the second\n")
    end = input("When does the subclip end? Enter the second\n")
    segment = clip.subclip(start, end)

    # Getting the subclip
    segment.write_videofile(f"{name[0]}_segment.mp4")
    return segment


# The function below allows the user to make screenshots and turn them to png files
def screen():
    # Entering the path
    url = input("Enter the path of the video\n")

    # Identifying the video
    clip = mp.VideoFileClip(url)

    # Choosing when to make a screenshot and giving it a title
    t = input("When should the programme make a screenshot?\n")
    name = input("How should the png file be named?\n")

    # Getting the screenshot
    picture = clip.save_frame(f"{name}.png", t)
    return picture


# Interacting with the user
intro = input("What would you like to do today: 1. Turn your video to an audio file, "
              "2. Create a subclip of your video, 3. Make a screenshot\n")

# Activating the functions based on user input

# If the user chooses "1", the first function will be launched

# The same applies to the other functions

if intro == "1":
    video_to_audio()

elif intro == "2":
    subclip()

elif intro == "3":
    screen()
