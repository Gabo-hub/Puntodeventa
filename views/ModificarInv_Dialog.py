# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ModificarInv_Dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_ModifiProducto(object):
    def setupUi(self, ModifiProducto):
        if not ModifiProducto.objectName():
            ModifiProducto.setObjectName(u"ModifiProducto")
        ModifiProducto.resize(449, 452)
        self.verticalLayout = QVBoxLayout(ModifiProducto)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabPrctos_body_frame = QFrame(ModifiProducto)
        self.tabPrctos_body_frame.setObjectName(u"tabPrctos_body_frame")
        self.tabPrctos_body_frame.setStyleSheet(u"QLineEdit {\n"
"	border-radius: 10px;\n"
"	padding: 5px 10px;\n"
"	background-color: rgb(255,255,255);\n"
"	color: rgb(0,0,0);\n"
"}\n"
"QFrame {\n"
"	border-radius:10px;\n"
"	background-color: rgb(242, 243, 245);\n"
"}")
        self.tabPrctos_body_frame.setFrameShape(QFrame.StyledPanel)
        self.tabPrctos_body_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.tabPrctos_body_frame)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalSpacer_3 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_3)

        self.codigoPrctoModifi_label = QLabel(self.tabPrctos_body_frame)
        self.codigoPrctoModifi_label.setObjectName(u"codigoPrctoModifi_label")
        font = QFont()
        font.setFamilies([u"Gotham"])
        font.setPointSize(10)
        self.codigoPrctoModifi_label.setFont(font)

        self.verticalLayout_13.addWidget(self.codigoPrctoModifi_label)

        self.codigoPrctoModifi_lineE = QLineEdit(self.tabPrctos_body_frame)
        self.codigoPrctoModifi_lineE.setObjectName(u"codigoPrctoModifi_lineE")

        self.verticalLayout_13.addWidget(self.codigoPrctoModifi_lineE)

        self.nombrePrctoModifi_label = QLabel(self.tabPrctos_body_frame)
        self.nombrePrctoModifi_label.setObjectName(u"nombrePrctoModifi_label")
        self.nombrePrctoModifi_label.setFont(font)

        self.verticalLayout_13.addWidget(self.nombrePrctoModifi_label)

        self.nombrePrctoModifi_lineE = QLineEdit(self.tabPrctos_body_frame)
        self.nombrePrctoModifi_lineE.setObjectName(u"nombrePrctoModifi_lineE")

        self.verticalLayout_13.addWidget(self.nombrePrctoModifi_lineE)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.cantidadPrctoModifi_label = QLabel(self.tabPrctos_body_frame)
        self.cantidadPrctoModifi_label.setObjectName(u"cantidadPrctoModifi_label")
        self.cantidadPrctoModifi_label.setFont(font)

        self.horizontalLayout_12.addWidget(self.cantidadPrctoModifi_label)

        self.cantidadCritPrctoModifi_label = QLabel(self.tabPrctos_body_frame)
        self.cantidadCritPrctoModifi_label.setObjectName(u"cantidadCritPrctoModifi_label")
        self.cantidadCritPrctoModifi_label.setFont(font)

        self.horizontalLayout_12.addWidget(self.cantidadCritPrctoModifi_label)


        self.verticalLayout_13.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.cantidadProctoModifi_lineE = QLineEdit(self.tabPrctos_body_frame)
        self.cantidadProctoModifi_lineE.setObjectName(u"cantidadProctoModifi_lineE")
        self.cantidadProctoModifi_lineE.setFrame(True)

        self.horizontalLayout_17.addWidget(self.cantidadProctoModifi_lineE)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_7)

        self.cantidadCritPrctoModifi_lineE = QLineEdit(self.tabPrctos_body_frame)
        self.cantidadCritPrctoModifi_lineE.setObjectName(u"cantidadCritPrctoModifi_lineE")

        self.horizontalLayout_17.addWidget(self.cantidadCritPrctoModifi_lineE)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_8)


        self.verticalLayout_13.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.precioCompraPrctoModifi_label = QLabel(self.tabPrctos_body_frame)
        self.precioCompraPrctoModifi_label.setObjectName(u"precioCompraPrctoModifi_label")
        self.precioCompraPrctoModifi_label.setFont(font)

        self.horizontalLayout_15.addWidget(self.precioCompraPrctoModifi_label)

        self.precioVentaPrctoModifi_label = QLabel(self.tabPrctos_body_frame)
        self.precioVentaPrctoModifi_label.setObjectName(u"precioVentaPrctoModifi_label")
        self.precioVentaPrctoModifi_label.setFont(font)

        self.horizontalLayout_15.addWidget(self.precioVentaPrctoModifi_label)


        self.verticalLayout_13.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.precioCompraPrctoModifi_lineE = QLineEdit(self.tabPrctos_body_frame)
        self.precioCompraPrctoModifi_lineE.setObjectName(u"precioCompraPrctoModifi_lineE")

        self.horizontalLayout_16.addWidget(self.precioCompraPrctoModifi_lineE)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_5)

        self.precioVentaPrctoModifi_lineE = QLineEdit(self.tabPrctos_body_frame)
        self.precioVentaPrctoModifi_lineE.setObjectName(u"precioVentaPrctoModifi_lineE")

        self.horizontalLayout_16.addWidget(self.precioVentaPrctoModifi_lineE)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_6)


        self.verticalLayout_13.addLayout(self.horizontalLayout_16)

        self.descuentoPrctoModifi_label = QLabel(self.tabPrctos_body_frame)
        self.descuentoPrctoModifi_label.setObjectName(u"descuentoPrctoModifi_label")
        self.descuentoPrctoModifi_label.setFont(font)

        self.verticalLayout_13.addWidget(self.descuentoPrctoModifi_label)

        self.descuentoPrctoModifi_lineE = QLineEdit(self.tabPrctos_body_frame)
        self.descuentoPrctoModifi_lineE.setObjectName(u"descuentoPrctoModifi_lineE")
        self.descuentoPrctoModifi_lineE.setFrame(False)

        self.verticalLayout_13.addWidget(self.descuentoPrctoModifi_lineE)

        self.medidaPrctoModifi_label = QLabel(self.tabPrctos_body_frame)
        self.medidaPrctoModifi_label.setObjectName(u"medidaPrctoModifi_label")
        self.medidaPrctoModifi_label.setFont(font)

        self.verticalLayout_13.addWidget(self.medidaPrctoModifi_label)

        self.medidaPrctoModifi_comboB = QComboBox(self.tabPrctos_body_frame)
        self.medidaPrctoModifi_comboB.setObjectName(u"medidaPrctoModifi_comboB")
        font1 = QFont()
        font1.setFamilies([u"Poppins"])
        font1.setPointSize(9)
        self.medidaPrctoModifi_comboB.setFont(font1)
        self.medidaPrctoModifi_comboB.setStyleSheet(u"border-radius: 10px;\n"
"padding: 5px 10px;\n"
"background-color: rgb(207, 218, 226);\n"
"color: rgb(0,0,0);")
        self.medidaPrctoModifi_comboB.setEditable(False)
        self.medidaPrctoModifi_comboB.setDuplicatesEnabled(False)
        self.medidaPrctoModifi_comboB.setFrame(False)

        self.verticalLayout_13.addWidget(self.medidaPrctoModifi_comboB)

        self.categoriaPrctoModifi_label = QLabel(self.tabPrctos_body_frame)
        self.categoriaPrctoModifi_label.setObjectName(u"categoriaPrctoModifi_label")
        self.categoriaPrctoModifi_label.setFont(font)

        self.verticalLayout_13.addWidget(self.categoriaPrctoModifi_label)

        self.categoriaPrctoModifi_comboB = QComboBox(self.tabPrctos_body_frame)
        self.categoriaPrctoModifi_comboB.setObjectName(u"categoriaPrctoModifi_comboB")
        self.categoriaPrctoModifi_comboB.setStyleSheet(u"border-radius: 10px;\n"
"padding: 5px 10px;\n"
"background-color: rgb(207, 218, 226);\n"
"color: rgb(0,0,0);")

        self.verticalLayout_13.addWidget(self.categoriaPrctoModifi_comboB)

        self.verticalSpacer_4 = QSpacerItem(20, 1, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_4)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(6)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer = QSpacerItem(60, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer)

        self.GuadarPrctoModifi_btton = QPushButton(self.tabPrctos_body_frame)
        self.GuadarPrctoModifi_btton.setObjectName(u"GuadarPrctoModifi_btton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GuadarPrctoModifi_btton.sizePolicy().hasHeightForWidth())
        self.GuadarPrctoModifi_btton.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Microsoft JhengHei UI"])
        self.GuadarPrctoModifi_btton.setFont(font2)
        self.GuadarPrctoModifi_btton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(80, 195, 144);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(91, 221, 163);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(80, 195, 144);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/redpack/rd-storage.png", QSize(), QIcon.Normal, QIcon.Off)
        self.GuadarPrctoModifi_btton.setIcon(icon)

        self.horizontalLayout_14.addWidget(self.GuadarPrctoModifi_btton)

        self.CancelarPrctoModifi_btton = QPushButton(self.tabPrctos_body_frame)
        self.CancelarPrctoModifi_btton.setObjectName(u"CancelarPrctoModifi_btton")
        sizePolicy.setHeightForWidth(self.CancelarPrctoModifi_btton.sizePolicy().hasHeightForWidth())
        self.CancelarPrctoModifi_btton.setSizePolicy(sizePolicy)
        self.CancelarPrctoModifi_btton.setFont(font2)
        self.CancelarPrctoModifi_btton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(195, 80, 85);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(213, 88, 94);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(195, 80, 85);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/redpack/rd-clean.png", QSize(), QIcon.Normal, QIcon.Off)
        self.CancelarPrctoModifi_btton.setIcon(icon1)

        self.horizontalLayout_14.addWidget(self.CancelarPrctoModifi_btton)


        self.verticalLayout_13.addLayout(self.horizontalLayout_14)

        self.verticalSpacer_5 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_5)


        self.verticalLayout.addWidget(self.tabPrctos_body_frame)


        self.retranslateUi(ModifiProducto)

        QMetaObject.connectSlotsByName(ModifiProducto)
    # setupUi

    def retranslateUi(self, ModifiProducto):
        ModifiProducto.setWindowTitle(QCoreApplication.translate("ModifiProducto", u"Dialog", None))
        self.codigoPrctoModifi_label.setText(QCoreApplication.translate("ModifiProducto", u"C\u00f3digo", None))
        self.codigoPrctoModifi_lineE.setInputMask(QCoreApplication.translate("ModifiProducto", u"9999999999999999999999", None))
        self.nombrePrctoModifi_label.setText(QCoreApplication.translate("ModifiProducto", u"Nombre del Producto", None))
        self.cantidadPrctoModifi_label.setText(QCoreApplication.translate("ModifiProducto", u"Cantidad", None))
        self.cantidadCritPrctoModifi_label.setText(QCoreApplication.translate("ModifiProducto", u"Cantidad Crit.", None))
        self.cantidadProctoModifi_lineE.setInputMask(QCoreApplication.translate("ModifiProducto", u"999999999999", None))
        self.cantidadCritPrctoModifi_lineE.setInputMask(QCoreApplication.translate("ModifiProducto", u"999", None))
        self.precioCompraPrctoModifi_label.setText(QCoreApplication.translate("ModifiProducto", u"Precio de Compra", None))
        self.precioVentaPrctoModifi_label.setText(QCoreApplication.translate("ModifiProducto", u"Precio de Venta", None))
        self.precioCompraPrctoModifi_lineE.setInputMask(QCoreApplication.translate("ModifiProducto", u"9999999999999", None))
        self.precioVentaPrctoModifi_lineE.setInputMask(QCoreApplication.translate("ModifiProducto", u"9999999999999", None))
        self.descuentoPrctoModifi_label.setText(QCoreApplication.translate("ModifiProducto", u"Descuento", None))
        self.descuentoPrctoModifi_lineE.setInputMask(QCoreApplication.translate("ModifiProducto", u"99", None))
        self.medidaPrctoModifi_label.setText(QCoreApplication.translate("ModifiProducto", u"Medida", None))
        self.categoriaPrctoModifi_label.setText(QCoreApplication.translate("ModifiProducto", u"Categoria", None))
        self.GuadarPrctoModifi_btton.setText(QCoreApplication.translate("ModifiProducto", u" Guardar", None))
        self.CancelarPrctoModifi_btton.setText(QCoreApplication.translate("ModifiProducto", u"Cancelar", None))
    # retranslateUi

