import os.path
import sys,login,operation,useregister

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtCore import QBasicTimer,QTime,QTimer
from captcha.image import ImageCaptcha
import random,string

import Sql


class user_register(QMainWindow,useregister.Ui_registration):
    def __init__(self):
        super(user_register,self).__init__()
        self.setupUi(self)
        self.code = ""
        self.Cancel_but.clicked.connect(self.Onlicked_quit)
        self.register_but.clicked.connect(self.Onlicked_register)
        self.tool_refrash.clicked.connect(self.Onlicked_refrash)
        self.auto_generation_code()
        self.Onlicked_refrash()

    def auto_generation_code(self):
        if os.path.isfile('code_file/code.jpg'):
            os.remove('code_file/code.jpg')
        self.chr_all = string.ascii_letters + string.digits
        self.chr_4 = ''.join(random.sample(self.chr_all, 4))
        image = ImageCaptcha().generate_image(self.chr_4)
        image.save('code_file/code.jpg')

    def Onlicked_refrash(self):
        self.auto_generation_code()
        self.codeimg = QtGui.QPixmap('code_file/code.jpg').scaled(self.codeimage.width(), self.codeimage.height())
        print(2)
        self.codeimage.setPixmap(self.codeimg)
        self.codeimage.update()

    def Onlicked_register(self):
        if self.Line_password != self.Line_passwordcomfire:
            return
        if Sql.user_insert(self.Line_username.text(),self.Line_password.text(),self.Line_email.text(),self.code,self.Linecode):
            self.destroy()
            user_op.show()


    def Onlicked_quit(self):
        mainWindow.show()
        self.destroy()
class user_login(QMainWindow,login.Ui_MainWindow):
    def __init__(self):
        super(user_login,self).__init__()
        self.setupUi(self)
        self.index = 10
        self.auto_index = 0
        self.timer1 = QBasicTimer()
        self.timer2 = QTimer()
        self.timer2.setInterval(1000)
        self.timer2.timeout.connect(self.auto_changed)
        self.auto_run()
        self.progressBar.setVisible(False)
        self.loginbut.clicked.connect(self.Onlicked_login)
        self.registerbut.clicked.connect(self.Onlicked_register)
        self.comply.clicked.connect(self.Onlicked_comply)

    def auto_changed(self):
        if self.auto_index <= 2:
            self.Propmt.setCurrentIndex(self.auto_index)
            self.Propmt.update()
            self.auto_index += 1
        else:
            self.auto_index = 0
    def auto_run(self):
        self.timer2.start()
    def Onlicked_register(self):
        self.hide()
        user_res.show()
    def Onlicked_login(self):
        if self.comply.isChecked():
            if len(self.usernameinput.text()) != 0 or len(self.passwordinput.text()) != 0:
                if Sql.user_search(self.usernameinput.text(),self.passwordinput.text()):
                    self.init_run()

    def init_run(self):
        self.progressBar.setVisible(True)
        self.timer1.start(100, self)

    def timerEvent(self, e):
        if self.index >= 100:
            self.progressBar.setValue(self.index)
            self.progressBar.update()
            self.index += 20
        else:
            self.timer1.stop()
            self.hide()
            user_op.show()


    def Onlicked_comply(self):
        self.comply.setEnabled(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = user_login()
    user_op = operation.usersyswindows()
    user_res = user_register()
    mainWindow.show()
    sys.exit(app.exec_())
