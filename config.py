from pathlib import Path

BASE_DIR = Path(__file__).parent
ASSETS_DIR = BASE_DIR / "assets"

IMAGES = {
"idle": "normal.png",
"happy": "smile1.png",
"laugh": "smile.png",
"type": "type.png",
"sad": "sad.png",
"music": "music.png",
"sus": "sus.png",
"blah": "blah.png",
"rage": "rage.png",
"fart": "fart.png"
}

REACTION_TIME ={
    "idle": 1500,
    "happy": 1800,
    "laugh": 1500,
    "type": 1500,
    "sad": 1500,
    "music": 1500,
    "sus": 1500,
    "blah": 1200,
    "rage": 1500,
    "fart":1000
}

RANDOM_STATES = ["sus", "blah", "happy", "laugh", "type", "music", "sad","rage", "fart"]

START_MARGIN = 30
BOB_DELAY = 70
BOB_HEIGHT = 6
CLICK_TIME = 1000


PET_WIDTH = 170
PET_HEIGHT = 162


RANDOM_DELAY = 60000
RANDOM_SHOW_TIME = 40000
SAD_AFTER = 900000
KEY_CHECK_DELAY = 2800
MUSIC_CHECK_DELAY = 3000