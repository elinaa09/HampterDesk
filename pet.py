import random

from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QTimer, Qt, QPoint
import config
import sensors

class Pet(QLabel):
     def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.FramelessWindowHint
                            | Qt.WindowStaysOnTopHint
                            | Qt.Tool)

        self.setAttribute(Qt.WA_TranslucentBackground)

        self.resize(config.PET_WIDTH, config.PET_HEIGHT)       #pets size on its window
        self.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)

        self.base_x = 0         #pet rests in this position
        self.base_y = 0
        self.place_in_corner()
        
        self.drag_offset = QPoint(0, 0)
        self.was_dragged = False         

        self.images = {}                                  #loads all image 
        for state_name in config.IMAGES:
         self.images[state_name] = self.load_image(config.IMAGES[state_name])


      
        self.is_sad = False
        self.music_playing = False
        self.is_dragging = False
        self.show_state("idle")

        self.random_timer = QTimer()
        self.random_timer.timeout.connect(self.random_reaction)
        self.random_timer.start(config.RANDOM_DELAY)


        self.random_timer.start(config.RANDOM_DELAY)

        self.bob_timer=QTimer()
        self.bob_timer.timeout.connect(self.bob)
        self.bob_timer.start(config.BOB_DELAY)
        self.bob_offset = 0        # bobbing up and down part
        self.bob_direction = 1

        self.reaction_timer = QTimer()
        self.reaction_timer.setSingleShot(True)
        self.reaction_timer.timeout.connect(self.go_back_to_rest)

        self.key_watcher = sensors.KeyWatcher()
        self.key_timer = QTimer()
        self.key_timer.timeout.connect(self.check_keys)
        self.key_timer.start(config.KEY_CHECK_DELAY)

        self.music_timer = QTimer()
        self.music_playing.setSingleShot(True)
        self.music_timer.start(config.MUSIC_CHECK_DELAY)

        self.lonely_timer = QTimer()
        self.lonely_timer.setSingleShot(True)
        self.lonely_timer.timeout.connect(self.get_sad)
        self.lonely_timer.start(config.SAD_AFTER)


     def load_image(self, file_name):
        path = config.ASSETS_DIR / file_name
        


        picture = QPixmap(str(path))
        return picture.scaled(config.PET_WIDTH, config.PET_HEIGHT,
                          Qt.KeepAspectRatio, Qt.SmoothTransformation)



     def place_in_corner(self):
        screen = self.screen().availableGeometry()
        self.base_x = screen.right() - self.width() - config.START_MARGIN
        self.base_y = screen.bottom() - self.height() - config.START_MARGIN
        self.move(self.base_x, self.base_y)

     def show_state(self, state_name):
        self.setPixmap(self.images[state_name])


     def show_reaction(self, state_name, how_long=None):
       if how_long is None:
          how_long = config.REACTION_TIME[state_name]
       self.show_state(state_name)
       self.reaction_timer.start(how_long)


     def go_back_to_rest(self):
        if self.is_sad:
            self.show_state("sad")
        elif self.music_playing:
            self.show_state("music")
        else:
            self.show_state("idle")
            


     def get_happy(self):
        self.is_clicked = True
        self.show_state("happy")


     def get_sad(self):
        self.is_sad = True
        if not self.reaction_timer.isActive():
         self.show_state("sad")


     def cheer_up(self): 
        self.is_sad = False
        self.lonely_timer.start(config.SAD_AFTER)

     def get_laugh(self):
        self.pet_state = "laugh"
        self.show_state("laugh")
        QTimer.singleShot(config.CLICK_TIME, self.go_idle)

    
     def get_music(self):
        self.pet_state = "music"
        self.show_state("music")
        self.music_timer = QTimer()
        self.music_timer.timeout.connect(self.check_music)
        self.music_timer.start(config.MUSIC_CHECK_DELAY)
        

     def check_music(self):
        self.music_playing = sensors.is_music_playing()

        if self.pet_state == "idle" or self.pet_state == "music":
         self.go_back_to_rest()


     def check_keys(self):
        if self.key_watcher.check() and not self.is_dragging:
            self.show_reaction("type")


     def random_reaction(self):
        if self.is_dragging or self.reaction_timer.isActive():               
            return
        state_name = random.choice(config.RANDOM_STATES)
        self.show_reaction(state_name, config.RANDOM_SHOW_TIME)


     def bob(self):                 
        self.bob_offset += self.bob_direction  


        if self.bob_offset >= config.BOB_HEIGHT:      # Turn around at the top and at the bottom
            self.bob_direction = -1
        if self.bob_offset <= 0:
            self.bob_direction = 1

        self.move(self.base_x, self.base_y - self.bob_offset)


     def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            mouse_position = event.globalPosition().toPoint()
            self.drag_offset = mouse_position - self.frameGeometry().topLeft()

     def mouseMoveEvent(self, event):      
        if event.buttons() & Qt.LeftButton:
            self.is_dragging = True
            mouse_position = event.globalPosition().toPoint()     #mouse follow
            new_position = mouse_position - self.drag_offset
            self.move(new_position)

            self.base_x = new_position.x()             #stays at mouse position
            self.base_y = new_position.y() + self.bob_offset

     def mouseReleaseEvent(self, event):
        if event.button() == Qt.RightButton:
            self.close()
        elif event.button() == Qt.LeftButton:
            if not self.is_dragging:
                self.cheer_up()
                self.show_reaction("happy")
            self.is_dragging = False