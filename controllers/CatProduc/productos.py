from views.Principal_Window import Ui_Form
from PySide6.QtWidgets import QTableWidgetItem
from PySide6 import QtWidgets
from PySide6.QtGui import *
from PySide6.QtCore import *
from db.connect import *
from controllers.caja_mensaje import *
from controllers.CatInventory.inventario import Inventario

class Producto(Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.cuerpo_productos_tabPaqt.setProperty("opacity", 1.0)
        self.validar = 0 
#====================================== Productos
    def cargarArtc(self):
        xCargarArtc = "SELECT idproduc, nombreproduc, (SELECT medida FROM public.medida WHERE medida.idmedida = medidaproduc) FROM public.productos ORDER BY idproduc ASC LIMIT 10;"
        cargarArtc = consultar_db(self.conector, xCargarArtc)
        
        if cargarArtc is not None:
            for i, fila in enumerate(cargarArtc):
                for j, columna in enumerate(fila):
                    self.pctosVista_tableW.setRowCount(i + 1)
                    self.pctosVista_tableW.setItem(i, j, QTableWidgetItem(str(columna)))
                    
    def guardarPrcto(self):
        
        TextoInfo = [self.codigoPrcto_lineE, self.nombrePrcto_lineE, 
                          self.cantidadProcto_lineE, self.cantidadCritPrcto_lineE, 
                          self.precioCompraPrcto_lineE, self.precioVentaPrcto_lineE,
                          self.descuentoPrcto_lineE]
        NumerosInfo = [self.codigoPrcto_lineE, self.cantidadProcto_lineE, 
                       self.cantidadCritPrcto_lineE, self.precioCompraPrcto_lineE, 
                       self.precioVentaPrcto_lineE, self.descuentoPrcto_lineE]
        ComboInfo = [self.medidaPrcto_comboB, self.categoriaPrcto_comboB]
            
        for a in TextoInfo:
            if len(a.text()) == 0:
                return MensajeCaja(self,"ERROR INFORMACION INCOMPLETA","POR FAVOR, RELLENE LOS CAMPOS VACIOS",3)
        for b in NumerosInfo:
            if int(b) < 0:
                return MensajeCaja(self,"ERROR DE INFORMACION","POR FAVOR, RELLENE LOS CAMPOS CON NUMEROS EN POSITIVO",3)
        for c in ComboInfo:
            if c.currentIndex() == -1:
                return MensajeCaja(self,"CATEGORIAS / DEPARTAMENTOS","POR FAVOR, INGRESA UNA CATEGORIA PARA EL PRODUCTO O CREA UNA.",1)
        
        xVerificarArt = f"""SELECT EXISTS (SELECT nombreproduc FROM public.productos WHERE nombreproduc='{self.nombrePrcto_lineE.text()}')"""
        verificarArt = consultar_db(self.conector, xVerificarArt)
        
        xVerificarArt2 = f"""SELECT EXISTS (SELECT idproduc FROM public.productos WHERE idproduc='{self.codigoPrcto_lineE.text()}')"""
        verificarArt2 = consultar_db(self.conector, xVerificarArt2)  
        
        #============ Verificacion para que no haya Categorias Duplicadas
        if verificarArt[0][0] == True or verificarArt2[0][0] == True: return MensajeCaja(self,"ERROR", f"NO PUEDES GUARDAR DOS PRODUCTOS/CODIGOS IGUALES",3)

        busquedacategoria = f"SELECT idcategoria FROM categoria WHERE categoria.categoria='{self.categoriaPrcto_comboB.currentText()}';"
        categoria = consultar_db(self.conector, busquedacategoria)
        
        cadena = f"""INSERT INTO public.productos(idproduc, nombreproduc, cantidadproduc, cantidadcritproduc, preciocproduc, preciovproduc, descuentoproduc, medidaproduc, kit, categoriaproduc) 
        VALUES ({int(self.codigoPrcto_lineE.text())}, '{self.nombrePrcto_lineE.text()}', 
        {int(self.cantidadProcto_lineE.text())}, {int(self.cantidadCritPrcto_lineE.text())}, 
        {int(self.precioCompraPrcto_lineE.text())}, {int(self.precioVentaPrcto_lineE.text())}, 
        {int(self.descuentoPrcto_lineE.text())}, {int(self.medidaPrcto_comboB.currentIndex())+1}, 
        {int(self.paquete)}, {int(categoria[0][0])});"""

        guardar_registro(self.conector, cadena)
        self.conector.connection.commit()
        MensajeCaja(self,"PRODUCTO", f"EL PRODUCTO HA SIDO AÑADIDO CORRECTAMENTE!",1)
        Producto.cargarArtc(self)
        Inventario.cargarInv(self)
                    
#====================================== Paquetes 
    def activarPaqueteProducto(self):
        self.cuerpo_productos_tabsW.setTabEnabled(1, True)
        tab_2 = self.tabPrincipal.widget(2)
        subtab_2 = self.cuerpo_productos_tabsW.widget(1)
            
        for i in range(self.tabPrincipal.count()):
            if self.tabPrincipal.widget(i) != tab_2:
                self.tabPrincipal.setTabEnabled(i, False)
            
        for i in range(self.cuerpo_productos_tabsW.count()):
            if self.cuerpo_productos_tabsW.widget(i) != subtab_2:
                self.cuerpo_productos_tabsW.setTabEnabled(i, False)
        
        MensajeCaja(self,"PAQUETE / KIT","POR FAVOR, AGREGUE UNO POR UNO LOS ARTICULOS QUE VAYA A AGREGAR A EL PAQUETE/KIT",1)
        
        xIDPact = f"""SELECT * FROM paquete ORDER BY idpaquete DESC LIMIT 1;"""
        IDPact = consultar_db(self.conector, xIDPact)
            
        if IDPact is None:
            self.paquete = 1
        else: 
            self.paquete = IDPact[0][0] + 1 
            
    def guardar_paquete(self):
        
        if int(self.cantidadPrctoPaqt_lineEdit.text()) < 0:
            return MensajeCaja(self,"ERROR DE INFORMACION","POR FAVOR, RELLENE LOS CAMPOS CON NUMEROS EN POSITIVO",3)
        for i in self.paqueteProduct:
            xCrearPact = f"INSERT INTO public.paquete(idpaquete, producpaquete, cantidadpaquete) VALUES ({self.paquete}, {i[0]}, {i[1]});"
            guardar_registro(self.conector, xCrearPact)
            print(xCrearPact)
        self.paqueteProduct.clear()
        self.paquete = 0
        Producto.guardarPrcto(self)
        Producto.cancelar_Pac(self)
        
    def añadirPrct_paquete(self):
        xVerificaArtc = f"SELECT nombreproduc FROM public.productos WHERE idproduc = {self.codigoBarrasPaqt_lineE.text()};"
        verificaArtc = consultar_db(self. conector, xVerificaArtc)
        
        if verificaArtc is not None:
            if len(self.cantidadPrctoPaqt_lineE.text()) == 0: return MensajeCaja(self,"ERROR", f"OCURRIO UN ERROR, INGRESE UNA CANTIDAD VALIDA DEL PRODUCTO",3)
            
            if any([int(self.codigoBarrasPaqt_lineE.text()) == sublista[0] for sublista in self.paqueteProduct]) is False:
                self.paqueteProduct.append([int(self.codigoBarrasPaqt_lineE.text()), int(self.cantidadPrctoPaqt_lineE.text())])
                row_count = self.paqtPrctosVista_tableW.rowCount()
                self.paqtPrctosVista_tableW.insertRow(row_count)
                self.paqtPrctosVista_tableW.setItem(row_count, 0, QTableWidgetItem(verificaArtc[0][0]))
                self.paqtPrctosVista_tableW.setItem(row_count, 1, QTableWidgetItem(self.cantidadPrctoPaqt_lineE.text()))
                    
        else: MensajeCaja(self,"ERROR", f"OCURRIO UN ERROR, INGRESE UN CODIGO DE BARRAS CORRECTO",3)
    
    def cancelar_Pac(self):         
        tab_2 = self.tabPrincipal.widget(2)
            
        for i in range(self.tabPrincipal.count()):
            if self.tabPrincipal.widget(i) != tab_2:
                self.tabPrincipal.setTabEnabled(i, True)
            
        self.codigoBarrasPaqt_lineE.clear()
        self.cantidadPrctoPaqt_lineE.clear()
        self.paqtPrctosVista_tableW.clearContents()
        self.paqtPrctosVista_tableW.setRowCount(0)
        self.nombrePrctoPaqt_label.setText("")
        self.paqueteProduct.clear()
        self.paquete = 0
        self.cuerpo_productos_tabsW.setTabEnabled(1, False)
        self.cuerpo_productos_tabsW.setTabEnabled(2, True)
        self.cuerpo_productos_tabsW.setTabEnabled(0, True)
