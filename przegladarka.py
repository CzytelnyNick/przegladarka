from PyQt6.QtWidgets import (
    QApplication,
    QToolBar,
    QMainWindow,
    QWidget,
    QMessageBox,
    QPushButton,
    QLabel,
    QFileDialog,
    QVBoxLayout
)
from PIL import Image
from PyQt6 import QtCore, uic
from PyQt6.QtGui import QPixmap, QAction, QIcon
import sys, os
import subprocess
from urllib.parse import urlparse
imageExtensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"]
class Login(QMainWindow):
    def __init__(self):
        global dialog
        
        global img
        dialog = ["", ""]
        img = QPixmap("selectPhoto.jpg")
        
        super().__init__()
        self.ui = uic.loadUi("przegladarka.ui", self)
        # self.ui.buttonLog.clicked.connect(self.autoryzacja)
        toolbar = QToolBar("My main toolbar")
        button1 = QAction(QIcon("explorer.svg"), "1Your button", self)
        button2 = QAction(QIcon("larrow.svg"), "2Your button", self)
        button3 = QAction(QIcon("rarrow.svg"), "3Your button", self)
        button1.triggered.connect(self.openFileExplorer)
        button2.triggered.connect(self.prevImg)
        button3.triggered.connect(self.nextImg)
        self.addToolBar(toolbar)
        toolbar.addAction(button1)
        toolbar.addAction(button2)
        toolbar.addAction(button3)
        self.imageContainer = QLabel()
        
        
        self.imageContainer.setPixmap(img)
        layout = QVBoxLayout()
        layout.addWidget(self.imageContainer)

        # Tworzenie widgetu z layout'em i ustawienie go jako centralnego widgetu QMainWindow
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        # self.imageContainer.setGeometry(200, 200, 200, 200)
        
        self.show()
    def nextImg(self):
        global imageExtensions
        global dialog
        print(dialog)
        parsed_url = urlparse(dialog[0])
        print(parsed_url)
        # Uzyskaj ostatni segment ścieżki, który powinien być nazwą pliku
        filename = os.path.basename(parsed_url.path)
        print()
        files = os.listdir("./galeria")
        print((os.path.splitext(dialog[0]))[1], (os.path.splitext(dialog[0]))[1] in imageExtensions)
        if filename in files and (os.path.splitext(dialog[0]))[1] in imageExtensions:
            index = files.index(filename)
            print(index)
            length = len(files)-2
            print(length)
            if index <= length:
                dialog = [dialog[0].replace(filename, files[index+1]), "JPG (*.jpg);;BMP (*.bmp);;CUR (*.cur);;GIF (*.gif);;ICNS (*.icns);;ICO (*.ico);;JPEG (*.jpeg);;PBM (*.pbm);;PGM (*.pgm);;PNG (*.png);;PPM (*.ppm);;SVG (*.svg);;SVGZ (*.svgz);;TGA (*.tga);;TIF (*.tif);;TIFF (*.tiff);;WBMP (*.wbmp);;WEBP (*.webp);;XBM (*.xbm);;XPM (*.xpm)"]
            else:
                dialog = [dialog[0].replace(filename, files[0]), "JPG (*.jpg);;BMP (*.bmp);;CUR (*.cur);;GIF (*.gif);;ICNS (*.icns);;ICO (*.ico);;JPEG (*.jpeg);;PBM (*.pbm);;PGM (*.pgm);;PNG (*.png);;PPM (*.ppm);;SVG (*.svg);;SVGZ (*.svgz);;TGA (*.tga);;TIF (*.tif);;TIFF (*.tiff);;WBMP (*.wbmp);;WEBP (*.webp);;XBM (*.xbm);;XPM (*.xpm)"]
            print(dialog)
            file_path = dialog[0]
            

            img = QPixmap(file_path)
            file_size = self.get_image_size(file_path)
            print(file_size)
            self.setFixedSize(file_size[0]+100,file_size[1]+100)
            self.imageContainer.setPixmap(img)
    def prevImg(self):
        global imageExtensions
        global dialog
        print(dialog)
        parsed_url = urlparse(dialog[0])
        print(parsed_url)
        # Uzyskaj ostatni segment ścieżki, który powinien być nazwą pliku
        filename = os.path.basename(parsed_url.path)
        print()
        files = os.listdir("./galeria")
        print((os.path.splitext(filename))[1], (os.path.splitext(filename))[1] in imageExtensions)
        if filename in files and (os.path.splitext(filename))[1] in imageExtensions:
            index = files.index(filename)
            print(index)
            length = len(files)-2
            print(length)
            if index <= length:
                dialog = [dialog[0].replace(filename, files[index-1]), "JPG (*.jpg);;BMP (*.bmp);;CUR (*.cur);;GIF (*.gif);;ICNS (*.icns);;ICO (*.ico);;JPEG (*.jpeg);;PBM (*.pbm);;PGM (*.pgm);;PNG (*.png);;PPM (*.ppm);;SVG (*.svg);;SVGZ (*.svgz);;TGA (*.tga);;TIF (*.tif);;TIFF (*.tiff);;WBMP (*.wbmp);;WEBP (*.webp);;XBM (*.xbm);;XPM (*.xpm)"]
            else:
                dialog = [dialog[0].replace(filename, files[0]), "JPG (*.jpg);;BMP (*.bmp);;CUR (*.cur);;GIF (*.gif);;ICNS (*.icns);;ICO (*.ico);;JPEG (*.jpeg);;PBM (*.pbm);;PGM (*.pgm);;PNG (*.png);;PPM (*.ppm);;SVG (*.svg);;SVGZ (*.svgz);;TGA (*.tga);;TIF (*.tif);;TIFF (*.tiff);;WBMP (*.wbmp);;WEBP (*.webp);;XBM (*.xbm);;XPM (*.xpm)"]
            print(dialog)
            file_path = dialog[0]
            

            img = QPixmap(file_path)
            file_size = self.get_image_size(file_path)
            print(file_size)
            self.setFixedSize(file_size[0]+100,file_size[1]+100)
            self.imageContainer.setPixmap(img)
    def get_image_size(self, file_path):
            try:
                if (os.path.splitext(file_path))[1] in imageExtensions:
                    with Image.open(file_path) as img:
                        width, height = img.size
                        return width, height
            except Exception as e:
                print(f"Błąd: {e}")
                return None

    def openFileExplorer(self):
        global dialog
        global imageExtensions
        
        dialog = QFileDialog.getOpenFileName(directory="./galeria", filter="JPG (*.jpg);;BMP (*.bmp);;CUR (*.cur);;GIF (*.gif);;ICNS (*.icns);;ICO (*.ico);;JPEG (*.jpeg);;PBM (*.pbm);;PGM (*.pgm);;PNG (*.png);;PPM (*.ppm);;SVG (*.svg);;SVGZ (*.svgz);;TGA (*.tga);;TIF (*.tif);;TIFF (*.tiff);;WBMP (*.wbmp);;WEBP (*.webp);;XBM (*.xbm);;XPM (*.xpm)")
        print(dialog)
        if (os.path.splitext(dialog[0]))[1] in imageExtensions:
            file_path = dialog[0]
            
            img = QPixmap(file_path)
            print(file_path)
            file_size = self.get_image_size(file_path)
            print(file_size)
            self.setFixedSize(file_size[0]+100,file_size[1]+100)
            # Use self.imageContainer instead of local imageContainer
            self.imageContainer.setPixmap(img)

app = QApplication(sys.argv)
logowanie = Login()
sys.exit(app.exec())