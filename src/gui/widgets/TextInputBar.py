from PyQt6.QtGui import QTextCursor
from PyQt6.QtWidgets import  QSizePolicy,  QTextEdit

from PyQt6.QtCore import QRect, Qt
from src.api.EventHandler import EvenHandlerInputText

class TextInputBar(QTextEdit):
  
    """
    the main user input for the chating with the agent.
    also has same rendering as the agent.
        (width:int) sets the maxwidth of the bar
    """
    from PyQt6.QtGui import QKeyEvent
    
    def __init__(self, width:int = 400) -> None:
        super().__init__()
        
        self.evenhandler = EvenHandlerInputText()
        self.setObjectName("textinput")     
        self.setFixedHeight(30)              
        self.setMaximumHeight(30)
        self.setMinimumWidth(width)
        self.setMaximumWidth(width)
        self.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        self.setPlaceholderText("Enter prompt here... cntrl+enter to send")
        self.textChanged.connect(self._updateTextEditHeight)
        
    def _updateTextEditHeight(self) -> None:
        from PyQt6.QtGui import QTextCursor
        
        # Adjust the height of QTextEdit based on the content
        cursor: QTextCursor = self.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)
        rect: QRect = self.cursorRect(cursor)
        if 3 <= rect.y() <= 300:
            self.setFixedHeight(rect.bottom() + 10)
    

    def keyPressEvent(self, event:QKeyEvent) -> None:
        event_control:Qt.Key = None
        if event.keyCombination().keyboardModifiers() == Qt.KeyboardModifier.ControlModifier:
            event_control = event
        if event_control != None and event.key() == 16777220:
            event_control = None
            txt = self.toPlainText()
            from src.data.DataBase import DataBase
            from src.data.profiles import USER_NAME
            db = DataBase()
            db.insert(USER_NAME,txt)
            db.close()
            self.setText("")
            
            self.evenhandler.invoke_On_text_changed(txt,self)
            #self.invoke_On_text_loaded(self.toPlainText(),self)   
        else:
          
            super().keyPressEvent(event)
        
        



