from PyQt6.QtWidgets import  QSizePolicy, QApplication, QMainWindow, QVBoxLayout, QTextEdit, QWidget
from PyQt6.QtGui import QTextCursor


class TextInputBar(QTextEdit):
    """
        (width:int) sets the maxwidth of the bar
    """
    def __init__(self, width:int = 400):
        super().__init__()       
        self.setFixedHeight(30)              
        self.setMaximumHeight(30)
        self.setMinimumWidth(width)
        self.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)
        self.setPlaceholderText("Enter prompt here...")
        self.textChanged.connect(self._updateTextEditHeight)
        

    def _updateTextEditHeight(self):
        # Adjust the height of QTextEdit based on the content
        cursor = self.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)
        rect = self.cursorRect(cursor)
        if 3 <= rect.y() <= 300:
            self.setFixedHeight(rect.bottom() + 10)


