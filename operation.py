import os.path
import sys

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QGraphicsScene, QMessageBox, QTreeWidgetItem
from PyQt5.QtGui import *
from PyQt5 import QtGui, QtCore, QtWidgets, sip
import sysinterface as s
import Imgsedit,dialog_warning,Sql,usermodify,userdelete,usertopup,Imagegeneration
import random,cv2
import detect

class userrevise(QMainWindow,usermodify.Ui_modify):
    def __init__(self):
        super(userrevise,self).__init__()
        self.setupUi(self)
        self.Cancel_but.clicked.connect(self.Onlicked_close)
        self.reset_but.clicked.connect(self.Onlicked_clear)
        self.submit_but.clicked.connect(self.Onlicked_submit)


    def Onlicked_submit(self):
        if len(self.emailline.text()) == 0 or len(self.passwwordline.text()) == 0 or len(self.lineEdit.text()) == 0 or len(self.lineEdit_2.text()) == 0:
            return

        if str(self.lineEdit.text()) != str(self.lineEdit_2.text()):
            return

        if Sql.user_verify(email=self.emailline.text()):
            Sql.user_modify(self.lineEdit.text(),self.emailline.text())

    def Onlicked_clear(self):
        self.emailline.clear()
        self.passwwordline.clear()
        self.lineEdit.clear()
        self.lineEdit_2.clear()
    def Onlicked_close(self):
        self.Onlicked_clear()
        self.close()

#------------------------------------------------------------------------------------------
class imgswarning(QMainWindow,dialog_warning.Ui_caution):
    def __init__(self):
        super(imgswarning,self).__init__()
        self.setupUi(self)
#------------------------------------------------------------------------------------------

class userdelaccount(QMainWindow,userdelete.Ui_Form):
    def __init__(self):
        super(userdelaccount,self).__init__()
        self.setupUi(self)
        self.buttonBox.accepted.connect(self.deleteuser)
        self.buttonBox.rejected.connect(self.canceluser)

    def usersetting(self):
        self.currentnameline.setText(Sql.tmp_username)
        self.currenttypeline.setText(Sql.user_infor_tranfer(n=5))
    def deleteuser(self):
        Sql.user_delete()
        sys.exit()
        print("Yes")
    def canceluser(self):
        self.close()

#------------------------------------------------------------------------------------------
class usersystopup(QMainWindow,usertopup.Ui_Top):
    def __init__(self):
        super(usersystopup,self).__init__()
        self.setupUi(self)
        self.listWidget.itemClicked.connect(self.Onlicked_option)
        self.modifyusername_but.clicked.connect(self.Onlicked_setread)
        self.Okey_but.clicked.connect(self.changetype)

    def changetype(self):
        self.lineEdit.setReadOnly(True)
        self.passwordline.setReadOnly(True)
        if len(self.lineEdit.text()) != 0 and len(self.passwordline.text()) != 0:
            if int(self.listWidget.currentIndex().row()) % 2 == 0:
                Sql.user_update(int(self.listWidget.currentIndex().row()),self.lineEdit.text(),self.passwordline.text())
                self.close()





    def Onlicked_setread(self):
        self.lineEdit.setReadOnly(False)
        self.passwordline.setReadOnly(False)

    def userinforsetting(self):
        self.lineEdit.setText(Sql.tmp_username)
        self.passwordline.setText(Sql.tmp_password)

        self.codepath = "D:/QTproject/yolov5-master/" + Imagegeneration.imgsname
        print(self.codepath)

        self.codeimg = QtGui.QPixmap(self.codepath).scaled(self.label.width(),self.label.height())
        print(2)
        self.label.setPixmap(self.codeimg)
        self.label.update()

    def Onlicked_option(self,item):
        if int(self.listWidget.currentIndex().row()) % 2 == 0:
            self.memberline.setText(str(item.text()))
        else:
            self.memberline.clear()

