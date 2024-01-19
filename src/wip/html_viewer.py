import markdown
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTextBrowser
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl 
import sys

# Create the HTML template that includes the Highlight.js library
html_template_code = """
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.3.1/styles/default.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.3.1/highlight.min.js"></script>
<script>hljs.highlightAll();</script>
</head>
<body>
{content}
</body>
</html>
"""

html_template_math = """
<html>
<head>
<meta charset="utf-8">
<script type="text/x-mathjax-config">
MathJax.Hub.Config({{
    tex2jax: {{ 
        inlineMath: [['$','$'], ['\\(','\\)']], 
        displayMath: [['$$','$$'], ['\\[','\\]']],
        processEscapes: true
    }}
}});
</script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-AMS_HTML"></script>
</head>
<body>
{content}
</body>
</html>
"""

#why this works on its own and not when i attach to to another widget is beyond me but somthing is amiss


class UltimateMD(QWidget):

   def __init__(self, content: str):
       super().__init__()
       # Convert the markdown to HTML
       html_content = markdown.markdown(
           content, extensions=['fenced_code', 'codehilite'])
       # Create the HTML template that includes the MathJax and Highlight.js libraries
       full_html = html_template_code.format(
           content=html_template_math.format(content=html_content))
       # Create QWebEngineView instance
       self.web_engine_view = QWebEngineView()
       # Set the HTML content with syntax-highlighted code and rendered math
       self.web_engine_view.setHtml(full_html)
       vbox = QVBoxLayout()
       self.setLayout(vbox)
       self.layout().addWidget(self.web_engine_view)  # type:ignore
       self.show()
       pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    markdown_content = """
This is an inline math example $e^{i\\pi} + 1 = 0$ 

# hi lo

This is a code block with syntax highlighting:

```Java

public void hello_world(){
    print("Hello, world!");
    }

hello_world();
```
And this is a displayed math example:

$$\\sum_{i=1}^{n} i = \\frac{n(n+1)}{2}$$ 

"""
    u = UltimateMD(content=markdown_content)
    u.show()
    app.exec()
