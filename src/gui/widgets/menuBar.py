
#from typing_extensions import override
from PyQt6 import QtGui
from PyQt6.QtWidgets import (
    QToolBar,
    QMenu,
    QApplication,  
    QWidget ,
    QHBoxLayout,
    QLabel,
    QSpacerItem,
    QSizePolicy,
    QFrame
)

from PyQt6.QtCore import QEvent, QSize, Qt, QPoint, QPointF
from PyQt6.QtGui import QIcon, QAction, QMouseEvent
from src.data.paths import GUI_IMGS



class CodeBlockHeader(QFrame):
    
    def __init__(self, code_type:str):
        super().__init__()
        from src.gui.widgets.Buttons import BTNClipboardCopy
        from src.data.paths import GUI_STYLES
        
        self.setMaximumHeight(36)
        self.setContentsMargins(0,0,0,0)
        self.setObjectName("code_header")
        
        
        layout = QHBoxLayout()
        self.setLayout(layout)
        layout.setSpacing(0)
        layout.setContentsMargins(0,0,0,0)
        
        text = QLabel(self)
        text.setObjectName("code_header_txt")
        text.setContentsMargins(15,5,5,5)
        text.setText(code_type)
        
        self.btn_clipboard = BTNClipboardCopy(id="code_header_btn")

        spacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        layout.setAlignment(Qt.AlignmentFlag.AlignLeft)        
        layout.addWidget(text)
        layout.addItem(spacer)
        layout.addWidget(self.btn_clipboard)      
        self.show()
        
        
        
        

class ToolBarHeader(QToolBar):
    '''
    start tool bar for additional option menus and allows 
    user to click and drag window around 
    '''
    def __init__(self):
        super().__init__()      
        self.setIconSize(QSize(48,48))
        self.setMaximumHeight(48)
        
       
        
    def drop_down(self):
        print("dropdown menu here")
    
    #@override    
    def mousePressEvent(self, event : QMouseEvent):
       '''
       grabs the mouse position and determines the start location for drag
       '''
       if event.button() == Qt.MouseButton.LeftButton:
            self.drag_start_position = event.globalPosition()
    #@override
    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        #print("relased") 
        #do nothing 
        
        delta : QPointF  = event.globalPosition() - self.drag_start_position # type: ignore
        new_delta = QPoint(self.window().pos().x()+int(delta.x()),self.window().pos().y()+int(delta.y()))       
        # print(event.pos().y())
        # print(new_delta)
        # print(self.window().pos().y())
        # print(QApplication.screenAt(event.pos()))
        # TODO:need tyo make work with multiple screens
        if new_delta.y() < 2 and not QApplication.activeWindow().isMaximized():
                    QApplication.activeWindow().showMaximized()
                

    
    #@override  
    def mouseMoveEvent(self, event : QMouseEvent):
        '''
        when moveing mouse calulates the new postion from the pressed location
        only while mouse button is pressed aka moves the window
        
        '''
        if event.buttons() & Qt.MouseButton.LeftButton:
          delta : QPointF  = event.globalPosition() - self.drag_start_position # type: ignore
          new_delta = QPoint(self.window().pos().x()+int(delta.x()),self.window().pos().y()+int(delta.y()))
        #   print(event.globalPosition())  
          if QApplication.activeWindow().isMaximized():
                QApplication.activeWindow().showNormal()
                # TODO: need tyo make work with multiple screens
                #self.window().move(int(event.globalPosition().x()/2)+event.pos().x(), int(event.globalPosition().y()))
                self.window().move(QPoint(int(event.pos().x()/2), event.pos().y()))
                self.drag_start_position = event.globalPosition()
                event.accept()
                return          

        
        if event.buttons() & Qt.MouseButton.LeftButton:     
            delta : QPointF  = event.globalPosition() - self.drag_start_position # type: ignore
            new_delta = QPoint(self.window().pos().x()+int(delta.x()),self.window().pos().y()+int(delta.y()))
            self.window().move(new_delta)
            self.drag_start_position = event.globalPosition()
            
           
            

        
#not yet implemented 
class StartMenu(QMenu):
    '''
    example of a menu item to add  to the tool bar
    '''
    def __init__(self):
        super().__init__()
       
        file_menu = self.addMenu("&")
        file_menu.setIcon(QIcon(GUI_IMGS+"\\logo-WT.png"))
        dir = file_menu.window
        # Create actions and add to the menu
        new_action = QAction("New", self)
        file_menu.addAction(new_action)

        open_action = QAction("Open", self)
        file_menu.addAction(open_action)

        exit_action = QAction("Exit", self)
        file_menu.addAction(exit_action)

