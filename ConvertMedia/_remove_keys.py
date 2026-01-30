import winreg
import subprocess


class UninstallKey:
    def __init__(self):
        UninstallKey.remove_context_menu(self, "video")
        UninstallKey.remove_context_menu(self, "image")
        UninstallKey.remove_context_menu_to_video_formats(self)

    def remove_context_menu(self, type: str):
        key_path = rf"Software\Classes\SystemFileAssociations\{type}\shell\ConvertImage"

        try:
            winreg.DeleteKey(winreg.HKEY_CURRENT_USER, key_path + r"\Command")
            winreg.DeleteKey(winreg.HKEY_CURRENT_USER, key_path)

            subprocess.call(["ie4uinit.exe", "-show"])

            print(f"Keys removed for {type}")

        except FileNotFoundError:
            pass

    def remove_context_menu_to_video_formats(self):
        formats = [
            ".webm",
            ".mp4",
            ".mkv",
            ".mov",
            ".avi",
            ".wmv",
            ".avchd",
            ".flv",
            ".f4v",
            ".swf",
            ".m2ts",
        ]

        for format in formats:
            key_path = (
                rf"Software\Classes\SystemFileAssociations\{format}\shell\ConvertVideo"
            )

            try:
                winreg.DeleteKey(winreg.HKEY_CURRENT_USER, key_path + r"\Command")
                winreg.DeleteKey(winreg.HKEY_CURRENT_USER, key_path)
            except FileNotFoundError:
                pass

        subprocess.call(["ie4uinit.exe", "-show"])

        print("Keys removed for videos")


if __name__ == "__main__":
    UninstallKey()
