from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QTimer, Qt, QPoint

import config

class Pet(QLabel):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.FramelessWindowHint
                            | Qt.WindowStaysOnTopHint
                            | Qt.Tool)

        self.setAttribute(Qt.WA_TranslucentBackground)

        self.current_image = self.load_image(config.START_IMAGE)
        self.setPixmap(self.current_image)
        self.resize(self.current_image.size())

        self.base_x = 0
        self.base_y = 0
        self.place_in_corner()

        self.drag_offset = QPoint(0, 0)

        self.bob_offset = 0        # how many pixels we are above the resting spot
        self.bob_direction = 1

        self.bob_timer = QTimer()
        self.bob_timer.timeout.connect(self.bob)
        self.bob_timer.start(config.BOB_DELAY)

    def load_image(self, file_name):
        """Open an image from the assets folder and resize it."""
        path = config.ASSETS_DIR / file_name
        if not path.exists():
         raise FileNotFoundError("Missing image file: " + str(path))
        

        picture = QPixmap(str(path))
        return picture.scaled(config.PET_WIDTH, config.PET_HEIGHT,
                              Qt.KeepAspectRatio, Qt.SmoothTransformation)

    def place_in_corner(self):
        """Put the pet in the bottom right corner of the screen."""
        screen = self.screen().availableGeometry()
        self.base_x = screen.right() - self.width() - config.START_MARGIN
        self.base_y = screen.bottom() - self.height() - config.START_MARGIN
        self.move(self.base_x, self.base_y)



    def bob(self):
        """Move the pet up or down by 1 pixel. Runs every few milliseconds."""
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
        elif event.button() == Qt.RightButton:


         def mouseMoveEvent(self, event):      
          if event.buttons() & Qt.LeftButton:
           mouse_position = event.globalPosition().toPoint()       #mouse follow
           new_position = mouse_position - self.drag_offset
           self.move(new_position)

           self.base_x = new_position.x()             #stays at mouse position
           self.base_y = new_position.y() + self.bob_offset