from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout
from views.AgregarInv_Dialog import Ui_Dialog
from db.connect import *

class AgregarInv(QDialog, Ui_Dialog):
    
    alFinal = Signal(int)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.mousedown=None
        self.mouseup=None
        
        self.conector = conectarse()
        
        self.cantidadProducInfo_label.textChanged.connect(self.busquedaArt)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.buttonBox.button(QDialogButtonBox.Save).setText("Guardar")
        self.buttonBox.button(QDialogButtonBox.Cancel).setText("Cancelar")
        
    #======================== BUSQUEDAS ======================================#
    def busquedaArt(self, data):
        if data and data.strip():
            consulta = f"SELECT nombreproduc, cantidadproduc FROM public.productos WHERE idproduc = {data};"
            resultado = consultar_db(self.conector, consulta)

            if resultado:
                self.descAgregarInfo_label.setText(resultado[0][0])
                self.cantActAgregar_label.setText(str(resultado[0][1]))
            else:
                self.descAgregarInfo_label.setText(" ")
                self.cantActAgregar_label.setText(" ")
        else:
            self.descAgregarInfo_label.setText(" ")
            self.cantActAgregar_label.setText(" ")
    
    def get_text(self):
        return [self.cantidadProducInfo_label.text(), self.cantidadAgregarInfo_label.text()]
    #======================== Mover Ventana sin bordes =======================#
    def mouseReleaseEvent(self,event):
        self.mouseup=True
        self.mousedown=False

    def mousePressEvent(self, event):
        #self.offset = event.pos()
        self.offset = event.pos()
        self.mouseup=False
        self.mousedown=True

    def mouseMoveEvent(self, event):
        if self.mousedown is True:
            x=event.globalX()
            y=event.globalY()
            x_w = self.offset.x()
            y_w = self.offset.y()
            self.move(x-x_w, y-y_w)
