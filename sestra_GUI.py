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

class Ui_sestra_Widget(object):
    def setupUi(self, sestra_Widget):
        sestra_Widget.setObjectName(_fromUtf8("sestra_Widget"))
        sestra_Widget.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../icrc.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        sestra_Widget.setWindowIcon(icon)
        self.horizontalLayout_5 = QtGui.QHBoxLayout(sestra_Widget)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.sestra_oib_sestre_label = QtGui.QLabel(sestra_Widget)
        self.sestra_oib_sestre_label.setObjectName(_fromUtf8("sestra_oib_sestre_label"))
        self.horizontalLayout.addWidget(self.sestra_oib_sestre_label)
        self.sestra_oib_sestre_lineEdit = QtGui.QLineEdit(sestra_Widget)
        self.sestra_oib_sestre_lineEdit.setMaxLength(11)
        self.sestra_oib_sestre_lineEdit.setObjectName(_fromUtf8("sestra_oib_sestre_lineEdit"))
        self.horizontalLayout.addWidget(self.sestra_oib_sestre_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.sestra_prezime_label = QtGui.QLabel(sestra_Widget)
        self.sestra_prezime_label.setObjectName(_fromUtf8("sestra_prezime_label"))
        self.horizontalLayout_2.addWidget(self.sestra_prezime_label)
        self.sestra_prezime_lineEdit = QtGui.QLineEdit(sestra_Widget)
        self.sestra_prezime_lineEdit.setObjectName(_fromUtf8("sestra_prezime_lineEdit"))
        self.horizontalLayout_2.addWidget(self.sestra_prezime_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.sestra_ime_label = QtGui.QLabel(sestra_Widget)
        self.sestra_ime_label.setObjectName(_fromUtf8("sestra_ime_label"))
        self.horizontalLayout_3.addWidget(self.sestra_ime_label)
        self.sestra_ime_lineEdit = QtGui.QLineEdit(sestra_Widget)
        self.sestra_ime_lineEdit.setObjectName(_fromUtf8("sestra_ime_lineEdit"))
        self.horizontalLayout_3.addWidget(self.sestra_ime_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.sestra_strucni_stupanj_label = QtGui.QLabel(sestra_Widget)
        self.sestra_strucni_stupanj_label.setObjectName(_fromUtf8("sestra_strucni_stupanj_label"))
        self.horizontalLayout_4.addWidget(self.sestra_strucni_stupanj_label)
        self.sestra_strucni_stupanj_lineEdit = QtGui.QLineEdit(sestra_Widget)
        self.sestra_strucni_stupanj_lineEdit.setMaxLength(5)
        self.sestra_strucni_stupanj_lineEdit.setObjectName(_fromUtf8("sestra_strucni_stupanj_lineEdit"))
        self.horizontalLayout_4.addWidget(self.sestra_strucni_stupanj_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.sestra_Add_button = QtGui.QPushButton(sestra_Widget)
        self.sestra_Add_button.setObjectName(_fromUtf8("sestra_Add_button"))
        self.verticalLayout_2.addWidget(self.sestra_Add_button)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.retranslateUi(sestra_Widget)
        QtCore.QMetaObject.connectSlotsByName(sestra_Widget)

    def retranslateUi(self, sestra_Widget):
        sestra_Widget.setWindowTitle(_translate("sestra_Widget", "Sestra", None))
        self.sestra_oib_sestre_label.setText(_translate("sestra_Widget", "OIB sestre", None))
        self.sestra_prezime_label.setText(_translate("sestra_Widget", "Prezime", None))
        self.sestra_ime_label.setText(_translate("sestra_Widget", "Ime", None))
        self.sestra_strucni_stupanj_label.setText(_translate("sestra_Widget", "Strucni stupanj", None))
        self.sestra_Add_button.setText(_translate("sestra_Widget", "Add", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    sestra_Widget = QtGui.QWidget()
    ui = Ui_sestra_Widget()
    ui.setupUi(sestra_Widget)
    sestra_Widget.show()
    sys.exit(app.exec_())

