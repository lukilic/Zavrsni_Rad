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

class Ui_report_Widget(object):
    def setupUi(self, report_Widget):
        report_Widget.setObjectName(_fromUtf8("report_Widget"))
        report_Widget.resize(302, 295)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../icrc.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        report_Widget.setWindowIcon(icon)
        self.horizontalLayout_5 = QtGui.QHBoxLayout(report_Widget)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.report_from_table_label = QtGui.QLabel(report_Widget)
        self.report_from_table_label.setObjectName(_fromUtf8("report_from_table_label"))
        self.horizontalLayout.addWidget(self.report_from_table_label)
        self.report_from_table_lineEdit = QtGui.QLineEdit(report_Widget)
        self.report_from_table_lineEdit.setObjectName(_fromUtf8("report_from_table_lineEdit"))
        self.horizontalLayout.addWidget(self.report_from_table_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.report_where_label = QtGui.QLabel(report_Widget)
        self.report_where_label.setObjectName(_fromUtf8("report_where_label"))
        self.horizontalLayout_2.addWidget(self.report_where_label)
        self.report_where_lineEdit = QtGui.QLineEdit(report_Widget)
        self.report_where_lineEdit.setObjectName(_fromUtf8("report_where_lineEdit"))
        self.horizontalLayout_2.addWidget(self.report_where_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.report_has_value_label = QtGui.QLabel(report_Widget)
        self.report_has_value_label.setObjectName(_fromUtf8("report_has_value_label"))
        self.horizontalLayout_3.addWidget(self.report_has_value_label)
        self.report_has_value_lineEdit = QtGui.QLineEdit(report_Widget)
        self.report_has_value_lineEdit.setObjectName(_fromUtf8("report_has_value_lineEdit"))
        self.horizontalLayout_3.addWidget(self.report_has_value_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.report_report_name_label = QtGui.QLabel(report_Widget)
        self.report_report_name_label.setObjectName(_fromUtf8("report_report_name_label"))
        self.horizontalLayout_4.addWidget(self.report_report_name_label)
        self.report_report_name_lineEdit = QtGui.QLineEdit(report_Widget)
        self.report_report_name_lineEdit.setObjectName(_fromUtf8("report_report_name_lineEdit"))
        self.horizontalLayout_4.addWidget(self.report_report_name_lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        spacerItem = QtGui.QSpacerItem(20, 28, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.report_Create_Report_button = QtGui.QPushButton(report_Widget)
        self.report_Create_Report_button.setObjectName(_fromUtf8("report_Create_Report_button"))
        self.verticalLayout_2.addWidget(self.report_Create_Report_button)
        spacerItem1 = QtGui.QSpacerItem(20, 28, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.retranslateUi(report_Widget)
        QtCore.QMetaObject.connectSlotsByName(report_Widget)

    def retranslateUi(self, report_Widget):
        report_Widget.setWindowTitle(_translate("report_Widget", "Report", None))
        self.report_from_table_label.setText(_translate("report_Widget", "Extract data from table", None))
        self.report_where_label.setText(_translate("report_Widget", "where", None))
        self.report_has_value_label.setText(_translate("report_Widget", "has value", None))
        self.report_report_name_label.setText(_translate("report_Widget", "Report name (.csv)", None))
        self.report_Create_Report_button.setText(_translate("report_Widget", "Create Report", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    report_Widget = QtGui.QWidget()
    ui = Ui_report_Widget()
    ui.setupUi(report_Widget)
    report_Widget.show()
    sys.exit(app.exec_())

