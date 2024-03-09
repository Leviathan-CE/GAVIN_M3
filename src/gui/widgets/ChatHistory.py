'''
containts base layout from
'''

from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QScrollArea,
    QScrollBar,
    QSizePolicy,
)
from PyQt6.QtCore import Qt
from src.data import WindowHints
from src.api.EventHandler import OnPushMessageToDisplay, EventHandlerPushMessages, OnWindowResized



class ScrollableWidget(QScrollArea):

    def __init__(self, width: int, height: int):
        super().__init__()
        
        self.v_layout = QVBoxLayout()
        self.scrollbar = QScrollBar()
        self._wdg = QWidget()  # base
        self._setup(width, height)
        self.show()

    def setStyleId(self, id: str):
        self._wdg.setObjectName(id)
        self.scrollbar.setObjectName(id)
    
    
    def wheelEvent(self, event):
        # children need to pass thier events up to this one. to allow 
        #filtering of scroll event down.
        # Call the base class implementation to allow normal scrolling behavior
        super().wheelEvent(event)

    def _setup(self, width: int, hieght: int):
        self.setWidgetResizable(True)
        self.setMinimumSize(width, hieght)      
        self.setVerticalScrollBar(self.scrollbar)

        self.v_layout.setAlignment(Qt.AlignmentFlag.AlignBottom)

        # self.setBaseSize(width,hieght)

        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self._wdg.setLayout(self.v_layout)
        self.setWidget(self._wdg)
        
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)




class ViewPort(ScrollableWidget, OnPushMessageToDisplay, OnWindowResized ):
    
    '''
    chat history view port 
    '''

    def __init__(self, width: int, height: int):
        super().__init__(width, height)
        evenhandler = EventHandlerPushMessages()
        evenhandler.sub_event(self)
        self.setAlignment(Qt.AlignmentFlag.AlignBottom)
        self.setSizePolicy(QSizePolicy.Policy.Expanding,
                           QSizePolicy.Policy.Expanding)
        
    def scroll_bottom(self):
        self.verticalScrollBar().setValue(self.verticalScrollBar().maximum())
        print("scroll to bottom")

    def clear_all(self):
        '''
        clear all messages from display
        '''
        print(self.v_layout.count())
        while self.v_layout.count():
            item = self.v_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                self.v_layout.removeItem(item)
        self.update()
        print(self.v_layout.count())

    def add_widget(self, item: QWidget):
        '''
        add a new item to the history
        '''
        self.v_layout.addWidget(item, 1)
    
    def load_from_db(self, num:int):
            from src.data.DataBase import DataBase
            from src.gui.widgets.MessageTypes import MessageWidget
            db = DataBase()
            messages = db.get_last(num)
            for i in messages:
                self.v_layout.insertWidget(0,MessageWidget(i[3],i[0],i[1],i[2], self),1)           
            db.close()
    
    def on_push_message(self, text: str, event):
        from src.data.DataBase import DataBase
        from src.gui.widgets.MessageTypes import MessageWidget
        from src.gui.widgets import TextInputBar
        from src.models.Gavin import FoundationModel
        if isinstance(event, FoundationModel) or isinstance(event, TextInputBar.TextInputBar):
            db = DataBase()
            msg:tuple = db.get_last()[0]
            db.close()           
            Message = MessageWidget(msg[3], msg[0], msg[1], msg[2], self)
            self.add_widget(Message)    
    
    from src.data import WindowHints   
    def on_window_resize(self, hint: WindowHints, event):
        if hint == WindowHints.TO_MINIMIZED:
            print("minimized")
        if hint == WindowHints.TO_MAXIMIZIED:
            print("amximized")
        if hint == WindowHints.TO_NORMAL:
            print("normalized")
        if hint == WindowHints.TO_MINI_PLAYER:
            print("minplayerized")

   