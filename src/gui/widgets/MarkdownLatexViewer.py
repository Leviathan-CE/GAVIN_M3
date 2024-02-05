from PyQt6.QtCore import QUrl, QSize, QMargins
from PyQt6.QtGui import QKeyEvent, QMouseEvent
from PyQt6.QtWidgets import QSizePolicy, QTextEdit, QVBoxLayout, QWidget, QLabel, QApplication, QMainWindow
from PyQt6.QtWebEngineWidgets import QWebEngineView
import mistune
from PyQt6.QtCore import Qt
from src.data.Paths import ROOT
from src.gui.widgets import ChatHistory
class MarkdownLatexViewer(QWidget):
    """_summary_
    a html formatter that extends markdown thats avaible to pyqt6
    to allow for $$ latex maths inline and reg expressions.
    
    """
    def __init__(self, markdown_content:str, chathist:ChatHistory.ViewPort):
        super().__init__(chathist)
        # Create a web engine view to display complex HTML content
        self.chat_hist = chathist
        layout = QVBoxLayout()
        layout.setContentsMargins(15, 15, 15, 15)
        self.setLayout(layout)
        self.webview = QWebEngineView()
        
        self.setMinimumHeight(50) 
        
        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)

        # self.setMaximumWidth(MAX_VIEW_WIDTH)
        # self.webview.setMaximumWidth(MAX_VIEW_WIDTH)
        self.webview.page().loadFinished.connect(self.on_load_finished)
        html_content = mistune.markdown(markdown_content.replace("\f", "\\f"))

     
        # self.webview.setSizePolicy(QSizePolicy.Policy.Expanding,
        #                     QSizePolicy.Policy.Expanding)
        # Add MathJax script to the HTML content for LaTeX rendering
        # local mathjax (not working..yet) path {ROOT}\\js\\mathjax\\2.7.7\\MathJax.js?config=TeX-AMS_HTML
        # web mathjax https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-AMS_HTML
        html_with_mathjax = f"""
 <html>
        <head>
        
        <meta charset="utf-8">       
       <base href="{ROOT}">
                  <script>
        document.addEventListener("DOMContentLoaded", function() {{
          
            var style = document.createElement('style');
            style.innerHTML = 'body {{ background-color: rgb(20, 20,20); color: white; }}';
            document.head.appendChild(style);
        }});
    </script> 
        <script type="text/x-mathjax-config">
        MathJax.Hub.Config({{ tex2jax: {{
                inlineMath: [['$', '$'], ['\\(', '\\)']],
                displayMath: [['$$', '$$'], ['\\[', '\\]']],
                processEscapes: true
            }}
        }});       
        </script>

        <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-AMS_HTML"></script>       

        </head>
        <body>
        <div>
        {html_content}
        </div>
        </body>
        </html>
        """

        #chaning baseurl allows images to render but not latex        
        base_url = QUrl.fromLocalFile(ROOT)
        # print(base_url)
        # Set the HTML content to the web engine view
        self.webview.setHtml(html_with_mathjax)       
      
        # Set the web engine view as the central widget
        layout.addWidget(self.webview) 
        
        print(self.webview.size())
        
    def on_load_finished(self, ok):
        # Adjust the minimum size based on the content size
        if ok:            
            size = QSize(self.webview.page().contentsSize().toSize()).grownBy(QMargins(0,0,0,70))
            self.setMinimumHeight(size.height())            
            self.webview.setMinimumHeight(size.height())
            print(f" new size: {self.webview.size()}")
            print(self.webview.sizeHint())
            self.chat_hist.scroll_bottom()
            #self.check_scrollbar()
            
    def check_scrollbar(self):
        '''
        better size for widget not yet working
        '''
        # Get the current scroll position and content size
        contents_size = self.webview.page().contentsSize().height().__round__()
        widget_h = self.height()
        print(f"web: {contents_size} widg: {widget_h}")
        hight: int = widget_h- contents_size
        print(hight)
        if max(contents_size,widget_h)==contents_size:
            self.setMinimumHeight(abs(hight)+self.height()+50)
        elif max(contents_size,widget_h) ==widget_h:
            self.setMaximumHeight(self.minimumHeight()+abs(hight)+20)
            self.webview.setMaximumHeight(self.minimumHeight()+abs(hight)+20)
        
        print(f"after: web: {contents_size} widg: {widget_h}")
        # Check if the scroll position is at the bottom and the contents are taller than the view
        # if 0 >= (hight):
        #     print("Scrollbar is visible.")
            
        #     print(hight)
        #     # self.chat_hist.size().setHeight(hight+self.height())          
        #     self.setMinimumHeight(abs(hight)+self.height()+50)
        #     self.webview.setMinimumHeight(abs(hight)+self.height()+50)
        #     print(f"after: web: {contents_size} widg: {widget_h}")
            
           
        # else:
        #     print(hight)
        #     self.setMinimumHeight(abs(hight)-self.height())
        #     self.webview.setMinimumHeight(abs(hight)-self.height())
        #     print("Scrollbar is not visible.")
        #     print(f"after: web: {contents_size} widg: {widget_h}")


class MarddownLatexViewer2(QTextEdit):
    '''
    supose to replace v1 so that we can scroll and still 
    copy paste text without issue and to be slightly faster 
    to render and possibly allow to continual rendering.
    '''
    def __init__(self, html_file:str):
        super().__init__()
