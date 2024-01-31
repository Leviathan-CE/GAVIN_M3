'''
containts base layout from
'''

from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QApplication,
    QGridLayout,
    QScrollArea,
    QScrollBar,
    QSizePolicy,
)
from PyQt6.QtCore import Qt
from src.data.Settings import MAX_VIEW_WIDTH
from src.api.EventHandler import OnTextLoaded



class ScrollableWidget(QScrollArea, OnTextLoaded):

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

class ViewPort(ScrollableWidget, OnTextLoaded):
    '''
    chat history view port 
    '''

    def __init__(self, width: int, height: int):
        super().__init__(width, height)
        self.setAlignment(Qt.AlignmentFlag.AlignBottom)
        self.setSizePolicy(QSizePolicy.Policy.Expanding,
                           QSizePolicy.Policy.Expanding)
        
    def scroll_bottom(self):
        self.verticalScrollBar().setValue(self.verticalScrollBar().maximum())
        print("scroll to bottom")

    def clear_all(self):
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
    
   
    def On_text_input_loaded(self, text: str, event):
        from src.gui.widgets.MessageTypes import MessageWidget
        Message = MessageWidget(text)
        self.add_widget(Message)
        #scroll to bottom after rendering has be done.


   