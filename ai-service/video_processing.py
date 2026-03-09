#convert the input videos into mp3

#os
#Used to interact with the operating system
#Here, it’s used to list files in a folder

#subprocess
# Used to run external programs (like commands you type in the terminal)
# In this case, it runs FFmpeg, a video/audio processing tool
# Think of subprocess as:
# “Python telling your computer: run this terminal command for me.” */

import os
import subprocess

files = os.listdir("short-sample-videos")
for file in files:
    name = file.split(".")[0]
    subprocess.run(["ffmpeg","-i",f"short-sample-videos/{file}",f'audios/{name}.mp3'])

# #"ffmpeg"
# The program being executed
# Must be installed and available in your system PATH

# "-i"
# Means input file

# f"short-sample-videos/{file}"
# The input video file

# f"audios/{name}.mp3"
# Output file


# FFmpeg automatically:
# Extracts audio from the video
# Converts it to MP3
# For each video, Python:
# Calls FFmpeg
# FFmpeg extracts the audio
# Saves it as .mp3 in the audios folder