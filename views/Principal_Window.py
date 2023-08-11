# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Principal_Window.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QFormLayout, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import views.resources

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(848, 591)
        icon = QIcon()
        icon.addFile(u":/Main_icons/cash-register-buy-purchases-shop-shops.256x212.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(u"background-color: rgb(88, 88, 88);")
        self.horizontalLayout_13 = QHBoxLayout(Form)
        self.horizontalLayout_13.setSpacing(6)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.tabPrincipal = QTabWidget(Form)
        self.tabPrincipal.setObjectName(u"tabPrincipal")
        font = QFont()
        font.setFamilies([u"Microsoft JhengHei UI"])
        font.setBold(False)
        self.tabPrincipal.setFont(font)
        self.tabPrincipal.setStyleSheet(u"QTabBar {\n"
"	background-color: rgb(217, 217, 217);\n"
"}\n"
"\n"
"QTabBar:tab { \n"
" 	border-style: solid;\n"
"	border-color: rgb(80, 195, 144);\n"
"	border-right-width: 0;\n"
"	padding: 3px 8px;\n"
"	background-color: rgb(217, 217, 217);\n"
"}\n"
"\n"
"QTabBar:tab:selected {\n"
"	border-top-width: 1.5;\n"
"	color: rgb(0, 170, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.tabPrincipal.setTabPosition(QTabWidget.North)
        self.tabPrincipal.setTabShape(QTabWidget.Rounded)
        self.tabPrincipal.setElideMode(Qt.ElideNone)
        self.tabPrincipal.setUsesScrollButtons(True)
        self.tabPrincipal.setDocumentMode(False)
        self.tabPrincipal.setTabsClosable(False)
        self.tabPrincipal.setMovable(False)
        self.tabPrincipal.setTabBarAutoHide(False)
        self.tab1_ventas = QWidget()
        self.tab1_ventas.setObjectName(u"tab1_ventas")
        font1 = QFont()
        font1.setFamilies([u"Poppins Medium"])
        self.tab1_ventas.setFont(font1)
        self.tab1_ventas.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton {\n"
"	border-radius: 10px;\n"
"	padding: 5px 10px;\n"
"	background-color: rgb(12, 95, 194);\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(15, 122, 244);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(12, 95, 194);\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.tab1_ventas)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_5 = QFrame(self.tab1_ventas)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 85))
        self.frame_5.setStyleSheet(u"QFrame {\n"
"	\n"
"	background-color: rgb(242, 243, 245);\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_5)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamilies([u"Gotham"])
        font2.setPointSize(11)
        font2.setBold(False)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.label)

        self.frame_2 = QFrame(self.frame_5)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMouseTracking(False)
        self.frame_2.setTabletTracking(False)
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(5, 0, 5, 5)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_2 = QLineEdit(self.frame_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setStyleSheet(u"padding: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius: 5px 5px;")
        self.lineEdit_2.setDragEnabled(False)
        self.lineEdit_2.setReadOnly(False)
        self.lineEdit_2.setClearButtonEnabled(False)

        self.verticalLayout_4.addWidget(self.lineEdit_2)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setFamilies([u"Rubik"])
        font3.setPointSize(10)
        font3.setBold(False)
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"border-radius: 0px;\n"
"background-color: rgb(255, 255, 255);\n"
"border-bottom-left-radius: 5px 5px;\n"
"padding: 3px;")
        self.label_3.setTextFormat(Qt.AutoText)
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setWordWrap(False)

        self.horizontalLayout_5.addWidget(self.label_3)


        self.verticalLayout_4.addWidget(self.frame_4)


        self.horizontalLayout.addWidget(self.frame_3)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)
        font4 = QFont()
        font4.setFamilies([u"Poppins"])
        self.pushButton.setFont(font4)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius: 0px;\n"
"	border-top-right-radius: 5px 5px;\n"
"	border-bottom-right-radius: 5px 5px;\n"
"	background-color: rgb(80, 195, 144);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(91, 221, 163);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(80, 195, 144);\n"
"}")
        self.pushButton.setFlat(False)

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.frame_2)


        self.verticalLayout_3.addWidget(self.frame_5)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame = QFrame(self.tab1_ventas)
        self.frame.setObjectName(u"frame")
        self.frame.setFont(font1)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_6 = QPushButton(self.frame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        font5 = QFont()
        font5.setFamilies([u"Microsoft JhengHei UI"])
        font5.setBold(True)
        self.pushButton_6.setFont(font5)
        self.pushButton_6.setFlat(True)

        self.horizontalLayout_3.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.frame)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setFont(font5)
        self.pushButton_7.setStyleSheet(u"")
        self.pushButton_7.setFlat(True)

        self.horizontalLayout_3.addWidget(self.pushButton_7)

        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFont(font5)
        self.pushButton_5.setFlat(True)

        self.horizontalLayout_3.addWidget(self.pushButton_5)

        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font5)
        self.pushButton_4.setFlat(True)

        self.horizontalLayout_3.addWidget(self.pushButton_4)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font5)
        self.pushButton_3.setFlat(True)

        self.horizontalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font5)
        self.pushButton_2.setFlat(True)

        self.horizontalLayout_3.addWidget(self.pushButton_2)


        self.horizontalLayout_2.addWidget(self.frame)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.tabWidget_2 = QTabWidget(self.tab1_ventas)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setTabShape(QTabWidget.Rounded)
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget_2.addTab(self.tab_4, "")

        self.verticalLayout_2.addWidget(self.tabWidget_2)

        self.frame_6 = QFrame(self.tab1_ventas)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setAcceptDrops(True)
        self.frame_6.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(242, 243, 245);\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.frame_6)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(2, 2, 0, 0)
        self.frame_9 = QFrame(self.frame_13)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_9)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"QFrame {\n"
"	border-top-left-radius:3px;\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_7)
        self.label_2.setObjectName(u"label_2")
        font6 = QFont()
        font6.setFamilies([u"Gotham"])
        font6.setPointSize(10)
        self.label_2.setFont(font6)
        self.label_2.setStyleSheet(u"padding: 5px 2px 2px 2px;")

        self.verticalLayout_5.addWidget(self.label_2)

        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton_11 = QPushButton(self.frame_8)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy3)
        self.pushButton_11.setFont(font5)

        self.horizontalLayout_6.addWidget(self.pushButton_11)

        self.pushButton_10 = QPushButton(self.frame_8)
        self.pushButton_10.setObjectName(u"pushButton_10")
        sizePolicy3.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy3)
        self.pushButton_10.setFont(font5)

        self.horizontalLayout_6.addWidget(self.pushButton_10)

        self.pushButton_12 = QPushButton(self.frame_8)
        self.pushButton_12.setObjectName(u"pushButton_12")
        sizePolicy3.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy3)
        self.pushButton_12.setFont(font5)

        self.horizontalLayout_6.addWidget(self.pushButton_12)


        self.verticalLayout_5.addWidget(self.frame_8)


        self.horizontalLayout_7.addWidget(self.frame_7)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)

        self.pushButton_13 = QPushButton(self.frame_9)
        self.pushButton_13.setObjectName(u"pushButton_13")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy4)
        font7 = QFont()
        font7.setFamilies([u"Poppins"])
        font7.setBold(False)
        self.pushButton_13.setFont(font7)
        self.pushButton_13.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(80, 195, 144);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91, 221, 163);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(80, 195, 144);\n"
