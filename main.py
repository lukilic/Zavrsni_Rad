import sys
import csv
from PyQt4.QtSql import *
from PyQt4 import QtCore, QtGui
from database_GUI import Ui_Main_GUI_Widget
from kirurg_GUI import Ui_kirurg_Widget
from pacijent_GUI import Ui_pacijent_Widget
from asistira_GUI import Ui_asistira_Widget
from konzultant_GUI import Ui_konzultant_Widget
from nadgleda_GUI import Ui_nadgleda_Widget
from operacija_GUI import Ui_operacija_Widget
from privatni_pacijent_GUI import Ui_privatni_pacijent_Widget
from sala_GUI import Ui_sala_Widget
from sestra_GUI import Ui_sestra_Widget
from soba_GUI import Ui_soba_Widget
from zaduzena_za_salu_GUI import Ui_zaduzena_za_salu_Widget
from zaduzena_za_sobu_GUI import Ui_zaduzena_za_sobu_Widget
from login_GUI import Ui_login_Widget
from delete_GUI import Ui_delete_Widget
from update_GUI import Ui_update_Widget
from search_GUI import Ui_search_Widget
from report_GUI import Ui_report_Widget


class login_GUI(QtGui.QWidget, Ui_login_Widget):
       def __init__(self):
              QtGui.QWidget.__init__(self)
              self.setupUi(self)
              self.login_login_button.clicked.connect(self.open_main_GUI)

       def open_main_GUI(self):
              username = self.login_username_lineEdit.text()
              password = self.login_password_lineEdit.text()
              if username == "user" and password == "pass":
                     self.close()
                     global main_GUI
                     main_GUI = database_GUI()
                     main_GUI.show()
              else:
                     msgBox = QtGui.QMessageBox()
                     msgBox.setWindowTitle("Error")
                     msgBox.setText("Invalid username or password")
                     msgBox.exec_()


class QCustomDelegate (QtGui.QItemDelegate):
    def paint (self, painterQPainter, optionQStyleOptionViewItem, indexQModelIndex):
        column = indexQModelIndex.column()
        if column == 0:
            textQString = '%.0f' % indexQModelIndex.model().data(indexQModelIndex, QtCore.Qt.EditRole)
            self.drawDisplay(painterQPainter, optionQStyleOptionViewItem, optionQStyleOptionViewItem.rect, textQString)
        else:
            QtGui.QItemDelegate.paint(self, painterQPainter, optionQStyleOptionViewItem, indexQModelIndex)

