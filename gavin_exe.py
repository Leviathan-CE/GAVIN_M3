from src.gui.widgets.Buttons import BTNMenu
from src.gui.widgets.Form import form
from PyQt6.QtWidgets import (
    QApplication,
    QWidget

)
import markdown
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import Qt
from src.data.Paths import GUI_STYLES


import sys
import os
from src.gui.widgets.MarkdownLatexViewer import MarkdownLatexViewer
from src.gui.widgets.ChatHistory import ScrollableWidget, ViewPort
from src.data.Paths import MD_CONTENT
from src.gui.widgets.MessageTypes import CodeBlock, MessageWidget
from src.gui.widgets.TextInputBar import TextInputBar
from src.models.Gavin import FoundationModel, GavinMarkI
from src.api.EventHandler import (
        EventObserver,
        EvenHandlerInputText,
        EventHandlerPushMessages,
        EventHandlerWindowSize
    )
from PyQt6.QtWidgets import QVBoxLayout
if __name__ == "__main__":
    
    
    eventhandlers: list = [EventObserver(),
                           EventHandlerWindowSize(),
                           EvenHandlerInputText(),
                           EventHandlerPushMessages()]

    app = QApplication(sys.argv)
    form_main = form()
    form_main.move((form_main.pos().x()/2).__round__(),
             (form_main.pos().y()/2).__round__())

    form_main.setFixedSize(600, 800)
    chat_scrol_view = ViewPort(550, 350)
    margins = QWidget()    
    input_text_bar = TextInputBar(500)
    llm_model = GavinMarkI()
    llm_model.active_model = GavinMarkI.MODEL

    # for what ever reason if vewier is not populated
    # then wierd minimize glitch occurs.
    empty_message = MarkdownLatexViewer(
        "", chat_scrol_view)
    empty_message.setMaximumHeight(0)
    chat_scrol_view.add_widget(empty_message)
    margins.setContentsMargins(10,0,10,10)

    form_main.setCenterWidget(margins)
    margins.setLayout(QVBoxLayout())
    margins.layout().addWidget(chat_scrol_view)
    margins.layout().addWidget(input_text_bar)
    

    margins.layout().setAlignment(input_text_bar, Qt.AlignmentFlag.AlignHCenter)
    margins.layout().setAlignment(chat_scrol_view, Qt.AlignmentFlag.AlignHCenter)


    file = open(GUI_STYLES+"\\dark_mode.css", "r")
    app.setStyleSheet(file.read())
    file.close()
    app.exec()