"}")

        self.horizontalLayout_7.addWidget(self.pushButton_13)


        self.horizontalLayout_10.addWidget(self.frame_9)

        self.label_10 = QLabel(self.frame_13)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QSize(200, 0))
        font8 = QFont()
        font8.setFamilies([u"Gotham"])
        font8.setPointSize(26)
        self.label_10.setFont(font8)
        self.label_10.setStyleSheet(u"color: rgb(211, 16, 42);")

        self.horizontalLayout_10.addWidget(self.label_10)


        self.verticalLayout_6.addWidget(self.frame_13)

        self.frame_12 = QFrame(self.frame_6)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_12)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_10)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_10)
        self.label_8.setObjectName(u"label_8")
        font9 = QFont()
        font9.setFamilies([u"Gotham"])
        font9.setPointSize(10)
        font9.setBold(False)
        self.label_8.setFont(font9)

        self.gridLayout.addWidget(self.label_8, 2, 1, 1, 1)

        self.label_7 = QLabel(self.frame_10)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font9)

        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)

        self.label_5 = QLabel(self.frame_10)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font9)

        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)

        self.label_4 = QLabel(self.frame_10)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font9)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_6 = QLabel(self.frame_10)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font9)

        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)

        self.label_9 = QLabel(self.frame_10)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font9)

        self.gridLayout.addWidget(self.label_9, 2, 2, 1, 1)


        self.horizontalLayout_9.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_12)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pushButton_9 = QPushButton(self.frame_11)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setFont(font5)

        self.horizontalLayout_8.addWidget(self.pushButton_9)

        self.pushButton_15 = QPushButton(self.frame_11)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setFont(font5)

        self.horizontalLayout_8.addWidget(self.pushButton_15)


        self.horizontalLayout_9.addWidget(self.frame_11)


        self.verticalLayout_6.addWidget(self.frame_12)


        self.verticalLayout_2.addWidget(self.frame_6)

        icon1 = QIcon()
        icon1.addFile(u":/blupack/bl-shopping-cart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabPrincipal.addTab(self.tab1_ventas, icon1, "")
        self.tab2_clientes = QWidget()
        self.tab2_clientes.setObjectName(u"tab2_clientes")
        self.tab2_clientes.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton {\n"
"	border-radius: 10px;\n"
"	padding: 5px 10px;\n"
"	background-color: rgb(12, 95, 194);\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(15, 122, 244);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(12, 95, 194);\n"
"}")
        self.verticalLayout_8 = QVBoxLayout(self.tab2_clientes)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.clientes_cabeza_frame = QFrame(self.tab2_clientes)
        self.clientes_cabeza_frame.setObjectName(u"clientes_cabeza_frame")
        self.clientes_cabeza_frame.setFrameShape(QFrame.StyledPanel)
        self.clientes_cabeza_frame.setFrameShadow(QFrame.Raised)
        self.clientes_cabeza_frame.setLineWidth(1)
        self.verticalLayout_7 = QVBoxLayout(self.clientes_cabeza_frame)
        self.verticalLayout_7.setSpacing(3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.titulo_clientes = QLabel(self.clientes_cabeza_frame)
        self.titulo_clientes.setObjectName(u"titulo_clientes")
        self.titulo_clientes.setFont(font2)
        self.titulo_clientes.setStyleSheet(u"border-top-right-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"background-color: rgb(233, 245, 254);\n"
"padding: 5px;")

        self.verticalLayout_7.addWidget(self.titulo_clientes)

        self.cabeza_clientes_cajaBtn = QFrame(self.clientes_cabeza_frame)
        self.cabeza_clientes_cajaBtn.setObjectName(u"cabeza_clientes_cajaBtn")
        self.cabeza_clientes_cajaBtn.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(97, 212, 207);\n"
"	border-bottom-right-radius: 5px;\n"
"	border-bottom-left-radius: 5px;\n"
"}")
        self.cabeza_clientes_cajaBtn.setFrameShape(QFrame.StyledPanel)
        self.cabeza_clientes_cajaBtn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.cabeza_clientes_cajaBtn)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.EstadoCuenta_bttn = QPushButton(self.cabeza_clientes_cajaBtn)
        self.EstadoCuenta_bttn.setObjectName(u"EstadoCuenta_bttn")
        font10 = QFont()
        font10.setFamilies([u"Microsoft JhengHei UI"])
        font10.setPointSize(9)
        font10.setBold(True)
        self.EstadoCuenta_bttn.setFont(font10)

        self.horizontalLayout_11.addWidget(self.EstadoCuenta_bttn)

        self.NuevoCliente_bttn = QPushButton(self.cabeza_clientes_cajaBtn)
        self.NuevoCliente_bttn.setObjectName(u"NuevoCliente_bttn")
        self.NuevoCliente_bttn.setFont(font10)

        self.horizontalLayout_11.addWidget(self.NuevoCliente_bttn)

        self.ModifiCliente_bttn = QPushButton(self.cabeza_clientes_cajaBtn)
        self.ModifiCliente_bttn.setObjectName(u"ModifiCliente_bttn")
        self.ModifiCliente_bttn.setFont(font10)

        self.horizontalLayout_11.addWidget(self.ModifiCliente_bttn)

        self.EliminarCliente_bttn = QPushButton(self.cabeza_clientes_cajaBtn)
        self.EliminarCliente_bttn.setObjectName(u"EliminarCliente_bttn")
        self.EliminarCliente_bttn.setFont(font10)

        self.horizontalLayout_11.addWidget(self.EliminarCliente_bttn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer)

        self.ReporteSaldo_bttn = QPushButton(self.cabeza_clientes_cajaBtn)
        self.ReporteSaldo_bttn.setObjectName(u"ReporteSaldo_bttn")
        self.ReporteSaldo_bttn.setFont(font10)

        self.horizontalLayout_11.addWidget(self.ReporteSaldo_bttn)


        self.verticalLayout_7.addWidget(self.cabeza_clientes_cajaBtn)


        self.verticalLayout_8.addWidget(self.clientes_cabeza_frame)

        self.clientes_cuerpo_frame = QFrame(self.tab2_clientes)
        self.clientes_cuerpo_frame.setObjectName(u"clientes_cuerpo_frame")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.clientes_cuerpo_frame.sizePolicy().hasHeightForWidth())
        self.clientes_cuerpo_frame.setSizePolicy(sizePolicy5)
        self.clientes_cuerpo_frame.setFrameShape(QFrame.StyledPanel)
        self.clientes_cuerpo_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.clientes_cuerpo_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer = QSpacerItem(20, 43, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 42, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(234, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 1, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(234, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.cuerpo_clientes_centro = QFrame(self.clientes_cuerpo_frame)
        self.cuerpo_clientes_centro.setObjectName(u"cuerpo_clientes_centro")
        self.cuerpo_clientes_centro.setStyleSheet(u"QFrame {\n"
"	border-radius: 10px;\n"
"	background-color: rgb(221, 233, 241);\n"
"}")
        self.cuerpo_clientes_centro.setFrameShape(QFrame.StyledPanel)
        self.cuerpo_clientes_centro.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.cuerpo_clientes_centro)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.centro_titulo_estado = QLabel(self.cuerpo_clientes_centro)
        self.centro_titulo_estado.setObjectName(u"centro_titulo_estado")
        font11 = QFont()
        font11.setFamilies([u"Gotham"])
        font11.setPointSize(11)
        self.centro_titulo_estado.setFont(font11)
        self.centro_titulo_estado.setStyleSheet(u"color: rgb(0,0,0);\n"
"background-color: rgb(191, 226, 229);\n"
"padding:3px 5px; ")

        self.verticalLayout_9.addWidget(self.centro_titulo_estado)

        self.centro_busqueda_frame = QFrame(self.cuerpo_clientes_centro)
        self.centro_busqueda_frame.setObjectName(u"centro_busqueda_frame")
        self.centro_busqueda_frame.setFrameShape(QFrame.StyledPanel)
        self.centro_busqueda_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.centro_busqueda_frame)
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.busqueda_cliente_qline = QLineEdit(self.centro_busqueda_frame)
        self.busqueda_cliente_qline.setObjectName(u"busqueda_cliente_qline")
        self.busqueda_cliente_qline.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"padding: 5px;\n"
"border-top-left-radius: 5px;\n"
"border-top-right-radius: 5px;")

        self.verticalLayout_10.addWidget(self.busqueda_cliente_qline)

        self.busqueda_cliente_qtableW = QTableWidget(self.centro_busqueda_frame)
        if (self.busqueda_cliente_qtableW.columnCount() < 2):
            self.busqueda_cliente_qtableW.setColumnCount(2)
        icon2 = QIcon()
        icon2.addFile(u":/Main_icons/squared-id.png", QSize(), QIcon.Normal, QIcon.On)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setIcon(icon2);
        self.busqueda_cliente_qtableW.setHorizontalHeaderItem(0, __qtablewidgetitem)
        icon3 = QIcon()
        icon3.addFile(u":/Main_icons/carnet-de-identidad.png", QSize(), QIcon.Normal, QIcon.On)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setIcon(icon3);
        self.busqueda_cliente_qtableW.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.busqueda_cliente_qtableW.setObjectName(u"busqueda_cliente_qtableW")
        self.busqueda_cliente_qtableW.setEnabled(True)
        self.busqueda_cliente_qtableW.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 0px;")
        self.busqueda_cliente_qtableW.setAutoScroll(True)
        self.busqueda_cliente_qtableW.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.busqueda_cliente_qtableW.setCornerButtonEnabled(True)
        self.busqueda_cliente_qtableW.horizontalHeader().setVisible(True)
        self.busqueda_cliente_qtableW.horizontalHeader().setCascadingSectionResizes(False)
        self.busqueda_cliente_qtableW.horizontalHeader().setHighlightSections(True)
        self.busqueda_cliente_qtableW.horizontalHeader().setProperty("showSortIndicator", False)
        self.busqueda_cliente_qtableW.horizontalHeader().setStretchLastSection(True)
        self.busqueda_cliente_qtableW.verticalHeader().setVisible(False)
        self.busqueda_cliente_qtableW.verticalHeader().setCascadingSectionResizes(False)
        self.busqueda_cliente_qtableW.verticalHeader().setHighlightSections(True)
        self.busqueda_cliente_qtableW.verticalHeader().setProperty("showSortIndicator", False)
        self.busqueda_cliente_qtableW.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_10.addWidget(self.busqueda_cliente_qtableW)


        self.verticalLayout_9.addWidget(self.centro_busqueda_frame)


        self.gridLayout_2.addWidget(self.cuerpo_clientes_centro, 1, 1, 1, 1)


        self.verticalLayout_8.addWidget(self.clientes_cuerpo_frame)

        icon4 = QIcon()
        icon4.addFile(u":/blupack/bl-clients.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabPrincipal.addTab(self.tab2_clientes, icon4, "")
        self.tab3_productos = QWidget()
        self.tab3_productos.setObjectName(u"tab3_productos")
        self.tab3_productos.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton {\n"
"	border-radius: 10px;\n"
"	padding: 5px 10px;\n"
"	background-color: rgb(12, 95, 194);\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout_12 = QVBoxLayout(self.tab3_productos)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.titulo_productos = QLabel(self.tab3_productos)
        self.titulo_productos.setObjectName(u"titulo_productos")
        self.titulo_productos.setFont(font6)
        self.titulo_productos.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(233, 245, 254);\n"
"padding: 5px;")

        self.verticalLayout_12.addWidget(self.titulo_productos)

        self.cuerpo_productos_tabsW = QTabWidget(self.tab3_productos)
        self.cuerpo_productos_tabsW.setObjectName(u"cuerpo_productos_tabsW")
        self.cuerpo_productos_tabsW.setEnabled(True)
        font12 = QFont()
        font12.setFamilies([u"Microsoft JhengHei UI"])
        self.cuerpo_productos_tabsW.setFont(font12)
        self.cuerpo_productos_tabsW.setAutoFillBackground(False)
        self.cuerpo_productos_tabsW.setStyleSheet(u"border-radius: 10px;")
        self.cuerpo_productos_tabsW.setTabShape(QTabWidget.Rounded)
        self.cuerpo_productos_tabsW.setTabBarAutoHide(False)
        self.cuerpo_productos_tabPrctos = QWidget()
        self.cuerpo_productos_tabPrctos.setObjectName(u"cuerpo_productos_tabPrctos")
        self.horizontalLayout_19 = QHBoxLayout(self.cuerpo_productos_tabPrctos)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.tabPrctos_body_tab = QFrame(self.cuerpo_productos_tabPrctos)
        self.tabPrctos_body_tab.setObjectName(u"tabPrctos_body_tab")
        self.tabPrctos_body_tab.setFrameShape(QFrame.StyledPanel)
        self.tabPrctos_body_tab.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.tabPrctos_body_tab)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.tabPrctos_body_frame = QFrame(self.tabPrctos_body_tab)
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
        self.nuevoProducto_Label = QLabel(self.tabPrctos_body_frame)
        self.nuevoProducto_Label.setObjectName(u"nuevoProducto_Label")
        self.nuevoProducto_Label.setFont(font6)
        self.nuevoProducto_Label.setStyleSheet(u"padding: 5px;")

        self.verticalLayout_13.addWidget(self.nuevoProducto_Label)

        self.verticalSpacer_3 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_3)

        self.codigoPrcto_label = QLabel(self.tabPrctos_body_frame)
        self.codigoPrcto_label.setObjectName(u"codigoPrcto_label")
        self.codigoPrcto_label.setFont(font6)

        self.verticalLayout_13.addWidget(self.codigoPrcto_label)

        self.codigoPrcto_lineE = QLineEdit(self.tabPrctos_body_frame)
        self.codigoPrcto_lineE.setObjectName(u"codigoPrcto_lineE")

        self.verticalLayout_13.addWidget(self.codigoPrcto_lineE)

        self.nombrePrcto_label = QLabel(self.tabPrctos_body_frame)
        self.nombrePrcto_label.setObjectName(u"nombrePrcto_label")
        self.nombrePrcto_label.setFont(font6)

        self.verticalLayout_13.addWidget(self.nombrePrcto_label)

        self.nombrePrcto_lineE = QLineEdit(self.tabPrctos_body_frame)
        self.nombrePrcto_lineE.setObjectName(u"nombrePrcto_lineE")

        self.verticalLayout_13.addWidget(self.nombrePrcto_lineE)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.cantidadPrcto_label = QLabel(self.tabPrctos_body_frame)
        self.cantidadPrcto_label.setObjectName(u"cantidadPrcto_label")
        self.cantidadPrcto_label.setFont(font6)

        self.horizontalLayout_12.addWidget(self.cantidadPrcto_label)

        self.cantidadCritPrcto_label = QLabel(self.tabPrctos_body_frame)
        self.cantidadCritPrcto_label.setObjectName(u"cantidadCritPrcto_label")
        self.cantidadCritPrcto_label.setFont(font6)

        self.horizontalLayout_12.addWidget(self.cantidadCritPrcto_label)


        self.verticalLayout_13.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.cantidadProcto_lineE = QLineEdit(self.tabPrctos_body_frame)
        self.cantidadProcto_lineE.setObjectName(u"cantidadProcto_lineE")
        self.cantidadProcto_lineE.setFrame(True)

        self.horizontalLayout_17.addWidget(self.cantidadProcto_lineE)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_7)

        self.cantidadCritPrcto_lineE = QLineEdit(self.tabPrctos_body_frame)
        self.cantidadCritPrcto_lineE.setObjectName(u"cantidadCritPrcto_lineE")

        self.horizontalLayout_17.addWidget(self.cantidadCritPrcto_lineE)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_8)


        self.verticalLayout_13.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.precioCompraPrcto_label = QLabel(self.tabPrctos_body_frame)
        self.precioCompraPrcto_label.setObjectName(u"precioCompraPrcto_label")
        self.precioCompraPrcto_label.setFont(font6)

        self.horizontalLayout_15.addWidget(self.precioCompraPrcto_label)

        self.precioVentaPrcto_label = QLabel(self.tabPrctos_body_frame)
        self.precioVentaPrcto_label.setObjectName(u"precioVentaPrcto_label")
        self.precioVentaPrcto_label.setFont(font6)

        self.horizontalLayout_15.addWidget(self.precioVentaPrcto_label)


        self.verticalLayout_13.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.precioCompraPrcto_lineE = QLineEdit(self.tabPrctos_body_frame)
        self.precioCompraPrcto_lineE.setObjectName(u"precioCompraPrcto_lineE")

        self.horizontalLayout_16.addWidget(self.precioCompraPrcto_lineE)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_5)

        self.precioVentaPrcto_lineE = QLineEdit(self.tabPrctos_body_frame)
        self.precioVentaPrcto_lineE.setObjectName(u"precioVentaPrcto_lineE")

        self.horizontalLayout_16.addWidget(self.precioVentaPrcto_lineE)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_6)


        self.verticalLayout_13.addLayout(self.horizontalLayout_16)

        self.descuentoPrcto_label = QLabel(self.tabPrctos_body_frame)
        self.descuentoPrcto_label.setObjectName(u"descuentoPrcto_label")
        self.descuentoPrcto_label.setFont(font6)

        self.verticalLayout_13.addWidget(self.descuentoPrcto_label)

        self.descuentoPrcto_lineE = QLineEdit(self.tabPrctos_body_frame)
        self.descuentoPrcto_lineE.setObjectName(u"descuentoPrcto_lineE")
        self.descuentoPrcto_lineE.setFrame(False)

        self.verticalLayout_13.addWidget(self.descuentoPrcto_lineE)

        self.medidaPrcto_label = QLabel(self.tabPrctos_body_frame)
        self.medidaPrcto_label.setObjectName(u"medidaPrcto_label")
        self.medidaPrcto_label.setFont(font6)

        self.verticalLayout_13.addWidget(self.medidaPrcto_label)

        self.medidaPrcto_comboB = QComboBox(self.tabPrctos_body_frame)
        self.medidaPrcto_comboB.setObjectName(u"medidaPrcto_comboB")
        font13 = QFont()
        font13.setFamilies([u"Poppins"])
        font13.setPointSize(9)
        self.medidaPrcto_comboB.setFont(font13)
        self.medidaPrcto_comboB.setStyleSheet(u"border-radius: 10px;\n"
"padding: 5px 10px;\n"
"background-color: rgb(207, 218, 226);\n"
"color: rgb(0,0,0);")
        self.medidaPrcto_comboB.setEditable(False)
        self.medidaPrcto_comboB.setDuplicatesEnabled(False)
        self.medidaPrcto_comboB.setFrame(False)

        self.verticalLayout_13.addWidget(self.medidaPrcto_comboB)

        self.categoriaPrcto_label = QLabel(self.tabPrctos_body_frame)
        self.categoriaPrcto_label.setObjectName(u"categoriaPrcto_label")
        self.categoriaPrcto_label.setFont(font6)

        self.verticalLayout_13.addWidget(self.categoriaPrcto_label)

        self.categoriaPrcto_comboB = QComboBox(self.tabPrctos_body_frame)
        self.categoriaPrcto_comboB.setObjectName(u"categoriaPrcto_comboB")
        self.categoriaPrcto_comboB.setStyleSheet(u"border-radius: 10px;\n"
"padding: 5px 10px;\n"
"background-color: rgb(207, 218, 226);\n"
"color: rgb(0,0,0);")

        self.verticalLayout_13.addWidget(self.categoriaPrcto_comboB)

        self.verticalSpacer_4 = QSpacerItem(20, 1, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_4)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(6)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.GuadarPrcto_btton = QPushButton(self.tabPrctos_body_frame)
        self.GuadarPrcto_btton.setObjectName(u"GuadarPrcto_btton")
        sizePolicy1.setHeightForWidth(self.GuadarPrcto_btton.sizePolicy().hasHeightForWidth())
        self.GuadarPrcto_btton.setSizePolicy(sizePolicy1)
        self.GuadarPrcto_btton.setFont(font12)
        self.GuadarPrcto_btton.setStyleSheet(u"QPushButton {\n"
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
        icon5 = QIcon()
        icon5.addFile(u":/redpack/rd-storage.png", QSize(), QIcon.Normal, QIcon.Off)
        self.GuadarPrcto_btton.setIcon(icon5)

        self.horizontalLayout_14.addWidget(self.GuadarPrcto_btton)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_13)

        self.LimpiarPrcto_btton = QPushButton(self.tabPrctos_body_frame)
        self.LimpiarPrcto_btton.setObjectName(u"LimpiarPrcto_btton")
        sizePolicy1.setHeightForWidth(self.LimpiarPrcto_btton.sizePolicy().hasHeightForWidth())
        self.LimpiarPrcto_btton.setSizePolicy(sizePolicy1)
        self.LimpiarPrcto_btton.setFont(font12)
        self.LimpiarPrcto_btton.setStyleSheet(u"QPushButton {\n"
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
        icon6 = QIcon()
        icon6.addFile(u":/redpack/rd-clean.png", QSize(), QIcon.Normal, QIcon.Off)
        self.LimpiarPrcto_btton.setIcon(icon6)

        self.horizontalLayout_14.addWidget(self.LimpiarPrcto_btton)


        self.verticalLayout_13.addLayout(self.horizontalLayout_14)

        self.verticalSpacer_5 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_5)


        self.horizontalLayout_4.addWidget(self.tabPrctos_body_frame)

        self.tabPrctos_body_tabla = QFrame(self.tabPrctos_body_tab)
        self.tabPrctos_body_tabla.setObjectName(u"tabPrctos_body_tabla")
        self.tabPrctos_body_tabla.setStyleSheet(u"	border-radius:10px;\n"
"	background-color: rgb(242, 243, 245);")
        self.tabPrctos_body_tabla.setFrameShape(QFrame.StyledPanel)
        self.tabPrctos_body_tabla.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.tabPrctos_body_tabla)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(7, 7, 7, 0)
        self.pctosVista_tableW = QTableWidget(self.tabPrctos_body_tabla)
        if (self.pctosVista_tableW.columnCount() < 3):
            self.pctosVista_tableW.setColumnCount(3)
        icon7 = QIcon()
        icon7.addFile(u":/blupack/bl-id-secure.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setIcon(icon7);
        self.pctosVista_tableW.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        icon8 = QIcon()
        icon8.addFile(u":/blupack/bl-tag.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setIcon(icon8);
        self.pctosVista_tableW.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        icon9 = QIcon()
        icon9.addFile(u":/blupack/bl-ruler.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setIcon(icon9);
        self.pctosVista_tableW.setHorizontalHeaderItem(2, __qtablewidgetitem4)
        self.pctosVista_tableW.setObjectName(u"pctosVista_tableW")
        self.pctosVista_tableW.setFrameShape(QFrame.NoFrame)
        self.pctosVista_tableW.setFrameShadow(QFrame.Plain)
        self.pctosVista_tableW.setAutoScroll(True)
        self.pctosVista_tableW.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.pctosVista_tableW.setGridStyle(Qt.SolidLine)
        self.pctosVista_tableW.horizontalHeader().setStretchLastSection(True)
        self.pctosVista_tableW.verticalHeader().setVisible(False)
        self.pctosVista_tableW.verticalHeader().setCascadingSectionResizes(False)
        self.pctosVista_tableW.verticalHeader().setHighlightSections(True)
        self.pctosVista_tableW.verticalHeader().setProperty("showSortIndicator", False)
        self.pctosVista_tableW.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_15.addWidget(self.pctosVista_tableW)


        self.horizontalLayout_4.addWidget(self.tabPrctos_body_tabla)


        self.horizontalLayout_19.addWidget(self.tabPrctos_body_tab)

        self.cuerpo_productos_tabsW.addTab(self.cuerpo_productos_tabPrctos, "")
        self.cuerpo_productos_tabPaqt = QWidget()
        self.cuerpo_productos_tabPaqt.setObjectName(u"cuerpo_productos_tabPaqt")
        self.cuerpo_productos_tabPaqt.setEnabled(True)
        self.verticalLayout_17 = QVBoxLayout(self.cuerpo_productos_tabPaqt)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(-1, 0, -1, -1)
        self.tabPaqt_body_tab = QFrame(self.cuerpo_productos_tabPaqt)
        self.tabPaqt_body_tab.setObjectName(u"tabPaqt_body_tab")
        self.tabPaqt_body_tab.setStyleSheet(u"QLineEdit {\n"
"	border-radius: 10px;\n"
"	padding: 5px 10px;\n"
"	background-color: rgb(255,255,255);\n"
"	color: rgb(0,0,0);\n"
"}\n"
"QFrame {\n"
"	border-radius:10px;\n"
"	background-color: rgb(242, 243, 245);\n"
"}")
        self.tabPaqt_body_tab.setFrameShape(QFrame.StyledPanel)
        self.tabPaqt_body_tab.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.tabPaqt_body_tab)
        self.verticalLayout_21.setSpacing(6)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(9, 9, 9, 9)
        self.ingresaNombre_label = QLabel(self.tabPaqt_body_tab)
        self.ingresaNombre_label.setObjectName(u"ingresaNombre_label")
        self.ingresaNombre_label.setFont(font6)

        self.verticalLayout_21.addWidget(self.ingresaNombre_label)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setHorizontalSpacing(6)
        self.codigoBarrasPaqt_label = QLabel(self.tabPaqt_body_tab)
        self.codigoBarrasPaqt_label.setObjectName(u"codigoBarrasPaqt_label")
        self.codigoBarrasPaqt_label.setFont(font6)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.codigoBarrasPaqt_label)

        self.codigoBarrasPaqt_lineE = QLineEdit(self.tabPaqt_body_tab)
        self.codigoBarrasPaqt_lineE.setObjectName(u"codigoBarrasPaqt_lineE")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.codigoBarrasPaqt_lineE)

        self.cantidadPrctoPaqt_label = QLabel(self.tabPaqt_body_tab)
        self.cantidadPrctoPaqt_label.setObjectName(u"cantidadPrctoPaqt_label")
        self.cantidadPrctoPaqt_label.setFont(font6)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.cantidadPrctoPaqt_label)

        self.cantidadPrctoPaqt_lineE = QLineEdit(self.tabPaqt_body_tab)
        self.cantidadPrctoPaqt_lineE.setObjectName(u"cantidadPrctoPaqt_lineE")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.cantidadPrctoPaqt_lineE)

        self.agregarProducPaqt_label = QLabel(self.tabPaqt_body_tab)
        self.agregarProducPaqt_label.setObjectName(u"agregarProducPaqt_label")
        self.agregarProducPaqt_label.setFont(font6)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.agregarProducPaqt_label)

        self.AnadirPrctoPaqt_bttn = QPushButton(self.tabPaqt_body_tab)
        self.AnadirPrctoPaqt_bttn.setObjectName(u"AnadirPrctoPaqt_bttn")
        self.AnadirPrctoPaqt_bttn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(212, 223, 231);\n"