class database_GUI(QtGui.QWidget, Ui_Main_GUI_Widget):
       def __init__(self):
              QtGui.QWidget.__init__(self)
              self.setupUi(self)
              self.View_Data_Button.clicked.connect(self.view_data)
              self.Add_button.clicked.connect(self.open_add_ui)
              self.Delete_button.clicked.connect(self.open_delete_ui)
              self.Update_button.clicked.connect(self.open_update_ui)
              self.Search_button.clicked.connect(self.open_search_ui)
              self.Report_button.clicked.connect(self.open_report_ui)

       def view_data(self):
              if self.Asistira_checkBox.isChecked():
                     asistira_query = QSqlQueryModel()
                     asistira_query.setQuery("SELECT * FROM asistira")
                     global view_asistira
                     view_asistira = QtGui.QTableView()
                     view_asistira.setItemDelegate(QCustomDelegate())
                     view_asistira.setModel(asistira_query)
                     view_asistira.setWindowTitle('asistira')
                     view_asistira.show()
                    
              if self.Kirurg_checkBox.isChecked():
                     Kirurg_query = QSqlQueryModel()
                     Kirurg_query.setQuery("SELECT * FROM kirurg")
                     global view_Kirurg
                     view_Kirurg = QtGui.QTableView()
                     view_Kirurg.setItemDelegate(QCustomDelegate())
                     view_Kirurg.setModel(Kirurg_query)
                     view_Kirurg.setWindowTitle('kirurg')
                     view_Kirurg.show()

              if self.Konzultant_checkBox.isChecked():
                     Konzultant_query = QSqlQueryModel()
                     Konzultant_query.setQuery("SELECT * FROM konzultant")
                     global view_Konzultant
                     view_Konzultant = QtGui.QTableView()
                     view_Konzultant.setItemDelegate(QCustomDelegate())
                     view_Konzultant.setModel(Konzultant_query)
                     view_Konzultant.setWindowTitle('konzultant')
                     view_Konzultant.show()

              if self.Nadgleda_checkBox.isChecked():
                     Nadgleda_query = QSqlQueryModel()
                     Nadgleda_query.setQuery("SELECT * FROM nadgleda")
                     global view_Nadgleda
                     view_Nadgleda = QtGui.QTableView()
                     view_Nadgleda.setItemDelegate(QCustomDelegate())
                     view_Nadgleda.setModel(Nadgleda_query)
                     view_Nadgleda.setWindowTitle('nadgleda')
                     view_Nadgleda.show()

              if self.Operacije_checkBox.isChecked():
                     Operacija_query = QSqlQueryModel()
                     Operacija_query.setQuery("SELECT * FROM operacija")
                     global view_Operacija
                     view_Operacija = QtGui.QTableView()
                     view_Operacija.setItemDelegate(QCustomDelegate())
                     view_Operacija.setModel(Operacija_query)
                     view_Operacija.setWindowTitle('operacija')
                     view_Operacija.show()

              if self.Pacijent_checkBox.isChecked():
                     Pacijent_query = QSqlQueryModel()
                     Pacijent_query.setQuery("SELECT * FROM pacijent")
                     global view_Pacijent
                     view_Pacijent = QtGui.QTableView()
                     view_Pacijent.setItemDelegate(QCustomDelegate())
                     view_Pacijent.setModel(Pacijent_query)
                     view_Pacijent.setWindowTitle('pacijent')
                     view_Pacijent.show()

              if self.Privatni_pacijent_checkBox.isChecked():
                     Privatni_pacijent_query = QSqlQueryModel()
                     Privatni_pacijent_query.setQuery("SELECT * FROM privatni_pacijent")
                     global view_Privatni_pacijent
                     view_Privatni_pacijent = QtGui.QTableView()
                     view_Privatni_pacijent.setItemDelegate(QCustomDelegate())
                     view_Privatni_pacijent.setModel(Privatni_pacijent_query)
                     view_Privatni_pacijent.setWindowTitle('privatni_pacijent')
                     view_Privatni_pacijent.show()

              if self.Sala_checkBox.isChecked():
                     Sala_query = QSqlQueryModel()
                     Sala_query.setQuery("SELECT * FROM sala")
                     global view_Sala
                     view_Sala = QtGui.QTableView()
                     view_Sala.setModel(Sala_query)
                     view_Sala.setWindowTitle('sala')
                     view_Sala.show()

              if self.Sestra_checkBox.isChecked():
                     Sestra_query = QSqlQueryModel()
                     Sestra_query.setQuery("SELECT * FROM sestra")
                     global view_Sestra
                     view_Sestra = QtGui.QTableView()
                     view_Sestra.setItemDelegate(QCustomDelegate())
                     view_Sestra.setModel(Sestra_query)
                     view_Sestra.setWindowTitle('sestra')
                     view_Sestra.show()

              if self.Soba_checkBox.isChecked():
                     Soba_query = QSqlQueryModel()
                     Soba_query.setQuery("SELECT * FROM soba")
                     global view_Soba
                     view_Soba = QtGui.QTableView()
                     view_Soba.setModel(Soba_query)
                     view_Soba.setWindowTitle('soba')
                     view_Soba.show()

              if self.Zaduzena_za_salu_checkBox.isChecked():
                     Zaduzena_za_salu_query = QSqlQueryModel()
                     Zaduzena_za_salu_query.setQuery("SELECT * FROM zaduzena_za_salu")
                     global view_Zaduzena_za_salu
                     view_Zaduzena_za_salu = QtGui.QTableView()
                     view_Zaduzena_za_salu.setItemDelegate(QCustomDelegate())
                     view_Zaduzena_za_salu.setModel(Zaduzena_za_salu_query)
                     view_Zaduzena_za_salu.setWindowTitle('zaduzena_za_salu')
                     view_Zaduzena_za_salu.show()

              if self.Zaduzena_za_sobu_checkBox.isChecked():
                     Zaduzena_za_sobu_query = QSqlQueryModel()
                     Zaduzena_za_sobu_query.setQuery("SELECT * FROM zaduzena_za_sobu")
                     global view_Zaduzena_za_sobu
                     view_Zaduzena_za_sobu = QtGui.QTableView()
                     view_Zaduzena_za_sobu.setItemDelegate(QCustomDelegate())
                     view_Zaduzena_za_sobu.setModel(Zaduzena_za_sobu_query)
                     view_Zaduzena_za_sobu.setWindowTitle('zaduzena_za_sobu')
                     view_Zaduzena_za_sobu.show()

              
       def open_add_ui(self):
              if self.Add_Data_comboBox.currentText() == "Kirurg":
                     global kirurg
                     kirurg = kirurg_GUI()
                     kirurg.show()
                     
              if self.Add_Data_comboBox.currentText() == "Pacijent":
                     global pacijent
                     pacijent = pacijent_GUI()
                     pacijent.show()
                     
              if self.Add_Data_comboBox.currentText() == "Asistira":
                     global asistira
                     asistira = asistira_GUI()
                     asistira.show()

              if self.Add_Data_comboBox.currentText() == "Konzultant":
                     global konzultant
                     konzultant = konzultant_GUI()
                     konzultant.show()

              if self.Add_Data_comboBox.currentText() == "Nadgleda":
                     global nadgleda
                     nadgleda = nadgleda_GUI()
                     nadgleda.show()

              if self.Add_Data_comboBox.currentText() == "Operacija":
                     global operacija
                     operacija = operacija_GUI()
                     operacija.show()

              if self.Add_Data_comboBox.currentText() == "Privatni pacijent":
                     global privatni_pacijent
                     privatni_pacijent = privatni_pacijent_GUI()
                     privatni_pacijent.show()

              if self.Add_Data_comboBox.currentText() == "Sala":
                     global sala
                     sala = sala_GUI()
                     sala.show()

              if self.Add_Data_comboBox.currentText() == "Sestra":
                     global sestra
                     sestra = sestra_GUI()
                     sestra.show()

              if self.Add_Data_comboBox.currentText() == "Soba":
                     global soba
                     soba = soba_GUI()
                     soba.show()

              if self.Add_Data_comboBox.currentText() == "Zaduzena za salu":
                     global zaduzena_za_salu
                     zaduzena_za_salu = zaduzena_za_salu_GUI()
                     zaduzena_za_salu.show()

              if self.Add_Data_comboBox.currentText() == "Zaduzena za sobu":
                     global zaduzena_za_sobu
                     zaduzena_za_sobu = zaduzena_za_sobu_GUI()
                     zaduzena_za_sobu.show()
                     
       def open_delete_ui(self):
              global delete
              delete = delete_GUI()
              delete.show()
                     
       def open_update_ui(self):
              global update
              update = update_GUI()
              update.show()

       def open_search_ui(self):
              global search
              search = search_GUI()
              search.show()

       def open_report_ui(self):
              global report
              report = report_GUI()
              report.show()
                                   
