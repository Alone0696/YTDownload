from pytube import YouTube
from PyQt5 import QtCore, QtGui, QtWidgets
from ui import Ui_Ramz_ild
import sys,os
import moviepy.editor as mpe


def down_not_optim(link,resol):
    try:  
        yt = YouTube('%s'%link)
        yt = yt.streams.filter(file_extension='mp4',res='%s'%resol).first()
        yt.download()
        ui.link_l.setText('Успешно')
    except:
        ui.link_l.setText('Ошибка(неверная ссылка или неверное качество')
def down_optim(link):
    try:
        yt = YouTube('%s'%link)
        yt = yt.streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first()
        yt.download()
        ui.link_l.setText('Успешно')
    except:
        ui.link_l.setText('Ошибка')

def down_sound(link):
    try:
        yt = YouTube('%s'%link)
        yt = yt.streams.filter(progressive=False,file_extension='mp4').first()
        yt.download(filename='s')
        video = mpe.VideoFileClip('s.mp4')
        video.audio.write_audiofile('sound.mp3')
        video.close()
        os.remove('s.mp4')
        ui.link_l.setText('Успешно')
    except:
        ui.link_l.setText('Ошибка')

app = QtWidgets.QApplication(sys.argv)
Ramz_ild = QtWidgets.QMainWindow()
ui = Ui_Ramz_ild()
ui.setupUi(Ramz_ild)
Ramz_ild.show()
def start():
    if ui.video_check.isChecked() == True:
        if ui.res.currentText() == 'Оптимальное качество':
            down_optim(ui.link_l.text())
        else:
            down_not_optim(ui.link_l.text(),ui.res.currentText())
    if ui.audio_check.isChecked() == True:
        down_sound(ui.link_l.text())
    if ui.video_check.isChecked() == False and ui.audio_check.isChecked() == False:
        ui.link_l.setText('Выберите параметр')
ui.down_p.clicked.connect(start)
sys.exit(app.exec_())