"	color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(192, 202, 209);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(212, 223, 231);\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/redpack/rd-add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.AnadirPrctoPaqt_bttn.setIcon(icon10)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.AnadirPrctoPaqt_bttn)


        self.horizontalLayout_21.addLayout(self.formLayout_2)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.nombrePrctoPaqt_label = QLabel(self.tabPaqt_body_tab)
        self.nombrePrctoPaqt_label.setObjectName(u"nombrePrctoPaqt_label")
        self.nombrePrctoPaqt_label.setFont(font6)

        self.verticalLayout_26.addWidget(self.nombrePrctoPaqt_label)

        self.verticalSpacer_6 = QSpacerItem(20, 63, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_26.addItem(self.verticalSpacer_6)


        self.horizontalLayout_21.addLayout(self.verticalLayout_26)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_11)


        self.verticalLayout_21.addLayout(self.horizontalLayout_21)

        self.paqtPrctosVista_tableW = QTableWidget(self.tabPaqt_body_tab)
        if (self.paqtPrctosVista_tableW.columnCount() < 2):
            self.paqtPrctosVista_tableW.setColumnCount(2)
        icon11 = QIcon()
        icon11.addFile(u":/blupack/bl-product.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setIcon(icon11);
        self.paqtPrctosVista_tableW.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        icon12 = QIcon()
        icon12.addFile(u":/blupack/bl-scale.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setIcon(icon12);
        self.paqtPrctosVista_tableW.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        self.paqtPrctosVista_tableW.setObjectName(u"paqtPrctosVista_tableW")
        sizePolicy5.setHeightForWidth(self.paqtPrctosVista_tableW.sizePolicy().hasHeightForWidth())
        self.paqtPrctosVista_tableW.setSizePolicy(sizePolicy5)
        self.paqtPrctosVista_tableW.setStyleSheet(u"background-color: rgb(255,255,255)")
        self.paqtPrctosVista_tableW.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.paqtPrctosVista_tableW.setGridStyle(Qt.SolidLine)
        self.paqtPrctosVista_tableW.setSortingEnabled(False)
        self.paqtPrctosVista_tableW.horizontalHeader().setVisible(True)
        self.paqtPrctosVista_tableW.horizontalHeader().setProperty("showSortIndicator", False)
        self.paqtPrctosVista_tableW.horizontalHeader().setStretchLastSection(False)
        self.paqtPrctosVista_tableW.verticalHeader().setVisible(False)
        self.paqtPrctosVista_tableW.verticalHeader().setCascadingSectionResizes(False)
        self.paqtPrctosVista_tableW.verticalHeader().setHighlightSections(True)
        self.paqtPrctosVista_tableW.verticalHeader().setProperty("showSortIndicator", False)
        self.paqtPrctosVista_tableW.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_21.addWidget(self.paqtPrctosVista_tableW)

        self.frame_14 = QFrame(self.tabPaqt_body_tab)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.guadarPaqt_btton = QPushButton(self.frame_14)
        self.guadarPaqt_btton.setObjectName(u"guadarPaqt_btton")
        font14 = QFont()
        font14.setFamilies([u"Microsoft YaHei UI"])
        font14.setPointSize(9)
        font14.setBold(False)
        self.guadarPaqt_btton.setFont(font14)
        self.guadarPaqt_btton.setStyleSheet(u"QPushButton {\n"
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
        self.guadarPaqt_btton.setIcon(icon5)

        self.horizontalLayout_27.addWidget(self.guadarPaqt_btton)

        self.limpiarPaqt_btton = QPushButton(self.frame_14)
        self.limpiarPaqt_btton.setObjectName(u"limpiarPaqt_btton")
        self.limpiarPaqt_btton.setFont(font14)
        self.limpiarPaqt_btton.setStyleSheet(u"QPushButton {\n"
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
        icon13 = QIcon()
        icon13.addFile(u":/redpack/rd-close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.limpiarPaqt_btton.setIcon(icon13)

        self.horizontalLayout_27.addWidget(self.limpiarPaqt_btton)

        self.tipPaqt_label = QLabel(self.frame_14)
        self.tipPaqt_label.setObjectName(u"tipPaqt_label")

        self.horizontalLayout_27.addWidget(self.tipPaqt_label)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_17)


        self.verticalLayout_21.addWidget(self.frame_14)


        self.verticalLayout_17.addWidget(self.tabPaqt_body_tab)

        self.cuerpo_productos_tabsW.addTab(self.cuerpo_productos_tabPaqt, "")
        self.cuerpo_productos_tabDepa = QWidget()
        self.cuerpo_productos_tabDepa.setObjectName(u"cuerpo_productos_tabDepa")
        self.verticalLayout_20 = QVBoxLayout(self.cuerpo_productos_tabDepa)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.tabDepa_body_tab = QFrame(self.cuerpo_productos_tabDepa)
        self.tabDepa_body_tab.setObjectName(u"tabDepa_body_tab")
        self.tabDepa_body_tab.setFrameShape(QFrame.StyledPanel)
        self.tabDepa_body_tab.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.tabDepa_body_tab)
        self.horizontalLayout_25.setSpacing(6)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.tabDepa_body_frame = QFrame(self.tabDepa_body_tab)
        self.tabDepa_body_frame.setObjectName(u"tabDepa_body_frame")
        self.tabDepa_body_frame.setStyleSheet(u"QLineEdit {\n"
"	border-radius: 10px;\n"
"	padding: 5px 10px;\n"
"	background-color: rgb(255,255,255);\n"
"	color: rgb(0,0,0);\n"
"}\n"
"QFrame {\n"
"	border-radius:10px;\n"
"	background-color: rgb(242, 243, 245);\n"
"}")
        self.tabDepa_body_frame.setFrameShape(QFrame.StyledPanel)
        self.tabDepa_body_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.tabDepa_body_frame)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.nuevaCategoriaDepa_label = QLabel(self.tabDepa_body_frame)
        self.nuevaCategoriaDepa_label.setObjectName(u"nuevaCategoriaDepa_label")
        self.nuevaCategoriaDepa_label.setFont(font6)
        self.nuevaCategoriaDepa_label.setStyleSheet(u"padding: 5px;")

        self.verticalLayout_18.addWidget(self.nuevaCategoriaDepa_label)

        self.categoriaDepa_label = QLabel(self.tabDepa_body_frame)
        self.categoriaDepa_label.setObjectName(u"categoriaDepa_label")
        self.categoriaDepa_label.setFont(font6)

        self.verticalLayout_18.addWidget(self.categoriaDepa_label)

        self.categoriaDepa_lineE = QLineEdit(self.tabDepa_body_frame)
        self.categoriaDepa_lineE.setObjectName(u"categoriaDepa_lineE")

        self.verticalLayout_18.addWidget(self.categoriaDepa_lineE)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setSpacing(6)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.guardarDepa_bttn = QPushButton(self.tabDepa_body_frame)
        self.guardarDepa_bttn.setObjectName(u"guardarDepa_bttn")
        sizePolicy1.setHeightForWidth(self.guardarDepa_bttn.sizePolicy().hasHeightForWidth())
        self.guardarDepa_bttn.setSizePolicy(sizePolicy1)
        self.guardarDepa_bttn.setFont(font12)
        self.guardarDepa_bttn.setStyleSheet(u"QPushButton {\n"
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
        self.guardarDepa_bttn.setIcon(icon5)

        self.horizontalLayout_30.addWidget(self.guardarDepa_bttn)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_14)

        self.limpiarDepa_bttn = QPushButton(self.tabDepa_body_frame)
        self.limpiarDepa_bttn.setObjectName(u"limpiarDepa_bttn")
        sizePolicy1.setHeightForWidth(self.limpiarDepa_bttn.sizePolicy().hasHeightForWidth())
        self.limpiarDepa_bttn.setSizePolicy(sizePolicy1)
        self.limpiarDepa_bttn.setFont(font12)
        self.limpiarDepa_bttn.setStyleSheet(u"QPushButton {\n"
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
        self.limpiarDepa_bttn.setIcon(icon6)

        self.horizontalLayout_30.addWidget(self.limpiarDepa_bttn)


        self.verticalLayout_18.addLayout(self.horizontalLayout_30)

        self.verticalSpacer_11 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_11)


        self.horizontalLayout_25.addWidget(self.tabDepa_body_frame)

        self.tabDepa_body_viewT = QFrame(self.tabDepa_body_tab)
        self.tabDepa_body_viewT.setObjectName(u"tabDepa_body_viewT")
        self.tabDepa_body_viewT.setStyleSheet(u"	border-radius:10px;\n"
"	background-color: rgb(242, 243, 245);")
        self.tabDepa_body_viewT.setFrameShape(QFrame.StyledPanel)
        self.tabDepa_body_viewT.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.tabDepa_body_viewT)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(7, 7, 7, 0)
        self.tipDepa_label = QLabel(self.tabDepa_body_viewT)
        self.tipDepa_label.setObjectName(u"tipDepa_label")
        self.tipDepa_label.setEnabled(True)
        self.tipDepa_label.setFont(font6)
        self.tipDepa_label.setStyleSheet(u"padding: 5px;")

        self.verticalLayout_19.addWidget(self.tipDepa_label)

        self.depaVista_listW = QListWidget(self.tabDepa_body_viewT)
        self.depaVista_listW.setObjectName(u"depaVista_listW")
        font15 = QFont()
        font15.setFamilies([u"Rubik Medium"])
        font15.setPointSize(11)
        self.depaVista_listW.setFont(font15)
        self.depaVista_listW.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.verticalLayout_19.addWidget(self.depaVista_listW)


        self.horizontalLayout_25.addWidget(self.tabDepa_body_viewT)


        self.verticalLayout_20.addWidget(self.tabDepa_body_tab)

        self.cuerpo_productos_tabsW.addTab(self.cuerpo_productos_tabDepa, "")

        self.verticalLayout_12.addWidget(self.cuerpo_productos_tabsW)

        icon14 = QIcon()
        icon14.addFile(u":/blupack/bl-shopping-cest.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabPrincipal.addTab(self.tab3_productos, icon14, "")
        self.tab4_inventario = QWidget()
        self.tab4_inventario.setObjectName(u"tab4_inventario")
        self.tab4_inventario.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton {\n"
"	border-radius: 10px;\n"
"	padding: 5px 10px;\n"
"	background-color: rgb(12, 95, 194);\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(15, 122, 244);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(12, 95, 194);\n"
"}")
        self.verticalLayout_14 = QVBoxLayout(self.tab4_inventario)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.titulo_inventario = QLabel(self.tab4_inventario)
        self.titulo_inventario.setObjectName(u"titulo_inventario")
        self.titulo_inventario.setFont(font6)
        self.titulo_inventario.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(233, 245, 254);\n"
"padding: 5px;")

        self.verticalLayout_14.addWidget(self.titulo_inventario)

        self.cabeza_inventario_cajaBtn = QFrame(self.tab4_inventario)
        self.cabeza_inventario_cajaBtn.setObjectName(u"cabeza_inventario_cajaBtn")
        self.cabeza_inventario_cajaBtn.setFrameShape(QFrame.StyledPanel)
        self.cabeza_inventario_cajaBtn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.cabeza_inventario_cajaBtn)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.agregarInv_bttn = QPushButton(self.cabeza_inventario_cajaBtn)
        self.agregarInv_bttn.setObjectName(u"agregarInv_bttn")
        self.agregarInv_bttn.setFont(font12)

        self.horizontalLayout_18.addWidget(self.agregarInv_bttn)

        self.modificarInv_bttn = QPushButton(self.cabeza_inventario_cajaBtn)
        self.modificarInv_bttn.setObjectName(u"modificarInv_bttn")
        self.modificarInv_bttn.setFont(font12)

        self.horizontalLayout_18.addWidget(self.modificarInv_bttn)

        self.productosCritInv_bttn = QPushButton(self.cabeza_inventario_cajaBtn)
        self.productosCritInv_bttn.setObjectName(u"productosCritInv_bttn")
        self.productosCritInv_bttn.setFont(font12)

        self.horizontalLayout_18.addWidget(self.productosCritInv_bttn)

        self.reporteInv_bttn = QPushButton(self.cabeza_inventario_cajaBtn)
        self.reporteInv_bttn.setObjectName(u"reporteInv_bttn")
        self.reporteInv_bttn.setFont(font12)

        self.horizontalLayout_18.addWidget(self.reporteInv_bttn)

        self.reporteMoviInv_bttn = QPushButton(self.cabeza_inventario_cajaBtn)
        self.reporteMoviInv_bttn.setObjectName(u"reporteMoviInv_bttn")
        self.reporteMoviInv_bttn.setFont(font12)

        self.horizontalLayout_18.addWidget(self.reporteMoviInv_bttn)


        self.verticalLayout_14.addWidget(self.cabeza_inventario_cajaBtn)

        self.subTitulo_inventario = QLabel(self.tab4_inventario)
        self.subTitulo_inventario.setObjectName(u"subTitulo_inventario")
        self.subTitulo_inventario.setFont(font6)
        self.subTitulo_inventario.setStyleSheet(u"color: rgb(0,0,0);\n"
"background-color: rgb(191, 226, 229);\n"
"padding:7px 10px; \n"
"border-radius:10px;")

        self.verticalLayout_14.addWidget(self.subTitulo_inventario)

        self.body_inventario_frame = QFrame(self.tab4_inventario)
        self.body_inventario_frame.setObjectName(u"body_inventario_frame")
        self.body_inventario_frame.setStyleSheet(u"QFrame {\n"
"	border-radius: 10px;\n"
"	background-color: rgb(221, 233, 241);\n"
"}")
        self.body_inventario_frame.setFrameShape(QFrame.StyledPanel)
        self.body_inventario_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.body_inventario_frame)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.categariasInv_label = QLabel(self.body_inventario_frame)
        self.categariasInv_label.setObjectName(u"categariasInv_label")
        self.categariasInv_label.setFont(font6)

        self.horizontalLayout_20.addWidget(self.categariasInv_label)

        self.categoriasInv_comboB = QComboBox(self.body_inventario_frame)
        self.categoriasInv_comboB.setObjectName(u"categoriasInv_comboB")
        sizePolicy1.setHeightForWidth(self.categoriasInv_comboB.sizePolicy().hasHeightForWidth())
        self.categoriasInv_comboB.setSizePolicy(sizePolicy1)
        self.categoriasInv_comboB.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(207, 218, 226);\n"