class kirurg_GUI(QtGui.QWidget, Ui_kirurg_Widget):
       def __init__(self):
              QtGui.QWidget.__init__(self)
              self.setupUi(self)
              self.kirurg_Add_button.clicked.connect(self.insert_kirurg)
              maxLength = 11
              self.kirurg_oib_kir_lineEdit.setInputMask(('9' * maxLength) + ';_')
              self.kirurg_oib_kir_lineEdit.setMaxLength(maxLength)

       def insert_kirurg(self):
              oib_kir = self.kirurg_oib_kir_lineEdit.text()
              if not oib_kir:
                     QtGui.QMessageBox.critical(self, 'Query error', 'OIB kirurga can not be empty')

              if oib_kir and len(str(oib_kir)) != self.kirurg_oib_kir_lineEdit.maxLength():
                     QtGui.QMessageBox.critical(self, 'Query error', 'OIB kirurga has to have 11 digits')

              if oib_kir and len(str(oib_kir)) == self.kirurg_oib_kir_lineEdit.maxLength(): 
                     query = QSqlQuery()
                     status = query.exec("INSERT INTO kirurg (oib_kir, prezime, ime, adresa, broj_telefona)"
                                         "VALUES ('%s', '%s', '%s', '%s', '%s')" % (''.join(self.kirurg_oib_kir_lineEdit.text()),
                                                                                    ''.join(self.kirurg_prezime_lineEdit.text()),
                                                                                    ''.join(self.kirurg_ime_lineEdit.text()),
                                                                                    ''.join(self.kirurg_adresa_lineEdit.text()),
                                                                                    ''.join(self.kirurg_broj_telefona_lineEdit.text())))
                     if status is not True:
                            errorText = query.lastError().text()
                            QtGui.QMessageBox.critical(self, 'Query error', errorText)

                     else:
                            msgBox = QtGui.QMessageBox()
                            msgBox.setWindowTitle("Kirurg")
                            msgBox.setText("Data entered successfully")
                            msgBox.exec_()
                            kirurg.close()
                     

class pacijent_GUI(QtGui.QWidget, Ui_pacijent_Widget):
       def __init__(self):
              QtGui.QWidget.__init__(self)
              self.setupUi(self)
              self.pacijent_Add_button.clicked.connect(self.insert_pacijent)
              maxLength = 11
              self.pacijent_oib_pac_lineEdit.setInputMask(('9' * maxLength) + ';_')
              self.pacijent_oib_pac_lineEdit.setMaxLength(maxLength)

       def insert_pacijent(self):
              oib_pac = self.pacijent_oib_pac_lineEdit.text()
              if not oib_pac:
                     QtGui.QMessageBox.critical(self, 'Query error', 'OIB pacijenta can not be empty')

              if oib_pac and len(str(oib_pac)) != self.pacijent_oib_pac_lineEdit.maxLength():
                     QtGui.QMessageBox.critical(self, 'Query error', 'OIB pacijenta has to have 11 digits') 
                     
              if oib_pac and len(str(oib_pac)) == self.pacijent_oib_pac_lineEdit.maxLength():
                     query = QSqlQuery()
                     status = query.exec("INSERT INTO pacijent (oib_pac, prezime, ime, id_sobe, adresa, datum_rodjenja, spol)"
                                         "VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (''.join(self.pacijent_oib_pac_lineEdit.text()),
                                                                                                ''.join(self.pacijent_prezime_lineEdit.text()),
                                                                                                ''.join(self.pacijent_ime_lineEdit.text()),
                                                                                                ''.join(self.pacijent_id_sobe_lineEdit.text()),
                                                                                                ''.join(self.pacijent_adresa_lineEdit.text()),
                                                                                                ''.join(self.pacijent_datum_rodjenja_lineEdit.text()),
                                                                                                ''.join(self.pacijent_spol_lineEdit.text())))
                     if status is not True:
                            errorText = query.lastError().text()
                            QtGui.QMessageBox.critical(self, 'Query error', errorText)

                     else:
                            msgBox = QtGui.QMessageBox()
                            msgBox.setWindowTitle("Pacijent")
                            msgBox.setText("Data entered successfully")
                            msgBox.exec_()
                            pacijent.close()

class asistira_GUI(QtGui.QWidget, Ui_asistira_Widget):
       def __init__(self):
              QtGui.QWidget.__init__(self)
              self.setupUi(self)
              self.asistira_Add_button.clicked.connect(self.insert_asistira)

       def insert_asistira(self):
              id_operacije = self.asistira_id_operacije_lineEdit.text()
              oib_kir = self.asistira_oib_kir_lineEdit.text()
              if not id_operacije or not oib_kir:
                     QtGui.QMessageBox.critical(self, 'Query error', 'ID operacije and OIB kirurga can not be empty')
              else:
                     query = QSqlQuery()
                     status = query.exec("INSERT INTO asistira (id_operacije, oib_kir, uloga)"
                                         "VALUES ('%s', '%s', '%s')" % (''.join(self.asistira_id_operacije_lineEdit.text()),
                                                                        ''.join(self.asistira_oib_kir_lineEdit.text()),
                                                                        ''.join(self.asistira_uloga_lineEdit.text())))
                     if status is not True:
                            errorText = query.lastError().text()
                            QtGui.QMessageBox.critical(self, 'Query error', errorText)

                     else:
                            msgBox = QtGui.QMessageBox()
                            msgBox.setWindowTitle("Asistira")
                            msgBox.setText("Data entered successfully")
                            msgBox.exec_()
                            asistira.close()

