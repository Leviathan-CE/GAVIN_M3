from src.gui.Buttons import BTNMenu
from src.gui.widgets import form
from PyQt6.QtWidgets import (
    QApplication

)
from src.data.paths import GUI_STYLES
if __name__ == "__main__":
    app = QApplication([])
    btn = form()
    btn.show()
    file = open(GUI_STYLES+"\\dark_mode.css","r")  
    app.setStyleSheet(file.read())
    app.exec()
