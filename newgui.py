import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QFrame, QGridLayout, QLabel, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Web Viewer")

        # Create web view
        self.webview = QWebEngineView()
        self.webview.load(QUrl("https://www.google.com"))

        # Create navigation buttons
        self.forward_button = QPushButton("Forward")
        self.forward_button.clicked.connect(lambda: print("Forward button clicked"))
        self.backward_button = QPushButton("Backward")
        self.backward_button.clicked.connect(lambda: print("Backward button clicked"))
        self.left_button = QPushButton("Left")
        self.left_button.clicked.connect(lambda: print("Left button clicked"))
        self.right_button = QPushButton("Right")
        self.right_button.clicked.connect(lambda: print("Right button clicked"))
        self.stop_button = QPushButton("Stop")
        self.stop_button.clicked.connect(lambda: print("Stop button clicked"))
        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.send_text)

        # Create text input field
        self.input_field = QLineEdit()
        self.input_field.returnPressed.connect(self.send_text)

        # Create layout
        layout = QGridLayout()
        layout.addWidget(self.forward_button, 0, 1)
        layout.addWidget(self.left_button, 1, 0)
        layout.addWidget(self.stop_button, 1, 1)
        layout.addWidget(self.right_button, 1, 2)
        layout.addWidget(self.backward_button, 2, 1)
        layout.addWidget(self.input_field, 3, 0, 1, 2)
        layout.addWidget(self.send_button, 3, 2)
        layout.addWidget(self.webview, 4, 0, 1, 3)

        # Set layout
        self.setLayout(layout)

    def send_text(self):
        text = self.input_field.text()
        self.webview.load(QUrl(text))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

