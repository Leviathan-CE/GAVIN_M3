from PyQt6.QtCore import QUrl, QSize, QMargins
from PyQt6.QtWidgets import QSizePolicy, QTextEdit, QVBoxLayout, QWidget, QLabel, QApplication, QMainWindow
from PyQt6.QtWebEngineWidgets import QWebEngineView
import mistune
from PyQt6.QtCore import Qt
from src.data.Paths import ROOT
from src.data.Settings import MAX_VIEW_WIDTH
class MarkdownLatexViewer(QMainWindow):
    """_summary_
    a html formatter that extends markdown thats avaible to pyqt6
    to allow for $$ latex maths inline and reg expressions.
    
    """
    def __init__(self, markdown_content:str):
        super().__init__()
        # Create a web engine view to display complex HTML content
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
        html_with_mathjax = fr"""
 <html>
        <head>
        
        <meta charset="utf-8">       
       <base href="{ROOT}">
                  <script>
        document.addEventListener("DOMContentLoaded", function() {{
          
            var style = document.createElement('style');
            style.innerHTML = 'body {{ background-color: rgb(15, 15,15); color: white; }}';
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
        self.setCentralWidget(self.webview) 
        print(self.webview.size())
        
    def on_load_finished(self, ok):
        # Adjust the minimum size based on the content size
        if ok:            
            size = QSize(self.webview.page().contentsSize().toSize()).grownBy(QMargins(0,0,0,70))
            self.setMinimumHeight(size.height())            
            self.webview.setMinimumHeight(size.height())
           

