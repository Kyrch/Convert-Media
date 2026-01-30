from _seek import Seek

import subprocess
import sys


def convert_video():
    input_file = sys.argv[1]

    format = input("Choose a format to convert (e.g. mp4, webm): ")

    while True:
        ss = input("Choose the start point to cut: ")
        if not Seek.validate(ss):
            print("Invalidated time")
            continue
        break

    while True:
        to = input("Choose the end point to cut: ")
        if not Seek.validate(to):
            print("Invalidated time")
            continue
        break

    seek = Seek(input_file, ss, to)
    output_file = input_file.split('.')[0] + "." + format

    command = f'ffmpeg {seek.get_seek_string()} "{output_file}"'

    subprocess.call(command, shell=True)

convert_video()