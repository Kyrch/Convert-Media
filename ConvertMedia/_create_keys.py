import winreg
import subprocess
import sys
import os


class RegisterKey:
    def __init__(self):
        self.video_command = RegisterKey.create_video_command()
        self.image_command = RegisterKey.create_image_command()
        RegisterKey.create_context_menu(self)
        RegisterKey.add_context_menu_to_video_formats(self)
        RegisterKey.add_context_menu_to_image(self)

    def create_video_command():
        python_path = os.path.dirname(sys.executable) + '\python.exe'
        script_path = os.path.dirname(os.path.abspath(__file__)) + '\_convert_video.py'
        command = f'"{python_path}" "{script_path}" "%1"'

        return command
    
    def create_image_command():
        python_path = os.path.dirname(sys.executable) + '\python.exe'
        script_path = os.path.dirname(os.path.abspath(__file__)) + '\_convert_image.py'
        command = f'"{python_path}" "{script_path}" "%1"'

        return command

    def create_context_menu(self):
        key_path = r"Software\Classes\SystemFileAssociations\video\shell\ConvertVideo\Command"
        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path)

        winreg.SetValueEx(key, "", 0, winreg.REG_SZ, self.video_command)
        winreg.CloseKey(key)

        subprocess.call(["ie4uinit.exe", "-show"])

    def add_context_menu_to_video_formats(self):
        formats = ['.webm', '.mp4', '.mkv', '.mov', '.avi', '.wmv', '.avchd', '.flv', '.f4v', '.swf', '.m2ts']

        for format in formats:
            key_path = fr"Software\Classes\SystemFileAssociations\{format}\shell\ConvertVideo\Command"
            key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path)

            winreg.SetValueEx(key, "", 0, winreg.REG_SZ, self.video_command)
            winreg.CloseKey(key)

        subprocess.call(["ie4uinit.exe", "-show"])

        print('Keys created for videos')

    def add_context_menu_to_image(self):
        key_path = r"Software\Classes\SystemFileAssociations\image\shell\ConvertImage\Command"
        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path)

        winreg.SetValueEx(key, "", 0, winreg.REG_SZ, self.image_command)
        winreg.CloseKey(key)

        subprocess.call(["ie4uinit.exe", "-show"])

        print('Keys created for images')

if __name__ == "__main__":
    RegisterKey()