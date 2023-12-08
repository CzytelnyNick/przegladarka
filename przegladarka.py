from PyQt6.QtWidgets import (
    QApplication,
    QToolBar,
    QMainWindow,
    QWidget,
    QMessageBox,
    QPushButton,
    QLabel,
    QFileDialog,
)
from PyQt6 import QtCore, uic
from PyQt6.QtGui import QPixmap, QAction, QIcon
import sys
import subprocess


class Login(QMainWindow):
    def __init__(self):
        dialog = ""
        
        super().__init__()
        self.ui = uic.loadUi("przegladarka.ui", self)
        # self.ui.buttonLog.clicked.connect(self.autoryzacja)
        toolbar = QToolBar("My main toolbar")
        button1 = QAction(QIcon("explorer.svg"), "1Your button", self)
        button2 = QAction(QIcon("larrow.svg"), "2Your button", self)
        button3 = QAction(QIcon("rarrow.svg"), "3Your button", self)
        button1.triggered.connect(self.openFileExplorer)
        self.addToolBar(toolbar)
        toolbar.addAction(button1)
        toolbar.addAction(button2)
        toolbar.addAction(button3)
        imageContainer = QLabel()
        img = QPixmap(dialog)
        imageContainer.setPixmap(img)
        print(dialog)
        
        
        self.show()

    def openFileExplorer(self):
        global dialog
        dialog = QFileDialog.getOpenFileName(directory="C:\\Users\\4TP2\\Desktop\\python\\designer\\galeria")
        print(dialog[0])
        dialog = dialog[0]


app = QApplication(sys.argv)
logowanie = Login()
sys.exit(app.exec())
