from win32 import win32gui
from win32 import win32process
from win32com.client import GetObject
from pycaw.pycaw import AudioUtilities

def get_audio_session(process_name):
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        if session.Process and session.Process.name() == process_name:
            return session.SimpleAudioVolume

def find_windown(process_name):
        global spotify_hwnd
        spotify_hwnd = None
        
        def find_hwnd_by_process_name(hwnd, process_name):
            global spotify_hwnd
            if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
                _, pid = win32process.GetWindowThreadProcessId(hwnd)
                _wmi = GetObject('winmgmts:')
                processes = _wmi.ExecQuery('Select * from win32_process')
                for p in processes:
                    if isinstance(p.ProcessId, int) and p.ProcessId == pid:
                        if p.Name == process_name and win32gui.GetWindowText(hwnd) != "":
                            spotify_hwnd=hwnd
                            return

        win32gui.EnumWindows(find_hwnd_by_process_name, process_name)
        return spotify_hwnd

def get_text(hwnd):
    return win32gui.GetWindowText(hwnd)