from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_kirurg_Widget(object):
    def setupUi(self, kirurg_Widget):
        kirurg_Widget.setObjectName(_fromUtf8("kirurg_Widget"))
        kirurg_Widget.resize(437, 301)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../icrc.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        kirurg_Widget.setWindowIcon(icon)
        self.horizontalLayout_6 = QtGui.QHBoxLayout(kirurg_Widget)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.kirurg_oib_kir_label = QtGui.QLabel(kirurg_Widget)
        self.kirurg_oib_kir_label.setObjectName(_fromUtf8("kirurg_oib_kir_label"))
        self.horizontalLayout.addWidget(self.kirurg_oib_kir_label)
        self.kirurg_oib_kir_lineEdit = QtGui.QLineEdit(kirurg_Widget)
        self.kirurg_oib_kir_lineEdit.setMaxLength(11)
        self.kirurg_oib_kir_lineEdit.setObjectName(_fromUtf8("kirurg_oib_kir_lineEdit"))
        self.horizontalLayout.addWidget(self.kirurg_oib_kir_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.kirurg_prezime_label = QtGui.QLabel(kirurg_Widget)
        self.kirurg_prezime_label.setObjectName(_fromUtf8("kirurg_prezime_label"))
        self.horizontalLayout_2.addWidget(self.kirurg_prezime_label)
        self.kirurg_prezime_lineEdit = QtGui.QLineEdit(kirurg_Widget)
        self.kirurg_prezime_lineEdit.setObjectName(_fromUtf8("kirurg_prezime_lineEdit"))
        self.horizontalLayout_2.addWidget(self.kirurg_prezime_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.kirurg_ime_label = QtGui.QLabel(kirurg_Widget)
        self.kirurg_ime_label.setObjectName(_fromUtf8("kirurg_ime_label"))
        self.horizontalLayout_3.addWidget(self.kirurg_ime_label)
        self.kirurg_ime_lineEdit = QtGui.QLineEdit(kirurg_Widget)
        self.kirurg_ime_lineEdit.setObjectName(_fromUtf8("kirurg_ime_lineEdit"))
        self.horizontalLayout_3.addWidget(self.kirurg_ime_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.kirurg_adresa_label = QtGui.QLabel(kirurg_Widget)
        self.kirurg_adresa_label.setObjectName(_fromUtf8("kirurg_adresa_label"))
        self.horizontalLayout_4.addWidget(self.kirurg_adresa_label)
        self.kirurg_adresa_lineEdit = QtGui.QLineEdit(kirurg_Widget)
        self.kirurg_adresa_lineEdit.setObjectName(_fromUtf8("kirurg_adresa_lineEdit"))
        self.horizontalLayout_4.addWidget(self.kirurg_adresa_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.kirurg_broj_telefona_label = QtGui.QLabel(kirurg_Widget)
        self.kirurg_broj_telefona_label.setObjectName(_fromUtf8("kirurg_broj_telefona_label"))
        self.horizontalLayout_5.addWidget(self.kirurg_broj_telefona_label)
        self.kirurg_broj_telefona_lineEdit = QtGui.QLineEdit(kirurg_Widget)
        self.kirurg_broj_telefona_lineEdit.setMaxLength(12)
        self.kirurg_broj_telefona_lineEdit.setObjectName(_fromUtf8("kirurg_broj_telefona_lineEdit"))
        self.horizontalLayout_5.addWidget(self.kirurg_broj_telefona_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.kirurg_Add_button = QtGui.QPushButton(kirurg_Widget)
        self.kirurg_Add_button.setObjectName(_fromUtf8("kirurg_Add_button"))
        self.verticalLayout_2.addWidget(self.kirurg_Add_button)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)

        self.retranslateUi(kirurg_Widget)
        QtCore.QMetaObject.connectSlotsByName(kirurg_Widget)

    def retranslateUi(self, kirurg_Widget):
        kirurg_Widget.setWindowTitle(_translate("kirurg_Widget", "Kirurg", None))
        self.kirurg_oib_kir_label.setText(_translate("kirurg_Widget", "OIB kirurga", None))
        self.kirurg_prezime_label.setText(_translate("kirurg_Widget", "Prezime", None))
        self.kirurg_ime_label.setText(_translate("kirurg_Widget", "Ime", None))
        self.kirurg_adresa_label.setText(_translate("kirurg_Widget", "Adresa", None))
        self.kirurg_broj_telefona_label.setText(_translate("kirurg_Widget", "Broj telefona", None))
        self.kirurg_Add_button.setText(_translate("kirurg_Widget", "Add", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    kirurg_Widget = QtGui.QWidget()
    ui = Ui_kirurg_Widget()
    ui.setupUi(kirurg_Widget)
    kirurg_Widget.show()
    sys.exit(app.exec_())

