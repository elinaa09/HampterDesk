import subprocess
from pynput import keyboard

def is_music_playing():
    """Check if music is currently playing on the system."""
    try:
        # Use 'playerctl' to check the status of the media player
        result = subprocess.run(["playerctl", "status"], capture_output=True, text=True, timeout=1)
        return result.stdout.strip() == "playing"
    except subprocess.TimeoutExpired:
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