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

class Ui_nadgleda_Widget(object):
    def setupUi(self, nadgleda_Widget):
        nadgleda_Widget.setObjectName(_fromUtf8("nadgleda_Widget"))
        nadgleda_Widget.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../icrc.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        nadgleda_Widget.setWindowIcon(icon)
        self.horizontalLayout_3 = QtGui.QHBoxLayout(nadgleda_Widget)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.nadgleda_oib_nadgledanog_label = QtGui.QLabel(nadgleda_Widget)
        self.nadgleda_oib_nadgledanog_label.setObjectName(_fromUtf8("nadgleda_oib_nadgledanog_label"))
        self.horizontalLayout.addWidget(self.nadgleda_oib_nadgledanog_label)
        self.nadgleda_oib_nadgledanog_lineEdit = QtGui.QLineEdit(nadgleda_Widget)
        self.nadgleda_oib_nadgledanog_lineEdit.setMaxLength(11)
        self.nadgleda_oib_nadgledanog_lineEdit.setObjectName(_fromUtf8("nadgleda_oib_nadgledanog_lineEdit"))
        self.horizontalLayout.addWidget(self.nadgleda_oib_nadgledanog_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.nadgleda_oib_konzultanta_label = QtGui.QLabel(nadgleda_Widget)
        self.nadgleda_oib_konzultanta_label.setObjectName(_fromUtf8("nadgleda_oib_konzultanta_label"))
        self.horizontalLayout_2.addWidget(self.nadgleda_oib_konzultanta_label)
        self.nadgleda_oib_konzultanta_lineEdit = QtGui.QLineEdit(nadgleda_Widget)
        self.nadgleda_oib_konzultanta_lineEdit.setMaxLength(11)
        self.nadgleda_oib_konzultanta_lineEdit.setObjectName(_fromUtf8("nadgleda_oib_konzultanta_lineEdit"))
        self.horizontalLayout_2.addWidget(self.nadgleda_oib_konzultanta_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.nadgleda_Add_button = QtGui.QPushButton(nadgleda_Widget)
        self.nadgleda_Add_button.setObjectName(_fromUtf8("nadgleda_Add_button"))
        self.verticalLayout.addWidget(self.nadgleda_Add_button)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(nadgleda_Widget)
        QtCore.QMetaObject.connectSlotsByName(nadgleda_Widget)

    def retranslateUi(self, nadgleda_Widget):
        nadgleda_Widget.setWindowTitle(_translate("nadgleda_Widget", "Nadgleda", None))
        self.nadgleda_oib_nadgledanog_label.setText(_translate("nadgleda_Widget", "OIB nadgledanog", None))
        self.nadgleda_oib_konzultanta_label.setText(_translate("nadgleda_Widget", "OIB konzultanta", None))
        self.nadgleda_Add_button.setText(_translate("nadgleda_Widget", "Add", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    nadgleda_Widget = QtGui.QWidget()
    ui = Ui_nadgleda_Widget()
    ui.setupUi(nadgleda_Widget)
    nadgleda_Widget.show()
    sys.exit(app.exec_())