class konzultant_GUI(QtGui.QWidget, Ui_konzultant_Widget):
       def __init__(self):
              QtGui.QWidget.__init__(self)
              self.setupUi(self)
              self.konzultant_Add_button.clicked.connect(self.insert_konzultant)

       def insert_konzultant(self):
              oib_konz = self.konzultant_oib_konz_lineEdit.text()
              if not oib_konz:
                     QtGui.QMessageBox.critical(self, 'Query error', 'OIB konzultanta can not be empty')
              else:
                     query = QSqlQuery()
                     status = query.exec("INSERT INTO konzultant (oib_konz, specijalnost)"
                                         "VALUES ('%s', '%s')" % (''.join(self.konzultant_oib_konz_lineEdit.text()),
                                                                  ''.join(self.konzultant_specijalnost_lineEdit.text())))
                     if status is not True:
                            errorText = query.lastError().text()
                            QtGui.QMessageBox.critical(self, 'Query error', errorText)

                     else:
                            msgBox = QtGui.QMessageBox()
                            msgBox.setWindowTitle("Konzultant")
                            msgBox.setText("Data entered successfully")
                            msgBox.exec_()
                            konzultant.close()

class nadgleda_GUI(QtGui.QWidget, Ui_nadgleda_Widget):
       def __init__(self):
              QtGui.QWidget.__init__(self)
              self.setupUi(self)
              self.nadgleda_Add_button.clicked.connect(self.insert_nadgleda)

       def insert_nadgleda(self):
              oib_nadgledanog = self.nadgleda_oib_nadgledanog_lineEdit.text()
              if not oib_nadgledanog:
                     QtGui.QMessageBox.critical(self, 'Query error', 'OIB nadgledanog can not be empty')
              else:
                     query = QSqlQuery()
                     status = query.exec("INSERT INTO nadgleda (oib_nadgledanog, oib_konzultanta)"
                                         "VALUES ('%s', '%s')" % (''.join(self.nadgleda_oib_nadgledanog_lineEdit.text()),
                                                                  ''.join(self.nadgleda_oib_konzultanta_lineEdit.text())))
                     if status is not True:
                            errorText = query.lastError().text()
                            QtGui.QMessageBox.critical(self, 'Query error', errorText)

                     else:
                            msgBox = QtGui.QMessageBox()
                            msgBox.setWindowTitle("Nadgleda")
                            msgBox.setText("Data entered successfully")
                            msgBox.exec_()
                            nadgleda.close()

class operacija_GUI(QtGui.QWidget, Ui_operacija_Widget):
       def __init__(self):
              QtGui.QWidget.__init__(self)
              self.setupUi(self)
              self.operacija_Add_button.clicked.connect(self.insert_operacija)

       def insert_operacija(self):
              id_operacije = self.operacija_id_operacije_lineEdit.text()
              if not id_operacije:
                     QtGui.QMessageBox.critical(self, 'Query error', 'ID operacije can not be empty')
              else:
                     query = QSqlQuery()
                     status = query.exec("INSERT INTO operacija (id_operacije, oib_kir, id_sale, oib_pac, tip_operacije, datum, vrijeme)"
                                         "VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (''.join(self.operacija_id_operacije_lineEdit.text()),
                                                                                                ''.join(self.operacija_oib_kir_lineEdit.text()),
                                                                                                ''.join(self.operacija_id_sale_lineEdit.text()),
                                                                                                ''.join(self.operacija_oib_pac_lineEdit.text()),
                                                                                                ''.join(self.operacija_tip_operacije_lineEdit.text()),
                                                                                                ''.join(self.operacija_datum_lineEdit.text()),
                                                                                                ''.join(self.operacija_vrijeme_lineEdit.text())))
                     if status is not True:
                            errorText = query.lastError().text()
                            QtGui.QMessageBox.critical(self, 'Query error', errorText)

                     else:
                            msgBox = QtGui.QMessageBox()
                            msgBox.setWindowTitle("Operacija")
                            msgBox.setText("Data entered successfully")
                            msgBox.exec_()
                            operacija.close()

class privatni_pacijent_GUI(QtGui.QWidget, Ui_privatni_pacijent_Widget):
       def __init__(self):
              QtGui.QWidget.__init__(self)
              self.setupUi(self)
              self.privatni_pacijent_Add_button.clicked.connect(self.insert_privatni_pacijent)

       def insert_privatni_pacijent(self):
              oib_pr_pac = self.privatni_pacijent_oib_pr_pac_lineEdit.text()
              if not oib_pr_pac:
                     QtGui.QMessageBox.critical(self, 'Query error', 'OIB privatnog pacijenta can not be empty')
              else:
                     query = QSqlQuery()
                     status = query.exec("INSERT INTO privatni_pacijent (oib_pr_pac, oib_konz, id_privatne_sobe)"
                                         "VALUES ('%s', '%s', '%s')" % (''.join(self.privatni_pacijent_oib_pr_pac_lineEdit.text()),
                                                                        ''.join(self.privatni_pacijent_oib_konz_lineEdit.text()),
                                                                        ''.join(self.privatni_pacijent_id_privatne_sobe_lineEdit.text())))
                     if status is not True:
                            errorText = query.lastError().text()
                            QtGui.QMessageBox.critical(self, 'Query error', errorText)

                     else:
                            msgBox = QtGui.QMessageBox()
                            msgBox.setWindowTitle("Privatni pacijent")
                            msgBox.setText("Data entered successfully")
                            msgBox.exec_()
                            privatni_pacijent.close()

