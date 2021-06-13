import psutil
from win32 import win32gui
from win32 import win32process

def find_spotify_windown():
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

def get_text(hwnd):
    return win32gui.GetWindowText(hwnd)