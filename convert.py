from moviepy.editor import *
import os

# for file name not have "."


def change_ext_name(name):
    return name.split(".")[0] + ".mp3"


all_files = [f for f in os.listdir('.') if os.path.isfile(f)]

for mp4_file in all_files:
    if(".mp4" not in mp4_file):
        continue
    mp3_file = change_ext_name(mp4_file)
    videoclip = VideoFileClip(mp4_file)
    audioclip = videoclip.audio
    audioclip.write_audiofile(mp3_file)
    audioclip.close()
    videoclip.close()