class sala_GUI(QtGui.QWidget, Ui_sala_Widget):
       def __init__(self):
              QtGui.QWidget.__init__(self)
              self.setupUi(self)
              self.sala_Add_button.clicked.connect(self.insert_sala)

       def insert_sala(self):
              id_sale = self.sala_id_sale_lineEdit.text()
              if not id_sale:
                     QtGui.QMessageBox.critical(self, 'Query error', 'ID sale can not be empty')
              else:
                     query = QSqlQuery()
                     status = query.exec("INSERT INTO sala (id_sale, tip_sale)"
                                         "VALUES ('%s', '%s')" % (''.join(self.sala_id_sale_lineEdit.text()),
                                                                  ''.join(self.sala_tip_sale_lineEdit.text())))
                     if status is not True:
                            errorText = query.lastError().text()
                            QtGui.QMessageBox.critical(self, 'Query error', errorText)

                     else:
                            msgBox = QtGui.QMessageBox()
                            msgBox.setWindowTitle("Sala")
                            msgBox.setText("Data entered successfully")
                            msgBox.exec_()
                            sala.close()

class sestra_GUI(QtGui.QWidget, Ui_sestra_Widget):
       def __init__(self):
              QtGui.QWidget.__init__(self)
              self.setupUi(self)
              self.sestra_Add_button.clicked.connect(self.insert_sestra)
              maxLength = 11
              self.sestra_oib_sestre_lineEdit.setInputMask(('9' * maxLength) + ';_')
              self.sestra_oib_sestre_lineEdit.setMaxLength(maxLength)

       def insert_sestra(self):
              oib_sestre = self.sestra_oib_sestre_lineEdit.text()
              if not oib_sestre:
                     QtGui.QMessageBox.critical(self, 'Query error', 'OIB sestre can not be empty')

              if oib_sestre and len(str(oib_sestre)) != self.sestra_oib_sestre_lineEdit.maxLength():
                     QtGui.QMessageBox.critical(self, 'Query error', 'OIB sestre has to have 11 digits')
              
              if oib_sestre and len(str(oib_sestre)) == self.sestra_oib_sestre_lineEdit.maxLength():
                     query = QSqlQuery()
                     status = query.exec("INSERT INTO sestra (oib_sestre, prezime, ime, strucni_stupanj)"
                                         "VALUES ('%s', '%s', '%s', '%s')" % (''.join(self.sestra_oib_sestre_lineEdit.text()),
                                                                              ''.join(self.sestra_prezime_lineEdit.text()),
                                                                              ''.join(self.sestra_ime_lineEdit.text()),
                                                                              ''.join(self.sestra_strucni_stupanj_lineEdit.text())))
                     if status is not True:
                            errorText = query.lastError().text()
                            QtGui.QMessageBox.critical(self, 'Query error', errorText)

                     else:
                            msgBox = QtGui.QMessageBox()
                            msgBox.setWindowTitle("Sestra")
                            msgBox.setText("Data entered successfully")
                            msgBox.exec_()
                            sestra.close()

class soba_GUI(QtGui.QWidget, Ui_soba_Widget):
       def __init__(self):
              QtGui.QWidget.__init__(self)
              self.setupUi(self)
              self.soba_Add_button.clicked.connect(self.insert_soba)

       def insert_soba(self):
              id_sobe = self.soba_id_sobe_lineEdit.text()
              if not id_sobe:
                     QtGui.QMessageBox.critical(self, 'Query error', 'ID sobe can not be empty')
              else:
                     query = QSqlQuery()
                     status = query.exec("INSERT INTO soba (id_sobe, tip_sobe, broj_kreveta)"
                                         "VALUES ('%s', '%s', '%s')" % (''.join(self.soba_id_sobe_lineEdit.text()),
                                                                        ''.join(self.soba_tip_sobe_lineEdit.text()),
                                                                        ''.join(self.soba_broj_kreveta_lineEdit.text())))
                     if status is not True:
                            errorText = query.lastError().text()
                            QtGui.QMessageBox.critical(self, 'Query error', errorText)

                     else:
                            msgBox = QtGui.QMessageBox()
                            msgBox.setWindowTitle("Soba")
                            msgBox.setText("Data entered successfully")
                            msgBox.exec_()
                            soba.close()

class zaduzena_za_salu_GUI(QtGui.QWidget, Ui_zaduzena_za_salu_Widget):
       def __init__(self):
              QtGui.QWidget.__init__(self)
              self.setupUi(self)
              self.zaduzena_za_salu_Add_button.clicked.connect(self.insert_zaduzena_za_salu)

       def insert_zaduzena_za_salu(self):
              oib_sestre = self.zaduzena_za_salu_oib_sestre_lineEdit.text()
              if not oib_sestre:
                     QtGui.QMessageBox.critical(self, 'Query error', 'OIB sestre can not be empty')
              else:
                     query = QSqlQuery()
                     status = query.exec("INSERT INTO zaduzena_za_salu (oib_sestre, id_sale, datum_zaduzivanja)"
                                         "VALUES ('%s', '%s', '%s')" % (''.join(self.zaduzena_za_salu_oib_sestre_lineEdit.text()),
                                                                        ''.join(self.zaduzena_za_salu_id_sale_lineEdit.text()),
                                                                        ''.join(self.zaduzena_za_salu_datum_zaduzivanja_lineEdit.text())))
                     if status is not True:
                            errorText = query.lastError().text()
                            QtGui.QMessageBox.critical(self, 'Query error', errorText)

                     else:
                            msgBox = QtGui.QMessageBox()
                            msgBox.setWindowTitle("Zaduzena za salu")
                            msgBox.setText("Data entered successfully")
                            msgBox.exec_()
                            zaduzena_za_salu.close()

