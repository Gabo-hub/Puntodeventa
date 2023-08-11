# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect, QSize, Qt,
                            QTime, QUrl)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QGradient, QIcon, QImage,
                           QKeySequence, QLinearGradient, QPainter, QPalette,
                           QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QFrame,
                               QHBoxLayout, QLabel, QLineEdit, QPushButton,
                               QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from views import resources


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(397, 460)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 16777215))
        self.widget.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_cerrar = QPushButton(self.widget)
        self.btn_cerrar.setObjectName(u"btn_cerrar")
        self.btn_cerrar.setMinimumSize(QSize(35, 25))
        self.btn_cerrar.setMaximumSize(QSize(35, 25))
        self.btn_cerrar.setStyleSheet(u"QPushButton {\n"
"color: black;\n"
"background-color:  rgb(241, 153, 0);\n"
"font: 12pt \"Arial\";\n"
"border-radius: 1px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: orange;\n"
"}\n"
"\n"
"")
        self.btn_cerrar.setFlat(True)

        self.verticalLayout_2.addWidget(self.btn_cerrar, 0, Qt.AlignRight)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 15, -1, -1)
        self.img_login = QLabel(self.widget)
        self.img_login.setObjectName(u"img_login")
        self.img_login.setMinimumSize(QSize(50, 100))
        self.img_login.setMaximumSize(QSize(110, 120))
        self.img_login.setStyleSheet(u"image: url(:/icons/icons/rocket_48x48.png);")
        self.img_login.setPixmap(QPixmap(u":/Logo_icon/rocket_48x48.png"))
        self.img_login.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.img_login, 0, Qt.AlignHCenter)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(50, 35, 59, -1)
        self.img_usuario = QLabel(self.widget)
        self.img_usuario.setObjectName(u"img_usuario")
        self.img_usuario.setStyleSheet(u"color: rgb(231, 231, 231);\n"
"font: 15pt \"Verdana\";")
        self.img_usuario.setPixmap(QPixmap(u":/Logo_icon/user_32x32.png"))
        self.img_usuario.setMargin(5)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.img_usuario)

        self.line_usuario = QLineEdit(self.widget)
        self.line_usuario.setObjectName(u"line_usuario")
        self.line_usuario.setMinimumSize(QSize(0, 40))
        self.line_usuario.setStyleSheet(u"QLineEdit {\n"
"      color: rgb(0, 0, 0);\n"
"      font: 15pt \"Verdana\";\n"
"      border: 2px solid rgb(212, 212, 212);\n"
"      border-bottom-color: darkgray;\n"
"      border-radius: 10px;\n"
"      padding: 0 8px;\n"
"      selection-background-color: darkgray;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid gray;\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(56, 220, 97);	\n"
"}")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.line_usuario)

        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"border: 2px solid orange;;")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.formLayout_2.setWidget(1, QFormLayout.SpanningRole, self.line)

        self.btn_contrasenaver = QPushButton(self.widget)
        self.btn_contrasenaver.setObjectName(u"btn_contrasenaver")
        self.btn_contrasenaver.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(u":/Logo_icon/lock2_32x32.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/Logo_icon/lock_32x32.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_contrasenaver.setIcon(icon)
        self.btn_contrasenaver.setIconSize(QSize(32, 32))
        self.btn_contrasenaver.setCheckable(True)
        self.btn_contrasenaver.setFlat(True)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.btn_contrasenaver)

        self.line_contrasena = QLineEdit(self.widget)
        self.line_contrasena.setObjectName(u"line_contrasena")
        self.line_contrasena.setMinimumSize(QSize(0, 40))
        self.line_contrasena.setStyleSheet(u"QLineEdit {\n"
"      color: rgb(0, 0, 0);\n"
"      font: 15pt \"Verdana\";\n"
"      border: 2px solid rgb(212, 212, 212);\n"
"      border-bottom-color: darkgray;\n"
"      border-radius: 10px;\n"
"      padding: 0 8px;\n"
"      selection-background-color: darkgray;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid gray;\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(56, 220, 97);	\n"
"}")
        self.line_contrasena.setEchoMode(QLineEdit.Password)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.line_contrasena)

        self.line_3 = QFrame(self.widget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setStyleSheet(u"border: 2px solid orange;;")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.formLayout_2.setWidget(3, QFormLayout.SpanningRole, self.line_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_2.setItem(6, QFormLayout.SpanningRole, self.verticalSpacer)

        self.btn_Entrar = QPushButton(self.widget)
        self.btn_Entrar.setObjectName(u"btn_Entrar")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Entrar.sizePolicy().hasHeightForWidth())
        self.btn_Entrar.setSizePolicy(sizePolicy)
        self.btn_Entrar.setMinimumSize(QSize(0, 60))
        self.btn_Entrar.setMaximumSize(QSize(16777215, 16777215))
        self.btn_Entrar.setAutoFillBackground(False)
        self.btn_Entrar.setStyleSheet(u"color: rgb(231, 231, 231);\n"
"font: 17pt \"Verdana\";\n"
"border: 2px solid orange;\n"
"padding: 5px;\n"
"border-radius: 3px;\n"
"opacity: 200;\n"
"background-color: rgb(20, 20, 39);")
        self.btn_Entrar.setAutoDefault(False)
        self.btn_Entrar.setFlat(False)

        self.formLayout_2.setWidget(7, QFormLayout.SpanningRole, self.btn_Entrar)

        self.btn_admin = QCheckBox(self.widget)
        self.btn_admin.setObjectName(u"btn_admin")
        self.btn_admin.setStyleSheet(u"QCheckBox {\n"
"	padding-left: 15px; \n"
"	padding-top: 3px;\n"
"}\n"
"")
        self.btn_admin.setIconSize(QSize(32, 32))

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.btn_admin)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(12)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(233, 151, 0);\n"
"color: rgb(20, 20, 39);")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.label_3)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_4)


        self.verticalLayout_3.addLayout(self.formLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)


        self.horizontalLayout_3.addWidget(self.widget)

        self.horizontalLayout_3.setStretch(0, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        QWidget.setTabOrder(self.line_usuario, self.line_contrasena)
        QWidget.setTabOrder(self.line_contrasena, self.btn_contrasenaver)
        QWidget.setTabOrder(self.btn_contrasenaver, self.btn_admin)
        QWidget.setTabOrder(self.btn_admin, self.btn_Entrar)
        QWidget.setTabOrder(self.btn_Entrar, self.btn_cerrar)

        self.retranslateUi(Form)
        self.btn_cerrar.clicked.connect(Form.close)

        self.btn_Entrar.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_cerrar.setText(QCoreApplication.translate("Form", u"x", None))
        self.img_login.setText("")
        self.img_usuario.setText("")
        self.btn_contrasenaver.setText("")
        self.btn_Entrar.setText(QCoreApplication.translate("Form", u"Sign In", None))
        self.btn_admin.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"Administrador", None))
        self.label_4.setText("")
    # retranslateUi

