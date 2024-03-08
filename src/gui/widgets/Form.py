'''
containts base layout from
'''
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QApplication,
    QGridLayout,
    QSystemTrayIcon,
    QMenu
)
from PyQt6.QtCore import Qt

from src.gui.widgets.Buttons import (
    BTNExit,
    BTNHide,
    BTNMenu,
    BTNMinMax
    
)
from PyQt6.QtGui import QIcon
from PyQt6.QtWebEngineWidgets import QWebEngineView

from src.gui.widgets.MenuBar import ToolBarHeader

from src.data.Paths import GUI_IMGS           

# ---------------------------------------------
# -------------BLANK Form----------------------
# ---------------------------------------------
class Form(QWidget):
    '''
    blank window
    '''
    
    def __init__(self):
        super().__init__()
        #note always put classs vars in init or you get attribute error   
        self.outterLayout = QVBoxLayout(self)
        self.wdg_header = QWidget()
        self.wdg_header.setObjectName("yolo")
        
       
        self.header = QGridLayout(self.wdg_header) 
              
        self.btn_hide = BTNHide()
        self.btn_min_max = BTNMinMax()      
        self.mbr_toolbar = ToolBarHeader()
        self.btn_menu = BTNMenu() 
        self.btn_exit = BTNExit()        
             
        self.wdg_header.setMinimumHeight(self.btn_exit.height())     
        self.setObjectName("Form")
        self.setMinimumHeight(250)
        self.setMinimumWidth(350)

        icon = QIcon(GUI_IMGS + "\\icon.png")
        if icon.isNull():
            print("icon is null")
        # Replace with the path to your icon
        self.setWindowIcon(icon)

        #set up tray icon on the bottom of the screen
        self.tray_icon = TrayIcon(icon=icon,mainWindow=self)
        self.tray_icon.activated.connect(self.showNormal)
        self.tray_icon.show()  

        #remove default window and set min size
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint) 
        self._setup()
        self.show()
        

        
    def setCenterWidget(self, widget):
        #  self.text = QLabel("HI")
        #  self.vlay = QVBoxLayout(self.text)
        print(self.header.children())        
        self._set_header()
        self.outterLayout.addWidget(self.wdg_header)
         #self.outterLayout.addWidget(self.text)
        self.outterLayout.addWidget(widget)
        print( self.outterLayout.count())
       
      
   
    def _set_header(self):
        self.outterLayout.setAlignment(Qt.AlignmentFlag.AlignTop)   
        self.outterLayout.setSpacing(10)
        self.outterLayout.setContentsMargins(0, 0,0, 0)    
        
        
        self.header.setObjectName("")
        self.header.setSpacing(0)
        self.header.setContentsMargins(0, 0, 0, 0)
        
        self.header.addWidget(self.btn_menu,0,0)
        self.header.addWidget(self.mbr_toolbar,0,1)      
        self.header.addWidget(self.btn_exit,0,4)
        self.header.addWidget(self.btn_hide,0,2)
        self.header.addWidget(self.btn_min_max,0,3)
        self.header.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.btn_exit.clicked.connect(self.exit)    
    
    def setLayout(self, layout):
         raise ReferenceError("use setCenterWidget instead")
        
    def _setup(self):
        
        self.outterLayout.setAlignment(Qt.AlignmentFlag.AlignTop)   
        self.outterLayout.setSpacing(10)
        self.outterLayout.setContentsMargins(0, 0,0, 0)               
        self._set_header()

        self.outterLayout.addWidget(self.wdg_header)
        
       # self.outterLayout.insertWidget(0,self.wdg_header,1)

    
    
    def exit(self):
        print("application terminated")
        QApplication.exit() 
        
        