"color: rgb(0,0,0);;\n"
"padding: 5px 5px;\n"
"")
        self.categoriasInv_comboB.setFrame(False)

        self.horizontalLayout_20.addWidget(self.categoriasInv_comboB)

        self.exportarInv_bttn = QPushButton(self.body_inventario_frame)
        self.exportarInv_bttn.setObjectName(u"exportarInv_bttn")
        self.exportarInv_bttn.setFont(font12)
        self.exportarInv_bttn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(212, 223, 231);\n"
"	color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(192, 202, 209);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(212, 223, 231);\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u":/redpack/rd-file-excel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exportarInv_bttn.setIcon(icon15)

        self.horizontalLayout_20.addWidget(self.exportarInv_bttn)

        self.imprimirInv_bttn = QPushButton(self.body_inventario_frame)
        self.imprimirInv_bttn.setObjectName(u"imprimirInv_bttn")
        font16 = QFont()
        font16.setFamilies([u"Microsoft JhengHei"])
        self.imprimirInv_bttn.setFont(font16)
        self.imprimirInv_bttn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(212, 223, 231);\n"
"	color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(192, 202, 209);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(212, 223, 231);\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u":/redpack/rd-printer-scan.png", QSize(), QIcon.Normal, QIcon.Off)
        self.imprimirInv_bttn.setIcon(icon16)

        self.horizontalLayout_20.addWidget(self.imprimirInv_bttn)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_10)


        self.verticalLayout_14.addWidget(self.body_inventario_frame)

        self.inventarioView_tableW = QTableWidget(self.tab4_inventario)
        if (self.inventarioView_tableW.columnCount() < 8):
            self.inventarioView_tableW.setColumnCount(8)
        icon17 = QIcon()
        icon17.addFile(u":/blupack/bl-barcode.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setIcon(icon17);
        self.inventarioView_tableW.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        icon18 = QIcon()
        icon18.addFile(u":/blupack/bl-description.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setIcon(icon18);
        self.inventarioView_tableW.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        icon19 = QIcon()
        icon19.addFile(u":/blupack/bl-money-sell.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setIcon(icon19);
        self.inventarioView_tableW.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        icon20 = QIcon()
        icon20.addFile(u":/blupack/bl-money-buy.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setIcon(icon20);
        self.inventarioView_tableW.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        icon21 = QIcon()
        icon21.addFile(u":/blupack/bl-gift.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setIcon(icon21);
        self.inventarioView_tableW.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setIcon(icon12);
        self.inventarioView_tableW.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        icon22 = QIcon()
        icon22.addFile(u":/blupack/bl-danger.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setIcon(icon22);
        self.inventarioView_tableW.setHorizontalHeaderItem(6, __qtablewidgetitem13)
        icon23 = QIcon()
        icon23.addFile(u":/blupack/bl-folder.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setIcon(icon23);
        self.inventarioView_tableW.setHorizontalHeaderItem(7, __qtablewidgetitem14)
        self.inventarioView_tableW.setObjectName(u"inventarioView_tableW")
        self.inventarioView_tableW.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.inventarioView_tableW.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.inventarioView_tableW.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.inventarioView_tableW.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.inventarioView_tableW.setProperty("showDropIndicator", True)
        self.inventarioView_tableW.setDragDropOverwriteMode(True)
        self.inventarioView_tableW.setShowGrid(True)
        self.inventarioView_tableW.setWordWrap(True)
        self.inventarioView_tableW.setCornerButtonEnabled(True)
        self.inventarioView_tableW.horizontalHeader().setVisible(True)
        self.inventarioView_tableW.horizontalHeader().setCascadingSectionResizes(False)
        self.inventarioView_tableW.horizontalHeader().setHighlightSections(True)
        self.inventarioView_tableW.horizontalHeader().setProperty("showSortIndicator", False)
        self.inventarioView_tableW.horizontalHeader().setStretchLastSection(False)
        self.inventarioView_tableW.verticalHeader().setCascadingSectionResizes(False)

        self.verticalLayout_14.addWidget(self.inventarioView_tableW)

        self.pie_inventario_frame = QFrame(self.tab4_inventario)
        self.pie_inventario_frame.setObjectName(u"pie_inventario_frame")
        self.pie_inventario_frame.setStyleSheet(u"background-color: rgb(88, 88, 88);\n"
"color: rgb(255, 255, 255);\n"
"padding: 2px;\n"
"border-radius: 10px;")
        self.pie_inventario_frame.setFrameShape(QFrame.StyledPanel)
        self.pie_inventario_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.pie_inventario_frame)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.frame_28 = QFrame(self.pie_inventario_frame)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFont(font6)
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_28)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.costoInv_label = QLabel(self.frame_28)
        self.costoInv_label.setObjectName(u"costoInv_label")
        self.costoInv_label.setFont(font13)

        self.verticalLayout_16.addWidget(self.costoInv_label)

        self.costoInv_lineE = QLabel(self.frame_28)
        self.costoInv_lineE.setObjectName(u"costoInv_lineE")
        sizePolicy.setHeightForWidth(self.costoInv_lineE.sizePolicy().hasHeightForWidth())
        self.costoInv_lineE.setSizePolicy(sizePolicy)
        self.costoInv_lineE.setFont(font13)
        self.costoInv_lineE.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.costoInv_lineE)


        self.horizontalLayout_22.addWidget(self.frame_28)

        self.frame_29 = QFrame(self.pie_inventario_frame)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_29)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(9, 0, 0, 0)
        self.cantidadPrctosInv_label = QLabel(self.frame_29)
        self.cantidadPrctosInv_label.setObjectName(u"cantidadPrctosInv_label")
        self.cantidadPrctosInv_label.setFont(font13)

        self.verticalLayout_11.addWidget(self.cantidadPrctosInv_label)

        self.cantidadPrctosInv_lineE = QLabel(self.frame_29)
        self.cantidadPrctosInv_lineE.setObjectName(u"cantidadPrctosInv_lineE")
        self.cantidadPrctosInv_lineE.setFont(font13)

        self.verticalLayout_11.addWidget(self.cantidadPrctosInv_lineE)


        self.horizontalLayout_22.addWidget(self.frame_29)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_9)


        self.verticalLayout_14.addWidget(self.pie_inventario_frame)

        icon24 = QIcon()
        icon24.addFile(u":/blupack/bl-inventory-store.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabPrincipal.addTab(self.tab4_inventario, icon24, "")
        self.tab5_compras = QWidget()
        self.tab5_compras.setObjectName(u"tab5_compras")
        self.tab5_compras.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton {\n"
"	border-radius: 10px;\n"
"	padding: 5px 10px;\n"
"	background-color: rgb(12, 95, 194);\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.horizontalLayout_40 = QHBoxLayout(self.tab5_compras)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.cuerpo_compras_frame = QFrame(self.tab5_compras)
        self.cuerpo_compras_frame.setObjectName(u"cuerpo_compras_frame")
        self.cuerpo_compras_frame.setFrameShape(QFrame.StyledPanel)
        self.cuerpo_compras_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.cuerpo_compras_frame)
        self.verticalLayout_23.setSpacing(2)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.cuerpo_cabeza_buqueda = QFrame(self.cuerpo_compras_frame)
        self.cuerpo_cabeza_buqueda.setObjectName(u"cuerpo_cabeza_buqueda")
        self.cuerpo_cabeza_buqueda.setStyleSheet(u"QFrame {\n"
"	border-top-left-radius: 5px;\n"
"	border-top-right-radius: 5px;\n"
"	background-color: rgb(233, 245, 254);\n"
"}\n"
"\n"
"QLineEdit {\n"
"	border-radius: 10px;\n"
"	padding: 5px 10px;\n"
"	background-color: rgb(255,255,255);\n"
"	color: rgb(0,0,0);\n"
"}")
        self.cuerpo_cabeza_buqueda.setFrameShape(QFrame.StyledPanel)
        self.cuerpo_cabeza_buqueda.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.cuerpo_cabeza_buqueda)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.comprasComprs_label = QLabel(self.cuerpo_cabeza_buqueda)
        self.comprasComprs_label.setObjectName(u"comprasComprs_label")
        self.comprasComprs_label.setFont(font6)
        self.comprasComprs_label.setStyleSheet(u"")

        self.horizontalLayout_41.addWidget(self.comprasComprs_label)

        self.comprasComprs_lineE = QLineEdit(self.cuerpo_cabeza_buqueda)
        self.comprasComprs_lineE.setObjectName(u"comprasComprs_lineE")
        self.comprasComprs_lineE.setStyleSheet(u"background-color: rgb(255,255,255);")
        self.comprasComprs_lineE.setFrame(False)

        self.horizontalLayout_41.addWidget(self.comprasComprs_lineE)

        self.comprasBusquedaComprs_bttn = QPushButton(self.cuerpo_cabeza_buqueda)
        self.comprasBusquedaComprs_bttn.setObjectName(u"comprasBusquedaComprs_bttn")
        self.comprasBusquedaComprs_bttn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(212, 223, 231);\n"
"	color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(192, 202, 209);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(212, 223, 231);\n"
"}")
        icon25 = QIcon()
        icon25.addFile(u":/redpack/rd-search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comprasBusquedaComprs_bttn.setIcon(icon25)

        self.horizontalLayout_41.addWidget(self.comprasBusquedaComprs_bttn)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_28)


        self.verticalLayout_23.addWidget(self.cuerpo_cabeza_buqueda)

        self.cuerpo_introduccion_informacion = QFrame(self.cuerpo_compras_frame)
        self.cuerpo_introduccion_informacion.setObjectName(u"cuerpo_introduccion_informacion")
        self.cuerpo_introduccion_informacion.setFrameShape(QFrame.StyledPanel)
        self.cuerpo_introduccion_informacion.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.cuerpo_introduccion_informacion)
        self.verticalLayout_27.setSpacing(2)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.introduccion_productos_frame = QFrame(self.cuerpo_introduccion_informacion)
        self.introduccion_productos_frame.setObjectName(u"introduccion_productos_frame")
        self.introduccion_productos_frame.setStyleSheet(u"QLineEdit {\n"
"	border-radius: 10px;\n"
"	padding: 5px 10px;\n"
"	background-color: rgb(255,255,255);\n"
"	color: rgb(0,0,0);\n"
"}\n"
"QFrame {\n"
"	border-bottom-left-radius: 5px;\n"
"	background-color: rgb(242, 243, 245);\n"
"}")
        self.introduccion_productos_frame.setFrameShape(QFrame.StyledPanel)
        self.introduccion_productos_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.introduccion_productos_frame)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(5, 5, 5, 5)
        self.frame_37 = QFrame(self.introduccion_productos_frame)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_37)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.cantidadPrctosComprs_label = QLabel(self.frame_37)
        self.cantidadPrctosComprs_label.setObjectName(u"cantidadPrctosComprs_label")
        self.cantidadPrctosComprs_label.setFont(font6)

        self.gridLayout_3.addWidget(self.cantidadPrctosComprs_label, 3, 0, 1, 1)

        self.codPrctoComprs_lineE = QLineEdit(self.frame_37)
        self.codPrctoComprs_lineE.setObjectName(u"codPrctoComprs_lineE")

        self.gridLayout_3.addWidget(self.codPrctoComprs_lineE, 2, 1, 1, 1)

        self.PrecioCompraComprs_lineE = QLineEdit(self.frame_37)
        self.PrecioCompraComprs_lineE.setObjectName(u"PrecioCompraComprs_lineE")
        self.PrecioCompraComprs_lineE.setEnabled(True)
        self.PrecioCompraComprs_lineE.setStyleSheet(u"background-color: rgb(255,255,255);")

        self.gridLayout_3.addWidget(self.PrecioCompraComprs_lineE, 4, 1, 1, 1)

        self.cantidadPrctosComprs_lineE = QLineEdit(self.frame_37)
        self.cantidadPrctosComprs_lineE.setObjectName(u"cantidadPrctosComprs_lineE")
        self.cantidadPrctosComprs_lineE.setFrame(True)

        self.gridLayout_3.addWidget(self.cantidadPrctosComprs_lineE, 3, 1, 1, 1)

        self.PrecioCompraComprs_label = QLabel(self.frame_37)
        self.PrecioCompraComprs_label.setObjectName(u"PrecioCompraComprs_label")
        self.PrecioCompraComprs_label.setFont(font6)

        self.gridLayout_3.addWidget(self.PrecioCompraComprs_label, 4, 0, 1, 1)

        self.proveedorComprs_label = QLabel(self.frame_37)
        self.proveedorComprs_label.setObjectName(u"proveedorComprs_label")
        self.proveedorComprs_label.setFont(font6)

        self.gridLayout_3.addWidget(self.proveedorComprs_label, 1, 0, 1, 1)

        self.label_60 = QLabel(self.frame_37)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setFont(font6)

        self.gridLayout_3.addWidget(self.label_60, 3, 2, 1, 1)

        self.label_61 = QLabel(self.frame_37)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setFont(font13)

        self.gridLayout_3.addWidget(self.label_61, 3, 3, 1, 1)

        self.codPrctoComprs_label = QLabel(self.frame_37)
        self.codPrctoComprs_label.setObjectName(u"codPrctoComprs_label")
        self.codPrctoComprs_label.setFont(font6)

        self.gridLayout_3.addWidget(self.codPrctoComprs_label, 2, 0, 1, 1)

        self.PrctoComprs_label = QLabel(self.frame_37)
        self.PrctoComprs_label.setObjectName(u"PrctoComprs_label")
        self.PrctoComprs_label.setFont(font6)

        self.gridLayout_3.addWidget(self.PrctoComprs_label, 2, 2, 1, 1)

        self.PrecioVentaComprs_label = QLabel(self.frame_37)
        self.PrecioVentaComprs_label.setObjectName(u"PrecioVentaComprs_label")
        self.PrecioVentaComprs_label.setFont(font6)

        self.gridLayout_3.addWidget(self.PrecioVentaComprs_label, 1, 2, 1, 1)

        self.PrecioVentaComprs_lineE = QLineEdit(self.frame_37)
        self.PrecioVentaComprs_lineE.setObjectName(u"PrecioVentaComprs_lineE")
        self.PrecioVentaComprs_lineE.setEnabled(True)
        self.PrecioVentaComprs_lineE.setStyleSheet(u"background-color: rgb(255,255,255);")

        self.gridLayout_3.addWidget(self.PrecioVentaComprs_lineE, 1, 3, 1, 1)

        self.AnadirPrctpComprs_bttn = QPushButton(self.frame_37)
        self.AnadirPrctpComprs_bttn.setObjectName(u"AnadirPrctpComprs_bttn")
        self.AnadirPrctpComprs_bttn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(212, 223, 231);\n"
