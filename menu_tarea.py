# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu_tarea.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSlider, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionCargar_Imagen = QAction(MainWindow)
        self.actionCargar_Imagen.setObjectName(u"actionCargar_Imagen")
        self.actionAbrir_Camara = QAction(MainWindow)
        self.actionAbrir_Camara.setObjectName(u"actionAbrir_Camara")
        self.actionSalir = QAction(MainWindow)
        self.actionSalir.setObjectName(u"actionSalir")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(40, 20, 271, 171))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label_imagen_original = QLabel(self.frame)
        self.label_imagen_original.setObjectName(u"label_imagen_original")
        self.label_imagen_original.setGeometry(QRect(0, 0, 271, 171))
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(141, 250, 371, 26))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(390, 220, 81, 26))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(180, 220, 111, 26))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(100, 360, 111, 16))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(100, 340, 111, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 290, 111, 16))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(280, 200, 91, 16))
        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(149, 280, 361, 20))
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(230, 320, 321, 84))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSlider_2 = QSlider(self.layoutWidget)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout.addWidget(self.horizontalSlider_2)

        self.horizontalSlider_3 = QSlider(self.layoutWidget)
        self.horizontalSlider_3.setObjectName(u"horizontalSlider_3")
        self.horizontalSlider_3.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout.addWidget(self.horizontalSlider_3)

        self.horizontalSlider_4 = QSlider(self.layoutWidget)
        self.horizontalSlider_4.setObjectName(u"horizontalSlider_4")
        self.horizontalSlider_4.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout.addWidget(self.horizontalSlider_4)

        self.horizontalSlider_5 = QSlider(self.layoutWidget)
        self.horizontalSlider_5.setObjectName(u"horizontalSlider_5")
        self.horizontalSlider_5.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout.addWidget(self.horizontalSlider_5)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(340, 20, 281, 171))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.histogramas = QLabel(self.frame_2)
        self.histogramas.setObjectName(u"histogramas")
        self.histogramas.setGeometry(QRect(-2, 5, 281, 161))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(100, 320, 111, 16))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(100, 380, 111, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionCargar_Imagen)
        self.menuArchivo.addAction(self.actionAbrir_Camara)
        self.menuArchivo.addAction(self.actionSalir)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionCargar_Imagen.setText(QCoreApplication.translate("MainWindow", u"Cargar Imagen", None))
        self.actionAbrir_Camara.setText(QCoreApplication.translate("MainWindow", u"Abrir Camara", None))
        self.actionSalir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.label_imagen_original.setText("")
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"RGB", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Escala de Grises", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Binaria", None))

        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Desactivar", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Activar", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Rotaci\u00f3n", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Traslaci\u00f3n Y", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Transformaci\u00f3nes", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Detecci\u00f3n Facial", None))
        self.histogramas.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Traslaci\u00f3n X", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Escalado (%)", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

