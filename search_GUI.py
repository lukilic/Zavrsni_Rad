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

class Ui_search_Widget(object):
    def setupUi(self, search_Widget):
        search_Widget.setObjectName(_fromUtf8("search_Widget"))
        search_Widget.resize(301, 249)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../icrc.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        search_Widget.setWindowIcon(icon)
        self.horizontalLayout_4 = QtGui.QHBoxLayout(search_Widget)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.search_from_table_label = QtGui.QLabel(search_Widget)
        self.search_from_table_label.setObjectName(_fromUtf8("search_from_table_label"))
        self.horizontalLayout.addWidget(self.search_from_table_label)
        self.search_from_table_lineEdit = QtGui.QLineEdit(search_Widget)
        self.search_from_table_lineEdit.setObjectName(_fromUtf8("search_from_table_lineEdit"))
        self.horizontalLayout.addWidget(self.search_from_table_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.search_where_label = QtGui.QLabel(search_Widget)
        self.search_where_label.setObjectName(_fromUtf8("search_where_label"))
        self.horizontalLayout_2.addWidget(self.search_where_label)
        self.search_where_lineEdit = QtGui.QLineEdit(search_Widget)
        self.search_where_lineEdit.setObjectName(_fromUtf8("search_where_lineEdit"))
        self.horizontalLayout_2.addWidget(self.search_where_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.search_has_value_label = QtGui.QLabel(search_Widget)
        self.search_has_value_label.setObjectName(_fromUtf8("search_has_value_label"))
        self.horizontalLayout_3.addWidget(self.search_has_value_label)
        self.search_has_value_lineEdit = QtGui.QLineEdit(search_Widget)
        self.search_has_value_lineEdit.setObjectName(_fromUtf8("search_has_value_lineEdit"))
        self.horizontalLayout_3.addWidget(self.search_has_value_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtGui.QSpacerItem(17, 28, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.Search_Search_button = QtGui.QPushButton(search_Widget)
        self.Search_Search_button.setObjectName(_fromUtf8("Search_Search_button"))
        self.verticalLayout_2.addWidget(self.Search_Search_button)
        spacerItem1 = QtGui.QSpacerItem(17, 28, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.retranslateUi(search_Widget)
        QtCore.QMetaObject.connectSlotsByName(search_Widget)

    def retranslateUi(self, search_Widget):
        search_Widget.setWindowTitle(_translate("search_Widget", "Search", None))
        self.search_from_table_label.setText(_translate("search_Widget", "Search data from table", None))
        self.search_where_label.setText(_translate("search_Widget", "where", None))
        self.search_has_value_label.setText(_translate("search_Widget", "has value", None))
        self.Search_Search_button.setText(_translate("search_Widget", "Search", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    search_Widget = QtGui.QWidget()
    ui = Ui_search_Widget()
    ui.setupUi(search_Widget)
    search_Widget.show()
    sys.exit(app.exec_())

