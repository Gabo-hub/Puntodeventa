import sys

from db.connect import *
from PySide6.QtCore import *
from PySide6.QtCore import Qt
from PySide6.QtGui import *
from PySide6.QtWidgets import QWidget, QCompleter
from views.Principal_Window import Ui_Form

from controllers.caja_mensaje import *
from controllers.CatDepa.departamentos import Departamento
from controllers.CatProduc.productos import Producto
from controllers.CatInventory.inventario import Inventario


class PrincipalWindow(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.showMaximized()
        self.conector = conectarse()
        self.cuerpo_productos_tabPaqt.setEnabled(False)
        self.cuerpo_productos_tabPaqt.setHidden(True)
        self.info_articulo = []
        self.paqueteProduct = []
        self.paquete = 0
        self.orden_ascendente = True
        
        xCargarArt = "SELECT idproduc, nombreproduc FROM productos"
        cargarArt = consultar_db(self.conector, xCargarArt)
        
        xCargarMedid = "SELECT idmedida, medida FROM public.medida;"
        cargarMedid = consultar_db(self. conector, xCargarMedid)
        
#============== Limpiar inputMask
        for self.line_edit in [self.codigoPrcto_lineE, self.cantidadProcto_lineE, 
                          self.cantidadCritPrcto_lineE, self.precioCompraPrcto_lineE, 
                          self.precioVentaPrcto_lineE, self.descuentoPrcto_lineE, 
                          self.codigoBarrasPaqt_lineE, self.cantidadPrctoPaqt_lineE,
                          self.codPrctoComprs_lineE, self.cantidadPrctosComprs_lineE,
                          self.PrecioCompraComprs_lineE, self.PrecioVentaComprs_lineE,
                          self.telefonoProvee_LineE]:
            self.line_edit.mousePressEvent = self.lineedit_clicked
#============= for cargas de informacion      
        for medid in range(0, len(cargarMedid)):
            self.medidaPrcto_comboB.addItem("")
            self.medidaPrcto_comboB.setItemText(medid, QCoreApplication.translate("Form", str(cargarMedid[medid][1]), None))

        for i in cargarArt:
            for x in i:
                self.info_articulo.append(str(x))
                
#============== Botones
        self.GuadarPrcto_btton.clicked.connect(self.guardarPrcto)
        self.guardarDepa_bttn.clicked.connect(self.guardar_Categoria)
        self.depaVista_listW.itemDoubleClicked.connect(self.edicion_Categoria)
        self.limpiarDepa_bttn.clicked.connect(self.cancelar_Edicion)
        self.codigoBarrasPaqt_lineE.textChanged.connect(self.panel_busqueda)
        self.limpiarPaqt_btton.clicked.connect(self.cancelar_paquete)
        self.guadarPaqt_btton.clicked.connect(self.guardar_paquetes)
        self.AnadirPrctoPaqt_bttn.clicked.connect(self.añadirPrct_paquetes)
        self.paqtPrctosVista_tableW.cellDoubleClicked.connect(self.eliminarPpaquete)
        self.categoriasInv_comboB.currentIndexChanged.connect(self.activarFiltro)
        self.agregarInv_bttn.clicked.connect(self.agregarInv)
        
#============== Variables        
        
        self.icon11 = QIcon()
        self.icon11.addFile(u":/blupack/bl-product.png", QSize(), QIcon.Normal, QIcon.Off)
        self.icon30 = QIcon()
        self.icon30.addFile(u":/blupack/bl-folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeEvent = self.on_close  
        
        #============== Cargar Info            
        Departamento.cargarDepar(self)        
        Producto.cargarArtc(self)
        Inventario.cargarInv(self)
        
#============== Funciones
#======================== Tab Productos

    def guardarPrcto(self):
        if self.medidaPrcto_comboB.currentIndex() != 2:
            Producto.guardarPrcto(self)
        else:
            Producto.activarPaqueteProducto(self)
        
#====================================== Tab Producto Departamentos    
    def edicion_Categoria(self, item):
        Departamento.activarEdit(self, item)
        
    def guardar_Categoria(self):
        if self.guardarDepa_bttn.text() == " Actualizar" and len(self.categoriaDepa_lineE.text()) == 0:
            return MensajeCaja(self,"ERROR INFORMACION INCOMPLETA","POR FAVOR, AÑADA UN NOMBRE PARA EDITAR EL DEPARTAMENTO / CATEGORIA",3)
        if len(self.categoriaDepa_lineE.text()) == 0:
                return MensajeCaja(self,"ERROR INFORMACION INCOMPLETA","POR FAVOR, AÑADA UN NOMBRE PARA EL DEPARTAMENTO / CATEGORIA",3)
        Departamento.guardarDepar(self)
    
    def cancelar_Edicion(self):
        Departamento.cancelarEliminar(self)

#====================================== Tab Producto Paquetes
    def panel_busqueda(self): # Panel de busqueda, Autoo completado
        self.completer = QCompleter(self.info_articulo);
        self.completer.setCaseSensitivity(Qt.CaseInsensitive);
        self.codigoBarrasPaqt_lineE.setCompleter(self.completer);
        
        if len(self.codigoBarrasPaqt_lineE.text()) != 0:
            xVerificarDepa = f"""SELECT EXISTS (SELECT nombreproduc FROM public.productos WHERE idproduc='{self.codigoBarrasPaqt_lineE.text()}')"""
            verificarDepa = consultar_db(self.conector, xVerificarDepa)
            
            if verificarDepa[0][0] == True:
                articulo = f"SELECT nombreproduc FROM public.productos WHERE idproduc = '{self.codigoBarrasPaqt_lineE.text()}';"
                acticulobuscado = consultar_db(self.conector, articulo)
            
                if acticulobuscado == "":
                    self.nombrePrctoPaqt_label.setText("Articulo No Encontrado!")
                else:
                    self.nombrePrctoPaqt_label.setText(acticulobuscado[0][0])
    
    def cancelar_paquete(self):
        Producto.cancelar_Pac(self)
        
    def añadirPrct_paquetes(self):
        Producto.añadirPrct_paquete(self)
        
    def guardar_paquetes(self):
        Producto.guardar_paquete(self)
    
    def eliminarPpaquete(self, index):
        confirmar = MensajeCaja(self,"ELIMINAR", f"SEGURO QUE QUIERES ELIMINAR EL ARTICULO?",2)
        if confirmar == 1:
            self.paqtPrctosVista_tableW.removeRow(index)
            self.paqueteProduct
        else:
            return
        
#======================== Tab Inventarios  
    def activarFiltro(self):
        Inventario.filtro_tabla(self)
        
    def agregarInv(self):
        Inventario.agregar_inventario(self)
    
#======================== Limpiar inputMask
    def lineedit_clicked(self, event):
        for self.line_edit in [self.codigoPrcto_lineE, self.cantidadProcto_lineE, 
                          self.cantidadCritPrcto_lineE, self.precioCompraPrcto_lineE, 
                          self.precioVentaPrcto_lineE, self.descuentoPrcto_lineE, 
                          self.codigoBarrasPaqt_lineE, self.cantidadPrctoPaqt_lineE,
                          self.codPrctoComprs_lineE, self.cantidadPrctosComprs_lineE,
                          self.PrecioCompraComprs_lineE, self.PrecioVentaComprs_lineE,
                          self.telefonoProvee_LineE]:
            if self.line_edit.text() == "":
                self.line_edit.clear()
                
#======================== Cerrar Programa
    def on_close(self, event):
        # Código a ejecutar cuando se cierre la ventana
        event.accept()  # Para aceptar el cierre de la ventana
        sys.exit()
