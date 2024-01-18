

from PyQt6.QtWidgets import (
    QPushButton,
    QApplication

)
from src.data.paths import GUI_IMGS
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon



BUTTON_DEFAULT_SIZE = [48, 48]


class Button(QPushButton):

    def __init__(self, id: str, size=BUTTON_DEFAULT_SIZE):
        super().__init__()
        self.setObjectName(id)
        self.setBaseSize(size[0], size[1])


class BTNExit(Button):
    def __init__(self, id: str = "btn_exit", size=BUTTON_DEFAULT_SIZE):
        super().__init__(id, size)
        self.setText("X")
        self.setMinimumSize(size[0], size[1])
        self.setMaximumSize(size[0], size[1])

        # self.clicked.connect(self.exit)

    def exit(self):
        QApplication.exit()


class BTNHide(Button):

    def __init__(self, id: str = "btn_hide", size=BUTTON_DEFAULT_SIZE):
        super().__init__(id, size)
        self.setText("-")
        self.setMinimumSize(size[0], size[1])
        self.setMaximumSize(size[0], size[1])
        self.clicked.connect(self.hide)

    def hide(self):
        QApplication.activeWindow().hide()


class BTNMinMax(Button):
    def __init__(self, id: str = "btn_min_max", size=BUTTON_DEFAULT_SIZE):
        super().__init__(id, size)
        self.setText("[  ]")
        self.setMinimumSize(size[0], size[1])
        self.setMaximumSize(size[0], size[1])
        self.clicked.connect(self.min_max)

    def min_max(self):
        QApplication.activeWindow()
        if QApplication.activeWindow().isMaximized():
            self.setText("[  ]")
            QApplication.activeWindow().showNormal()
           # QApplication.activeWindow().showMaximized()
        else:
            self.setText("[]")
            QApplication.activeWindow().showMaximized()


class BTNMenu(Button):

    def __init__(self, id: str = "", size=BUTTON_DEFAULT_SIZE):
        super().__init__(id, size)
        self._img = QIcon(GUI_IMGS+"\\logo-WT.png")
        self.setIconSize(QSize(size[0], size[1]))
        self.setIcon(self._img)
        self.setText("")
        self.setMinimumSize(size[0], size[1])
        self.setMaximumSize(size[0], size[1])
        self.clicked.connect(self.open_menu)

    def open_menu(self):
        print("menu button pressed")


