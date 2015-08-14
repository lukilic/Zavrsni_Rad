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

class Ui_delete_Widget(object):
    def setupUi(self, delete_Widget):
        delete_Widget.setObjectName(_fromUtf8("delete_Widget"))
        delete_Widget.resize(303, 298)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../icrc.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        delete_Widget.setWindowIcon(icon)
        self.horizontalLayout_4 = QtGui.QHBoxLayout(delete_Widget)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.delete_from_table_label = QtGui.QLabel(delete_Widget)
        self.delete_from_table_label.setObjectName(_fromUtf8("delete_from_table_label"))
        self.horizontalLayout.addWidget(self.delete_from_table_label)
        self.delete_from_table_lineEdit = QtGui.QLineEdit(delete_Widget)
        self.delete_from_table_lineEdit.setObjectName(_fromUtf8("delete_from_table_lineEdit"))
        self.horizontalLayout.addWidget(self.delete_from_table_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.delete_where_label = QtGui.QLabel(delete_Widget)
        self.delete_where_label.setObjectName(_fromUtf8("delete_where_label"))
        self.horizontalLayout_2.addWidget(self.delete_where_label)
        self.delete_where_lineEdit = QtGui.QLineEdit(delete_Widget)
        self.delete_where_lineEdit.setObjectName(_fromUtf8("delete_where_lineEdit"))
        self.horizontalLayout_2.addWidget(self.delete_where_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.delete_has_value_label = QtGui.QLabel(delete_Widget)
        self.delete_has_value_label.setObjectName(_fromUtf8("delete_has_value_label"))
        self.horizontalLayout_3.addWidget(self.delete_has_value_label)
        self.delete_has_value_lineEdit = QtGui.QLineEdit(delete_Widget)
        self.delete_has_value_lineEdit.setObjectName(_fromUtf8("delete_has_value_lineEdit"))
        self.horizontalLayout_3.addWidget(self.delete_has_value_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtGui.QSpacerItem(20, 28, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.Delete_Delete_button = QtGui.QPushButton(delete_Widget)
        self.Delete_Delete_button.setObjectName(_fromUtf8("Delete_Delete_button"))
        self.verticalLayout_2.addWidget(self.Delete_Delete_button)
        spacerItem1 = QtGui.QSpacerItem(20, 28, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.retranslateUi(delete_Widget)
        QtCore.QMetaObject.connectSlotsByName(delete_Widget)

    def retranslateUi(self, delete_Widget):
        delete_Widget.setWindowTitle(_translate("delete_Widget", "Delete", None))
        self.delete_from_table_label.setText(_translate("delete_Widget", "Delete from table", None))
        self.delete_where_label.setText(_translate("delete_Widget", "where column", None))
        self.delete_has_value_label.setText(_translate("delete_Widget", "has value", None))
        self.Delete_Delete_button.setText(_translate("delete_Widget", "Delete", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    delete_Widget = QtGui.QWidget()
    ui = Ui_delete_Widget()
    ui.setupUi(delete_Widget)
    delete_Widget.show()
    sys.exit(app.exec_())

