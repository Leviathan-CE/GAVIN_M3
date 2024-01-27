
from PyQt6.QtWidgets import QTextEdit, QVBoxLayout, QFrame, QSizePolicy, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QApplication, QSpacerItem
from PyQt6.QtCore import Qt, QSize


class MessageWidget(QWidget):
    """
    parses incoming data into markdown code and text blocks 
    then displays them using code and markdown latex widgets
    """
    
    def __init__(self, message:str):
        super().__init__()
        from src.gui.InputParser import get_text_blocks
        from src.gui.MarkdownLatexViewer import MarkdownLatexViewer
        layout = QVBoxLayout()
        self.setLayout(layout)
        blocks:list[dict[str,str]] = get_text_blocks(message)
        self.setSizePolicy(QSizePolicy.Policy.Expanding,
                            QSizePolicy.Policy.Expanding)
        
        
        for blk in blocks:           
            if(blk is not None):
                if blk['type'] == "code":
                    print(blk['content'])
                    layout.addWidget(CodeBlock(blk['content']))
                if blk['type'] == "text":
                    layout.addWidget(MarkdownLatexViewer(blk['content']))

          


class CodeBlock(QWidget):
    
    def __init__(self, code:str):
        super().__init__()        
        from src.gui.menuBar import CodeBlockHeader
        import mistune         
               
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        main_layout.setSpacing(0)
        
        
        code_header = CodeBlockHeader(code.split()[0].strip("```"))
        code_header.btn_clipboard.clicked.connect(self.copy_to_clipboard)
        html_content = mistune.markdown(code)

        self.code_string = QTextEdit(html_content)        
        self.code_string.setReadOnly(True)
        self.code_string.setObjectName("code")   
        self.code_string.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.MinimumExpanding)
        
        
        main_layout.addWidget(code_header)
        main_layout.addWidget(self.code_string)

        #set size of code block for my sanity no touchy
        char = self.code_string.document().characterCount()
        blk = self.code_string.document().blockCount()        
        doc_height =  max(max(blk*12+150,float.__round__(char*.5)), blk*10+float.__round__(char*.3) )
        self.setMinimumHeight(doc_height)        
   

    def copy_to_clipboard(self):
        from PyQt6.QtGui import QClipboard 
        from PyQt6.QtCore import QMimeData
        mimdat = QMimeData()
        mimdat.setText(self.code_string.text())
        clipboard = QApplication.clipboard()
        clipboard.setMimeData(mimdat,mode=QClipboard.Mode.Clipboard)

        