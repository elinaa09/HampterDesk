from pathlib import Path

BASE_DIR = Path(__file__).parent
ASSETS_DIR = BASE_DIR / "assets"

IMAGES = {
"idle": "normal.png",
"happy": "smile1.png",
"laugh": "smile3.png",
"type": "type.png",
"sad": "sad.png",
"music": "music.png",
"sus": "sus.png",
"blah": "blah.png",
"rage": "rage.png"
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
    "rage": 1500
}

RANDOM_STATES = ["sus", "blah", "happy", "laugh", "type", "music", "sad","rage"]

START_MARGIN = 30
BOB_DELAY = 70
BOB_HEIGHT = 6
CLICK_TIME = 1000


PET_WIDTH = 160
PET_HEIGHT = 152


RANDOM_DELAY = 23000
RANDOM_SHOW_TIME = 4000 
SAD_AFTER = 60000
KEY_CHECK_DELAY = 300
MUSIC_CHECK_DELAY = 3000



