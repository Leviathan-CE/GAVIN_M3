from PyQt6.QtGui import QColor, QTextCharFormat, QSyntaxHighlighter, QFont
from PyQt6.QtCore import QRegularExpression 
from PyQt6.QtWidgets import QApplication

from PyQt6.QtWidgets import ( 
    QLabel,
    QPlainTextEdit,
    QVBoxLayout,
    QWidget,
    )
import sys

class CodeHighlighterPython(QSyntaxHighlighter):
    def __init__(self, document):
        super().__init__(document)
        self.parent = document
        
        # Define keyword format
        keyword_format = QTextCharFormat()
        keyword_format.setForeground(QColor("#1e90ff"))
        keyword_format.setFontWeight(2)
        
        # Define comment format
        comment_format = QTextCharFormat()
        comment_format.setForeground(QColor("#8f8f8f"))
        
        # Define string format
        string_format = QTextCharFormat()
        string_format.setForeground(QColor("#008000"))
        
        # Define function format
        function_format = QTextCharFormat()
        function_format.setForeground(QColor("#ff7f00"))
        function_format.setFontWeight(2)
        
        # Define operator format
        operator_format = QTextCharFormat()
        operator_format.setForeground(QColor("#ff1493"))
        
        # Define number format
        number_format = QTextCharFormat()
        number_format.setForeground(QColor("#cd5c5c"))
        
        # Define formats for each type of token
        self.highlighting_rules = [
            (QRegularExpression("\\bint\\b"), keyword_format),
            (QRegularExpression("\\bfloat\\b"), keyword_format),
            (QRegularExpression("\\bstr\\b"), keyword_format),
            (QRegularExpression("\\bif\\b"), keyword_format),
            (QRegularExpression("\\belse\\b"), keyword_format),
            (QRegularExpression("\\bfor\\b"), keyword_format),
            (QRegularExpression("\\bwhile\\b"), keyword_format),
            (QRegularExpression("\\bdef\\b"), keyword_format),
            (QRegularExpression("#.*"), comment_format),
            (QRegularExpression("\".*\""), string_format),
            (QRegularExpression("\'.*\'"), string_format),
            (QRegularExpression("\\b[A-Za-z_]+(?=\\()"), function_format),
            (QRegularExpression("[+\-*/%=]"), operator_format),
            (QRegularExpression("\\b[0-9]+\\b"), number_format),
            (QRegularExpression("\\bimport\\b"), keyword_format),
            (QRegularExpression("\\bfrom\\b"), keyword_format),
        ]

    def highlightBlock(self, text):
        # Apply highlighting rules to current block of text
        for pattern, format_ in self.highlighting_rules:
            expression = QRegularExpression(pattern)
            it = expression.globalMatch(text)
            while it.hasNext():
                match = it.next()
                self.setFormat(match.capturedStart(), match.capturedLength(), format_)


class TextHighlighter(QSyntaxHighlighter):
    '''
    sets text colour ofa document to almost white
    '''    
    def __init__(self, document):
        super().__init__(document)
        self.parent = document

        self.code_format = QTextCharFormat()
        self.code_format.setForeground(QColor(200,200,200))

    def highlightBlock(self, text):
        self.setFormat(0, len(text), self.code_format)


#----------test code-------------------
class CodeWidget(QWidget):
    ''''
    for testing purposes only
    '''
    
    def __init__(self):
        super().__init__()
        
        # Create layout
        layout = QVBoxLayout(self)
        
        # Create text edit widget
        self.text_edit = QPlainTextEdit(self)
        self.text_edit.setReadOnly(True)
        self.text_edit.setTabStopDistance(40)
      
        
        # Create syntax highlighter and set it on text edit
        self.highlighter = CodeHighlighterPython(self.text_edit.document())
        self.text_edit.setPlainText("To create a new window in Python using PyQt6, you can follow these steps:\n\n1. Import the necessary modules:\n\n```python\nfrom PyQt6.QtWidgets import QApplication, QMainWindow, QWidget\n```\n\n2. Create a new `QMainWindow` object:\n\n```python\napp = QApplication([])\nwindow = QMainWindow()\n```\n\n3. Create a new `QWidget` object to be used as the central widget of the main window:\n\n```python\ncentral_widget = QWidget()\nwindow.setCentralWidget(central_widget)\n```\n\n4. Set the size and title of the main window:\n\n```python\nwindow.setGeometry(100, 100, 500, 500)\nwindow.setWindowTitle(\"New Window\")\n```\n\n5. Show the main window:\n\n```python\nwindow.show()\n```\n\nHere's the complete code:\n\n```python\nfrom PyQt6.QtWidgets import QApplication, QMainWindow, QWidget\n\napp = QApplication([])\nwindow = QMainWindow()\n\ncentral_widget = QWidget()\nwindow.setCentralWidget(central_widget)\n\nwindow.setGeometry(100, 100, 500, 500)\nwindow.setWindowTitle(\"New Window\")\n\nwindow.show()\n\napp.exec()\n``` \n\nThis will create a new window with a size of 500x500 pixels and a title of \"New Window\". You can customize the window further by adding more widgets and layouts to the central widget.")
        
        # Add text edit to layout
        layout.addWidget(self.text_edit)
    
    def setText(self, text):
          self.text_edit.setPlainText(text=text)

