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

class Ui_asistira_Widget(object):
    def setupUi(self, asistira_Widget):
        asistira_Widget.setObjectName(_fromUtf8("asistira_Widget"))
        asistira_Widget.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../icrc.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        asistira_Widget.setWindowIcon(icon)
        self.horizontalLayout_4 = QtGui.QHBoxLayout(asistira_Widget)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.asistira_id_operacije_label = QtGui.QLabel(asistira_Widget)
        self.asistira_id_operacije_label.setObjectName(_fromUtf8("asistira_id_operacije_label"))
        self.horizontalLayout.addWidget(self.asistira_id_operacije_label)
        self.asistira_id_operacije_lineEdit = QtGui.QLineEdit(asistira_Widget)
        self.asistira_id_operacije_lineEdit.setMaxLength(12)
        self.asistira_id_operacije_lineEdit.setObjectName(_fromUtf8("asistira_id_operacije_lineEdit"))
        self.horizontalLayout.addWidget(self.asistira_id_operacije_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.asistira_oib_kir_label = QtGui.QLabel(asistira_Widget)
        self.asistira_oib_kir_label.setObjectName(_fromUtf8("asistira_oib_kir_label"))
        self.horizontalLayout_2.addWidget(self.asistira_oib_kir_label)
        self.asistira_oib_kir_lineEdit = QtGui.QLineEdit(asistira_Widget)
        self.asistira_oib_kir_lineEdit.setMaxLength(11)
        self.asistira_oib_kir_lineEdit.setObjectName(_fromUtf8("asistira_oib_kir_lineEdit"))
        self.horizontalLayout_2.addWidget(self.asistira_oib_kir_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.asistira_uloga_label = QtGui.QLabel(asistira_Widget)
        self.asistira_uloga_label.setObjectName(_fromUtf8("asistira_uloga_label"))
        self.horizontalLayout_3.addWidget(self.asistira_uloga_label)
        self.asistira_uloga_lineEdit = QtGui.QLineEdit(asistira_Widget)
        self.asistira_uloga_lineEdit.setObjectName(_fromUtf8("asistira_uloga_lineEdit"))
        self.horizontalLayout_3.addWidget(self.asistira_uloga_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.asistira_Add_button = QtGui.QPushButton(asistira_Widget)
        self.asistira_Add_button.setObjectName(_fromUtf8("asistira_Add_button"))
        self.verticalLayout_2.addWidget(self.asistira_Add_button)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.retranslateUi(asistira_Widget)
        QtCore.QMetaObject.connectSlotsByName(asistira_Widget)

    def retranslateUi(self, asistira_Widget):
        asistira_Widget.setWindowTitle(_translate("asistira_Widget", "Asistira", None))
        self.asistira_id_operacije_label.setText(_translate("asistira_Widget", "ID operacije", None))
        self.asistira_oib_kir_label.setText(_translate("asistira_Widget", "OIB kirurga", None))
        self.asistira_uloga_label.setText(_translate("asistira_Widget", "Uloga", None))
        self.asistira_Add_button.setText(_translate("asistira_Widget", "Add", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    asistira_Widget = QtGui.QWidget()
    ui = Ui_asistira_Widget()
    ui.setupUi(asistira_Widget)
    asistira_Widget.show()
    sys.exit(app.exec_())

