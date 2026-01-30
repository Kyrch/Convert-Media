import subprocess
import sys


def convert_image():
    input_file = sys.argv[1]
    format = input("Choose a format to convert (e.g. jpg, png): ")
    output_file = input_file.split('.')[0] + "." + format
    command = f'ffmpeg -i "{input_file}" "{output_file}"'
    subprocess.call(command, shell=True)

convert_image()