"	color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(192, 202, 209);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(212, 223, 231);\n"
"}")
        self.AnadirPrctpComprs_bttn.setIcon(icon10)

        self.gridLayout_3.addWidget(self.AnadirPrctpComprs_bttn, 4, 2, 1, 1)

        self.proveedorComprs_comboB = QComboBox(self.frame_37)
        self.proveedorComprs_comboB.setObjectName(u"proveedorComprs_comboB")
        self.proveedorComprs_comboB.setStyleSheet(u"border-radius: 10px;\n"
"padding: 5px 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0,0,0);")

        self.gridLayout_3.addWidget(self.proveedorComprs_comboB, 1, 1, 1, 1)

        self.PrctoComprs_lineE = QLabel(self.frame_37)
        self.PrctoComprs_lineE.setObjectName(u"PrctoComprs_lineE")

        self.gridLayout_3.addWidget(self.PrctoComprs_lineE, 2, 3, 1, 1)


        self.verticalLayout_22.addWidget(self.frame_37)


        self.verticalLayout_27.addWidget(self.introduccion_productos_frame)

        self.introduccion_table_frame = QFrame(self.cuerpo_introduccion_informacion)
        self.introduccion_table_frame.setObjectName(u"introduccion_table_frame")
        sizePolicy5.setHeightForWidth(self.introduccion_table_frame.sizePolicy().hasHeightForWidth())
        self.introduccion_table_frame.setSizePolicy(sizePolicy5)
        self.introduccion_table_frame.setStyleSheet(u"border-bottom-right-radius: 5px;\n"
"background-color: rgb(242, 243, 245);")
        self.introduccion_table_frame.setFrameShape(QFrame.StyledPanel)
        self.introduccion_table_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.introduccion_table_frame)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(7, 7, 7, 0)
        self.ComprsViews_tableW = QTableWidget(self.introduccion_table_frame)
        if (self.ComprsViews_tableW.columnCount() < 6):
            self.ComprsViews_tableW.setColumnCount(6)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setIcon(icon7);
        self.ComprsViews_tableW.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setIcon(icon8);
        self.ComprsViews_tableW.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setIcon(icon12);
        self.ComprsViews_tableW.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setIcon(icon20);
        self.ComprsViews_tableW.setHorizontalHeaderItem(3, __qtablewidgetitem18)
        icon26 = QIcon()
        icon26.addFile(u":/blupack/bl-data-analysis.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setIcon(icon26);
        self.ComprsViews_tableW.setHorizontalHeaderItem(4, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setIcon(icon9);
        self.ComprsViews_tableW.setHorizontalHeaderItem(5, __qtablewidgetitem20)
        self.ComprsViews_tableW.setObjectName(u"ComprsViews_tableW")
        self.ComprsViews_tableW.setFrameShape(QFrame.NoFrame)
        self.ComprsViews_tableW.setFrameShadow(QFrame.Plain)
        self.ComprsViews_tableW.setAutoScroll(True)
        self.ComprsViews_tableW.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ComprsViews_tableW.setGridStyle(Qt.SolidLine)
        self.ComprsViews_tableW.horizontalHeader().setStretchLastSection(True)
        self.ComprsViews_tableW.verticalHeader().setVisible(True)
        self.ComprsViews_tableW.verticalHeader().setCascadingSectionResizes(False)
        self.ComprsViews_tableW.verticalHeader().setHighlightSections(True)
        self.ComprsViews_tableW.verticalHeader().setProperty("showSortIndicator", False)
        self.ComprsViews_tableW.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_24.addWidget(self.ComprsViews_tableW)

        self.frame_35 = QFrame(self.introduccion_table_frame)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setStyleSheet(u"background-color: rgb(212, 223, 231);\n"
"padding: 3px;\n"
"border-radius:10px;")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_23.setSpacing(4)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(2, 2, 2, 2)
        self.guardarComprs_bttn = QPushButton(self.frame_35)
        self.guardarComprs_bttn.setObjectName(u"guardarComprs_bttn")
        self.guardarComprs_bttn.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.guardarComprs_bttn.sizePolicy().hasHeightForWidth())
        self.guardarComprs_bttn.setSizePolicy(sizePolicy1)
        self.guardarComprs_bttn.setFont(font12)
        self.guardarComprs_bttn.setStyleSheet(u"QPushButton {\n"
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
        self.guardarComprs_bttn.setIcon(icon5)

        self.horizontalLayout_23.addWidget(self.guardarComprs_bttn)

        self.limparComprs_bttn = QPushButton(self.frame_35)
        self.limparComprs_bttn.setObjectName(u"limparComprs_bttn")
        self.limparComprs_bttn.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.limparComprs_bttn.sizePolicy().hasHeightForWidth())
        self.limparComprs_bttn.setSizePolicy(sizePolicy1)
        self.limparComprs_bttn.setFont(font12)
        self.limparComprs_bttn.setStyleSheet(u"QPushButton {\n"
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
        self.limparComprs_bttn.setIcon(icon6)

        self.horizontalLayout_23.addWidget(self.limparComprs_bttn)

        self.horizontalSpacer_16 = QSpacerItem(80, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_16)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_15)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_12)


        self.verticalLayout_24.addWidget(self.frame_35)


        self.verticalLayout_27.addWidget(self.introduccion_table_frame)


        self.verticalLayout_23.addWidget(self.cuerpo_introduccion_informacion)


        self.horizontalLayout_40.addWidget(self.cuerpo_compras_frame)

        icon27 = QIcon()
        icon27.addFile(u":/blupack/bl-shop-article.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabPrincipal.addTab(self.tab5_compras, icon27, "")
        self.tab6_proveedores = QWidget()
        self.tab6_proveedores.setObjectName(u"tab6_proveedores")
        self.tab6_proveedores.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton {\n"
"	border-radius: 10px;\n"
"	padding: 5px 10px;\n"
"	background-color: rgb(12, 95, 194);\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout_33 = QVBoxLayout(self.tab6_proveedores)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.cuerpo_proveedores_frame = QFrame(self.tab6_proveedores)
        self.cuerpo_proveedores_frame.setObjectName(u"cuerpo_proveedores_frame")
        self.cuerpo_proveedores_frame.setFrameShape(QFrame.StyledPanel)
        self.cuerpo_proveedores_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.cuerpo_proveedores_frame)
        self.verticalLayout_29.setSpacing(2)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.titulo_proveedores = QLabel(self.cuerpo_proveedores_frame)
        self.titulo_proveedores.setObjectName(u"titulo_proveedores")
        self.titulo_proveedores.setFont(font6)
        self.titulo_proveedores.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(233, 245, 254);\n"
"padding: 5px;")

        self.verticalLayout_29.addWidget(self.titulo_proveedores)

        self.cuerpo_centro_buqueda = QFrame(self.cuerpo_proveedores_frame)
        self.cuerpo_centro_buqueda.setObjectName(u"cuerpo_centro_buqueda")
        self.cuerpo_centro_buqueda.setFrameShape(QFrame.StyledPanel)
        self.cuerpo_centro_buqueda.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.cuerpo_centro_buqueda)
        self.verticalLayout_30.setSpacing(2)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.centro_cabeza_ingresar = QFrame(self.cuerpo_centro_buqueda)
        self.centro_cabeza_ingresar.setObjectName(u"centro_cabeza_ingresar")
        self.centro_cabeza_ingresar.setStyleSheet(u"QLineEdit {\n"
"	border-radius: 10px;\n"
"	padding: 5px 10px;\n"
"	background-color: rgb(255,255,255);\n"
"	color: rgb(0,0,0);\n"
"}\n"
"QFrame {\n"
"	border-bottom-left-radius: 5px;\n"
"	background-color: rgb(242, 243, 245);\n"
"}")
        self.centro_cabeza_ingresar.setFrameShape(QFrame.StyledPanel)
        self.centro_cabeza_ingresar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.centro_cabeza_ingresar)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(5, 5, 5, 5)
        self.frame_44 = QFrame(self.centro_cabeza_ingresar)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_44)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.telefonoProvee_LineE = QLineEdit(self.frame_44)
        self.telefonoProvee_LineE.setObjectName(u"telefonoProvee_LineE")
        self.telefonoProvee_LineE.setEnabled(True)
        self.telefonoProvee_LineE.setStyleSheet(u"background-color: rgb(255,255,255);")

        self.gridLayout_5.addWidget(self.telefonoProvee_LineE, 1, 4, 1, 1)

        self.proveedorProvee_label = QLabel(self.frame_44)
        self.proveedorProvee_label.setObjectName(u"proveedorProvee_label")
        self.proveedorProvee_label.setFont(font6)

        self.gridLayout_5.addWidget(self.proveedorProvee_label, 1, 0, 1, 1)

        self.guardarProvee_bttn = QPushButton(self.frame_44)
        self.guardarProvee_bttn.setObjectName(u"guardarProvee_bttn")
        self.guardarProvee_bttn.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.guardarProvee_bttn.sizePolicy().hasHeightForWidth())
        self.guardarProvee_bttn.setSizePolicy(sizePolicy1)
        self.guardarProvee_bttn.setFont(font12)
        self.guardarProvee_bttn.setStyleSheet(u"QPushButton {\n"
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
        self.guardarProvee_bttn.setIcon(icon6)

        self.gridLayout_5.addWidget(self.guardarProvee_bttn, 6, 4, 1, 1)

        self.direccionProvee_label = QLabel(self.frame_44)
        self.direccionProvee_label.setObjectName(u"direccionProvee_label")
        self.direccionProvee_label.setFont(font6)

        self.gridLayout_5.addWidget(self.direccionProvee_label, 6, 0, 1, 1)

        self.correoEProvee_label = QLabel(self.frame_44)
        self.correoEProvee_label.setObjectName(u"correoEProvee_label")
        self.correoEProvee_label.setFont(font6)

        self.gridLayout_5.addWidget(self.correoEProvee_label, 2, 3, 1, 1)

        self.correoEProvee_lineE = QLineEdit(self.frame_44)
        self.correoEProvee_lineE.setObjectName(u"correoEProvee_lineE")
        self.correoEProvee_lineE.setEnabled(True)
        self.correoEProvee_lineE.setStyleSheet(u"background-color: rgb(255,255,255);")

        self.gridLayout_5.addWidget(self.correoEProvee_lineE, 2, 4, 1, 1)

        self.direccionProvee_lineE = QLineEdit(self.frame_44)
        self.direccionProvee_lineE.setObjectName(u"direccionProvee_lineE")
        self.direccionProvee_lineE.setFrame(True)

        self.gridLayout_5.addWidget(self.direccionProvee_lineE, 6, 2, 1, 1)

        self.telefonoProvee_label = QLabel(self.frame_44)
        self.telefonoProvee_label.setObjectName(u"telefonoProvee_label")
        self.telefonoProvee_label.setFont(font6)

        self.gridLayout_5.addWidget(self.telefonoProvee_label, 1, 3, 1, 1)

        self.limpiarProvee_bttn = QPushButton(self.frame_44)
        self.limpiarProvee_bttn.setObjectName(u"limpiarProvee_bttn")
        self.limpiarProvee_bttn.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.limpiarProvee_bttn.sizePolicy().hasHeightForWidth())
        self.limpiarProvee_bttn.setSizePolicy(sizePolicy1)
        self.limpiarProvee_bttn.setFont(font12)
        self.limpiarProvee_bttn.setStyleSheet(u"QPushButton {\n"
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
        self.limpiarProvee_bttn.setIcon(icon5)

        self.gridLayout_5.addWidget(self.limpiarProvee_bttn, 6, 3, 1, 1)

        self.numDocProvee_lineE = QLineEdit(self.frame_44)
        self.numDocProvee_lineE.setObjectName(u"numDocProvee_lineE")

        self.gridLayout_5.addWidget(self.numDocProvee_lineE, 4, 2, 1, 1)

        self.proveedorProvee_lineE = QLineEdit(self.frame_44)
        self.proveedorProvee_lineE.setObjectName(u"proveedorProvee_lineE")

        self.gridLayout_5.addWidget(self.proveedorProvee_lineE, 1, 2, 1, 1)

        self.tipoDocProvee_label = QLabel(self.frame_44)
        self.tipoDocProvee_label.setObjectName(u"tipoDocProvee_label")
        self.tipoDocProvee_label.setFont(font6)

        self.gridLayout_5.addWidget(self.tipoDocProvee_label, 2, 0, 1, 1)

        self.numDocProvee_label = QLabel(self.frame_44)
        self.numDocProvee_label.setObjectName(u"numDocProvee_label")
        self.numDocProvee_label.setFont(font6)

        self.gridLayout_5.addWidget(self.numDocProvee_label, 4, 0, 1, 1)

        self.tipoDocProvee_comboB = QComboBox(self.frame_44)
        self.tipoDocProvee_comboB.addItem("")
        self.tipoDocProvee_comboB.addItem("")
        self.tipoDocProvee_comboB.addItem("")
        self.tipoDocProvee_comboB.setObjectName(u"tipoDocProvee_comboB")
        self.tipoDocProvee_comboB.setStyleSheet(u"border-radius: 10px;\n"
"padding: 5px 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0,0,0);")

        self.gridLayout_5.addWidget(self.tipoDocProvee_comboB, 2, 2, 1, 1)

        self.paginaProvee_lineE = QLineEdit(self.frame_44)
        self.paginaProvee_lineE.setObjectName(u"paginaProvee_lineE")
        self.paginaProvee_lineE.setEnabled(True)

        self.gridLayout_5.addWidget(self.paginaProvee_lineE, 4, 4, 1, 1)

        self.paginaProvee_label = QLabel(self.frame_44)
        self.paginaProvee_label.setObjectName(u"paginaProvee_label")
        self.paginaProvee_label.setFont(font6)

        self.gridLayout_5.addWidget(self.paginaProvee_label, 4, 3, 1, 1)


        self.verticalLayout_31.addWidget(self.frame_44)


        self.verticalLayout_30.addWidget(self.centro_cabeza_ingresar)

        self.centro_body_busqueda = QFrame(self.cuerpo_centro_buqueda)
        self.centro_body_busqueda.setObjectName(u"centro_body_busqueda")
        self.centro_body_busqueda.setStyleSheet(u"background-color: rgb(221, 233, 241);\n"
"padding: 3px;\n"
"border-radius:10px;")
        self.centro_body_busqueda.setFrameShape(QFrame.StyledPanel)
        self.centro_body_busqueda.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.centro_body_busqueda)
        self.horizontalLayout_26.setSpacing(4)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(2, 2, 2, 2)
        self.buscarProvee_label = QLabel(self.centro_body_busqueda)
        self.buscarProvee_label.setObjectName(u"buscarProvee_label")
        self.buscarProvee_label.setFont(font6)
        self.buscarProvee_label.setStyleSheet(u"")

        self.horizontalLayout_26.addWidget(self.buscarProvee_label)

        self.buscarProvee_lineE = QLineEdit(self.centro_body_busqueda)
        self.buscarProvee_lineE.setObjectName(u"buscarProvee_lineE")
        self.buscarProvee_lineE.setStyleSheet(u"background-color: rgb(255,255,255);")
        self.buscarProvee_lineE.setFrame(False)

        self.horizontalLayout_26.addWidget(self.buscarProvee_lineE)

        self.buscarProvee_bttn = QPushButton(self.centro_body_busqueda)
        self.buscarProvee_bttn.setObjectName(u"buscarProvee_bttn")
        self.buscarProvee_bttn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(212, 223, 231);\n"
