from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QGraphicsScene, QMessageBox
from PyQt5.QtGui import *
from PyQt5 import QtGui, QtCore, QtWidgets, sip

import Automaticpreprocessing
import Sql,Automaticpreprocessing as auto
import edit
import cv2 as cv
import os
import numpy as np

Automatically_generate_number_of_pictures = 0
class imgswindows(QMainWindow,edit.Ui_editimgsform):
    def __init__(self):
        super(imgswindows,self).__init__()
        self.setupUi(self)
        self.editimgsname = ""
        self.editimgsheight = None
        self.editimgswidth = None
        self.copyfilename = None
        self.loadimgspath = ""
        self.prosavedname = "pro"
        self.savedfiletypes = ".jpg"
        self.pix = ""
        self.imgsN = 0
        self.savedname = "O"
        self.savedfile = 0
        self.exit_but.clicked.connect(self.Onlicked_exit)
        self.profilename = None
        self.check_show.stateChanged.connect(self.Onlicked_showimgs)
        self.setting1.valueChanged.connect(self.Onlicked_updatevalue)
        self.confirm_but2.clicked.connect(self.erodingimgs)
        self.confirm_but.clicked.connect(self.smoothimgs)
        self.Updatecombox()
        self.recover.clicked.connect(self.recoverimgs)
        self.saveimgs.clicked.connect(self.saveimgsfile)
        self.dilatingSlider.valueChanged.connect(self.Onlicked_updatevalue_set2)
        self.confirm_but3.clicked.connect(self.dilationimgs)
        self.toolsarea.currentChanged.connect(self.Updateimgssitepage)
        self.revise_but.clicked.connect(self.modifylines)
        self.saveset_but.clicked.connect(self.savelinesset)
        self.confirmbut.clicked.connect(self.Onlicked_autoimgs)
        self.confirm_pressed.clicked.connect(self.Onlicked_setread)
        self.tools.clicked.connect(self.Onlicked_change)
        self.cleanbut.clicked.connect(self.Onlicked_initoption)
        self.effectnumber = 0
        self.effectnumberlist = []
        self.commonfiletype = ".jpg/.png/.jpeg"
        self.himgsname = None


    def Onlicked_initoption(self):
        self.check1.setChecked(False)
        self.check2.setChecked(False)
        self.check3.setChecked(False)
        self.check4.setChecked(False)
        self.check5.setChecked(False)
        self.numberofimgs.setValue(0)

    def Onlicked_change(self):
        self.pathframe.setReadOnly(False)
    def Onlicked_setread(self):
        self.pathframe.setReadOnly(True)

    def Checked_isanytrue(self):
        n = 0
        if len(self.effectnumberlist) != 0:
            self.effectnumberlist.clear()

        for i in range(5):
            box = self.findChild(QtWidgets.QCheckBox,("check"+str(i + 1)))
            if box.isChecked():
                self.effectnumberlist.append(i + 1)
                n += 1
        if n == 0:
            return True
        self.effectnumber = n
        return False
    def Onlicked_autoimgs(self):
        global Automatically_generate_number_of_pictures
        if len(self.pathframe.toPlainText()) == 0:
            print("No path")
            return

        if self.Checked_isanytrue():
            print("No selected")
            return

        Automatically_generate_number_of_pictures = int(self.numberofimgs.text())
        if Automatically_generate_number_of_pictures == 0:
            print("number is 0")
            return

        if os.path.isdir(str(self.pathframe.toPlainText())):
            Automaticpreprocessing.filepath = self.editimgsname
            Automaticpreprocessing.savepath = self.pathframe.toPlainText()
            Automaticpreprocessing.Quantitymeasurement(Automatically_generate_number_of_pictures,int(self.effectnumber))
            for i in range(self.effectnumber):
                Automaticpreprocessing.main(self.effectnumberlist[i])

            print("Finished")
        else:
            self.pathframe.setReadOnly(False)
            self.pathframe.clear()
            self.pathframe.setReadOnly(True)


    def locklines(self):
        self.prosavedname = "pro"
        self.savedfiletypes = ".jpg"
        self.savedname = "O"
        self.filetypeline.setReadOnly(True)
        self.savenameline.setReadOnly(True)
        self.originalnameline.setReadOnly(True)

    def savelinesset(self):

        if len(self.savenameline.text()) <= 10 and len(self.originalnameline.text()) <= 10 and self.filetypeline.text() in list(self.commonfiletype.split('/')):
            self.prosavedname = str(self.savenameline.text())
            self.savedname = str(self.originalnameline.text())
            self.savedfiletypes = str(self.filetypeline.text())
            self.savenameline.setReadOnly(True)
            self.filetypeline.setReadOnly(True)
            self.originalnameline.setReadOnly(True)
        else:
            self.locklines()


    def modifylines(self):
        self.savenameline.setReadOnly(False)
        self.filetypeline.setReadOnly(False)
        self.originalnameline.setReadOnly(False)

    def getimgsinfor(self,copyfile = None):
        self.copyfilename = copyfile
        print(self.copyfilename)
    def getinitimgsname(self):
        return list(self.editimgsname.split('/'))[len(list(self.editimgsname.split('/'))) - 1]
    def Updateimgssitepage(self):
        if int(self.toolsarea.currentIndex()) == 1:
            self.UpdateHistoricalimgs()
            print("Heeloo")
            self.nameofimg = self.getinitimgsname()
            self.imgnameline.setText(self.nameofimg)
            self.imgnameline.update()
            self.pathline.setText(self.loadimgspath)
            self.pathline.update()

            self.tmpimg = cv.imread(self.copyfilename)
            self.h , self.w = self.tmpimg.shape[:2]

            self.resolutionline.setText(str(self.h) + "x" + str(self.w))
            self.resolutionline.update()

            self.heightline.setText(str(self.h))
            self.heightline.update()
            self.widthline.setText(str(self.w))
            self.widthline.update()

            self.savenameline.setText(self.prosavedname)
            self.savenameline.update()

            self.filetypeline.setText(self.savedfiletypes)

            self.filetypeline.update()

            self.originalnameline.setText(self.savedname)
            self.originalnameline.update()
        elif int(self.toolsarea.currentIndex()) == 2:
            if Sql.user_isstandarduser():
                self.ad_dock.setEnabled(False)
                print("None")


    def UpdateHistoricalimgs(self):
        self.listWidget.clear()
        self.lcdNumber_3.display(str(0))
        for i in os.listdir(self.loadimgspath):
            tmptype = '.' + i.split(".")[1]
            if tmptype in list(self.commonfiletype.split('/')):
                self.listWidget.addItem(str(i))
                self.imgsN += 1
                self.lcdNumber_3.display(self.imgsN)
                self.lcdNumber_3.update()
    def dilationimgs(self):
        self.processedimgs = self.saveinitimgs()
        self.imgsread = cv.imread(self.processedimgs)
        self.kelement = np.ones((self.dilatingSlider.value(),self.dilatingSlider.value()),np.uint8)
        self.dilation_dst = cv.dilate(self.imgsread,self.kelement,iterations=1)
        self.saveproimgs(path=self.loadimgspath, n=self.savedfile - 1, photo=self.dilation_dst)
        self.Update_imgsarea(filename=self.proimgsname)
        print("working!")


    def Onlicked_updatevalue_set2(self):
        self.lcdNumber_2.display(int(self.dilatingSlider.value()))
        self.lcdNumber_2.update()
    def saveimgsfile(self):
        print("saved")

    def recoverimgs(self):
        self.removeproimgsfromos(imganame=self.prosavedname,path=self.loadimgspath)
        self.removeproimgsfromos(imganame=self.savedname, path=self.loadimgspath)
        self.Update_imgsarea(filename=self.editimgsname)
        self.savedfile = 0



    def smoothimgs(self):
        self.processedimgs = self.saveinitimgs()
        self.imgsread = cv.imread(self.processedimgs)
        print(self.comboBox.currentText())

        self.element2 = int(self.spinBox.value())
        if self.element2 % 2 == 0:
            self.element2 = self.element2 + 1
        if int(self.comboBox.currentIndex()) == 0:
            self.smooth_dst = cv.GaussianBlur(self.imgsread,(self.element2,self.element2),0)
            self.saveproimgs(path=self.loadimgspath, n=self.savedfile, photo=self.smooth_dst)
            self.Update_imgsarea(filename=self.proimgsname)
            print("working!")
        elif int(self.comboBox.currentIndex()) == 1:
            if self.element2 == 1:
                self.element2 = 3
            self.median_dst = cv.medianBlur(self.imgsread,self.element2)
            self.saveproimgs(path=self.loadimgspath, n=self.savedfile - 1, photo=self.median_dst)
            self.Update_imgsarea(filename=self.proimgsname)
            print("Median")
        else:
            self.bilateral_dst = cv.bilateralFilter(self.imgsread,self.element2,int(self.element2 * 2),int(self.element2 / 2))
            self.saveproimgs(path=self.loadimgspath, n=self.savedfile - 1, photo=self.bilateral_dst)
            self.Update_imgsarea(filename=self.proimgsname)
            print("Bilateral")
    def showcombox(self):
        print(self.comboBox.currentText())

    def Updatecombox(self):
        self.comboBox.addItem("Gaussian")
        self.comboBox.addItem("Median")
        self.comboBox.addItem("Bilateral")
        self.comboBox.update()
        self.comboBox.currentTextChanged.connect(self.showcombox)

    def verifysystemimgs(self,path = None):
        tmplist = []
        for i in os.listdir(path):
            if i[:len(i) - 5] == self.prosavedname:
                tmplist.append(i)

        if len(tmplist) == 0:
            return None

        if len(tmplist) == 1:
            return tmplist[0]

        for j in range(len(tmplist)):
            for k in range(len(tmplist)):
                if int(tmplist[j].split(".")[0][3]) > int(tmplist[k].split(".")[0][3]):
                    tmplist[j],tmplist[k] = tmplist[k],tmplist[j]

        return tmplist[len(tmplist) - 1]


    def savetoos(self,savednames = None, number = None,imgspath = None,path = None):
        self.show_imgs = cv.imread(imgspath)
        cv.imwrite(path + savednames + str(number) + self.savedfiletypes, self.show_imgs)
    def saveinitimgs(self):
        if self.savedfile != 0:
            for i in range(self.savedfile):
                if os.path.isfile(self.loadimgspath + self.savedname + str(i) + self.savedfiletypes):
                    self.savetoos(savednames=self.savedname,number=self.savedfile,imgspath=self.editimgsname,path=self.loadimgspath)
                    self.Update_imgsarea(filename=self.loadimgspath + self.savedname + str(self.savedfile) + self.savedfiletypes)

        else:
            self.removeproimgsfromos(imganame=self.prosavedname,path=self.loadimgspath)
            self.removeproimgsfromos(imganame=self.savedname, path=self.loadimgspath)
            #self.removeimgsfromos(self.savedname, self.savedfile, self.loadimgspath)
            self.savetoos(savednames=self.savedname, number=self.savedfile, imgspath=self.editimgsname,path=self.loadimgspath)
            #save the orginal images
            self.Update_imgsarea(filename=self.loadimgspath + self.savedname + str(self.savedfile) + self.savedfiletypes)



        copyfilename = self.loadimgspath + self.savedname + str(self.savedfile) + self.savedfiletypes
        copyimgs = self.verifysystemimgs(path=self.loadimgspath)
        self.savedfile = self.savedfile + 1
        if copyimgs == None:
            print(copyfilename)
            return copyfilename

        print(copyimgs)
        return self.loadimgspath + copyimgs




    def removeproimgsfromos(self,imganame = None,path = None):
        tmpfile = path + imganame
        for i in os.listdir(path):
            mkl = True
            for j in range(len(i) - 5):
                if imganame[j] != i[j]:
                    mkl = False
                    break
            if mkl:
                os.remove(tmpfile + i[j + 1] + self.savedfiletypes)
                print("remove success")





    def saveproimgs(self,path = None,n = 0,photo = None):
        self.proimgsname = path + self.prosavedname + str(n) + self.savedfiletypes
        print("working!")
        print(self.proimgsname)
        cv.imwrite(self.proimgsname, photo)

    def erodingimgs(self):
        self.processedimgs = self.saveinitimgs()

        print("working!123123")

        if os.path.isfile(self.editimgsname):
            self.imgsread = cv.imread(self.processedimgs)
            self.element = np.ones((self.setting1.value(), self.setting1.value()), np.uint8)
            self.erosion_dst = cv.erode(self.imgsread,self.element)

            self.saveproimgs(path=self.loadimgspath,n=self.savedfile - 1,photo=self.erosion_dst)
            self.Update_imgsarea(filename=self.proimgsname)
            print("working!")
        
        
        





    def Onlicked_updatevalue(self):
        self.lcdNumber.display(self.setting1.value())
        self.lcdNumber.update()
        print(self.setting1.value())
    def Onlicked_showimgs(self):
        if self.check_show.isChecked():
            self.pix = QtGui.QPixmap(self.editimgsname).scaled(self.originalarea.width(), self.originalarea.height())
            self.originalarea.setPixmap(self.pix)
            self.originalarea.update()
            self.originalarea.show()
            print("show")
        else:
            self.originalarea.hide()
    def set_imgs(self):
        if len(self.loadimgspath) > 1:
            self.loadimgspath = ""

        print(self.editimgsname)

        if self.editimgsname != "":
            self.Update_imgsarea(filename=self.editimgsname)
            self.tmp = list(self.editimgsname.split('/'))

            for i in range(len(self.tmp) - 1):
                self.loadimgspath = self.loadimgspath + self.tmp[i] + '/'
            print(self.loadimgspath)

    def Update_imgsarea(self,filename = None):
        self.profilename = filename
        self.pix = QtGui.QPixmap(filename).scaled(self.label_2.width(), self.label_2.height())
        self.label_2.setPixmap(self.pix)
        self.label_2.update()
    def Onlicked_exit(self):
        self.close()






