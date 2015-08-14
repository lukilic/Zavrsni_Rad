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

class Ui_sala_Widget(object):
    def setupUi(self, sala_Widget):
        sala_Widget.setObjectName(_fromUtf8("sala_Widget"))
        sala_Widget.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../icrc.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        sala_Widget.setWindowIcon(icon)
        self.horizontalLayout_3 = QtGui.QHBoxLayout(sala_Widget)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.sala_id_sale_label = QtGui.QLabel(sala_Widget)
        self.sala_id_sale_label.setObjectName(_fromUtf8("sala_id_sale_label"))
        self.horizontalLayout.addWidget(self.sala_id_sale_label)
        self.sala_id_sale_lineEdit = QtGui.QLineEdit(sala_Widget)
        self.sala_id_sale_lineEdit.setMaxLength(3)
        self.sala_id_sale_lineEdit.setObjectName(_fromUtf8("sala_id_sale_lineEdit"))
        self.horizontalLayout.addWidget(self.sala_id_sale_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.sala_tip_sale_label = QtGui.QLabel(sala_Widget)
        self.sala_tip_sale_label.setObjectName(_fromUtf8("sala_tip_sale_label"))
        self.horizontalLayout_2.addWidget(self.sala_tip_sale_label)
        self.sala_tip_sale_lineEdit = QtGui.QLineEdit(sala_Widget)
        self.sala_tip_sale_lineEdit.setMaxLength(3)
        self.sala_tip_sale_lineEdit.setObjectName(_fromUtf8("sala_tip_sale_lineEdit"))
        self.horizontalLayout_2.addWidget(self.sala_tip_sale_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.sala_Add_button = QtGui.QPushButton(sala_Widget)
        self.sala_Add_button.setObjectName(_fromUtf8("sala_Add_button"))
        self.verticalLayout_2.addWidget(self.sala_Add_button)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(sala_Widget)
        QtCore.QMetaObject.connectSlotsByName(sala_Widget)

    def retranslateUi(self, sala_Widget):
        sala_Widget.setWindowTitle(_translate("sala_Widget", "Sala", None))
        self.sala_id_sale_label.setText(_translate("sala_Widget", "ID sale", None))
        self.sala_tip_sale_label.setText(_translate("sala_Widget", "Tip sale", None))
        self.sala_Add_button.setText(_translate("sala_Widget", "Add", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    sala_Widget = QtGui.QWidget()
    ui = Ui_sala_Widget()
    ui.setupUi(sala_Widget)
    sala_Widget.show()
    sys.exit(app.exec_())

