import markdown
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit
from PyQt6.QtGui import QPixmap 
from PyQt6.QtWebEngineWidgets import QWebEngineView
import sys
import matplotlib.pyplot as plt
import io
import re


class UltimateMD(QWidget):
    def __init__(self, content: str):
        super().__init__()


        # Define a regular expression pattern with the delimiters
        delimiter_pattern = r'\$\$|\$'

        # Use re.split() to split the string based on the pattern
        blocks = re.split(delimiter_pattern, content)
        # Split the content into blocks using triple backticks
        # blocks = content.split(["$","$$"])

        # Create a layout to hold the widgets
        layout = QVBoxLayout(self)

        # Loop through the blocks
        for i, block in enumerate(blocks):
            print(block)
            # If the block is even, it's a Markdown block
            if i % 2 == 0:
                html_content = markdown.markdown(block,extensions=['fenced_code'])
                label = QTextEdit()
                label.setHtml(html_content)
                layout.addWidget(label)

            # If the block is odd, it's a latex block
            elif len(block) != 0:
                fig, ax = plt.subplots(figsize=[5,1])
                ax.text(0.5, 0.5, f"${block}$", size=20, ha='center', va='center')
                ax.axis('off')

                # Convert the figure to a QPixmap
                buffer = io.BytesIO()
                plt.savefig(buffer, format='png',
                            bbox_inches='tight', pad_inches=0)
                buffer.seek(0)
                pixmap = QPixmap()
                pixmap.loadFromData(buffer.read())

                # Create QLabel to display the rendered image
                label = QLabel()
                label.setPixmap(pixmap)
                layout.addWidget(label)

        self.setLayout(layout)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Your content
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
    sys.exit(app.exec())
