import time

from util import get_audio_session, find_windown, get_text

SPOTIFY_PROCESS = "Spotify.exe"

class SpotiFree():

    def __init__(self, start=True):
        self.hwnd = find_windown(SPOTIFY_PROCESS)
        self.adv = False
        self.volume = get_audio_session(SPOTIFY_PROCESS)
        self.unmute()
        if start:
            self.start()

    def start(self):
        while 1:
            self.verify()
            time.sleep(1)

    def mute(self):
        self.volume.SetMute(1, None) 

    def unmute(self):
        self.volume.SetMute(0, None) 

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

    def get_text(self):
        return get_text(self.hwnd)

SpotiFree()