from views.Principal_Window import Ui_Form
from PySide6.QtWidgets import QTableWidgetItem, QHeaderView, QDialog
from PySide6 import QtWidgets
from PySide6.QtGui import *
from PySide6.QtCore import *
from db.connect import *
from controllers.caja_mensaje import *

class Inventario(Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        
#====================================== Cargar Inventario
    def cargarInv(self):
        header = self.inventarioView_tableW.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        
        precios = 0
        items = 0
        categoria_inv = False
        cargarInvCadena = "SELECT idproduc, nombreproduc, preciocproduc, preciovproduc, descuentoproduc, cantidadproduc, cantidadcritproduc, (SELECT categoria FROM categoria WHERE idcategoria = categoriaproduc) FROM public.productos ORDER BY idproduc ASC;"
        xCargarInvCadena = consultar_db(self.conector, cargarInvCadena)
                
        for f in range(0, len(xCargarInvCadena)):
            items += 1
            precios = precios + xCargarInvCadena[f][2]
            self.inventarioView_tableW.setRowCount(f + 1)
            self.inventarioView_tableW.setItem(f,0,QTableWidgetItem(str(xCargarInvCadena[f][0])))
            self.inventarioView_tableW.setItem(f,1,QTableWidgetItem(str(xCargarInvCadena[f][1])))
            self.inventarioView_tableW.setItem(f,2,QTableWidgetItem(str(xCargarInvCadena[f][2])+" Bs."))
            self.inventarioView_tableW.setItem(f,3,QTableWidgetItem(str(xCargarInvCadena[f][3])+" Bs."))
            self.inventarioView_tableW.setItem(f,4,QTableWidgetItem(str(xCargarInvCadena[f][4])))
            self.inventarioView_tableW.setItem(f,5,QTableWidgetItem(str(xCargarInvCadena[f][5])))
            self.inventarioView_tableW.setItem(f,6,QTableWidgetItem(str(xCargarInvCadena[f][6])))
            if xCargarInvCadena[f][7] is None and categoria_inv is False:
                categoria_inv = True
                MensajeCaja(self,"INVENTARIO", f"ALGUNOS ARTICULOS NO TIENEN CATEGORIA, \nTE RECOMENDAMOS ACTUALIZARLOS / ELIMINARLOS",3)
            self.inventarioView_tableW.setItem(f,7,QTableWidgetItem(str(xCargarInvCadena[f][7])))
            
        self.cantidadPrctosInv_lineE.setText(str(items))
        self.costoInv_lineE.setText("{:.2f} Bs | {:.2f} $".format(precios, precios / 24.5))
        self.inventarioView_tableW.horizontalHeader().sectionClicked.connect(
    lambda logicalIndex: Inventario.ordenar_tabla(self, logicalIndex))

#======================================= Ordenar tabla ======================   
    def ordenar_tabla(self, logicalIndex):
        header = self.inventarioView_tableW.horizontalHeader()
        header.setSortIndicator(logicalIndex, QtCore.Qt.AscendingOrder if self.orden_ascendente else QtCore.Qt.DescendingOrder)
        self.inventarioView_tableW.sortItems(logicalIndex, QtCore.Qt.AscendingOrder if self.orden_ascendente else QtCore.Qt.DescendingOrder)
        self.orden_ascendente = not self.orden_ascendente

#====================================== Filtrar inv ========================    
    def filtro_tabla(self):
        categoria = self.categoriasInv_comboB.currentText()
        if categoria == "Por Defecto":
            for i in range(self.inventarioView_tableW.rowCount()):
                self.inventarioView_tableW.showRow(i)
        else:
            for fila in range(self.inventarioView_tableW.rowCount()):
                categoria_item = self.inventarioView_tableW.item(fila, 7)
                if categoria_item.text() == categoria:
                    self.inventarioView_tableW.setRowHidden(fila, False)
                else:
                    self.inventarioView_tableW.setRowHidden(fila, True)

#===================================== Agregar inv =========================
    def agregar_inventario(self):
        from controllers.CatInventory.agregarinv_window import AgregarInv
        dialog = AgregarInv()
        result = dialog.exec_()
          
        
        if result == QDialog.Accepted:
            texto = dialog.get_text()
            if int(texto[1]) > 0:
                consulta = f"SELECT cantidadproduc FROM public.productos WHERE idproduc = {int(texto[0])};"
                cantidadAct = consultar_db(self.conector, consulta)
                cadena = f"UPDATE public.productos SET cantidadproduc={ int(texto[1])+int(cantidadAct[0][0]) } WHERE idproduc = {int(texto[0])};"
                guardar_registro(self.conector, cadena)
                self.conector.connection.commit()
                Inventario.cargarInv(self)
            else:
                MensajeCaja(self,"ERROR DE INFORMACION","POR FAVOR, RELLENE LOS CAMPOS CON NUMEROS EN POSITIVO",3)
        else:
            print("El usuario presionó el botón de cancelar.")
