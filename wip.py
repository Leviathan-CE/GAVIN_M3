from src.gui.Buttons import BTNMenu
from src.gui.widgets import form
from src.gui.html_viewer import UltimateMD
from PyQt6.QtWidgets import (
    QApplication

)

from src.data.paths import GUI_STYLES
if __name__ == "__main__":
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
    latex_content = """
    $x+4/3 = 0$
    """
    import sys
    import src.gui.md2_viewer as view
    app = QApplication(sys.argv)
    btn = form() 
    btn.setFixedSize(500,800)      
    viewer = UltimateMD(markdown_content)
    btn.setCenterWidget(viewer)
    viewer.show()
    file = open(GUI_STYLES+"\\dark_mode.css","r")  
    app.setStyleSheet(file.read())
    app.exec()