class zaduzena_za_sobu_GUI(QtGui.QWidget, Ui_zaduzena_za_sobu_Widget):
       def __init__(self):
              QtGui.QWidget.__init__(self)
              self.setupUi(self)
              self.zaduzena_za_sobu_Add_button.clicked.connect(self.insert_zaduzena_za_sobu)

       def insert_zaduzena_za_sobu(self):
              oib_sestre = self.zaduzena_za_sobu_oib_sestre_lineEdit.text()
              if not oib_sestre:
                     QtGui.QMessageBox.critical(self, 'Query error', 'OIB sestre can not be empty')
              else:
                     query = QSqlQuery()
                     status = query.exec("INSERT INTO zaduzena_za_sobu (oib_sestre, id_sobe, datum_zaduzivanja)"
                                         "VALUES ('%s', '%s', '%s')" % (''.join(self.zaduzena_za_sobu_oib_sestre_lineEdit.text()),
                                                                        ''.join(self.zaduzena_za_sobu_id_sobe_lineEdit.text()),
                                                                        ''.join(self.zaduzena_za_sobu_datum_zaduzivanja_lineEdit.text())))
                     if status is not True:
                            errorText = query.lastError().text()
                            QtGui.QMessageBox.critical(self, 'Query error', errorText)

                     else:
                            msgBox = QtGui.QMessageBox()
                            msgBox.setWindowTitle("Zaduzena za sobu")
                            msgBox.setText("Data entered successfully")
                            msgBox.exec_()
                            zaduzena_za_sobu.close()

class delete_GUI(QtGui.QWidget, Ui_delete_Widget):
       def __init__(self):
              QtGui.QWidget.__init__(self)
              self.setupUi(self)
              self.Delete_Delete_button.clicked.connect(self.delete_data)

       def delete_data(self):
              query = QSqlQuery()
              status = query.exec(""" DELETE FROM "%s" WHERE "%s" = '%s' """ % (str(self.delete_from_table_lineEdit.text()), str(self.delete_where_lineEdit.text()), str(self.delete_has_value_lineEdit.text())))

              if status is not True:
                     errorText = query.lastError().text()
                     QtGui.QMessageBox.critical(self, 'Query error', errorText)

              else:
                     msgBox = QtGui.QMessageBox()
                     msgBox.setWindowTitle("Delete")
                     msgBox.setText("Data deleted successfully")
                     msgBox.exec_()
                     delete.close()
              
class update_GUI(QtGui.QWidget, Ui_update_Widget):
       def __init__(self):
              QtGui.QWidget.__init__(self)
              self.setupUi(self)
              self.Update_Update_button.clicked.connect(self.update_data)

       def update_data(self):
              query = QSqlQuery()
              status = query.exec(""" UPDATE "%s" SET "%s" = '%s' WHERE "%s" = '%s' """ % (str(self.update_from_table_lineEdit.text()), str(self.update_column_lineEdit.text()), str(self.update_to_lineEdit.text()), str(self.update_where_lineEdit.text()), str(self.update_has_value_lineEdit.text())))
              maxLength = 11

              if self.update_column_lineEdit.text() == "oib_kir":
                     self.update_to_lineEdit.setInputMask(('9' * maxLength) + ';_')
                     self.update_to_lineEdit.setMaxLength(maxLength)

                     oib_kir = self.update_to_lineEdit.text()
                     if not oib_kir:
                            QtGui.QMessageBox.critical(self, 'Query error', 'OIB kirurga can not be empty')
                     
                     if oib_kir and len(str(oib_kir)) != self.update_to_lineEdit.maxLength():
                            QtGui.QMessageBox.critical(self, 'Query error', 'OIB kirurga has to have 11 digits')

                     if oib_kir and len(str(oib_kir)) == self.update_to_lineEdit.maxLength():
                            if status is not True:
                                   errorText = query.lastError().text()
                                   QtGui.QMessageBox.critical(self, 'Query error', errorText)

                            else:
                                   msgBox = QtGui.QMessageBox()
                                   msgBox.setWindowTitle("Update")
                                   msgBox.setText("Data updated successfully")
                                   msgBox.exec_()
                                   update.close()

              if self.update_column_lineEdit.text() == "oib_pac":
                     self.update_to_lineEdit.setInputMask(('9' * maxLength) + ';_')
                     self.update_to_lineEdit.setMaxLength(maxLength)

                     oib_pac = self.update_to_lineEdit.text()
                     if not oib_pac:
                            QtGui.QMessageBox.critical(self, 'Query error', 'OIB pacijenta can not be empty')

                     if oib_pac and len(str(oib_pac)) != self.update_to_lineEdit.maxLength():
                            QtGui.QMessageBox.critical(self, 'Query error', 'OIB pacijenta has to have 11 digits')
                     
                     if oib_pac and len(str(oib_pac)) == self.update_to_lineEdit.maxLength():
                            if status is not True:
                                   errorText = query.lastError().text()
                                   QtGui.QMessageBox.critical(self, 'Query error', errorText)

                            else:
                                   msgBox = QtGui.QMessageBox()
                                   msgBox.setWindowTitle("Update")
                                   msgBox.setText("Data updated successfully")
                                   msgBox.exec_()
                                   update.close()

              if self.update_column_lineEdit.text() == "oib_sestre":
                     self.update_to_lineEdit.setInputMask(('9' * maxLength) + ';_')
                     self.update_to_lineEdit.setMaxLength(maxLength)

                     oib_sestre = self.update_to_lineEdit.text()
                     if not oib_sestre:
                            QtGui.QMessageBox.critical(self, 'Query error', 'OIB sestre can not be empty')

                     if oib_sestre and len(str(oib_sestre)) != self.update_to_lineEdit.maxLength():
                            QtGui.QMessageBox.critical(self, 'Query error', 'OIB sestre has to have 11 digits')
                     
                     if oib_sestre and len(str(oib_sestre)) == self.update_to_lineEdit.maxLength():
                            if status is not True:
                                   errorText = query.lastError().text()
                                   QtGui.QMessageBox.critical(self, 'Query error', errorText)

                            else:
                                   msgBox = QtGui.QMessageBox()
                                   msgBox.setWindowTitle("Update")
                                   msgBox.setText("Data updated successfully")
                                   msgBox.exec_()
                                   update.close()
              
              if self.update_column_lineEdit.text() != "oib_kir" and self.update_column_lineEdit.text() != "oib_pac" and self.update_column_lineEdit.text() != "oib_sestre":
                     if status is not True:
                            errorText = query.lastError().text()
                            QtGui.QMessageBox.critical(self, 'Query error', errorText)

                     else:
                            msgBox = QtGui.QMessageBox()
                            msgBox.setWindowTitle("Update")
                            msgBox.setText("Data updated successfully")
                            msgBox.exec_()
                            update.close()

