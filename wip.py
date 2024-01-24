from src.gui.Buttons import BTNMenu
from src.gui.widgets import form
from PyQt6.QtWidgets import (
    QApplication,
    QWidget

)
import markdown
from PyQt6.QtWebEngineWidgets import QWebEngineView

from src.data.paths import GUI_STYLES



if __name__ == "__main__":
    markdown_content = """
    # hi lo

This is an inline math example $e^{i\pi} + 1 = 0$

This is a code block with syntax highlighting:

```java
    public void hello_world(){
        print("Hello, world!");
        }

    hello_world();
```
 
And this is a displayed math example:

$$\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$$

![yup](src/gui/imgs/icon.png)

    """
    latex_content = """
            <html>
        <head>
        <meta charset="utf-8">
        <script type="text/x-mathjax-config">
        MathJax.Hub.Config({
            tex2jax: {
                inlineMath: [['$','$'], ['\(','\)']],
                displayMath: [['$$','$$'], ['\[','\]']],
                processEscapes: true
            }
        });
        </script>
       <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-AMS_HTML"></script>
        </head>
        <body>
        <div>
        <p>This is an inline math example $e^{i\pi} + 1 = 0$ </p>
<h1>hi lo</h1>
<p>This is a code block with syntax highlighting:</p>
<pre><code class="language-Java">
public void hello_world(){
    print(&quot;Hello, world!&quot;);
    }

hello_world();
</code></pre>
<p>And this is a displayed math example:</p>
<p>$$\sum_{i=1}^{n} i = \\frac{n(n+1)}{2}$$ </p>
        </div>
        </body>
        </html>
    """

    import sys
    import src.wip.md2_viewer as view
    from src.gui.md_filereader import MarkdownLatexViewer
    from src.wip.html_viewer import UltimateMD, UltimateMD_allinone
    from src.gui.ChatHistory import ScrollableWidget, ViewPort
    from src.data.paths import MD_CONTENT
    app = QApplication(sys.argv)
    btn = form()
    
    btn.setFixedSize(500,800)      
    viewer = MarkdownLatexViewer(
        MD_CONTENT)
    scrol_view = ViewPort(300,400)
    btn.setCenterWidget(scrol_view)    
    scrol_view.add_widget(viewer)
 
    
    file = open(GUI_STYLES+"\\dark_mode.css","r")  
    app.setStyleSheet(file.read())
    
    app.exec()
