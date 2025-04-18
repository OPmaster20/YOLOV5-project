# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 416)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/Bao/Downloads/management_settings_cogwheel_options_icon_262697.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.framework = QtWidgets.QFrame(self.centralwidget)
        self.framework.setGeometry(QtCore.QRect(10, 10, 781, 391))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.framework.setPalette(palette)
        self.framework.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.framework.setAutoFillBackground(False)
        self.framework.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.framework.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.framework.setObjectName("framework")
        self.formLayoutWidget = QtWidgets.QWidget(self.framework)
        self.formLayoutWidget.setGeometry(QtCore.QRect(460, 110, 301, 116))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.Input1 = QtWidgets.QLabel(self.formLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.Input1.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Input1.setFont(font)
        self.Input1.setAlignment(QtCore.Qt.AlignCenter)
        self.Input1.setObjectName("Input1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Input1)
        self.usernameinput = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.usernameinput.setFrame(False)
        self.usernameinput.setObjectName("usernameinput")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.usernameinput)
        self.Input2 = QtWidgets.QLabel(self.formLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.Input2.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Input2.setFont(font)
        self.Input2.setAlignment(QtCore.Qt.AlignCenter)
        self.Input2.setObjectName("Input2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Input2)
        self.passwordinput = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.passwordinput.setText("")
        self.passwordinput.setFrame(False)
        self.passwordinput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordinput.setObjectName("passwordinput")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.passwordinput)
        self.loginbut = QtWidgets.QPushButton(self.formLayoutWidget)
        self.loginbut.setEnabled(True)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 216, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 216, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 216, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.loginbut.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.loginbut.setFont(font)
        self.loginbut.setAutoFillBackground(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/Bao/Downloads/icons8-login-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.loginbut.setIcon(icon1)
        self.loginbut.setObjectName("loginbut")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.loginbut)
        self.registerbut = QtWidgets.QPushButton(self.formLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.registerbut.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.registerbut.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/Bao/Downloads/icons8-register-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.registerbut.setIcon(icon2)
        self.registerbut.setObjectName("registerbut")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.registerbut)
        self.comply = QtWidgets.QRadioButton(self.formLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.comply.setPalette(palette)
        font = QtGui.QFont()
        font.setItalic(True)
        font.setUnderline(True)
        font.setStrikeOut(False)
        self.comply.setFont(font)
        self.comply.setObjectName("comply")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comply)
        self.line1 = QtWidgets.QFrame(self.framework)
        self.line1.setGeometry(QtCore.QRect(430, 10, 31, 341))
        self.line1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line1.setLineWidth(2)
        self.line1.setFrameShape(QtWidgets.QFrame.VLine)
        self.line1.setObjectName("line1")
        self.Propmt = QtWidgets.QStackedWidget(self.framework)
        self.Propmt.setGeometry(QtCore.QRect(30, 30, 391, 311))
        self.Propmt.setFrameShape(QtWidgets.QFrame.Box)
        self.Propmt.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Propmt.setObjectName("Propmt")
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        self.photo1 = QtWidgets.QLabel(self.page1)
        self.photo1.setGeometry(QtCore.QRect(10, 10, 371, 291))
        self.photo1.setText("")
        self.photo1.setPixmap(QtGui.QPixmap("C:/Users/Bao/Desktop/bd/wallhaven-wqyqzx.jpg"))
        self.photo1.setScaledContents(True)
        self.photo1.setObjectName("photo1")
        self.Propmt.addWidget(self.page1)
        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName("page2")
        self.photo2 = QtWidgets.QLabel(self.page2)
        self.photo2.setGeometry(QtCore.QRect(10, 10, 371, 291))
        self.photo2.setText("")
        self.photo2.setPixmap(QtGui.QPixmap("C:/Users/Bao/Desktop/bd/wallhaven-476lgv.jpg"))
        self.photo2.setScaledContents(True)
        self.photo2.setObjectName("photo2")
        self.Propmt.addWidget(self.page2)
        self.page3 = QtWidgets.QWidget()
        self.page3.setObjectName("page3")
        self.photo3 = QtWidgets.QLabel(self.page3)
        self.photo3.setGeometry(QtCore.QRect(10, 10, 371, 291))
        self.photo3.setText("")
        self.photo3.setPixmap(QtGui.QPixmap("C:/Users/Bao/Desktop/bd/wallhaven-q2wker.png"))
        self.photo3.setScaledContents(True)
        self.photo3.setObjectName("photo3")
        self.Propmt.addWidget(self.page3)
        self.line2 = QtWidgets.QFrame(self.framework)
        self.line2.setGeometry(QtCore.QRect(30, 350, 741, 20))
        self.line2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line2.setLineWidth(1)
        self.line2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line2.setObjectName("line2")
        self.Title = QtWidgets.QLabel(self.framework)
        self.Title.setGeometry(QtCore.QRect(470, 50, 281, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.Title.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setAutoFillBackground(False)
        self.Title.setScaledContents(False)
        self.Title.setWordWrap(False)
        self.Title.setObjectName("Title")
        self.progressBar = QtWidgets.QProgressBar(self.framework)
        self.progressBar.setGeometry(QtCore.QRect(460, 280, 311, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.progressBar.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.progressBar.setFont(font)
        self.progressBar.setMouseTracking(False)
        self.progressBar.setProperty("value", 10)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progressBar.setObjectName("progressBar")
        self.bg = QtWidgets.QLabel(self.framework)
        self.bg.setGeometry(QtCore.QRect(0, 0, 781, 381))
        self.bg.setText("")
        self.bg.setPixmap(QtGui.QPixmap("C:/Users/Bao/Desktop/bd/wallhaven-4gxmpd.jpg"))
        self.bg.setScaledContents(True)
        self.bg.setObjectName("bg")
        self.Text = QtWidgets.QLabel(self.framework)
        self.Text.setGeometry(QtCore.QRect(570, 300, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setBold(True)
        font.setWeight(75)
        self.Text.setFont(font)
        self.Text.setObjectName("Text")
        self.label = QtWidgets.QLabel(self.framework)
        self.label.setGeometry(QtCore.QRect(730, 0, 51, 51))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/Bao/Downloads/FAUGET.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.bg.raise_()
        self.formLayoutWidget.raise_()
        self.line1.raise_()
        self.Propmt.raise_()
        self.line2.raise_()
        self.Title.raise_()
        self.progressBar.raise_()
        self.Text.raise_()
        self.label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionPlatform_version = QtWidgets.QAction(MainWindow)
        self.actionPlatform_version.setObjectName("actionPlatform_version")

        self.retranslateUi(MainWindow)
        self.Propmt.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Traffic Sign Detection Platform"))
        self.Input1.setText(_translate("MainWindow", "USERNAME"))
        self.usernameinput.setPlaceholderText(_translate("MainWindow", "Please enter your username"))
        self.Input2.setText(_translate("MainWindow", "PASSWORD"))
        self.passwordinput.setPlaceholderText(_translate("MainWindow", "Please enter your password"))
        self.loginbut.setText(_translate("MainWindow", "LOGIN"))
        self.registerbut.setText(_translate("MainWindow", "REGISTER"))
        self.comply.setText(_translate("MainWindow", "Comply with user regulations"))
        self.Title.setText(_translate("MainWindow", "Intelligent traffic sign recognition"))
        self.Text.setText(_translate("MainWindow", "Loading"))
        self.actionPlatform_version.setText(_translate("MainWindow", "Platform version"))
