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
filesArr = []
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
        button1 = QAction(QIcon("./explorer.png"), "1Your button", self)
        button2 = QAction(QIcon("larrow.png"), "2Your button", self)
        button3 = QAction(QIcon("rarrow.png"), "3Your button", self)
        self.ui.actionOtw_rz.triggered.connect(self.openFileExplorer)
        self.ui.actionZamknij.triggered.connect(exit)
        self.ui.actionNast_pny_2.triggered.connect(self.nextImg)
        self.ui.actionPoprzedni_2.triggered.connect(self.prevImg)
        self.ui.menuNie_klikaj.triggered.connect(self.skinnyRatEvent)
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
        files = os.listdir(dialog[0].replace(filename, ""))
        print(files)
        
        print((os.path.splitext(dialog[0]))[1], (os.path.splitext(dialog[0]))[1] in imageExtensions)
        if filename in files and (os.path.splitext(dialog[0]))[1] in imageExtensions:
            
            index = filesArr.index(filename)
            print(index)
            length = len(filesArr)
            print(length)
            if index < length-1:
                dialog = [dialog[0].replace(filename, filesArr[index+1]), "JPG (*.jpg);;BMP (*.bmp);;CUR (*.cur);;GIF (*.gif);;ICNS (*.icns);;ICO (*.ico);;JPEG (*.jpeg);;PBM (*.pbm);;PGM (*.pgm);;PNG (*.png);;PPM (*.ppm);;SVG (*.svg);;SVGZ (*.svgz);;TGA (*.tga);;TIF (*.tif);;TIFF (*.tiff);;WBMP (*.wbmp);;WEBP (*.webp);;XBM (*.xbm);;XPM (*.xpm)"]
            else:
                dialog = [dialog[0].replace(filename, filesArr[0]), "JPG (*.jpg);;BMP (*.bmp);;CUR (*.cur);;GIF (*.gif);;ICNS (*.icns);;ICO (*.ico);;JPEG (*.jpeg);;PBM (*.pbm);;PGM (*.pgm);;PNG (*.png);;PPM (*.ppm);;SVG (*.svg);;SVGZ (*.svgz);;TGA (*.tga);;TIF (*.tif);;TIFF (*.tiff);;WBMP (*.wbmp);;WEBP (*.webp);;XBM (*.xbm);;XPM (*.xpm)"]
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
        files = os.listdir(dialog[0].replace(filename, ""))
        print(files)
        
        print((os.path.splitext(filename))[1], (os.path.splitext(filename))[1] in imageExtensions)
        if filename in files and (os.path.splitext(filename))[1] in imageExtensions:
            index = filesArr.index(filename)
            print(index)
            length = len(filesArr)
            print(length)
            if index < length-1:
                dialog = [dialog[0].replace(filename, filesArr[index-1]), "JPG (*.jpg);;BMP (*.bmp);;CUR (*.cur);;GIF (*.gif);;ICNS (*.icns);;ICO (*.ico);;JPEG (*.jpeg);;PBM (*.pbm);;PGM (*.pgm);;PNG (*.png);;PPM (*.ppm);;SVG (*.svg);;SVGZ (*.svgz);;TGA (*.tga);;TIF (*.tif);;TIFF (*.tiff);;WBMP (*.wbmp);;WEBP (*.webp);;XBM (*.xbm);;XPM (*.xpm)"]
            else:
                dialog = [dialog[0].replace(filename, filesArr[0]), "JPG (*.jpg);;BMP (*.bmp);;CUR (*.cur);;GIF (*.gif);;ICNS (*.icns);;ICO (*.ico);;JPEG (*.jpeg);;PBM (*.pbm);;PGM (*.pgm);;PNG (*.png);;PPM (*.ppm);;SVG (*.svg);;SVGZ (*.svgz);;TGA (*.tga);;TIF (*.tif);;TIFF (*.tiff);;WBMP (*.wbmp);;WEBP (*.webp);;XBM (*.xbm);;XPM (*.xpm)"]
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
        global filesArr
        filesArr = []
        dialog = QFileDialog.getOpenFileName(directory="./galeria", filter="JPG (*.jpg);;BMP (*.bmp);;CUR (*.cur);;GIF (*.gif);;ICNS (*.icns);;ICO (*.ico);;JPEG (*.jpeg);;PBM (*.pbm);;PGM (*.pgm);;PNG (*.png);;PPM (*.ppm);;SVG (*.svg);;SVGZ (*.svgz);;TGA (*.tga);;TIF (*.tif);;TIFF (*.tiff);;WBMP (*.wbmp);;WEBP (*.webp);;XBM (*.xbm);;XPM (*.xpm)")
        print(dialog)
        parsed_url = urlparse(dialog[0])
        print(parsed_url)
        # Uzyskaj ostatni segment ścieżki, który powinien być nazwą pliku
        filename = os.path.basename(parsed_url.path)
        print()
        files = os.listdir(dialog[0].replace(filename, ""))
        print(files)
        for el in files:
            print(el, "Element")
            if (os.path.splitext(el))[1] in imageExtensions:
                print((os.path.splitext(el))[1])
                filesArr.append(el)
        print(filesArr)
        if (os.path.splitext(dialog[0]))[1] in imageExtensions:
            file_path = dialog[0]
            
            img = QPixmap(file_path)
            print(file_path)
            file_size = self.get_image_size(file_path)
            print(file_size)
            self.setFixedSize(file_size[0]+100,file_size[1]+100)
            # Use self.imageContainer instead of local imageContainer
            self.imageContainer.setPixmap(img)
    def skinnyRatEvent(self):
        
        file_path = "./typowyszczur.jpg"
        img = QPixmap(file_path)
        self.imageContainer.setPixmap(img)
app = QApplication(sys.argv)
logowanie = Login()
sys.exit(app.exec())