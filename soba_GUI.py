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

class Ui_soba_Widget(object):
    def setupUi(self, soba_Widget):
        soba_Widget.setObjectName(_fromUtf8("soba_Widget"))
        soba_Widget.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../icrc.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        soba_Widget.setWindowIcon(icon)
        self.horizontalLayout_4 = QtGui.QHBoxLayout(soba_Widget)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.soba_id_sobe_label = QtGui.QLabel(soba_Widget)
        self.soba_id_sobe_label.setObjectName(_fromUtf8("soba_id_sobe_label"))
        self.horizontalLayout.addWidget(self.soba_id_sobe_label)
        self.soba_id_sobe_lineEdit = QtGui.QLineEdit(soba_Widget)
        self.soba_id_sobe_lineEdit.setMaxLength(3)
        self.soba_id_sobe_lineEdit.setObjectName(_fromUtf8("soba_id_sobe_lineEdit"))
        self.horizontalLayout.addWidget(self.soba_id_sobe_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.soba_tip_sobe_label = QtGui.QLabel(soba_Widget)
        self.soba_tip_sobe_label.setObjectName(_fromUtf8("soba_tip_sobe_label"))
        self.horizontalLayout_2.addWidget(self.soba_tip_sobe_label)
        self.soba_tip_sobe_lineEdit = QtGui.QLineEdit(soba_Widget)
        self.soba_tip_sobe_lineEdit.setMaxLength(3)
        self.soba_tip_sobe_lineEdit.setObjectName(_fromUtf8("soba_tip_sobe_lineEdit"))
        self.horizontalLayout_2.addWidget(self.soba_tip_sobe_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.soba_broj_kreveta_label = QtGui.QLabel(soba_Widget)
        self.soba_broj_kreveta_label.setObjectName(_fromUtf8("soba_broj_kreveta_label"))
        self.horizontalLayout_3.addWidget(self.soba_broj_kreveta_label)
        self.soba_broj_kreveta_lineEdit = QtGui.QLineEdit(soba_Widget)
        self.soba_broj_kreveta_lineEdit.setObjectName(_fromUtf8("soba_broj_kreveta_lineEdit"))
        self.horizontalLayout_3.addWidget(self.soba_broj_kreveta_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.soba_Add_button = QtGui.QPushButton(soba_Widget)
        self.soba_Add_button.setObjectName(_fromUtf8("soba_Add_button"))
        self.verticalLayout_2.addWidget(self.soba_Add_button)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.retranslateUi(soba_Widget)
        QtCore.QMetaObject.connectSlotsByName(soba_Widget)

    def retranslateUi(self, soba_Widget):
        soba_Widget.setWindowTitle(_translate("soba_Widget", "Soba", None))
        self.soba_id_sobe_label.setText(_translate("soba_Widget", "ID sobe", None))
        self.soba_tip_sobe_label.setText(_translate("soba_Widget", "Tip sobe", None))
        self.soba_broj_kreveta_label.setText(_translate("soba_Widget", "Broj kreveta", None))
        self.soba_Add_button.setText(_translate("soba_Widget", "Add", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    soba_Widget = QtGui.QWidget()
    ui = Ui_soba_Widget()
    ui.setupUi(soba_Widget)
    soba_Widget.show()
    sys.exit(app.exec_())