class search_GUI(QtGui.QWidget, Ui_search_Widget):
       def __init__(self):
              QtGui.QWidget.__init__(self)
              self.setupUi(self)
              self.Search_Search_button.clicked.connect(self.search_data)

       def search_data(self):
              myQSqlQueryModel = QSqlQueryModel()
              query = QSqlQueryModel()
              global myQTableView 
              myQTableView = QtGui.QTableView()
              querySuccess = False
              for queryCommand in [""" SELECT * FROM "%s" WHERE "%s" = '%s' """ % (str(self.search_from_table_lineEdit.text()), str(self.search_where_lineEdit.text()), str(self.search_has_value_lineEdit.text()))]:
                     myQSqlQueryModel.setQuery(queryCommand)
                     if myQSqlQueryModel.rowCount() > 0:
                            myQTableView.setModel(myQSqlQueryModel)
                            myQTableView.setItemDelegate(QCustomDelegate())
                            myQTableView.show()
                            search.close()
                            querySuccess = True
                            break
              if not querySuccess:
                     query.setQuery(""" SELECT * FROM "%s" WHERE METAPHONE("%s", 3) = METAPHONE('%s', 3) OR LEVENSHTEIN("%s", '%s') < 4 """ % (str(self.search_from_table_lineEdit.text()), str(self.search_where_lineEdit.text()), str(self.search_has_value_lineEdit.text()), str(self.search_where_lineEdit.text()), str(self.search_has_value_lineEdit.text())))
                     global var
                     var = QtGui.QTableView()
                     var.setItemDelegate(QCustomDelegate())
                     var.setModel(query)
                     var.show()
                     search.close()

