from src.gui.Buttons import BTNMenu
from src.gui.widgets import form
from PyQt6.QtWidgets import (
    QApplication,
    QWidget

)
import markdown
from PyQt6.QtWebEngineWidgets import QWebEngineView

from src.data.paths import GUI_STYLES



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
    
    from src.gui.MarkdownLatexViewer import MarkdownLatexViewer    
    from src.gui.ChatHistory import ScrollableWidget, ViewPort
    from src.data.paths import MD_CONTENT
    from src.gui.MessageTypes import CodeBlock, MessageWidget
    from src.gui.TextInputBar import TextInputBar
    app = QApplication(sys.argv)
    btn = form()
    
    btn.setFixedSize(500,800) 
    scrol_view = ViewPort(300, 400)
    input = TextInputBar(400)
    viewer = MarkdownLatexViewer(
        markdown_content)
    
    btn.setCenterWidget(scrol_view)
    
    scrol_view.add_widget(viewer)
    btn.layout().addWidget(input)
    code_block = CodeBlock(markdown_content)
    scrol_view.add_widget(code_block)
    
    msg = MessageWidget(markdown_content)
    scrol_view.add_widget(msg)
    
    file = open(GUI_STYLES+"\\dark_mode.css","r")  
    app.setStyleSheet(file.read())
    file.close()
    app.exec()
