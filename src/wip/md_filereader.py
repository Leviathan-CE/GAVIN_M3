import sys
import markdown2
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWebEngineWidgets import QWebEngineView
import mistune
from src.data.paths import ROOT
class MarkdownLatexViewer(QMainWindow):
    def __init__(self, md_file_path):
        super().__init__()

        self.setWindowTitle("Markdown and LaTeX Viewer")

        # Create a web engine view to display HTML content
        self.webview = QWebEngineView()

        # Read the Markdown content from the file and convert it to HTML
        with open(md_file_path, 'r', encoding='utf-8') as file:
            markdown_content = file.read()
            html_content = mistune.markdown(f"{markdown_content}")

        # Add MathJax script to the HTML content for LaTeX rendering
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
        <script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-AMS_HTML"></script>
        </head>
        <body>
        <div>
        {html_content}
        </div>
        </body>
        </html>
        """

        # Set the HTML content to the web engine view
        self.webview.setHtml(html_with_mathjax)

        # Set the web engine view as the central widget
        self.setCentralWidget(self.webview)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Replace 'path/to/your/file.md' with the actual path to your Markdown file
    md_file_path = r"C:\Users\Levi\Desktop\GAVIN_M3\markdowntext.md"

    viewer = MarkdownLatexViewer(md_file_path)
    viewer.show()

    sys.exit(app.exec())
