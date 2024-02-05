from src.gui.widgets.Buttons import BTNMenu
from src.gui.widgets.Widgets import form
from PyQt6.QtWidgets import (
    QApplication,
    QWidget

)
import markdown
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import Qt
from src.data.Paths import GUI_STYLES


if __name__ == "__main__":
    markdown_content = """
# hi lo
contents_size
contents_sizewwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
contents_size

contents_size
contents_size
contents_size

contents_sizecontents_size
contents_sizecontents_size

"""
#![yup](src/gui/imgs/icon.png)
    import sys
    import os
    from src.gui.widgets.MarkdownLatexViewer import MarkdownLatexViewer
    from src.gui.widgets.ChatHistory import ScrollableWidget, ViewPort
    from src.data.Paths import MD_CONTENT
    from src.gui.widgets.MessageTypes import CodeBlock, MessageWidget
    from src.gui.widgets.TextInputBar import TextInputBar
    from src.GAVIN import FoundationModel, GavinMarkI
    from src.api.EventHandler import (
        EventObserver,
        EvenHandlerInputText,
        EventHandlerPushMessages,
        EventHandlerWindowSize
    )
if __name__ == "__main__":
    eventhandlers: list = [EventObserver(),
                           EventHandlerWindowSize(),
                           EvenHandlerInputText(),
                           EventHandlerPushMessages()]

    app = QApplication(sys.argv)
    btn = form()
    btn.move((btn.pos().x()/2).__round__(),
             (btn.pos().y()/2).__round__())

    btn.setFixedSize(600, 800)
    scrol_view = ViewPort(600, 400)

    input = TextInputBar(600)

    test = GavinMarkI()
    test.active_model = GavinMarkI.MODEL

    # for what ever reason if vewier is not populated
    # then wierd minimize glitch occurs.
    viewer = MarkdownLatexViewer(
        "", scrol_view)
    scrol_view.add_widget(viewer)

    btn.setCenterWidget(scrol_view)

    btn.layout().addWidget(input)
    btn.layout().setAlignment(input, Qt.AlignmentFlag.AlignHCenter)
    btn.layout().setAlignment(scrol_view, Qt.AlignmentFlag.AlignHCenter)


    file = open(GUI_STYLES+"\\dark_mode.css", "r")
    app.setStyleSheet(file.read())
    file.close()
    app.exec()
