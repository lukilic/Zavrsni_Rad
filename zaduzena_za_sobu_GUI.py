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

class Ui_zaduzena_za_sobu_Widget(object):
    def setupUi(self, zaduzena_za_sobu_Widget):
        zaduzena_za_sobu_Widget.setObjectName(_fromUtf8("zaduzena_za_sobu_Widget"))
        zaduzena_za_sobu_Widget.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../icrc.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        zaduzena_za_sobu_Widget.setWindowIcon(icon)
        self.horizontalLayout_4 = QtGui.QHBoxLayout(zaduzena_za_sobu_Widget)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.zaduzena_za_sobu_oib_sestre_label = QtGui.QLabel(zaduzena_za_sobu_Widget)
        self.zaduzena_za_sobu_oib_sestre_label.setObjectName(_fromUtf8("zaduzena_za_sobu_oib_sestre_label"))
        self.horizontalLayout.addWidget(self.zaduzena_za_sobu_oib_sestre_label)
        self.zaduzena_za_sobu_oib_sestre_lineEdit = QtGui.QLineEdit(zaduzena_za_sobu_Widget)
        self.zaduzena_za_sobu_oib_sestre_lineEdit.setMaxLength(11)
        self.zaduzena_za_sobu_oib_sestre_lineEdit.setObjectName(_fromUtf8("zaduzena_za_sobu_oib_sestre_lineEdit"))
        self.horizontalLayout.addWidget(self.zaduzena_za_sobu_oib_sestre_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.zaduzena_za_sobu_id_sobe_label = QtGui.QLabel(zaduzena_za_sobu_Widget)
        self.zaduzena_za_sobu_id_sobe_label.setObjectName(_fromUtf8("zaduzena_za_sobu_id_sobe_label"))
        self.horizontalLayout_2.addWidget(self.zaduzena_za_sobu_id_sobe_label)
        self.zaduzena_za_sobu_id_sobe_lineEdit = QtGui.QLineEdit(zaduzena_za_sobu_Widget)
        self.zaduzena_za_sobu_id_sobe_lineEdit.setMaxLength(3)
        self.zaduzena_za_sobu_id_sobe_lineEdit.setObjectName(_fromUtf8("zaduzena_za_sobu_id_sobe_lineEdit"))
        self.horizontalLayout_2.addWidget(self.zaduzena_za_sobu_id_sobe_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.zaduzena_za_sobu_datum_zaduzivanja_label = QtGui.QLabel(zaduzena_za_sobu_Widget)
        self.zaduzena_za_sobu_datum_zaduzivanja_label.setObjectName(_fromUtf8("zaduzena_za_sobu_datum_zaduzivanja_label"))
        self.horizontalLayout_3.addWidget(self.zaduzena_za_sobu_datum_zaduzivanja_label)
        self.zaduzena_za_sobu_datum_zaduzivanja_lineEdit = QtGui.QLineEdit(zaduzena_za_sobu_Widget)
        self.zaduzena_za_sobu_datum_zaduzivanja_lineEdit.setObjectName(_fromUtf8("zaduzena_za_sobu_datum_zaduzivanja_lineEdit"))
        self.horizontalLayout_3.addWidget(self.zaduzena_za_sobu_datum_zaduzivanja_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.zaduzena_za_sobu_Add_button = QtGui.QPushButton(zaduzena_za_sobu_Widget)
        self.zaduzena_za_sobu_Add_button.setObjectName(_fromUtf8("zaduzena_za_sobu_Add_button"))
        self.verticalLayout_2.addWidget(self.zaduzena_za_sobu_Add_button)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.retranslateUi(zaduzena_za_sobu_Widget)
        QtCore.QMetaObject.connectSlotsByName(zaduzena_za_sobu_Widget)

    def retranslateUi(self, zaduzena_za_sobu_Widget):
        zaduzena_za_sobu_Widget.setWindowTitle(_translate("zaduzena_za_sobu_Widget", "Zaduzena za sobu", None))
        self.zaduzena_za_sobu_oib_sestre_label.setText(_translate("zaduzena_za_sobu_Widget", "OIB sestre", None))
        self.zaduzena_za_sobu_id_sobe_label.setText(_translate("zaduzena_za_sobu_Widget", "ID sobe", None))
        self.zaduzena_za_sobu_datum_zaduzivanja_label.setText(_translate("zaduzena_za_sobu_Widget", "Datum zaduzivanja (YYYY-MM-DD)", None))
        self.zaduzena_za_sobu_Add_button.setText(_translate("zaduzena_za_sobu_Widget", "Add", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    zaduzena_za_sobu_Widget = QtGui.QWidget()
    ui = Ui_zaduzena_za_sobu_Widget()
    ui.setupUi(zaduzena_za_sobu_Widget)
    zaduzena_za_sobu_Widget.show()
    sys.exit(app.exec_())

