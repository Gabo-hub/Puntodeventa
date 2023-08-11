from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import QLineEdit, QWidget
from views.Login import Ui_Form


class LoginWindows(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.setWindowFlag(Qt.FramelessWindowHint)

        #====================== Botones =========================#
        self.btn_contrasenaver.clicked.connect(self.mostrarContra)
        self.btn_Entrar.clicked.connect(self.entrar)
    
    #========================== Funciones =======================# 
    
    def mostrarContra(self): 
        if self.btn_contrasenaver.isChecked(): 
            self.line_contrasena.setEchoMode(QLineEdit.Normal)
        else: 
            self.line_contrasena.setEchoMode(QLineEdit.Password)
        
    def entrar(self):         
        from controllers.principal_window import PrincipalWindow
        self.windows = PrincipalWindow()
        self.windows.show()
        self.hide() 