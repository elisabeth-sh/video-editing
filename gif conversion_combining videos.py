#importing the right modules
from moviepy.editor import *


# A function that will make gif files from mp4 files
def gif_converter():
    path = input("Enter the path of the video\n")
    start = input("When should the programme start recording the gif file? Enter the second\n")
    finish = input("When should the programme stop recording the gif file? Enter the second\n")
    title = input("Enter the title of the gif file\n")
    video = VideoFileClip(path).subclip(start, finish)
    video.write_gif(f"{title}.gif")

#A function that will combine several mp4 or gif files into one mp4 file
def concatenation():
    path1 = input("Enter the path of the first video\n")
    path2 = input("Enter the path of the second video\n")
    clip1 = VideoFileClip(path1)
    clip2 = VideoFileClip(path2)
    result = concatenate_videoclips([clip1, clip2])
    fork = input("Do you want to add another clip? y/n\n")
    if fork == "y":
        path3 = input("Enter the path of the video?\n")
        clip = VideoFileClip(path3)
        result = concatenate_videoclips([result, clip])
        title = input("Enter the title of the file\n")
        result.write_videofile(f"{title}.mp4")
    else:
        title = input("Enter the title of the file\n")
        result.write_videofile(f"{title}.mp4")

