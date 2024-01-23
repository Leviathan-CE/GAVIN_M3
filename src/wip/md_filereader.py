import sys
import markdown2
from PyQt6.QtCore import QUrl, QSize, QMargins
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWebEngineWidgets import QWebEngineView
import mistune
from src.data.paths import ROOT, MD_CONTENT
class MarkdownLatexViewer(QMainWindow):
    def __init__(self, md_file_path):
        super().__init__()
        
        self.setWindowTitle("Markdown and LaTeX Viewer")

        # Create a web engine view to display HTML content
        self.webview = QWebEngineView()
        
        self.webview.page().loadFinished.connect(self.on_load_finished)
        # Read the Markdown content from the file and convert it to HTML
        with open(md_file_path, 'r', encoding='utf-8') as file:
            markdown_content = file.read() 
            html_content = mistune.markdown(f"{markdown_content}")

        # Add MathJax script to the HTML content for LaTeX rendering
        # local mathjax path {ROOT}\\js\\mathjax\\2.7.7\\MathJax.js?config=TeX-AMS_HTML
        # web mathjax https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-AMS_HTML
        html_with_mathjax = fr"""
 <html>
        <head>
        <base href="{ROOT}">
        <meta charset="utf-8">        
        
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
        
        base_url = QUrl.fromLocalFile(ROOT)
        print(base_url)
        # Set the HTML content to the web engine view
        self.webview.setHtml(html_with_mathjax)
        print(self.webview.page().url())
        # Set the web engine view as the central widget
        self.setCentralWidget(self.webview)
        # print(self.webview.page().contentsSize().toSize().height())
        # print(self.webview.page().contentsSize().toSize().width())
        # self.setFixedSize(self.webview.page().contentsSize().toSize())
        # self.webview.setFixedSize(self.webview.page().contentsSize().toSize())

    def on_load_finished(self, ok):
        if ok:
            self.webview.page().runJavaScript(
                "MathJax.Hub.Queue(['Typeset', MathJax.Hub]);")
            # Adjust the minimum size based on the content size
            size = QSize(self.webview.page().contentsSize().toSize()).grownBy(QMargins(0,0,0,50))
            self.setMinimumSize(size)
            self.webview.setMinimumSize(size)



