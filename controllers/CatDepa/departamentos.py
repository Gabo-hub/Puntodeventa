from views.Principal_Window import Ui_Form
from PySide6.QtWidgets import QListWidgetItem
from PySide6.QtGui import *
from PySide6.QtCore import *
from db.connect import *
from controllers.caja_mensaje import *

class Departamento(Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.categoriaEditar = ""
        self.conector = conectarse()

    # Activar Edicion 
    def activarEdit(self, item):
        xVerificarDepa = f"""SELECT EXISTS (SELECT categoria FROM public.categoria WHERE categoria='{item.text()}')"""
        verificarDepa = consultar_db(self.conector, xVerificarDepa)
        
        # Verificacion antes de Cambiar los Botones para la Act
        if verificarDepa[0][0] == True:
            self.categoriaDepa_lineE.setText(item.text())
            self.categoriaEditar = item.text()
            self.guardarDepa_bttn.setText(" Actualizar")
            self.guardarDepa_bttn.setStyleSheet(u"""QPushButton {background-color: rgb(76, 172, 231);} QPushButton:hover {background-color: rgb(84, 187, 255);} QPushButton:pressed {background-color: rgb(76, 172, 231);}""")
            self.limpiarDepa_bttn.setText(" Cancelar")
            self.limpiarDepa_bttn.setStyleSheet(u"QPushButton {background-color: rgb(208, 142, 60);} QPushButton:hover {background-color: rgb(227, 154, 66);} QPushButton:pressed {background-color: rgb(208, 142, 60);}")
        
        else: MensajeCaja(self,"ERROR", f"OCURRIO UN ERROR, VUELVA A INTENTARLO",3)
        
        print("consulta: "+str(verificarDepa[0][0]))
            
    def guardarDepar(self):
        #============ Guardar Actualizacion de Informacion  
        if self.guardarDepa_bttn.text() == " Actualizar":
            
                categoria = f"SELECT idcategoria FROM public.categoria WHERE categoria = '{self.categoriaEditar}';"
                idcategoria = consultar_db(self.conector, categoria)
                confirmar = MensajeCaja(self,"ACTUALIZACION", f"SEGURO QUE QUIERES ACTUALIZAR LA CATEGORIA {self.categoriaEditar} A {self.categoriaDepa_lineE.text()}?",2)

                #============ Si la busqueda de la actualizacion es buena, Actualiza, Guarda y cambia los Botones
                if confirmar == 1:
                    xActualizar = f"""UPDATE public.categoria SET categoria='{self.categoriaDepa_lineE.text()}' WHERE idcategoria = {idcategoria[0][0]};"""
                    actualizar_db(self.conector, xActualizar)
                    self.conector.connection.commit()
                    MensajeCaja(self,"ACTUALIZAR ", f"LA CATEGORIA HA SIDO ACTUALIZADA CORRECTAMENTE!",1)
                    self.categoriaDepa_lineE.clear()
                    self.guardarDepa_bttn.setText(" Guardar")
                    self.guardarDepa_bttn.setStyleSheet(u"QPushButton {background-color: rgb(80, 195, 144);} QPushButton:hover {background-color: rgb(91, 221, 163);} QPushButton:pressed {background-color: rgb(80, 195, 144);}")
                    self.limpiarDepa_bttn.setText(" Limpiar")
                    self.limpiarPaqt_btton.setStyleSheet(u"QPushButton {background-color: rgb(195, 80, 85);} QPushButton:hover {background-color: rgb(213, 88, 94);} QPushButton:pressed {background-color: rgb(195, 80, 85);}")
                    Departamento.cargarDepar(self)
                    self.lineedit_clicked()
                else:
                    return
                
        #============ Guardar Nueva Categoria      
        elif self.guardarDepa_bttn.text() == " Guardar":
            
            confirmar = MensajeCaja(self,"ACTUALIZACION", f"SEGURO QUE QUIERES GUARDAR LA CATEGORIA {self.categoriaDepa_lineE.text()}?",2)
            xVerificarDepa = f"""SELECT EXISTS (SELECT categoria FROM public.categoria WHERE categoria='{self.categoriaDepa_lineE.text()}')"""
            verificarDepa = consultar_db(self.conector, xVerificarDepa)
            
            #============ Verificacion para que no haya Categorias Duplicadas
            if verificarDepa[0][0] == True: return MensajeCaja(self,"ERROR", f"NO PUEDES GUARDAR DOS ARTICULOS CON EL MISMO NOMBRE",3)
            
            #============ Ingresa Informacion
            if confirmar == 1:
                cadena = f"INSERT INTO public.categoria(categoria) VALUES ('{self.categoriaDepa_lineE.text()}');"
                guardar_registro(self.conector, cadena)
                self.conector.connection.commit()
                MensajeCaja(self,"GUARDAR", f"LA CATEGORIA HA SIDO GUARDADA CORRECTAMENTE!",1)
                Departamento.cargarDepar(self)
            else:
                return
    
    def cargarDepar(self):
        icon13 = QIcon()
        icon13.addFile(u":/blupack/bl-folder.png", QSize(), QIcon.Normal, QIcon.Off)
        xCargarDepa = f"""SELECT idcategoria, categoria FROM public.categoria ORDER BY idcategoria;"""
        cargarDepa = consultar_db(self. conector, xCargarDepa)
        self.depaVista_listW.clear()
        __sortingEnabled = self.depaVista_listW.isSortingEnabled()
        self.depaVista_listW.setSortingEnabled(False)
        font13 = QFont()
        font13.setFamilies([u"Poppins"])
        font13.setPointSize(9)
        self.categoriaPrcto_label.setFont(font13)
        self.categoriaPrcto_comboB.clear()
        self.depaVista_listW.setSortingEnabled(__sortingEnabled)
        
        if cargarDepa is not None:
            #============ Cargar en List Widget los departamentos
            for cat in range(0,len(cargarDepa)):
                __qlistwidgetitem = QListWidgetItem(self.depaVista_listW)
                __qlistwidgetitem.setIcon(icon13);
                ___qlistwidgetitem = self.depaVista_listW.item(cat)
                ___qlistwidgetitem.setText(QCoreApplication.translate("Form", f"{cargarDepa[cat][1]}", None));
            
            self.categoriasInv_comboB.addItem("")
            self.categoriasInv_comboB.setItemText(0, QCoreApplication.translate("Form", "Por Defecto", None))
            
            #=========== Cargar en Combo Box de Productos
            for pro in range(0, len(cargarDepa)):
                self.categoriaPrcto_comboB.addItem("")
                self.categoriaPrcto_comboB.setItemText(pro, QCoreApplication.translate("Form", str(cargarDepa[pro][1]), None))
                self.categoriasInv_comboB.addItem("")
                self.categoriasInv_comboB.setItemText(pro+1, QCoreApplication.translate("Form", str(cargarDepa[pro][1]), None))
            print(cargarDepa)
    
    def cancelarEliminar(self):
        if self.limpiarDepa_bttn.text() == " Cancelar":
            
            self.categoriaDepa_lineE.clear()
            self.guardarDepa_bttn.setText(" Guardar")
            self.guardarDepa_bttn.setStyleSheet(u"QPushButton {background-color: rgb(80, 195, 144);} QPushButton:hover {background-color: rgb(91, 221, 163);} QPushButton:pressed {background-color: rgb(80, 195, 144);}")
            self.limpiarDepa_bttn.setText(" Eliminar")
            self.limpiarDepa_bttn.setStyleSheet(u"QPushButton {background-color: rgb(195, 80, 85);} QPushButton:hover {background-color: rgb(213, 88, 94);} QPushButton:pressed {background-color: rgb(195, 80, 85);}")
        
        elif self.limpiarDepa_bttn.text() == " Eliminar" and len(self.categoriaDepa_lineE.text()) != 0:
            
            xVerificarDepa = f"""SELECT EXISTS (SELECT categoria FROM public.categoria WHERE categoria='{self.categoriaDepa_lineE.text()}')"""
            verificarDepa = consultar_db(self.conector, xVerificarDepa)
            
            if verificarDepa[0][0] == True:                 
                confirmar = MensajeCaja(self,"ELIMINAR", f"SEGURO QUE QUIERES ELIMINAR LA CATEGORIA {self.categoriaDepa_lineE.text()}?",2)
                
                if confirmar == 1:              
                    xElimiarDepa = f"""DELETE FROM public.categoria WHERE idcategoria = (SELECT idcategoria FROM public.categoria WHERE categoria = '{self.categoriaDepa_lineE.text()}');"""
                    actualizar_db(self.conector, xElimiarDepa)
                    self.conector.connection.commit()
                    
                    confirmar = MensajeCaja(self,"ELIMINAR", f"LA CATEGORIA HA SIDO ELIMINADA CORRECTAMENTE!",1)
                    Departamento.cargarDepar(self)                   
                else: 
                    return
            else:
                confirmar = MensajeCaja(self,"ELIMINAR", f"LA CATEGORIA {self.categoriaDepa_lineE.text()} NO HA SIDO ENCONTRADA VUELVA A INTENTARLO",3)
            return
        