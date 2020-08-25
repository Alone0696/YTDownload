from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Ramz_ild(object):
    def setupUi(self, Ramz_ild):
        Ramz_ild.setObjectName("Ramz_ild")
        Ramz_ild.resize(550, 350)
        Ramz_ild.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(Ramz_ild)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 220, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 120, 471, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(14, 30, 541, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        Ramz_ild.setCentralWidget(self.centralwidget)

        self.retranslateUi(Ramz_ild)
        QtCore.QMetaObject.connectSlotsByName(Ramz_ild)

    def retranslateUi(self, Ramz_ild):
        _translate = QtCore.QCoreApplication.translate
        Ramz_ild.setWindowTitle(_translate("Ramz_ild", "Ramz_ild"))
        self.pushButton.setText(_translate("Ramz_ild", "Скачать"))
        self.label.setText(_translate("Ramz_ild", "Вставьте ссылку и нажмите кнопку скачать"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ramz_ild = QtWidgets.QMainWindow()
    ui = Ui_Ramz_ild()
    ui.setupUi(Ramz_ild)
    Ramz_ild.show()
    sys.exit(app.exec_())