#------------------------------------------------------------------------------------------
class usersyswindows(QMainWindow,s.Ui_Form):
    def __init__(self):
        super(usersyswindows,self).__init__()
        self.imgs = None
        self.setupUi(self)
        self.is_imgshow = False
        self.labeledimgs = ""
        self.currentimgsheight = None
        self.currentimgswidth = None
        self.Upload_but.clicked.connect(self.imgfromlocal)
        self.upbut.clicked.connect(self.Onclicked_upimgs)
        self.delete_but.clicked.connect(self.Onlicked_deleteimgs)
        self.downbut.clicked.connect(self.Onclicked_downimgs)
        self.infordict = dict()
        self.syswarn = imgswarning()
        self.sysdelete = userdelaccount()
        self.systopup = usersystopup()
        self.userrevisepass = userrevise()
        self.onlist = 1
        self.setscrollhet = 800
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(False)
        self.scrollAreaWidgetContents.setGeometry(0,0,208,self.setscrollhet)
        self.scrollAreaWidgetContents.update()
        self.topup_but.clicked.connect(self.Onlicked_Opentopup)
        self.clear_but.clicked.connect(self.Onlicked_clearimgs)
        self.edit_but.clicked.connect(self.Onlicked_movepages)
        self.detection_but.clicked.connect(self.Onlicked_detectionimgs)
        self.alter_but.clicked.connect(self.Onlicked_modifybut)
        self.confirm_but.clicked.connect(self.Onlicked_savepathimgs)
        self.usertools.currentChanged.connect(self.Changed_setting)
        self.changepass_but.clicked.connect(self.Onlicked_moveusermodify)
        self.Treetools.currentItemChanged.connect(self.Onlicked_items)
        self.deletaccount_but.clicked.connect(self.Onlicked_Openui)
        self.video_but.clicked.connect(self.Onlicked_video)
        self.imgsfilearea.clicked.connect(lambda p: self.displayimgs(self.imgsfilearea.objectName()))
        self.yolopath = "D:/QTproject/yolov5-master/runs/detect/"
        self.yolofile = ""
        self.yoloorder = 1
        self.plainTextEdit.setPlainText(self.yolopath)
        self.sysedit = Imgsedit.imgswindows()

    def Onlicked_video(self):
        detect.run(source=0)


    def Onlicked_Opentopup(self):
        self.systopup.userinforsetting()
        self.systopup.show()
    def Onlicked_Openui(self):
        self.sysdelete.usersetting()
        self.sysdelete.show()
    def Onlicked_moveusermodify(self):
        self.userrevisepass.show()

    def Onlicked_items(self):
        item = self.Treetools.currentItem().text()
        print(item)
    def Call_fun_update(self,i = None):
        root = QTreeWidgetItem(self.Treetools)
        root.setText(0, str(i))
    def Updated_treearea(self):
        for i in os.listdir("D:/"):
            self.Call_fun_update(i)

    def Changed_setting(self):
        self.plainTextEdit.setReadOnly(True)
        if int(self.usertools.currentIndex()) == 2:
            self.retimesline.setText(str(Sql.user_infor_tranfer(1)))
            self.usernameline.setText(str(Sql.user_infor_tranfer(2)))
            self.logintimeline.setText(str(Sql.user_infor_tranfer(3)))
            self.lcdNumber_2.display(str(Sql.user_infor_tranfer(4)))
            self.usertypeline.setText(str(Sql.user_infor_tranfer(5)))
        elif int(self.usertools.currentIndex()) == 0:
            self.Updated_treearea()



    def Onlicked_savepathimgs(self):
        stringtmp = self.plainTextEdit.toPlainText()
        if not os.path.exists(stringtmp):
            self.plainTextEdit.clear()
            self.syswarn.resettext(300)
            self.syswarn.show()
        self.plainTextEdit.setReadOnly(True)
    def Onlicked_modifybut(self):
        self.plainTextEdit.setReadOnly(False)
    def Onlicked_movepages(self):
        if self.is_imgshow:
            self.sysedit.editimgsname = self.labeledimgs
            self.sysedit.getimgsinfor(self.labeledimgs)

            self.sysedit.set_imgs()

            self.sysedit.show()

            self.showMinimized()
        else:
            self.syswarn.resettext(100)
            self.syswarn.show()


    def Verifyosfiles(self,sysfilename = None):
        if os.path.isfile(sysfilename):
            print("Yes exist")
            return True
        return False

    def Onlicked_detectionimgs(self):
        if self.labeledimgs == "":
            self.syswarn.resettext(100)
            self.syswarn.show()
            return
        if len(self.plainTextEdit.toPlainText()) == 0:
            self.syswarn.resettext(200)
            self.syswarn.show()
            return

        if int(Sql.user_infor_tranfer(1)) != 0:
            Sql.user_detecttimes()
            self.usertypeline.setText(str(Sql.user_infor_tranfer(5)))
            self.lcdNumber_2.display(str(Sql.user_infor_tranfer(1)))
            self.lcdNumber_2.update()
            self.retimesline.setText(str(Sql.user_infor_tranfer(4)))
            self.retimesline.update()

            if self.plainTextEdit.toPlainText() != self.yolopath:
                detect.run(source=self.labeledimgs,project=self.plainTextEdit.toPlainText())
            else:
                detect.run(source=self.labeledimgs)

            pos = len(list(self.labeledimgs.split("/")))
            self.yolofile = list(self.labeledimgs.split("/"))[pos - 1]


            if self.yoloorder == 1:
                print((self.yolopath + "exp" + "/" + self.yolofile))
                self.imgs = QtGui.QPixmap(self.yolopath + "exp" + "/" + self.yolofile).scaled(
                    self.modelshow.width(),
                    self.modelshow.height())
            else:
                print((self.yolopath + "exp" + str(self.yoloorder) + "/" + self.yolofile))

                self.imgs = QtGui.QPixmap(self.yolopath + "exp" + str(self.yoloorder) + "/" + self.yolofile).scaled(self.modelshow.width(),
                                                                                   self.modelshow.height())

            self.modelshow.setPixmap(self.imgs)
            self.modelshow.update()
            self.yoloorder += 1


        else:
            self.syswarn.resettext(400)
            self.syswarn.show()

    def Onlicked_clearimgs(self):
        if self.is_imgshow:
            self.imgshow.clear()
            self.imgshow.update()
            self.labeledimgs = ""
            self.is_imgshow = False
            return
    def Onlicked_changedictblock(self):
        for i in range(len(list(self.infordict.values()))):
            if list(self.infordict.values())[i] == self.labeledimgs:
                self.tmp = list(self.infordict.keys())[i]

                self.Onlicked_updatelednumber()

                print(self.tmp)
                self.Onlicked_deleteimgsblock(self.tmp)
                self.realupdate(i + 1)

                print(self.infordict)
                del self.infordict[list(self.infordict.keys())[i]]

                for i in range(len(list(self.infordict.keys()))):
                    if i != 0:
                        self.infordict["imgs_" + str(i + 1)] = self.infordict.pop(list(self.infordict.keys())[i])

    def Onlicked_deleteimgs(self):
        self.modelshow.clear()
        self.modelshow.update()
        if self.is_imgshow:
            self.imgshow.clear()
            self.imgshow.update()
            self.tmp = ""
            if self.labeledimgs == list(self.infordict.values())[0] and len(self.infordict) == 1:
                self.imgsfilearea.setIcon(QIcon())
                self.imgsfilearea.update()
                del self.infordict[list(self.infordict.keys())[0]]
                self.Onlicked_updatelednumber()
                self.imgsy = 10

            elif self.labeledimgs == list(self.infordict.values())[0] and len(self.infordict) >= 2:
                self.tmp = list(self.infordict.keys())[1]

                self.infordict['imgsfilearea'] = ""
                print(self.infordict)
                for i in range(len(self.infordict)):
                    if i >= 1:
                        self.infordict[list(self.infordict.keys())[i - 1]] = list(self.infordict.values())[i]

                print(self.infordict)
                self.Onlicked_updatelednumber()

                for i in range(self.onlist - 1):
                    if i >= 1:
                        self.imgs_k = self.findChild(QtWidgets.QPushButton, "imgs_" + str(i + 1))
                        print(i)
                        self.imgs_k.setIcon(QIcon(list(self.infordict.values())[i]))
                        self.imgs_k.setIconSize(QSize(181, 191))

                        print(i)
                        self.imgs_k.update()

                print("Okey")
                self.Onlicked_showimgsareatmp(list(self.infordict.values())[0])
                self.Onlicked_deleteimgsblock("imgs_" + str(self.onlist))
                self.infordict.popitem()
                self.onlist -= 1
                self.imgsy -= 170

            elif self.labeledimgs != list(self.infordict.values())[0] and self.labeledimgs != ("imgs_" + str(self.onlist)):
                index_pos = 0
                for n in range(len(self.infordict)):
                    if list(self.infordict.values())[n] == self.labeledimgs:
                        self.infordict[list(self.infordict.keys())[n]] = ""
                        index_pos = n
                        break
                print(self.infordict)


                for k in range(len(self.infordict) - 1):
                    if k >= index_pos:
                        print("k=",k)
                        self.infordict[list(self.infordict.keys())[k]] = list(self.infordict.values())[k + 1]

                self.Onlicked_updatelednumber()
                print(self.infordict)

                for i in range(self.onlist - 1):
                    if i >= index_pos:
                        self.imgs_k = self.findChild(QtWidgets.QPushButton, "imgs_" + str(i + 1))
                        print(i)
                        self.imgs_k.setIcon(QIcon(list(self.infordict.values())[i]))
                        self.imgs_k.setIconSize(QSize(181, 191))

                        print(i)
                        self.imgs_k.update()

                print("Okey")
                self.Onlicked_showimgsareatmp(list(self.infordict.values())[0])
                self.Onlicked_deleteimgsblock("imgs_" + str(self.onlist))
                self.infordict.popitem()
                self.onlist -= 1
                self.imgsy -= 170



            else:
                if list(self.infordict.keys())[len(list(self.infordict.keys())) - 1] == self.labeledimgs:
                    self.tmp = list(self.infordict.keys())[len(list(self.infordict.keys())) - 1]
                    self.Onlicked_deleteimgsblock(self.tmp)

                self.Onlicked_changedictblock()
                print(self.infordict)

            self.labeledimgs = ""
            self.is_imgshow = False
            return


    def Onlicked_showimgsareatmp(self,imgs = None):
        self.imgsfilearea.setIcon(QIcon(imgs))
        self.imgsfilearea.setIconSize(QSize(181, 191))
        self.imgsfilearea.update()
        print("display")

    def realupdate(self,moveint = 0):
        print("delete")
        for k in range(len(list(self.infordict.keys()))):
            if k >= moveint:
                self.tmphut = self.findChild(QtWidgets.QPushButton, "imgs_" + str(k + 1))
                self.imgsy -= 170
                print("delete")
                self.tmphut.setGeometry(QtCore.QRect(10, self.imgsy, 211, 161))
                self.tmphut.update()

    def Onlicked_deleteimgsblock(self,objname = None):
        self.hut = self.findChild(QtWidgets.QPushButton, objname)
        sip.delete(self.hut)


    def Onlicked_updatelednumber(self,a0 = 0):
        if a0 == 1:
            self.lcdNumber.display(self.lcdNumber.value() + 1)
        else:
            self.lcdNumber.display(self.lcdNumber.value() - 1)
        self.lcdNumber.update()

    def Onclicked_downimgs(self):
        if self.is_imgshow:
            if list(self.infordict.values())[len(list(self.infordict.values())) - 1] != self.labeledimgs:
                for i in range(len(list(self.infordict.values()))):
                    if list(self.infordict.values())[i] == self.labeledimgs:
                        if self.Verifyosfiles(self.labeledimgs):
                            self.imgs = QtGui.QPixmap(list(self.infordict.values())[i + 1]).scaled(self.imgshow.width(), self.imgshow.height())
                            self.imgshow.setPixmap(self.imgs)
                            self.imgshow.update()
                            self.labeledimgs = list(self.infordict.values())[i + 1]
                            self.sysedit.editimgsname = self.labeledimgs
                            self.sysedit.set_imgs()
                            break
    def Onclicked_upimgs(self):
        if self.is_imgshow:
            if list(self.infordict.values())[0] != self.labeledimgs:
                for i in range(len(list(self.infordict.values()))):
                    if list(self.infordict.values())[i] == self.labeledimgs:
                        if self.Verifyosfiles(self.labeledimgs):
                            self.imgs = QtGui.QPixmap(list(self.infordict.values())[i - 1]).scaled(self.imgshow.width(), self.imgshow.height())
                            self.imgshow.setPixmap(self.imgs)
                            self.imgshow.update()
                            self.labeledimgs = list(self.infordict.values())[i - 1]
                            self.sysedit.editimgsname = self.labeledimgs
                            self.sysedit.set_imgs()
                            break


    def displayimgs(self,obname = ''):
        print("clicked " + obname)
        self.filename = ""
        if len(self.infordict) == 0:
            return
        for i in self.infordict:
            if i == obname:
                self.filename = self.infordict[i]
                self.labeledimgs = self.infordict[i]
                break
        print(self.filename)
        self.imgs = QtGui.QPixmap(self.filename).scaled(self.imgshow.width(), self.imgshow.height())
        self.imgshow.setPixmap(self.imgs)
        self.imgshow.update()
        openimg = cv2.imread(self.filename)
        size = openimg.shape
        self.currentimgswidth = size[1]
        self.currentimgsheight = size[0]
        print(self.currentimgsheight,self.currentimgswidth)
        self.is_imgshow = True



    def imgfromlocal(self):
        self.imgname, self.imgtype = QFileDialog.getOpenFileName(self,"open img","","*.jpg;;*.png;;All Files(*)")
        self.imgs = QtGui.QPixmap(self.imgname).scaled(self.imgshow.width(),self.imgshow.height())

        if self.Verifyosfiles(self.imgname):
            if len(self.infordict) != 0:
                print("yes")
                self.createimgblock(objectname="imgs_" + str(len(self.infordict) + 1))
                self.imgsname.setIcon(QIcon(self.imgname))
                self.imgsname.setIconSize(QSize(181, 191))
                self.imgsname.update()


                self.imgsname.clicked.connect(lambda : self.displayimgs(self.imgsname.objectName()))

                self.imgshow.setPixmap(self.imgs)
                self.imgshow.update()
                self.is_imgshow = True
                self.labeledimgs = self.imgname

                self.Onlicked_updatelednumber(a0 = 1)

                self.infordict[self.imgsname.objectName()] = self.imgname

                self.setscrollhet += 200
                self.scrollAreaWidgetContents.setGeometry(0, 0, 208, self.setscrollhet)
                self.scrollAreaWidgetContents.update()
            else:
                print("yes2")
                self.imgshow.setPixmap(self.imgs)
                self.imgshow.update()
                self.Onlicked_updatelednumber(a0 = 1)

                self.Onlicked_showimgsareatmp(self.imgname)
                self.is_imgshow = True
                self.labeledimgs = self.imgname

                self.infordict[self.imgsfilearea.objectName()] = self.imgname






    def createimgblock(self, objectname = ""):
        print("in there!")
        self.onlist += 1
        imgsname = "imgs_" + str(self.onlist)
        setattr(self,imgsname, "Some value")
        self.imgsname = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        print(imgsname)

        self.imgsy += 170
        self.imgsname.setGeometry(QtCore.QRect(10, self.imgsy, 211, 161))
        self.imgsname.setText("")
        self.imgsname.setIconSize(QtCore.QSize(191, 181))
        self.imgsname.setDefault(False)
        self.imgsname.setFlat(True)
        self.imgsname.setObjectName(objectname)
        self.imgsname.show()
        self.scrollArea.update()
        self.scrollAreaWidgetContents.update()
        print(self.imgsy)
