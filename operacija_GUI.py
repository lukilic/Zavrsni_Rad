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

class Ui_operacija_Widget(object):
    def setupUi(self, operacija_Widget):
        operacija_Widget.setObjectName(_fromUtf8("operacija_Widget"))
        operacija_Widget.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../icrc.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        operacija_Widget.setWindowIcon(icon)
        self.horizontalLayout_8 = QtGui.QHBoxLayout(operacija_Widget)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.operacija_id_operacije_label = QtGui.QLabel(operacija_Widget)
        self.operacija_id_operacije_label.setObjectName(_fromUtf8("operacija_id_operacije_label"))
        self.horizontalLayout.addWidget(self.operacija_id_operacije_label)
        self.operacija_id_operacije_lineEdit = QtGui.QLineEdit(operacija_Widget)
        self.operacija_id_operacije_lineEdit.setMaxLength(12)
        self.operacija_id_operacije_lineEdit.setObjectName(_fromUtf8("operacija_id_operacije_lineEdit"))
        self.horizontalLayout.addWidget(self.operacija_id_operacije_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.operacija_oib_kir_label = QtGui.QLabel(operacija_Widget)
        self.operacija_oib_kir_label.setObjectName(_fromUtf8("operacija_oib_kir_label"))
        self.horizontalLayout_2.addWidget(self.operacija_oib_kir_label)
        self.operacija_oib_kir_lineEdit = QtGui.QLineEdit(operacija_Widget)
        self.operacija_oib_kir_lineEdit.setMaxLength(11)
        self.operacija_oib_kir_lineEdit.setObjectName(_fromUtf8("operacija_oib_kir_lineEdit"))
        self.horizontalLayout_2.addWidget(self.operacija_oib_kir_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.operacija_id_sale_label = QtGui.QLabel(operacija_Widget)
        self.operacija_id_sale_label.setObjectName(_fromUtf8("operacija_id_sale_label"))
        self.horizontalLayout_3.addWidget(self.operacija_id_sale_label)
        self.operacija_id_sale_lineEdit = QtGui.QLineEdit(operacija_Widget)
        self.operacija_id_sale_lineEdit.setMaxLength(3)
        self.operacija_id_sale_lineEdit.setObjectName(_fromUtf8("operacija_id_sale_lineEdit"))
        self.horizontalLayout_3.addWidget(self.operacija_id_sale_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.operacija_oib_pac_label = QtGui.QLabel(operacija_Widget)
        self.operacija_oib_pac_label.setObjectName(_fromUtf8("operacija_oib_pac_label"))
        self.horizontalLayout_4.addWidget(self.operacija_oib_pac_label)
        self.operacija_oib_pac_lineEdit = QtGui.QLineEdit(operacija_Widget)
        self.operacija_oib_pac_lineEdit.setMaxLength(11)
        self.operacija_oib_pac_lineEdit.setObjectName(_fromUtf8("operacija_oib_pac_lineEdit"))
        self.horizontalLayout_4.addWidget(self.operacija_oib_pac_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.operacija_tip_operacije_label = QtGui.QLabel(operacija_Widget)
        self.operacija_tip_operacije_label.setObjectName(_fromUtf8("operacija_tip_operacije_label"))
        self.horizontalLayout_5.addWidget(self.operacija_tip_operacije_label)
        self.operacija_tip_operacije_lineEdit = QtGui.QLineEdit(operacija_Widget)
        self.operacija_tip_operacije_lineEdit.setMaxLength(5)
        self.operacija_tip_operacije_lineEdit.setObjectName(_fromUtf8("operacija_tip_operacije_lineEdit"))
        self.horizontalLayout_5.addWidget(self.operacija_tip_operacije_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.operacija_datum_label = QtGui.QLabel(operacija_Widget)
        self.operacija_datum_label.setObjectName(_fromUtf8("operacija_datum_label"))
        self.horizontalLayout_6.addWidget(self.operacija_datum_label)
        self.operacija_datum_lineEdit = QtGui.QLineEdit(operacija_Widget)
        self.operacija_datum_lineEdit.setObjectName(_fromUtf8("operacija_datum_lineEdit"))
        self.horizontalLayout_6.addWidget(self.operacija_datum_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.operacija_vrijeme_label = QtGui.QLabel(operacija_Widget)
        self.operacija_vrijeme_label.setObjectName(_fromUtf8("operacija_vrijeme_label"))
        self.horizontalLayout_7.addWidget(self.operacija_vrijeme_label)
        self.operacija_vrijeme_lineEdit = QtGui.QLineEdit(operacija_Widget)
        self.operacija_vrijeme_lineEdit.setObjectName(_fromUtf8("operacija_vrijeme_lineEdit"))
        self.horizontalLayout_7.addWidget(self.operacija_vrijeme_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtGui.QSpacerItem(20, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.operacija_Add_button = QtGui.QPushButton(operacija_Widget)
        self.operacija_Add_button.setObjectName(_fromUtf8("operacija_Add_button"))
        self.verticalLayout_2.addWidget(self.operacija_Add_button)
        spacerItem1 = QtGui.QSpacerItem(20, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_8.addLayout(self.verticalLayout_2)

        self.retranslateUi(operacija_Widget)
        QtCore.QMetaObject.connectSlotsByName(operacija_Widget)

    def retranslateUi(self, operacija_Widget):
        operacija_Widget.setWindowTitle(_translate("operacija_Widget", "Operacija", None))
        self.operacija_id_operacije_label.setText(_translate("operacija_Widget", "ID operacije", None))
        self.operacija_oib_kir_label.setText(_translate("operacija_Widget", "OIB kirurga", None))
        self.operacija_id_sale_label.setText(_translate("operacija_Widget", "ID sale", None))
        self.operacija_oib_pac_label.setText(_translate("operacija_Widget", "OIB pacijenta", None))
        self.operacija_tip_operacije_label.setText(_translate("operacija_Widget", "Tip operacije", None))
        self.operacija_datum_label.setText(_translate("operacija_Widget", "Datum (YYYY-MM-DD)", None))
        self.operacija_vrijeme_label.setText(_translate("operacija_Widget", "Vrijeme (HH:MM:SS)", None))
        self.operacija_Add_button.setText(_translate("operacija_Widget", "Add", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    operacija_Widget = QtGui.QWidget()
    ui = Ui_operacija_Widget()
    ui.setupUi(operacija_Widget)
    operacija_Widget.show()
    sys.exit(app.exec_())

