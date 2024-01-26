from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFrame

app = QApplication([])

# Create a QWidget
widget = QWidget()

# Create a QVBoxLayout
layout = QVBoxLayout(widget)

# Create a header
header = QFrame()
header.setFixedHeight(50)  # Set the height of the header
# Set the background color of the header
header.setStyleSheet("background-color: blue;")

# Create widgets for items
item1 = QPushButton("Item 1")
item2 = QPushButton("Item 2")

# Add widgets to the layout
layout.addWidget(header)
layout.addWidget(item1)
layout.addWidget(item2)

widget.show()
app.exec()
