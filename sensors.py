from pynput import keyboard


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
    