"	padding: 5px 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(192, 202, 209);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(212, 223, 231);\n"
"}")
        self.buscarProvee_bttn.setIcon(icon25)

        self.horizontalLayout_26.addWidget(self.buscarProvee_bttn)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_30)


        self.verticalLayout_30.addWidget(self.centro_body_busqueda)

        self.centro_pie_visualizar = QFrame(self.cuerpo_centro_buqueda)
        self.centro_pie_visualizar.setObjectName(u"centro_pie_visualizar")
        sizePolicy5.setHeightForWidth(self.centro_pie_visualizar.sizePolicy().hasHeightForWidth())
        self.centro_pie_visualizar.setSizePolicy(sizePolicy5)
        self.centro_pie_visualizar.setStyleSheet(u"border-bottom-right-radius: 5px;\n"
"background-color: rgb(242, 243, 245);")
        self.centro_pie_visualizar.setFrameShape(QFrame.StyledPanel)
        self.centro_pie_visualizar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.centro_pie_visualizar)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(7, 7, 7, 0)
        self.ProveedorView_tableW = QTableWidget(self.centro_pie_visualizar)
        if (self.ProveedorView_tableW.columnCount() < 5):
            self.ProveedorView_tableW.setColumnCount(5)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setIcon(icon7);
        self.ProveedorView_tableW.setHorizontalHeaderItem(0, __qtablewidgetitem21)
        icon28 = QIcon()
        icon28.addFile(u":/blupack/bl-id.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setIcon(icon28);
        self.ProveedorView_tableW.setHorizontalHeaderItem(1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setIcon(icon8);
        self.ProveedorView_tableW.setHorizontalHeaderItem(2, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setIcon(icon20);
        self.ProveedorView_tableW.setHorizontalHeaderItem(3, __qtablewidgetitem24)
        icon29 = QIcon()
        icon29.addFile(u":/blupack/bl-directions.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setIcon(icon29);
        self.ProveedorView_tableW.setHorizontalHeaderItem(4, __qtablewidgetitem25)
        self.ProveedorView_tableW.setObjectName(u"ProveedorView_tableW")
        self.ProveedorView_tableW.setFrameShape(QFrame.NoFrame)
        self.ProveedorView_tableW.setFrameShadow(QFrame.Plain)
        self.ProveedorView_tableW.setAutoScroll(True)
        self.ProveedorView_tableW.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ProveedorView_tableW.setGridStyle(Qt.SolidLine)
        self.ProveedorView_tableW.horizontalHeader().setStretchLastSection(True)
        self.ProveedorView_tableW.verticalHeader().setVisible(True)
        self.ProveedorView_tableW.verticalHeader().setCascadingSectionResizes(False)
        self.ProveedorView_tableW.verticalHeader().setHighlightSections(True)
        self.ProveedorView_tableW.verticalHeader().setProperty("showSortIndicator", False)
        self.ProveedorView_tableW.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_32.addWidget(self.ProveedorView_tableW)


        self.verticalLayout_30.addWidget(self.centro_pie_visualizar)


        self.verticalLayout_29.addWidget(self.cuerpo_centro_buqueda)


        self.verticalLayout_33.addWidget(self.cuerpo_proveedores_frame)

        icon30 = QIcon()
        icon30.addFile(u":/blupack/bl-supplier.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabPrincipal.addTab(self.tab6_proveedores, icon30, "")
        self.tab7_corte = QWidget()
        self.tab7_corte.setObjectName(u"tab7_corte")
        self.tabPrincipal.addTab(self.tab7_corte, icon26, "")
        self.tab8_configuracion = QWidget()
        self.tab8_configuracion.setObjectName(u"tab8_configuracion")
        icon31 = QIcon()
        icon31.addFile(u":/blupack/bl-setting.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabPrincipal.addTab(self.tab8_configuracion, icon31, "")

        self.horizontalLayout_13.addWidget(self.tabPrincipal)


        self.retranslateUi(Form)

        self.tabPrincipal.setCurrentIndex(0)
        self.pushButton.setDefault(False)
        self.tabWidget_2.setCurrentIndex(0)
        self.cuerpo_productos_tabsW.setCurrentIndex(0)
        self.tipoDocProvee_comboB.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Punto de Venta", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">VENTA - TICKET 1</p></body></html>", None))
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"Introduce el Nombre o el C\u00f3digo de Barras para buscar un Art\u00edculo", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><img src=\":/blupack/bl-search.png\" width=\"16\" height=\"16\"/>    B\u00daSQUEDA</p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u" Enter \n"
" Agregar producto", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"INS VARIOS", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"Buscar", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"Mayoreo", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"Entradas", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Salidas", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Limpiar", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("Form", u"Tab 1", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("Form", u"Tab 2", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">0 Productos en Venta Actualmente</p></body></html>", None))
        self.pushButton_11.setText(QCoreApplication.translate("Form", u"Cambiar", None))
        self.pushButton_10.setText(QCoreApplication.translate("Form", u"Pendiente", None))
        self.pushButton_12.setText(QCoreApplication.translate("Form", u"Eliminar", None))
        self.pushButton_13.setText(QCoreApplication.translate("Form", u"Cobrar", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">0.00 Bs</p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">0.00</p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">0.00</p></body></html>", None))
        self.label_5.setText("")
        self.label_4.setText("")
        self.label_6.setText("")
        self.label_9.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">0.00</p></body></html>", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"Reimprimir ultimo Ticket", None))
        self.pushButton_15.setText(QCoreApplication.translate("Form", u"Ventas del d\u00eda y Devoluciones", None))
        self.tabPrincipal.setTabText(self.tabPrincipal.indexOf(self.tab1_ventas), QCoreApplication.translate("Form", u"Ventas", None))
        self.titulo_clientes.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">CREDITO Y CLIENTES</p></body></html>", None))
        self.EstadoCuenta_bttn.setText(QCoreApplication.translate("Form", u"Estado de Cuenta", None))
        self.NuevoCliente_bttn.setText(QCoreApplication.translate("Form", u"Nuevo Cliente", None))
        self.ModifiCliente_bttn.setText(QCoreApplication.translate("Form", u"Modificar Cliente", None))
        self.EliminarCliente_bttn.setText(QCoreApplication.translate("Form", u"Eliminar Cliente", None))
        self.ReporteSaldo_bttn.setText(QCoreApplication.translate("Form", u"Reporte de Saldos", None))
        self.centro_titulo_estado.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">ESTADO DE CUENTA</p></body></html>", None))
        self.busqueda_cliente_qline.setPlaceholderText(QCoreApplication.translate("Form", u"Ingresa el nombre de algun cliente...", None))
        ___qtablewidgetitem = self.busqueda_cliente_qtableW.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID", None));
        ___qtablewidgetitem1 = self.busqueda_cliente_qtableW.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"CLIENTE", None));
        self.tabPrincipal.setTabText(self.tabPrincipal.indexOf(self.tab2_clientes), QCoreApplication.translate("Form", u"Clientes", None))
        self.titulo_productos.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>ADMINISTRACION DE PRODUCTOS</p></body></html>", None))
        self.nuevoProducto_Label.setText(QCoreApplication.translate("Form", u"Nuevo Producto", None))
        self.codigoPrcto_label.setText(QCoreApplication.translate("Form", u"C\u00f3digo", None))
        self.codigoPrcto_lineE.setInputMask(QCoreApplication.translate("Form", u"9999999999999999999999", None))
        self.nombrePrcto_label.setText(QCoreApplication.translate("Form", u"Nombre del Producto", None))
        self.cantidadPrcto_label.setText(QCoreApplication.translate("Form", u"Cantidad", None))
        self.cantidadCritPrcto_label.setText(QCoreApplication.translate("Form", u"Cantidad Crit.", None))
        self.cantidadProcto_lineE.setInputMask(QCoreApplication.translate("Form", u"999999999999", None))
        self.cantidadCritPrcto_lineE.setInputMask(QCoreApplication.translate("Form", u"999", None))
        self.precioCompraPrcto_label.setText(QCoreApplication.translate("Form", u"Precio de Compra", None))
        self.precioVentaPrcto_label.setText(QCoreApplication.translate("Form", u"Precio de Venta", None))
        self.precioCompraPrcto_lineE.setInputMask(QCoreApplication.translate("Form", u"9999999999999", None))
        self.precioVentaPrcto_lineE.setInputMask(QCoreApplication.translate("Form", u"9999999999999", None))
        self.descuentoPrcto_label.setText(QCoreApplication.translate("Form", u"Descuento", None))
        self.descuentoPrcto_lineE.setInputMask(QCoreApplication.translate("Form", u"99", None))
        self.medidaPrcto_label.setText(QCoreApplication.translate("Form", u"Medida", None))
        self.categoriaPrcto_label.setText(QCoreApplication.translate("Form", u"Categoria", None))
        self.GuadarPrcto_btton.setText(QCoreApplication.translate("Form", u" Guardar", None))
        self.LimpiarPrcto_btton.setText(QCoreApplication.translate("Form", u"Limpiar", None))
        ___qtablewidgetitem2 = self.pctosVista_tableW.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"ID", None));
        ___qtablewidgetitem3 = self.pctosVista_tableW.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"NOMBRE", None));
        ___qtablewidgetitem4 = self.pctosVista_tableW.horizontalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"UNIDAD DE MEDIDA", None));
        self.cuerpo_productos_tabsW.setTabText(self.cuerpo_productos_tabsW.indexOf(self.cuerpo_productos_tabPrctos), QCoreApplication.translate("Form", u"Productos", None))
        self.ingresaNombre_label.setText(QCoreApplication.translate("Form", u"Ingresa el Nombre/Codigo y la cantidad de articulos para tu Kit", None))
        self.codigoBarrasPaqt_label.setText(QCoreApplication.translate("Form", u"C\u00f3digo de Barras", None))
        self.codigoBarrasPaqt_lineE.setInputMask(QCoreApplication.translate("Form", u"9999999999999999999999", None))
        self.cantidadPrctoPaqt_label.setText(QCoreApplication.translate("Form", u"Cantidad", None))
        self.cantidadPrctoPaqt_lineE.setInputMask(QCoreApplication.translate("Form", u"999999999", None))
        self.agregarProducPaqt_label.setText(QCoreApplication.translate("Form", u"Agregar", None))
        self.AnadirPrctoPaqt_bttn.setText(QCoreApplication.translate("Form", u" A\u00f1adir Producto", None))
        self.nombrePrctoPaqt_label.setText("")
        ___qtablewidgetitem5 = self.paqtPrctosVista_tableW.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Producto", None));
        ___qtablewidgetitem6 = self.paqtPrctosVista_tableW.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Cantidad", None));
        self.guadarPaqt_btton.setText(QCoreApplication.translate("Form", u" Guardar", None))
        self.limpiarPaqt_btton.setText(QCoreApplication.translate("Form", u"Cancelar", None))
        self.tipPaqt_label.setText(QCoreApplication.translate("Form", u"\u2022 Doble click para eliminar una Articulo", None))
        self.cuerpo_productos_tabsW.setTabText(self.cuerpo_productos_tabsW.indexOf(self.cuerpo_productos_tabPaqt), QCoreApplication.translate("Form", u"Contenido del paquete", None))
        self.nuevaCategoriaDepa_label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">Nueva Categoria - Editar Categoria</p></body></html>", None))
        self.categoriaDepa_label.setText(QCoreApplication.translate("Form", u"Categoria", None))
        self.categoriaDepa_lineE.setText("")
        self.guardarDepa_bttn.setText(QCoreApplication.translate("Form", u" Guardar", None))
        self.limpiarDepa_bttn.setText(QCoreApplication.translate("Form", u" Eliminar", None))
        self.tipDepa_label.setText(QCoreApplication.translate("Form", u"\u2022 Doble click para editar una Categoria", None))
        self.cuerpo_productos_tabsW.setTabText(self.cuerpo_productos_tabsW.indexOf(self.cuerpo_productos_tabDepa), QCoreApplication.translate("Form", u"Categoria - Departamento", None))
        self.tabPrincipal.setTabText(self.tabPrincipal.indexOf(self.tab3_productos), QCoreApplication.translate("Form", u"Productos", None))
        self.titulo_inventario.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>ADMINISTRACION DE INVENTARIO</p></body></html>", None))
        self.agregarInv_bttn.setText(QCoreApplication.translate("Form", u"Agregar a Inv", None))
        self.modificarInv_bttn.setText(QCoreApplication.translate("Form", u"Modificar Inv", None))
        self.productosCritInv_bttn.setText(QCoreApplication.translate("Form", u"Productos Criticos", None))
        self.reporteInv_bttn.setText(QCoreApplication.translate("Form", u"Reporte de Inventario", None))
        self.reporteMoviInv_bttn.setText(QCoreApplication.translate("Form", u"Reporte de Movimientos", None))
        self.subTitulo_inventario.setText(QCoreApplication.translate("Form", u"Reporte de inventario", None))
        self.categariasInv_label.setText(QCoreApplication.translate("Form", u"Categorias:", None))
        self.exportarInv_bttn.setText(QCoreApplication.translate("Form", u"Exportar", None))
        self.imprimirInv_bttn.setText(QCoreApplication.translate("Form", u"IImprimir", None))
        ___qtablewidgetitem7 = self.inventarioView_tableW.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"C\u00d3DIGO DE BARRAS", None));
        ___qtablewidgetitem8 = self.inventarioView_tableW.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"DESCRIPCI\u00d3N DEL PRODUCTO", None));
        ___qtablewidgetitem9 = self.inventarioView_tableW.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"PRECIO COMPRA", None));
        ___qtablewidgetitem10 = self.inventarioView_tableW.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"PRECIO VENTA", None));
        ___qtablewidgetitem11 = self.inventarioView_tableW.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Form", u"DESCUENTO", None));
        ___qtablewidgetitem12 = self.inventarioView_tableW.horizontalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Form", u"CANTIDAD", None));
        ___qtablewidgetitem13 = self.inventarioView_tableW.horizontalHeaderItem(6)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Form", u"CANTIDAD CRITICA", None));
        ___qtablewidgetitem14 = self.inventarioView_tableW.horizontalHeaderItem(7)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Form", u"CATEGORIA", None));
        self.costoInv_label.setText(QCoreApplication.translate("Form", u"Costo de Inventario", None))
        self.costoInv_lineE.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">0.00 Bs | 0.00 $</p></body></html>", None))
        self.cantidadPrctosInv_label.setText(QCoreApplication.translate("Form", u"Cantidad de Productos en Inventario", None))
        self.cantidadPrctosInv_lineE.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">0</p></body></html>", None))
        self.tabPrincipal.setTabText(self.tabPrincipal.indexOf(self.tab4_inventario), QCoreApplication.translate("Form", u"Inventario", None))
        self.comprasComprs_label.setText(QCoreApplication.translate("Form", u"COMPRAS", None))
        self.comprasBusquedaComprs_bttn.setText("")
        self.cantidadPrctosComprs_label.setText(QCoreApplication.translate("Form", u"Cantidad", None))
        self.codPrctoComprs_lineE.setInputMask(QCoreApplication.translate("Form", u"9999999999999999999999", None))
        self.PrecioCompraComprs_lineE.setInputMask(QCoreApplication.translate("Form", u"9999999999999", None))
        self.cantidadPrctosComprs_lineE.setInputMask(QCoreApplication.translate("Form", u"999999999999", None))
        self.PrecioCompraComprs_label.setText(QCoreApplication.translate("Form", u"Precio de Compra", None))
        self.proveedorComprs_label.setText(QCoreApplication.translate("Form", u"Proveedor", None))
        self.label_60.setText(QCoreApplication.translate("Form", u"En Existencia:", None))
        self.label_61.setText(QCoreApplication.translate("Form", u"0", None))
        self.codPrctoComprs_label.setText(QCoreApplication.translate("Form", u"Cod. Producto", None))
        self.PrctoComprs_label.setText(QCoreApplication.translate("Form", u"Producto:", None))
        self.PrecioVentaComprs_label.setText(QCoreApplication.translate("Form", u"Precio de Venta", None))
        self.PrecioVentaComprs_lineE.setInputMask(QCoreApplication.translate("Form", u"9999999999999", None))
        self.AnadirPrctpComprs_bttn.setText(QCoreApplication.translate("Form", u" A\u00f1adir Producto", None))
        self.PrctoComprs_lineE.setText("")
        ___qtablewidgetitem15 = self.ComprsViews_tableW.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Form", u"CODIGO", None));
        ___qtablewidgetitem16 = self.ComprsViews_tableW.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Form", u"NOMBRE", None));
        ___qtablewidgetitem17 = self.ComprsViews_tableW.horizontalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Form", u"CANTIDAD", None));
        ___qtablewidgetitem18 = self.ComprsViews_tableW.horizontalHeaderItem(3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Form", u"PRECIO COMPRA", None));
        ___qtablewidgetitem19 = self.ComprsViews_tableW.horizontalHeaderItem(4)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Form", u"SUBTOTAL", None));
        ___qtablewidgetitem20 = self.ComprsViews_tableW.horizontalHeaderItem(5)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("Form", u"UNIDAD DE MEDIDA", None));
        self.guardarComprs_bttn.setText(QCoreApplication.translate("Form", u" Guardar", None))
        self.limparComprs_bttn.setText(QCoreApplication.translate("Form", u" Limpiar", None))
        self.tabPrincipal.setTabText(self.tabPrincipal.indexOf(self.tab5_compras), QCoreApplication.translate("Form", u"Compras", None))
        self.titulo_proveedores.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>ADMINISTRACION DE PROVEEDORES</p></body></html>", None))
        self.telefonoProvee_LineE.setInputMask(QCoreApplication.translate("Form", u"(9999) 999-99999", None))
        self.proveedorProvee_label.setText(QCoreApplication.translate("Form", u"Proveedor", None))
        self.guardarProvee_bttn.setText(QCoreApplication.translate("Form", u" Limpiar", None))
        self.direccionProvee_label.setText(QCoreApplication.translate("Form", u"Direcci\u00f3n", None))
        self.correoEProvee_label.setText(QCoreApplication.translate("Form", u"Correo Electronico", None))
        self.direccionProvee_lineE.setInputMask("")
        self.telefonoProvee_label.setText(QCoreApplication.translate("Form", u"Telefono", None))
        self.limpiarProvee_bttn.setText(QCoreApplication.translate("Form", u" Guardar", None))
        self.tipoDocProvee_label.setText(QCoreApplication.translate("Form", u"Tipo de Documento", None))
        self.numDocProvee_label.setText(QCoreApplication.translate("Form", u"Num. Documento", None))
        self.tipoDocProvee_comboB.setItemText(0, QCoreApplication.translate("Form", u"C\u00e9dula", None))
        self.tipoDocProvee_comboB.setItemText(1, QCoreApplication.translate("Form", u"NIT", None))
        self.tipoDocProvee_comboB.setItemText(2, QCoreApplication.translate("Form", u"Otro", None))

        self.paginaProvee_lineE.setText("")
        self.paginaProvee_label.setText(QCoreApplication.translate("Form", u"Pagina Web / Opcional", None))
        self.buscarProvee_label.setText(QCoreApplication.translate("Form", u"Buscar Proveedor", None))
        self.buscarProvee_bttn.setText("")
        ___qtablewidgetitem21 = self.ProveedorView_tableW.horizontalHeaderItem(0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("Form", u"DOCUMENTO", None));
        ___qtablewidgetitem22 = self.ProveedorView_tableW.horizontalHeaderItem(1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("Form", u"TIPO", None));
        ___qtablewidgetitem23 = self.ProveedorView_tableW.horizontalHeaderItem(2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("Form", u"PROVEEDOR", None));
        ___qtablewidgetitem24 = self.ProveedorView_tableW.horizontalHeaderItem(3)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("Form", u"TELEFONO", None));
        ___qtablewidgetitem25 = self.ProveedorView_tableW.horizontalHeaderItem(4)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("Form", u"DIRECCI\u00d3N", None));
        self.tabPrincipal.setTabText(self.tabPrincipal.indexOf(self.tab6_proveedores), QCoreApplication.translate("Form", u"Proveedores", None))
        self.tabPrincipal.setTabText(self.tabPrincipal.indexOf(self.tab7_corte), QCoreApplication.translate("Form", u"Corte", None))
        self.tabPrincipal.setTabText(self.tabPrincipal.indexOf(self.tab8_configuracion), QCoreApplication.translate("Form", u"Configuraci\u00f3n", None))
    # retranslateUi

