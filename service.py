import time
import psutil
import pyautogui

from win32 import win32gui
from win32 import win32process


class SpotiFree():

    def __init__(self, start=True):
        self.hwnd = self.find_spotify_windown()
        self.adv = False
        if start:
            self.start()

    def start(self):
        while 1:
            self.verify()
            time.sleep(1)

    def mute(self):
        # check volux
        pyautogui.press('volumemute')

    def unmute(self):
        # check volux
        pyautogui.press('volumemute')

    def verify(self):
        text = self.get_text()
        if text:
            if not '-' in text and not 'Spotify' in text:
                if not self.adv:
                    self.adv = True
                    self.mute()
            elif self.adv:
                self.adv = False
                self.unmute()
        else:
            raise Exception("Spotify está fechado")

    def find_spotify_windown(self):
        global spotify_hwnd
        spotify_hwnd = None
        
        def find_hwnd_by_process_name(hwnd, process_name):
            global spotify_hwnd
            if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
                nID=win32process.GetWindowThreadProcessId(hwnd)
                del nID[0]
                for abc in nID:
                    try:
                        pro=psutil.Process(abc).name()
                    except psutil.NoSuchProcess:
                        pass
                    else:
                        if pro == process_name and win32gui.GetWindowText(hwnd) != "":
                            spotify_hwnd=hwnd
                            return

        win32gui.EnumWindows(find_hwnd_by_process_name, "Spotify.exe")
        return spotify_hwnd

    def get_text(self):
        return win32gui.GetWindowText(self.hwnd)
