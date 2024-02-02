from PyQt6.QtWidgets import  QSizePolicy, QApplication, QMainWindow, QVBoxLayout, QTextEdit, QWidget
from PyQt6.QtGui import QTextCursor, QKeyEvent
from PyQt6.QtCore import Qt, QEvent
from src.api.EventHandler import EventObserver

class TextInputBar(QTextEdit):
  
    """
        (width:int) sets the maxwidth of the bar
    """
    def __init__(self, width:int = 400):
        super().__init__()
        
        self.evenhandler = EventObserver()
        self.setObjectName("textinput")     
        self.setFixedHeight(30)              
        self.setMaximumHeight(30)
        self.setMinimumWidth(width)
        self.setMaximumWidth(width)
        self.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)
        self.setPlaceholderText("Enter prompt here... cntrl+enter to send")
        self.textChanged.connect(self._updateTextEditHeight)
        
    def _updateTextEditHeight(self):
        # Adjust the height of QTextEdit based on the content
        cursor = self.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)
        rect = self.cursorRect(cursor)
        if 3 <= rect.y() <= 300:
            self.setFixedHeight(rect.bottom() + 10)
    

    def keyPressEvent(self, event:QKeyEvent):
        event_control:Qt.Key = None
        if event.keyCombination().keyboardModifiers() == Qt.KeyboardModifier.ControlModifier:
            event_control = event
        if event_control != None and event.key() == 16777220:
            event_control = None
            txt = self.toPlainText()
            self.setText("")
            self.evenhandler.invoke_On_text_changed(txt,self)
            #self.invoke_On_text_loaded(self.toPlainText(),self)   
        else:
          
            super().keyPressEvent(event)
        
        



