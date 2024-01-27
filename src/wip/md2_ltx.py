from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import QWidget, QSizePolicy, QApplication, QMainWindow, QVBoxLayout, QScrollArea, QLabel
from PyQt5.QtWebEngineWidgets import QWebEngineView


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Scrollable Main Window")

        # Create a central widget
        central_widget = QWidget(self)
        central_layout = QVBoxLayout(central_widget)
        central_widget.setLayout(central_layout)

        # Add regular widgets to the layout (for demonstration purposes)
        label1 = QLabel("Regular Label 1")
        central_layout.addWidget(label1)

        label2 = QLabel("Regular Label 2")
        central_layout.addWidget(label2)

        # Add a QWebEngineView to the layout
        webview = QWebEngineView(self)
        webview.load(QUrl('https://www.example.com'))

        # Set size policy to Expanding so that QWebEngineView can take up available space
        webview.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        central_layout.addWidget(webview)

        label3 = QLabel("Regular Label 3")
        central_layout.addWidget(label3)

        # Create a scroll area and set the central widget
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(central_widget)

        # Set the scroll area as the central widget
        self.setCentralWidget(scroll_area)


if __name__ == "__main__":
    app = QApplication([])

    main_window = MainWindow()
    main_window.showMaximized()

    app.exec()
