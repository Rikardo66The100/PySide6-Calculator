from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QGridLayout,
    QLabel,
    QPushButton,
    QLineEdit,
)

from PySide6.QtCore import Qt

from PySide6.QtGui import (
    QFont,
    QFontDatabase
)

from pathlib import Path

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        PathFont = Path(__file__).resolve().parent.parent / "assets" / "Xolonium-pn4D.ttf"

        IdFont = QFontDatabase.addApplicationFont(str(PathFont))

        FamilyFont = QFontDatabase.applicationFontFamilies(IdFont)[0]

        self.CustomFont = QFont(FamilyFont)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setGeometry(1250, 250, 600, 400)

        self.LayoutMain = QVBoxLayout()
        self.LayoutMain.setContentsMargins(0, 0, 0, 0)

        self.BarFrame = QWidget()
        self.BarFrame.setStyleSheet(
            """
            background-color: #000000;
            """
        )

        self.LayoutFrame = QHBoxLayout()
        self.LayoutFrame.setContentsMargins(0, 0, 0, 0)

        self.LabelFrameTitle = QLabel("Hello")
        self.LabelFrameTitle.setFont(QFont(self.CustomFont))
        self.LabelFrameTitle.setStyleSheet(
            """
            background-color: #000000;
            color: #ffffff;
            """
        )

        self.ButtonMinimize = QPushButton("\uE921")
        self.ButtonMinimize.setFixedSize(50, 50)
        self.ButtonMinimize.setToolTip("Minimize")
        self.ButtonMinimize.setFont(QFont("Segoe MDL2 Assets"))
        self.ButtonMinimize.setStyleSheet(
            """
            background-color: #000000;
            """
        )

        self.ButtonMaximize = QPushButton("\uE922")
        self.ButtonMaximize.setFixedSize(50, 50)
        self.ButtonMaximize.setDisabled(True)
        self.ButtonMaximize.setFont(QFont("Segoe MDL2 Assets"))
        self.ButtonMaximize.setStyleSheet(
            """
            background-color: #000000;
            """
        )

        self.ButtonClose = QPushButton("\uE8BB")
        self.ButtonClose.setFixedSize(50, 50)
        self.ButtonClose.setToolTip("Close")
        self.ButtonClose.setFont(QFont("Segoe MDL2 Assets"))
        self.ButtonClose.setStyleSheet(
            """
            background-color: #000000;
            """
        )

        self.LayoutFrame.addWidget(self.LabelFrameTitle)
        self.LayoutFrame.addStretch()
        self.LayoutFrame.addWidget(self.ButtonMinimize)
        self.LayoutFrame.addWidget(self.ButtonMaximize)
        self.LayoutFrame.addWidget(self.ButtonClose)

        self.BarFrame.setLayout(self.LayoutFrame)

        self.Display = QLineEdit("")
        self.Display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.Display.setReadOnly(True)
        self.Display.setStyleSheet(
            """
            background-color: #ffffff;
            font-size: 32px;
            """
        )

        self.LayoutGrid = QGridLayout()

        self.ButtonForMain = [
            ("7", 0, 0),
            ("8", 0, 1),
            ("9", 0, 2),
            ("+", 0, 3),
            ("4", 1, 0),
            ("5", 1, 1),
            ("6", 1, 2),
            ("-", 1, 3),
            ("1", 2, 0),
            ("2", 2, 1),
            ("3", 2, 2),
            ("*", 2, 3),
            ("C", 3, 0),
            ("0", 3, 1),
            ("=", 3, 2),
            ("/", 3, 3)
        ]

        for text, row, col in self.ButtonForMain:
            self.ButtonMain = QPushButton(text)
            self.ButtonMain.setFixedSize(50, 50)
            self.ButtonMain.clicked.connect(lambda _, t = text: self.ClickedButtonMain(t))
            self.LayoutGrid.addWidget(self.ButtonMain, row, col)

        self.LayoutMain.addWidget(self.BarFrame)
        self.LayoutMain.addWidget(self.Display)
        self.LayoutMain.addLayout(self.LayoutGrid)

        self.setLayout(self.LayoutMain)

        self.show()

app = QApplication()

window = Calculator()

app.exec()