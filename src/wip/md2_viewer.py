from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt6.QtGui import QPixmap
import sys
import matplotlib.pyplot as plt
import io


class LaTeXWidget(QWidget):
    def __init__(self, latex_content):
        super().__init__()

        # Render LaTeX content using matplotlib
        fig, ax = plt.subplots()
        ax.text(0.5, 0.5, f"${latex_content}$",
                size=20, ha='center', va='center')
        ax.axis('off')

        # Convert the figure to a QPixmap
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png', bbox_inches='tight', pad_inches=0)
        buffer.seek(0)
        pixmap = QPixmap()
        pixmap.loadFromData(buffer.read())

        # Create QLabel to display the rendered image
        label = QLabel()
        label.setPixmap(pixmap)

        # Set up layout
        layout = QVBoxLayout(self)
        layout.addWidget(label)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Your LaTeX content
    latex_content = "e^{i\pi} + 1 = 0"

    viewer = LaTeXWidget(latex_content)
    viewer.show()

    sys.exit(app.exec())