#---------------------------------------------
#-------------SYS TRAY ICON-------------------
#---------------------------------------------
class TrayIcon(QSystemTrayIcon):

    '''
    is the Icon that sits at the bottom corner on a windows machine
    when apps run in the back ground.
    '''

    def __init__(self, icon: QIcon, mainWindow: Form):
        super().__init__()
        print("try icon start")
        # Create the system tray icon
        self.setIcon(icon)
        self.setVisible(True)

        # Create the system tray menu
        self.tray_menu = QMenu(mainWindow)
        self.tray_menu.addAction("Restore", mainWindow.showNormal)
        self.tray_menu.addAction("Quit", mainWindow.exit)
        self.setContextMenu(self.tray_menu)
        self.activated.connect(self.on_tray_icon_activated)
        print("try icon made")
    
    def on_tray_icon_activated(self, reason):
        if reason == QSystemTrayIcon.ActivationReason.Trigger:
            from src.data import WindowHints
            from src.api.EventHandler import EventHandlerWindowSize
            EventHandlerWindowSize().invoke_on_window_size_changed(WindowHints.TO_NORMAL, self)




# ---------------------------------------------
# -------------API KEY Form--------------------
# ---------------------------------------------
from PyQt6.QtWidgets import QVBoxLayout, QTextEdit, QLabel
from src.gui.widgets.Buttons import Button
from PyQt6.QtCore import Qt,QTimer
import subprocess
from src.data.profiles import OPENAI_KEY_NAME
import openai
import os, time
class ApiKeyForm(Form):
    
    def __init__(self, function_main):
        super().__init__()
        self.main = function_main
        self.label = QLabel("Please input your OpenAI api key")
        self.inputbar = QTextEdit(self)
        self.inputbar.setObjectName("textinput")
        self.inputbar.setFixedHeight(30)
        self.ok_button = Button(id="ok_button", size=[80,48])
        self.ok_button.setFixedSize(80, 48)
        self.ok_button.setText("Ok")
        self.ok_button.clicked.connect(self.confirm_api_key)                   
       
        layout = QVBoxLayout()
        layout.setContentsMargins(20,5,20,5)
        center_widget = QWidget()
        center_widget.setLayout(layout)
        layout.addWidget(self.label)
        layout.addWidget(self.inputbar)
        layout.addWidget(self.ok_button)
        layout.setAlignment(self.ok_button,Qt.AlignmentFlag.AlignHCenter)
        
        self.setCenterWidget(center_widget)
        self.show()
        

    
    def confirm_api_key(self):
        from src.data.DataBase import KeyManager
        apiManager = KeyManager()
        
        self.label.setText("setting key...")
        key = self.inputbar.toPlainText()
        self.inputbar.clear        
        #subprocess.run(["setx", OPENAI_KEY_NAME,key])
        apiManager.set_key(OPENAI_KEY_NAME,key)
        try:
            #using regular env vars doesnt work because 
            #dynamic instancing isn't a thing will move to 
            #.evn var set up with permission only for this program
            # and use  'keyring' for encryption of keys

             openai.api_key = apiManager.get_key(OPENAI_KEY_NAME)
             print(openai.api_key)
             # ------------------------------------------------------
             openai.chat.completions.create( #type:ignore
                                            model="gpt-3.5-turbo",
                 messages=[{"role": "user", "content": "this is a test"}],
                                            temperature=.45,  # .6
                                            max_tokens=1000,  # max 4096
                                            user="User")
        #      #-----------------------------------------------------
             apiManager.close()
             print(openai.api_key)
             print("key found") 
             self.label.setText("Api key recognized; please restart program... ")             
             QTimer.singleShot(5000, self.close)           
        except Exception as e:
            print(e)
            self.label.setText("Api key note recognized please enter valid key.")
            
 
        # try:
        #     #------------------------------------------------------
        #      openai.chat.completions.create( #type:ignore
        #                                     model="gpt-3.5-turbo",
        #          messages=[{"role": "user", "content": "this is a test"}],
        #                                     temperature=.45,  # .6
        #                                     max_tokens=1000,  # max 4096
        #                                     user="User")
        #      #-----------------------------------------------------
        #      print("runing with it")            
        # except Exception as e: 
        #     print(e)
        #     self.label.setText("Api key not valid please input a valid Api key")
           
        

            
        
