
from PyQt6.QtWidgets import QFrame, QSizePolicy, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QApplication, QSpacerItem
from PyQt6.QtCore import Qt


class MessageWidget(QWidget):
    
    
    def __init__(self, message:str):
        super().__init__()
        from src.gui.InputParser import get_text_blocks
        blocks:[list[dict[str,str]]] = get_text_blocks(message)


class CodeBlock(QWidget):
    
    def __init__(self, code:str):
        super().__init__()
        from src.gui.Buttons import BTNClipboardCopy
        from src.gui.menuBar import CodeBlockHeader
        import mistune  
        from src.data.paths import GUI_STYLES       
        from src.gui.textHighLighters import TextHighlighter
               
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        main_layout.setSpacing(0)
        
        
        code_header = CodeBlockHeader(code.split()[1])
        code_header.btn_clipboard.clicked.connect(self.copy_tp_clipboard)
        html_content = mistune.markdown(code)

        self.code_string = QLabel(html_content)
        self.code_string.setObjectName("code")   
        
        
        main_layout.addWidget(code_header)
        main_layout.addWidget(self.code_string)
        
        
        # file = open(GUI_STYLES+"/code_block.css","r", encoding="utf-8")   
        # css = file.read()       
        # self.code_string.setStyleSheet(css)
        #file.close()

        pass
    
    def copy_tp_clipboard(self):
        from PyQt6.QtGui import QClipboard 
        from PyQt6.QtCore import QMimeData
        mimdat = QMimeData()
        mimdat.setText(self.code_string.text())
        clipboard = QApplication.clipboard()
        clipboard.setMimeData(mimdat,mode=QClipboard.Mode.Clipboard)

        