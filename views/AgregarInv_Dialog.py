# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AgregarInv_Dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QLabel, QLineEdit, QSizePolicy,
    QVBoxLayout, QWidget, QBoxLayout)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(429, 193)
        Dialog.setStyleSheet(u"QDialog {\n"
"	border-radius:10px;\n"
"	background-color: rgb(242, 243, 245);\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.HeaderTitulos_label = QLabel(Dialog)
        self.HeaderTitulos_label.setObjectName(u"HeaderTitulos_label")
        font = QFont()
        font.setFamilies([u"Gotham"])
        font.setPointSize(11)
        self.HeaderTitulos_label.setFont(font)
        self.HeaderTitulos_label.setStyleSheet(u"color: rgb(0,0,0);\n"
"background-color: rgb(191, 226, 229);\n"
"padding:3px 5px; \n"
"border-radius: 10px;")

        self.verticalLayout.addWidget(self.HeaderTitulos_label)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(15)
        self.formLayout.setVerticalSpacing(10)
        self.codigoProducText_label = QLabel(Dialog)
        self.codigoProducText_label.setObjectName(u"codigoProducText_label")
        font1 = QFont()
        font1.setFamilies([u"Gotham"])
        font1.setPointSize(10)
        self.codigoProducText_label.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.codigoProducText_label)

        self.cantidadProducInfo_label = QLineEdit(Dialog)
        self.cantidadProducInfo_label.setObjectName(u"cantidadProducInfo_label")
        self.cantidadProducInfo_label.setStyleSheet(u"QLineEdit {\n"
"	border-radius: 10px;\n"
"	padding: 5px 10px;\n"
"	background-color: rgb(255,255,255);\n"
"	color: rgb(0,0,0);\n"
"}")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.cantidadProducInfo_label)

        self.descAgregarInfo_label = QLabel(Dialog)
        self.descAgregarInfo_label.setObjectName(u"descAgregarInfo_label")
        self.descAgregarInfo_label.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.descAgregarInfo_label)

        self.cantidadActText_label = QLabel(Dialog)
        self.cantidadActText_label.setObjectName(u"cantidadActText_label")
        self.cantidadActText_label.setFont(font1)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.cantidadActText_label)

        self.cantActAgregar_label = QLabel(Dialog)
        self.cantActAgregar_label.setObjectName(u"cantActAgregar_label")
        self.cantActAgregar_label.setFont(font1)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.cantActAgregar_label)

        self.cantidadAgregarText_label = QLabel(Dialog)
        self.cantidadAgregarText_label.setObjectName(u"cantidadAgregarText_label")
        self.cantidadAgregarText_label.setFont(font1)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.cantidadAgregarText_label)

        self.cantidadAgregarInfo_label = QLineEdit(Dialog)
        self.cantidadAgregarInfo_label.setObjectName(u"cantidadAgregarInfo_label")
        self.cantidadAgregarInfo_label.setStyleSheet(u"QLineEdit {\n"
"	border-radius: 10px;\n"
"	padding: 5px 10px;\n"
"	background-color: rgb(255,255,255);\n"
"	color: rgb(0,0,0);\n"
"}")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.cantidadAgregarInfo_label)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        font2 = QFont()
        font2.setFamilies([u"Microsoft JhengHei UI"])
        self.buttonBox.setFont(font2)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(False)

        self.verticalLayout.addWidget(self.buttonBox)   


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.HeaderTitulos_label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">Agregar Inventario</p></body></html>", None))
        self.codigoProducText_label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>C\u00f3digo del Producto</p></body></html>", None))
        self.descAgregarInfo_label.setText("")
        self.cantidadActText_label.setText(QCoreApplication.translate("Dialog", u"Cantidad Actual", None))
        self.cantActAgregar_label.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.cantidadAgregarText_label.setText(QCoreApplication.translate("Dialog", u"Cantidad", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Descripci\u00f3n", None))
    # retranslateUi

