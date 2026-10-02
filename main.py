import os
import os.path
import subprocess
from playsound3 import playsound

class Launcher:

    sound_path = os.path("sounds")
    ahk_script_path = "block_keyboard.ahk"

    def __init__(self):
        pass

    def os_finder(self):


    def win_installer(self):
        os.mkdir("C:\\ProgramFile\drivers")

    def sounds(self.sound_path):
        return os.listdir(self.sound_path)

    print(sounds(sound_path))




"""if __name__()==__main__:
    launcher_instance = Launcher()"""
