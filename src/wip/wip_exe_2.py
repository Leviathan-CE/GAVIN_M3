
if __name__ == "__main__":
    from PyQt6.QtWidgets import (
        QApplication,
        QWidget

    )
    import sys
    from src.data.DataBase import DataBase
    from src.gui.widgets.MarkdownLatexViewer import MardownLatexWidget
    db = DataBase()
    app = QApplication(sys.argv)
    print(db.get_last(1)[0][3])
    message:str = db.get_last(4)[2][3]

    viewer = MardownLatexWidget(message)

    viewer.show()
    app.exec()