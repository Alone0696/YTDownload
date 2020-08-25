from pytube import YouTube
from PyQt5 import QtCore, QtGui, QtWidgets
from ui import Ui_Ramz_ild
import sys


def down(link):
    try:
        yt = YouTube('%s'%link)
        yt = yt.streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first()
        yt.download()
        ui.lineEdit.setText('Успешно')
    except:
        ui.lineEdit.setText('Неверная ссылка')


app = QtWidgets.QApplication(sys.argv)
Ramz_ild = QtWidgets.QMainWindow()
ui = Ui_Ramz_ild()
ui.setupUi(Ramz_ild)
Ramz_ild.show()
def start():
    down(ui.lineEdit.text())
ui.pushButton.clicked.connect(start)
sys.exit(app.exec_())
