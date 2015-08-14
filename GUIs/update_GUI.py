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

class Ui_update_Widget(object):
    def setupUi(self, update_Widget):
        update_Widget.setObjectName(_fromUtf8("update_Widget"))
        update_Widget.resize(296, 290)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../icrc.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        update_Widget.setWindowIcon(icon)
        self.horizontalLayout_6 = QtGui.QHBoxLayout(update_Widget)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.update_from_table_label = QtGui.QLabel(update_Widget)
        self.update_from_table_label.setObjectName(_fromUtf8("update_from_table_label"))
        self.horizontalLayout.addWidget(self.update_from_table_label)
        self.update_from_table_lineEdit = QtGui.QLineEdit(update_Widget)
        self.update_from_table_lineEdit.setObjectName(_fromUtf8("update_from_table_lineEdit"))
        self.horizontalLayout.addWidget(self.update_from_table_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.update_column_label = QtGui.QLabel(update_Widget)
        self.update_column_label.setObjectName(_fromUtf8("update_column_label"))
        self.horizontalLayout_2.addWidget(self.update_column_label)
        self.update_column_lineEdit = QtGui.QLineEdit(update_Widget)
        self.update_column_lineEdit.setObjectName(_fromUtf8("update_column_lineEdit"))
        self.horizontalLayout_2.addWidget(self.update_column_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.update_to_label = QtGui.QLabel(update_Widget)
        self.update_to_label.setObjectName(_fromUtf8("update_to_label"))
        self.horizontalLayout_3.addWidget(self.update_to_label)
        self.update_to_lineEdit = QtGui.QLineEdit(update_Widget)
        self.update_to_lineEdit.setObjectName(_fromUtf8("update_to_lineEdit"))
        self.horizontalLayout_3.addWidget(self.update_to_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.update_where_label = QtGui.QLabel(update_Widget)
        self.update_where_label.setObjectName(_fromUtf8("update_where_label"))
        self.horizontalLayout_4.addWidget(self.update_where_label)
        self.update_where_lineEdit = QtGui.QLineEdit(update_Widget)
        self.update_where_lineEdit.setObjectName(_fromUtf8("update_where_lineEdit"))
        self.horizontalLayout_4.addWidget(self.update_where_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.update_has_value_label = QtGui.QLabel(update_Widget)
        self.update_has_value_label.setObjectName(_fromUtf8("update_has_value_label"))
        self.horizontalLayout_5.addWidget(self.update_has_value_label)
        self.update_has_value_lineEdit = QtGui.QLineEdit(update_Widget)
        self.update_has_value_lineEdit.setObjectName(_fromUtf8("update_has_value_lineEdit"))
        self.horizontalLayout_5.addWidget(self.update_has_value_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtGui.QSpacerItem(20, 18, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.Update_Update_button = QtGui.QPushButton(update_Widget)
        self.Update_Update_button.setObjectName(_fromUtf8("Update_Update_button"))
        self.verticalLayout_2.addWidget(self.Update_Update_button)
        spacerItem1 = QtGui.QSpacerItem(18, 17, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)

        self.retranslateUi(update_Widget)
        QtCore.QMetaObject.connectSlotsByName(update_Widget)

    def retranslateUi(self, update_Widget):
        update_Widget.setWindowTitle(_translate("update_Widget", "Update", None))
        self.update_from_table_label.setText(_translate("update_Widget", "Update table", None))
        self.update_column_label.setText(_translate("update_Widget", "set column", None))
        self.update_to_label.setText(_translate("update_Widget", "to ", None))
        self.update_where_label.setText(_translate("update_Widget", "where", None))
        self.update_has_value_label.setText(_translate("update_Widget", "has value", None))
        self.Update_Update_button.setText(_translate("update_Widget", "Update", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    update_Widget = QtGui.QWidget()
    ui = Ui_update_Widget()
    ui.setupUi(update_Widget)
    update_Widget.show()
    sys.exit(app.exec_())

