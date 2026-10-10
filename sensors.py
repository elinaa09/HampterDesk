import sys 
import subprocess
from pynput import keyboard

def _linux_audio_playing():
    try:
        result = subprocess.run(["playerctl", "status"], 
                                capture_output=True, text=True, timeout=1)
        return result.stdout.strip() == "playing"
    except subprocess.TimeoutExpired:
        return False

def _windows_audio_playing():
    try:
        from pycaw.pycaw import AudioUtilities, IAudioMeterInformation
        for session in AudioUtilities.GetAllSessions():
            if session.Process is None:
                continue
            meter = session._ctl.QueryInterface(IAudioMeterInformation)
            if meter.GetPeakValue() > 0.001:
                return True
        return False
    except Exception:
        return False


class KeyWatcher:
    def __init__(self):
        self.key_pressed = False
        self.listener = keyboard.Listener(on_press=self.on_key_press)
        self.listener.start()

    def on_key_press(self, event):
        self.key_pressed = True

    def check(self):
        pressed = self.key_pressed
        self.key_pressed = False
        return pressed
    