class report_GUI(QtGui.QWidget, Ui_report_Widget):
       def __init__(self):
              QtGui.QWidget.__init__(self)
              self.setupUi(self)
              self.report_Create_Report_button.clicked.connect(self.report_data)

       def report_data(self):
              FILE_NAME = self.report_report_name_lineEdit.text()
              exportQSqlQueryModel = QSqlQueryModel()
              exportQSqlQueryModel.setQuery(""" SELECT * FROM "%s" WHERE "%s" = '%s' """ % (str(self.report_from_table_lineEdit.text()), str(self.report_where_lineEdit.text()), str(self.report_has_value_lineEdit.text())))
              exportFile = open(FILE_NAME, 'wt')
              writer = csv.writer(exportFile)

              if (self.report_from_table_lineEdit.text() == "pacijent"):
                  exportQSqlQueryModel.setHeaderData(0, QtCore.Qt.Horizontal, 'OIB pacijenta')
                  exportQSqlQueryModel.setHeaderData(1, QtCore.Qt.Horizontal, 'Prezime')
                  exportQSqlQueryModel.setHeaderData(2, QtCore.Qt.Horizontal, 'Ime')
                  exportQSqlQueryModel.setHeaderData(3, QtCore.Qt.Horizontal, 'ID sobe')
                  exportQSqlQueryModel.setHeaderData(4, QtCore.Qt.Horizontal, 'Adresa')
                  exportQSqlQueryModel.setHeaderData(5, QtCore.Qt.Horizontal, 'Datum rodjenja')
                  exportQSqlQueryModel.setHeaderData(6, QtCore.Qt.Horizontal, 'Spol')

              if (self.report_from_table_lineEdit.text() == "asistira"):
                  exportQSqlQueryModel.setHeaderData(0, QtCore.Qt.Horizontal, 'ID operacije')
                  exportQSqlQueryModel.setHeaderData(1, QtCore.Qt.Horizontal, 'OIB kirurga')
                  exportQSqlQueryModel.setHeaderData(2, QtCore.Qt.Horizontal, 'Uloga')

              if (self.report_from_table_lineEdit.text() == "kirurg"):
                  exportQSqlQueryModel.setHeaderData(0, QtCore.Qt.Horizontal, 'OIB kirurga')
                  exportQSqlQueryModel.setHeaderData(1, QtCore.Qt.Horizontal, 'Prezime')
                  exportQSqlQueryModel.setHeaderData(2, QtCore.Qt.Horizontal, 'Ime')
                  exportQSqlQueryModel.setHeaderData(3, QtCore.Qt.Horizontal, 'Adresa')
                  exportQSqlQueryModel.setHeaderData(4, QtCore.Qt.Horizontal, 'Broj telefona')

              if (self.report_from_table_lineEdit.text() == "konzultant"):
                  exportQSqlQueryModel.setHeaderData(0, QtCore.Qt.Horizontal, 'OIB konzultanta')
                  exportQSqlQueryModel.setHeaderData(1, QtCore.Qt.Horizontal, 'Specijalnost')

              if (self.report_from_table_lineEdit.text() == "nadgleda"):
                  exportQSqlQueryModel.setHeaderData(0, QtCore.Qt.Horizontal, 'OIB nadgledanog')
                  exportQSqlQueryModel.setHeaderData(1, QtCore.Qt.Horizontal, 'OIB konzultanta')

              if (self.report_from_table_lineEdit.text() == "operacija"):
                  exportQSqlQueryModel.setHeaderData(0, QtCore.Qt.Horizontal, 'ID operacije')
                  exportQSqlQueryModel.setHeaderData(1, QtCore.Qt.Horizontal, 'OIB kirurga')
                  exportQSqlQueryModel.setHeaderData(2, QtCore.Qt.Horizontal, 'ID sale')
                  exportQSqlQueryModel.setHeaderData(3, QtCore.Qt.Horizontal, 'OIB pacijenta')
                  exportQSqlQueryModel.setHeaderData(4, QtCore.Qt.Horizontal, 'Tip operacije')
                  exportQSqlQueryModel.setHeaderData(5, QtCore.Qt.Horizontal, 'Datum')
                  exportQSqlQueryModel.setHeaderData(6, QtCore.Qt.Horizontal, 'Vrijeme')

              if (self.report_from_table_lineEdit.text() == "privatni_pacijent"):
                  exportQSqlQueryModel.setHeaderData(0, QtCore.Qt.Horizontal, 'OIB privatnog pacijenta')
                  exportQSqlQueryModel.setHeaderData(1, QtCore.Qt.Horizontal, 'OIB konzultanta')
                  exportQSqlQueryModel.setHeaderData(2, QtCore.Qt.Horizontal, 'ID privatne sobe')

              if (self.report_from_table_lineEdit.text() == "sala"):
                  exportQSqlQueryModel.setHeaderData(0, QtCore.Qt.Horizontal, 'ID sale')
                  exportQSqlQueryModel.setHeaderData(1, QtCore.Qt.Horizontal, 'Tip sale')

              if (self.report_from_table_lineEdit.text() == "sestra"):
                  exportQSqlQueryModel.setHeaderData(0, QtCore.Qt.Horizontal, 'OIB sestre')
                  exportQSqlQueryModel.setHeaderData(1, QtCore.Qt.Horizontal, 'Prezime')
                  exportQSqlQueryModel.setHeaderData(2, QtCore.Qt.Horizontal, 'Ime')
                  exportQSqlQueryModel.setHeaderData(3, QtCore.Qt.Horizontal, 'Strucni stupanj')

              if (self.report_from_table_lineEdit.text() == "soba"):
                  exportQSqlQueryModel.setHeaderData(0, QtCore.Qt.Horizontal, 'ID sobe')
                  exportQSqlQueryModel.setHeaderData(1, QtCore.Qt.Horizontal, 'Tip sobe')
                  exportQSqlQueryModel.setHeaderData(2, QtCore.Qt.Horizontal, 'Broj kreveta')

              if (self.report_from_table_lineEdit.text() == "zaduzena_za_salu"):
                  exportQSqlQueryModel.setHeaderData(0, QtCore.Qt.Horizontal, 'OIB sestre')
                  exportQSqlQueryModel.setHeaderData(1, QtCore.Qt.Horizontal, 'ID sale')
                  exportQSqlQueryModel.setHeaderData(2, QtCore.Qt.Horizontal, 'Datum zaduzivanja')

              if (self.report_from_table_lineEdit.text() == "zaduzena_za_sobu"):
                  exportQSqlQueryModel.setHeaderData(0, QtCore.Qt.Horizontal, 'OIB sestre')
                  exportQSqlQueryModel.setHeaderData(1, QtCore.Qt.Horizontal, 'ID sobe')
                  exportQSqlQueryModel.setHeaderData(2, QtCore.Qt.Horizontal, 'Datum zaduzivanja')

              listsTmpData = []
              for column in range(exportQSqlQueryModel.columnCount()):
                     listsTmpData.append(str(exportQSqlQueryModel.headerData(column, QtCore.Qt.Horizontal)))
              writer.writerow(listsTmpData)

              for row in range(exportQSqlQueryModel.rowCount()):
                     listsTmpData = []
                     for column in range(exportQSqlQueryModel.columnCount()):
                            listsTmpData.append(str(exportQSqlQueryModel.record(row).value(column)))
                     writer.writerow(listsTmpData)
              exportFile.close()
              msgBox = QtGui.QMessageBox()
              msgBox.setWindowTitle("Report")
              msgBox.setText("Report created successfully")
              msgBox.exec_()
              report.close()

if __name__ == "__main__":
       app = QtGui.QApplication(sys.argv)
       login = login_GUI()
       login.show()

db = QSqlDatabase.addDatabase("QPSQL")
db.setHostName("localhost")
db.setDatabaseName("BP Za bolnicu")
db.setUserName("postgres")
db.setPassword("zanoktica")
db.setPort(5432)
ok = db.open()

if ok:
    print("Connected to database")
else:
    print("Error connecting to database")

sys.exit(app.exec_())
