import markdown
from PyQt6.QtWidgets import QApplication 
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTextBrowser, QTextEdit
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEnginePage
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QTextDocument

# Your code using QTextDocument goes here

import sys

# Create the HTML template that includes the Highlight.js library


#why this works on its own and not when i attach to to another widget is beyond me but somthing is amiss
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

\\[sum_{i=1}^{n} i = \\frac{n(n+1)}{2}\\]

"""

class UltimateMD(QWebEngineView):
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
   def __init__(self, content: str):
       super().__init__()
       self.setObjectName("md")
       
       # Convert the markdown to HTML
       html_content = markdown.markdown(
           content, extensions=['fenced_code', 'codehilite'])
       # Create the HTML template that includes the MathJax and Highlight.js libraries
       full_html = UltimateMD.html_template_code.format(content=UltimateMD.html_template_math.format(content=html_content))
       # Create QWebEngineView instance        
       self.setHtml(full_html)      
       self.page().runJavaScript(full_html)       
       self.show()
       

class UltimateMD_allinone(QWebEngineView):
   '''
   currently works standalone however adding this class to 
   a new laout ends up with nothing being parsed into html 
   '''
   def __init__(self, content: str):
       super().__init__()
            
       self.html: str = self._init_html(content)
       print(f"HTML::::{self.html}")
       self.setHtml(self.html)
       self.show()
       
   def _init_html(self, content:str):      
        html_viewer = """
       <html>
        <head>
        <meta charset="utf-8">
        <script type="text/x-mathjax-config">
        MathJax.Hub.Config({{ tex2jax: {{
                inlineMath: [['$', '$'], ['\\(', '\\)']],
                displayMath: [['$$', '$$'], ['\\[', '\\]']],
                processEscapes: true
            }},
            jax: ["input/TeX", "output/HTML-CSS"],
            "HTML-CSS": {{ availableFonts: ["TeX"] }}
        }});
        </script>
        <script type="text/javascript" async src="C:/Users/Levi/Desktop/GAVIN_M3/src/gui/js/MathJax-2.7.7/MathJax.js"></script>
        </head>
        <body>
        <div>
        {content}
        </div>
        </body>
        </html>
        """

         # Convert the markdown to HTML
        html_content = markdown.markdown(
            content, extensions=['fenced_code'], output_format='html')     
        
        print(html_content)
        # Create the HTML template that includes the MathJax
        full_html = html_viewer.format(content=html_content)
        
        # Create QWebEngineView instance
        return full_html
       
        

if __name__ == "__main__":
    
    app = QApplication(sys.argv)  
    form = QWidget()  
    vb = QVBoxLayout()
    form.setLayout(vb)
    u = UltimateMD_allinone(content=markdown_content)
    ub = UltimateMD_allinone(content=markdown_content)
    form.layout().addWidget(u)
    form.layout().addWidget(ub)
   
    form.show()
    app.exec()
