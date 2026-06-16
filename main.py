import sys
import cv2
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtGui import QPixmap
from menu_tarea import Ui_MainWindow

class MiApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  
        self.ui.setupUi(self)

        
        self.ui.pushButton.clicked.connect(self.activar)
        self.ui.pushButton_2.clicked.connect(self.desactivar)

        
        self.ui.actionCargar_Imagen.triggered.connect(self.cargar_imagen)
        self.ui.actionAbrir_Camara.triggered.connect(self.abrir_camara)
        self.ui.actionSalir.triggered.connect(self.close)

    def activar(self):
        print("Activado")

    def desactivar(self):
        print("Desactivado")

    def cargar_imagen(self):
        ruta, _ = QFileDialog.getOpenFileName(self, "Abrir imagen", "", "Imágenes (*.png *.jpg *.bmp)")
        if ruta:
            print(f"Imagen cargada: {ruta}")

    def abrir_camara(self):
        print("Abrir cámara")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MiApp()
    ventana.show()
    sys.exit(app.exec())