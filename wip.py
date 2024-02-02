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

This is an inline math example $e^{i\pi} + 1 = 0$

This is a code block with syntax highlighting: to this is a really long sentance and i like it

```Python

from PyQt6.QtWidgets import QTextEdit, QApplication

class MyTextEdit(QTextEdit):
    def __init__(self):
        super().__init__()
        self.document().contentsChanged.connect(self.adjustSize)

from PyQt6.QtWidgets import QTextEdit, QApplication

```
 
And this is a displayed math example:

$$\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$$



g

g


g

g

g
g

g
g

g
g
g

g
"""
#![yup](src/gui/imgs/icon.png)
    import sys
    
    from src.gui.widgets.MarkdownLatexViewer import MarkdownLatexViewer    
    from src.gui.widgets.ChatHistory import ScrollableWidget, ViewPort
    from src.data.Paths import MD_CONTENT
    from src.gui.widgets.MessageTypes import CodeBlock, MessageWidget
    from src.gui.widgets.TextInputBar import TextInputBar
    from src.GAVIN import ModelFoundation, GavinMarkI
    from src.api.EventHandler import EventObserver
   
    def ismaxed():
        print("tolo")
        if btn.isMaximized():
            scrol_view.resize(1000,scrol_view.size().height())
        else:
            scrol_view.resize(500,scrol_view.size().height())
    app = QApplication(sys.argv)
    btn = form()
    
    
    test = GavinMarkI()
    test.active_model = GavinMarkI.MODEL 
    btn.setFixedSize(600,800) 
    scrol_view = ViewPort(600, 400)
  
    input = TextInputBar(600)
    viewer = MarkdownLatexViewer(
        markdown_content)
    
    input.sub_event(listeners=scrol_view)
    
    
    btn.setCenterWidget(scrol_view)
    
    scrol_view.add_widget(viewer)
    btn.layout().addWidget(input)
    btn.layout().setAlignment(input, Qt.AlignmentFlag.AlignHCenter)
    btn.layout().setAlignment(scrol_view, Qt.AlignmentFlag.AlignHCenter)

    # code_block = CodeBlock(markdown_content)
    # scrol_view.add_widget(code_block)
    
    btn.btn_min_max.clicked.connect(ismaxed)
    
    
    # msg = MessageWidget(markdown_content)
    # scrol_view.add_widget(msg)
    
    file = open(GUI_STYLES+"\\dark_mode.css","r")  
    app.setStyleSheet(file.read())
    file.close()
    app.exec()



