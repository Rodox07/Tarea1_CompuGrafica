import sys
import cv2
import numpy as np
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import QTimer
from PySide6.QtGui import QImage, QPixmap, QAction
from menu_tarea import Ui_MainWindow

class MiApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  
        self.ui.setupUi(self)

        # 1. Variables de control
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.actualizar_frame)
        self.cap = None
        self.imagen_original = None  # Guarda el frame puro de la cámara o la imagen cargada
        self.deteccion_activada = False
        self.bordes_activado = False  # Controla el bonus de bordes/suavizado de forma independiente
        
        # Cargar el modelo Haar Cascade para detección facial (viene con OpenCV)
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # 2. Configurar rangos iniciales de los Sliders
        # horizontalSlider = Umbral para imagen binaria (0 a 255)
        self.ui.horizontalSlider.setRange(0, 255)
        self.ui.horizontalSlider.setValue(127) 
        
        # Traslación X e Y (-200 a 200 pixeles)
        self.ui.horizontalSlider_2.setRange(-200, 200)
        self.ui.horizontalSlider_2.setValue(0)
        self.ui.horizontalSlider_3.setRange(-200, 200)
        self.ui.horizontalSlider_3.setValue(0)
        
        # Rotación (-180 a 180 grados)
        self.ui.horizontalSlider_4.setRange(-180, 180)
        self.ui.horizontalSlider_4.setValue(0)
        
        # Escalado (1% a 200%)
        self.ui.horizontalSlider_5.setRange(1, 200)
        self.ui.horizontalSlider_5.setValue(100)

        # 3. Conexión de botones y menú
        self.ui.pushButton.clicked.connect(self.activar)
        self.ui.pushButton_2.clicked.connect(self.desactivar)
        self.ui.actionCargar_Imagen.triggered.connect(self.cargar_imagen)
        self.ui.actionAbrir_Camara.triggered.connect(self.abrir_camara)
        self.ui.actionSalir.triggered.connect(self.close)

        # --- Control independiente para el bonus de Bordes/Suavizado ---
        # Como no hay un botón propio para esto en el diseño original, lo agregamos
        # como una opción de menú (checkable) que el usuario puede activar/desactivar a voluntad.
        self.menu_efectos = self.menuBar().addMenu("Efectos")
        self.action_bordes = QAction("Detección de bordes / Suavizado", self)
        self.action_bordes.setCheckable(True)
        self.action_bordes.setChecked(False)
        self.action_bordes.toggled.connect(self.toggle_bordes)
        self.menu_efectos.addAction(self.action_bordes)

        # 4. Conectar los sliders y combobox para que actualicen la imagen en tiempo real
        self.ui.comboBox.currentIndexChanged.connect(self.procesar_y_mostrar)
        self.ui.horizontalSlider.valueChanged.connect(self.procesar_y_mostrar)
        self.ui.horizontalSlider_2.valueChanged.connect(self.procesar_y_mostrar)
        self.ui.horizontalSlider_3.valueChanged.connect(self.procesar_y_mostrar)
        self.ui.horizontalSlider_4.valueChanged.connect(self.procesar_y_mostrar)
        self.ui.horizontalSlider_5.valueChanged.connect(self.procesar_y_mostrar)

    # --- FUNCIONES DE CONTROL ---

    def activar(self):
        self.deteccion_activada = True
        self.procesar_y_mostrar()

    def desactivar(self):
        self.deteccion_activada = False
        self.procesar_y_mostrar()

    def toggle_bordes(self, activado):
        self.bordes_activado = activado
        self.procesar_y_mostrar()

    def cargar_imagen(self):
        # Si la cámara estaba abierta, la detenemos
        if self.timer.isActive():
            self.timer.stop()
            if self.cap:
                self.cap.release()

        ruta, _ = QFileDialog.getOpenFileName(self, "Abrir imagen", "", "Imágenes (*.png *.jpg *.bmp *.jpeg)")
        if ruta:
            # OpenCV lee en formato BGR
            img = cv2.imread(ruta)
            if img is not None:
                self.imagen_original = img
                self.procesar_y_mostrar()

    def abrir_camara(self):
        self.cap = cv2.VideoCapture(0)
        if self.cap.isOpened():
            self.timer.start(30) # Captura un frame cada 30 ms (aprox 30 FPS)

    def actualizar_frame(self):
        if self.cap is not None:
            ret, frame = self.cap.read()
            if ret:
                self.imagen_original = frame
                self.procesar_y_mostrar()

    # --- EL "MOTOR" MATEMÁTICO Y DE PROCESAMIENTO ---

    def procesar_y_mostrar(self):
        if self.imagen_original is None:
            return

        # Trabajamos sobre una copia para no destruir el frame original
        img = self.imagen_original.copy()
        alto, ancho = img.shape[:2]

        # 1. Transformaciones Geométricas
        escala = self.ui.horizontalSlider_5.value() / 100.0
        tx = self.ui.horizontalSlider_2.value()
        ty = self.ui.horizontalSlider_3.value()
        angulo = self.ui.horizontalSlider_4.value()

        # El truco: getRotationMatrix2D permite aplicar rotación y escala al mismo tiempo
        centro = (ancho // 2, alto // 2)
        matriz_transformacion = cv2.getRotationMatrix2D(centro, angulo, escala)
        
        # Añadir traslación (X e Y) a la matriz resultante
        matriz_transformacion[0, 2] += tx
        matriz_transformacion[1, 2] += ty

        # Aplicamos la transformación manteniendo el tamaño original del lienzo
        # Así evitamos que la interfaz gráfica nos anule el efecto visual
        img = cv2.warpAffine(img, matriz_transformacion, (ancho, alto))

        # 2. Conversión de Color / Filtros
        opcion_color = self.ui.comboBox.currentIndex()
        
        if opcion_color == 0:
            # RGB (Recuerda que OpenCV usa BGR, por lo que para mostrarlo debemos pasarlo a RGB)
            img_final = img.copy() 
            img_mostrar = cv2.cvtColor(img_final, cv2.COLOR_BGR2RGB)
            imagen_grises_para_hist = cv2.cvtColor(img_final, cv2.COLOR_BGR2GRAY) # Necesario para el histograma
        
        elif opcion_color == 1:
            # Escala de Grises
            img_final = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img_mostrar = img_final
            imagen_grises_para_hist = img_final
            
        elif opcion_color == 2:
            # Binaria
            umbral = self.ui.horizontalSlider.value()
            img_grises = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            _, img_final = cv2.threshold(img_grises, umbral, 255, cv2.THRESH_BINARY)
            img_mostrar = img_final
            imagen_grises_para_hist = img_final

        # 3. Detección Facial (Color Azul)
        if self.deteccion_activada:
            # Haar Cascade necesita una imagen en blanco y negro para detectar
            if len(img_final.shape) == 3:
                gris_deteccion = cv2.cvtColor(img_final, cv2.COLOR_BGR2GRAY)
            else:
                gris_deteccion = img_final
                
            rostros = self.face_cascade.detectMultiScale(gris_deteccion, 1.1, 4)
            
            for (x, y, w, h) in rostros:
                if len(img_mostrar.shape) == 3:
                    # En formato RGB, el azul puro es (0, 0, 255)
                    cv2.rectangle(img_mostrar, (x, y), (x+w, y+h), (0, 0, 255), 2)
                else:
                    # Si está en escala de grises o binario, dibujamos el rectángulo blanco/negro
                    cv2.rectangle(img_mostrar, (x, y), (x+w, y+h), (255, 255, 255), 2)

        # 3b. BONUS: Procesamiento adicional de la imagen (Detección de bordes - Canny)
        # Se activa/desactiva de forma independiente desde el menú "Efectos".
        if self.bordes_activado:
            # Suavizamos un poco antes de buscar bordes, para reducir ruido (paso de preprocesamiento clásico)
            if len(img_final.shape) == 3:
                gris_bordes = cv2.cvtColor(img_final, cv2.COLOR_BGR2GRAY)
            else:
                gris_bordes = img_final

            gris_suavizado = cv2.GaussianBlur(gris_bordes, (5, 5), 0)
            bordes = cv2.Canny(gris_suavizado, 80, 160)

            if len(img_mostrar.shape) == 3:
                # Resaltamos los bordes detectados en verde sobre la imagen mostrada
                img_mostrar[bordes != 0] = (0, 255, 0)
            else:
                # En escala de grises o binario, los bordes se marcan en blanco puro
                img_mostrar[bordes != 0] = 255

        # 4. Mostrar Imagen Principal
        self.mostrar_en_label(img_mostrar, self.ui.label_imagen_original)

        # 5. Calcular y mostrar Histograma
        self.dibujar_histograma(imagen_grises_para_hist)

    def dibujar_histograma(self, img_grises):
        # Dimensiones del QLabel donde va el histograma (281x161 según tu UI)
        hist_w = 281
        hist_h = 161
        imagen_hist = np.zeros((hist_h, hist_w, 3), dtype=np.uint8)

        # Calcular histograma (solo 1 canal, 256 bins, rango 0-256)
        hist = cv2.calcHist([img_grises], [0], None, [256], [0, 256])
        cv2.normalize(hist, hist, 0, hist_h, cv2.NORM_MINMAX)

        bin_w = int(round(hist_w / 256))

        # Dibujar líneas blancas para el histograma
        for i in range(1, 256):
            # CORRECCIÓN APLICADA: Extracción del escalar [0]
            valor_anterior = int(hist[i - 1][0])
            valor_actual = int(hist[i][0])
            
            cv2.line(imagen_hist, 
                     (bin_w * (i - 1), hist_h - valor_anterior),
                     (bin_w * i, hist_h - valor_actual), 
                     (255, 255, 255), 2)

        # Mostrar histograma en la interfaz (es una imagen BGR que pasamos a RGB)
        self.mostrar_en_label(cv2.cvtColor(imagen_hist, cv2.COLOR_BGR2RGB), self.ui.histogramas)

    def mostrar_en_label(self, img_array, label_widget):
        # Convierte el arreglo Numpy de OpenCV al formato QPixmap de PySide6
        if len(img_array.shape) == 3:
            alto, ancho, canales = img_array.shape
            bytes_por_linea = canales * ancho
            formato = QImage.Format_RGB888
        else:
            alto, ancho = img_array.shape
            bytes_por_linea = ancho
            formato = QImage.Format_Grayscale8

        imagen_qt = QImage(img_array.data, ancho, alto, bytes_por_linea, formato)
        pixmap = QPixmap.fromImage(imagen_qt)
        
        # Insertar imagen y decirle al label que ajuste el tamaño
        label_widget.setPixmap(pixmap)
        label_widget.setScaledContents(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MiApp()
    ventana.show()
    sys.exit(app.exec())
