from src.gui.Buttons import BTNMenu
from src.gui.widgets import form
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
    import sys
    app = QApplication(sys.argv)
    btn = form()   
    
    file = open(GUI_STYLES+"\\dark_mode.css","r")  
    app.setStyleSheet(file.read())
    app.exec()
