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

class Ui_privatni_pacijent_Widget(object):
    def setupUi(self, privatni_pacijent_Widget):
        privatni_pacijent_Widget.setObjectName(_fromUtf8("privatni_pacijent_Widget"))
        privatni_pacijent_Widget.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../icrc.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        privatni_pacijent_Widget.setWindowIcon(icon)
        self.horizontalLayout_4 = QtGui.QHBoxLayout(privatni_pacijent_Widget)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.privatni_pacijent_oib_pr_pac_label = QtGui.QLabel(privatni_pacijent_Widget)
        self.privatni_pacijent_oib_pr_pac_label.setObjectName(_fromUtf8("privatni_pacijent_oib_pr_pac_label"))
        self.horizontalLayout.addWidget(self.privatni_pacijent_oib_pr_pac_label)
        self.privatni_pacijent_oib_pr_pac_lineEdit = QtGui.QLineEdit(privatni_pacijent_Widget)
        self.privatni_pacijent_oib_pr_pac_lineEdit.setMaxLength(11)
        self.privatni_pacijent_oib_pr_pac_lineEdit.setObjectName(_fromUtf8("privatni_pacijent_oib_pr_pac_lineEdit"))
        self.horizontalLayout.addWidget(self.privatni_pacijent_oib_pr_pac_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.privatni_pacijent_oib_konz_label = QtGui.QLabel(privatni_pacijent_Widget)
        self.privatni_pacijent_oib_konz_label.setObjectName(_fromUtf8("privatni_pacijent_oib_konz_label"))
        self.horizontalLayout_2.addWidget(self.privatni_pacijent_oib_konz_label)
        self.privatni_pacijent_oib_konz_lineEdit = QtGui.QLineEdit(privatni_pacijent_Widget)
        self.privatni_pacijent_oib_konz_lineEdit.setMaxLength(11)
        self.privatni_pacijent_oib_konz_lineEdit.setObjectName(_fromUtf8("privatni_pacijent_oib_konz_lineEdit"))
        self.horizontalLayout_2.addWidget(self.privatni_pacijent_oib_konz_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.privatni_pacijent_id_privatne_sobe_label = QtGui.QLabel(privatni_pacijent_Widget)
        self.privatni_pacijent_id_privatne_sobe_label.setObjectName(_fromUtf8("privatni_pacijent_id_privatne_sobe_label"))
        self.horizontalLayout_3.addWidget(self.privatni_pacijent_id_privatne_sobe_label)
        self.privatni_pacijent_id_privatne_sobe_lineEdit = QtGui.QLineEdit(privatni_pacijent_Widget)
        self.privatni_pacijent_id_privatne_sobe_lineEdit.setMaxLength(3)
        self.privatni_pacijent_id_privatne_sobe_lineEdit.setObjectName(_fromUtf8("privatni_pacijent_id_privatne_sobe_lineEdit"))
        self.horizontalLayout_3.addWidget(self.privatni_pacijent_id_privatne_sobe_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.privatni_pacijent_Add_button = QtGui.QPushButton(privatni_pacijent_Widget)
        self.privatni_pacijent_Add_button.setObjectName(_fromUtf8("privatni_pacijent_Add_button"))
        self.verticalLayout_2.addWidget(self.privatni_pacijent_Add_button)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.retranslateUi(privatni_pacijent_Widget)
        QtCore.QMetaObject.connectSlotsByName(privatni_pacijent_Widget)

    def retranslateUi(self, privatni_pacijent_Widget):
        privatni_pacijent_Widget.setWindowTitle(_translate("privatni_pacijent_Widget", "Privatni pacijent", None))
        self.privatni_pacijent_oib_pr_pac_label.setText(_translate("privatni_pacijent_Widget", "OIB privatnog pacijenta", None))
        self.privatni_pacijent_oib_konz_label.setText(_translate("privatni_pacijent_Widget", "OIB konzultanta", None))
        self.privatni_pacijent_id_privatne_sobe_label.setText(_translate("privatni_pacijent_Widget", "ID privatne sobe", None))
        self.privatni_pacijent_Add_button.setText(_translate("privatni_pacijent_Widget", "Add", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    privatni_pacijent_Widget = QtGui.QWidget()
    ui = Ui_privatni_pacijent_Widget()
    ui.setupUi(privatni_pacijent_Widget)
    privatni_pacijent_Widget.show()
    sys.exit(app.exec_())

