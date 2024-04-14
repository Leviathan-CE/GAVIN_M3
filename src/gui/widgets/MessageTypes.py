
from PyQt6.QtWidgets import QTextEdit, QVBoxLayout, QSizePolicy, QWidget,  QVBoxLayout, QApplication
import datetime
from src.gui.widgets import ChatHistory




class MessageWidget(QWidget):
    """
    parses incoming data into markdown code and text blocks 
    then displays them using code and markdown latex widgets
    """

    
    def __init__(self, message:str, id:int, user:str, date:datetime.datetime = datetime.datetime.now(), chathist:ChatHistory.ViewPort = None, scrol_bot:bool = True): # type: ignore
        super().__init__()
        
        from src.gui.widgets.MenuBar import MessageHeader
        from src.gui.InputParser import get_text_blocks
        from src.gui.widgets.MarkdownLatexViewer import MardownLatexWidget
        
        self.id: int = id
        self.user: str = user
        self.date: datetime.datetime = date
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        blocks:list[dict[str,str]] = get_text_blocks(message)
        #self.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.MinimumExpanding)
       
        message_header = MessageHeader(self.user,self.date)
        layout.addWidget(message_header)
        
        for blk in blocks:           
            if(blk is not None):
                if blk['type'] == "code":
                    layout.addWidget(CodeBlock(blk['content']))
                if blk['type'] == "text":
                    layout.addWidget(MardownLatexWidget(blk['content'], chathist))
        if chathist != None and scrol_bot == True:
            chathist.scroll_bottom()

    


class CodeBlock(QWidget):
    
    def __init__(self, code:str):
        super().__init__()        
        from src.gui.widgets.MenuBar import CodeBlockHeader
        import mistune         
               
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        main_layout.setSpacing(0)
        
        
        code_header = CodeBlockHeader(code.split()[0].strip("```"))
        code_header.btn_clipboard.clicked.connect(self.copy_to_clipboard)
        html_content: str = mistune.markdown(code)

        self.code_string = QTextEdit(html_content)        
        self.code_string.setReadOnly(True)
        self.code_string.setObjectName("code")   
        self.code_string.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.MinimumExpanding)
        
        
        main_layout.addWidget(code_header)
        main_layout.addWidget(self.code_string)

        #set size of code block for my sanity no touchy
        char = self.code_string.document().characterCount() #type:ignore
        blk = self.code_string.document().blockCount()  #type:ignore      
        doc_height =  max(max(blk*12+150,float.__round__(char*.5)), blk*10+float.__round__(char*.3) )
        self.setMinimumHeight(doc_height)        
   

    def copy_to_clipboard(self):
        '''
        copies text inside the block to windows clipboard for 
        use of shrotcuts to paste elsewere does not copy html
        just raw text.
        '''
        from PyQt6.QtGui import QClipboard 
        from PyQt6.QtCore import QMimeData
        mimdat = QMimeData()
        mimdat.setText(self.code_string.toPlainText())
        clipboard = QApplication.clipboard()
        clipboard.setMimeData(mimdat,mode=QClipboard.Mode.Clipboard)#type:ignore

        