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

class Ui_login_Widget(object):
    def setupUi(self, login_Widget):
        login_Widget.setObjectName(_fromUtf8("login_Widget"))
        login_Widget.resize(253, 246)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../icrc.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        login_Widget.setWindowIcon(icon)
        self.horizontalLayout = QtGui.QHBoxLayout(login_Widget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.login_username_label = QtGui.QLabel(login_Widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.login_username_label.setFont(font)
        self.login_username_label.setObjectName(_fromUtf8("login_username_label"))
        self.verticalLayout.addWidget(self.login_username_label)
        self.login_username_lineEdit = QtGui.QLineEdit(login_Widget)
        self.login_username_lineEdit.setObjectName(_fromUtf8("login_username_lineEdit"))
        self.verticalLayout.addWidget(self.login_username_lineEdit)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.login_password_label = QtGui.QLabel(login_Widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.login_password_label.setFont(font)
        self.login_password_label.setObjectName(_fromUtf8("login_password_label"))
        self.verticalLayout_2.addWidget(self.login_password_label)
        self.login_password_lineEdit = QtGui.QLineEdit(login_Widget)
        self.login_password_lineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.login_password_lineEdit.setObjectName(_fromUtf8("login_password_lineEdit"))
        self.verticalLayout_2.addWidget(self.login_password_lineEdit)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.login_login_button = QtGui.QPushButton(login_Widget)
        self.login_login_button.setObjectName(_fromUtf8("login_login_button"))
        self.verticalLayout_4.addWidget(self.login_login_button)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.retranslateUi(login_Widget)
        QtCore.QMetaObject.connectSlotsByName(login_Widget)

    def retranslateUi(self, login_Widget):
        login_Widget.setWindowTitle(_translate("login_Widget", "Login", None))
        self.login_username_label.setText(_translate("login_Widget", "Username", None))
        self.login_password_label.setText(_translate("login_Widget", "Password", None))
        self.login_login_button.setText(_translate("login_Widget", "Login", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    login_Widget = QtGui.QWidget()
    ui = Ui_login_Widget()
    ui.setupUi(login_Widget)
    login_Widget.show()
    sys.exit(app.exec_())

