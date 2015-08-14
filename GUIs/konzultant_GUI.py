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

class Ui_konzultant_Widget(object):
    def setupUi(self, konzultant_Widget):
        konzultant_Widget.setObjectName(_fromUtf8("konzultant_Widget"))
        konzultant_Widget.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../icrc.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        konzultant_Widget.setWindowIcon(icon)
        self.horizontalLayout_3 = QtGui.QHBoxLayout(konzultant_Widget)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.konzultant_oib_konz_label = QtGui.QLabel(konzultant_Widget)
        self.konzultant_oib_konz_label.setObjectName(_fromUtf8("konzultant_oib_konz_label"))
        self.horizontalLayout.addWidget(self.konzultant_oib_konz_label)
        self.konzultant_oib_konz_lineEdit = QtGui.QLineEdit(konzultant_Widget)
        self.konzultant_oib_konz_lineEdit.setMaxLength(11)
        self.konzultant_oib_konz_lineEdit.setObjectName(_fromUtf8("konzultant_oib_konz_lineEdit"))
        self.horizontalLayout.addWidget(self.konzultant_oib_konz_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.konzultant_specijalnost_label = QtGui.QLabel(konzultant_Widget)
        self.konzultant_specijalnost_label.setObjectName(_fromUtf8("konzultant_specijalnost_label"))
        self.horizontalLayout_2.addWidget(self.konzultant_specijalnost_label)
        self.konzultant_specijalnost_lineEdit = QtGui.QLineEdit(konzultant_Widget)
        self.konzultant_specijalnost_lineEdit.setObjectName(_fromUtf8("konzultant_specijalnost_lineEdit"))
        self.horizontalLayout_2.addWidget(self.konzultant_specijalnost_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.konzultant_Add_button = QtGui.QPushButton(konzultant_Widget)
        self.konzultant_Add_button.setObjectName(_fromUtf8("konzultant_Add_button"))
        self.verticalLayout_2.addWidget(self.konzultant_Add_button)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(konzultant_Widget)
        QtCore.QMetaObject.connectSlotsByName(konzultant_Widget)

    def retranslateUi(self, konzultant_Widget):
        konzultant_Widget.setWindowTitle(_translate("konzultant_Widget", "Konzultant", None))
        self.konzultant_oib_konz_label.setText(_translate("konzultant_Widget", "OIB konzultanta", None))
        self.konzultant_specijalnost_label.setText(_translate("konzultant_Widget", "Specijalnost", None))
        self.konzultant_Add_button.setText(_translate("konzultant_Widget", "Add", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    konzultant_Widget = QtGui.QWidget()
    ui = Ui_konzultant_Widget()
    ui.setupUi(konzultant_Widget)
    konzultant_Widget.show()
    sys.exit(app.exec_())

