from FRIDAYUI import Ui_MainWindow
from PyQt5 import QtCore , QtGui , QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt , QTimer , QDate
from PyQt5.uic import loadUiType
import os
import webbrowser 
import sys
from Body.Speak import Speak

print("Starting The Friday : Wait For Some Seconds")




class MainThread(QThread): 

    def __init__(self):
        super(MainThread,self).__init__()
     
    def run(self):
        from Friday2 import WakeupDetected
        WakeupDetected()
         

startExe = MainThread()


class Gui_Start(QMainWindow):

    def __init__(self): 
        super().__init__()

        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)

        self.gui.pushButton_start.clicked.connect(self.startTask)
        self.gui.pushButton_close.clicked.connect(self.close)
        
    def startTask(self):

        self.gui.label1 = QtGui.QMovie("GUIfiles/aibackgroundpicolo.gif")
        self.gui.Gif_1.setMovie(self.gui.label1)
        self.gui.label1.start()

        self.gui.label2 = QtGui.QMovie("GUIfiles//Earth_Template.gif")
        self.gui.Gif_2.setMovie(self.gui.label2)
        self.gui.label2.start()

        self.gui.label3 = QtGui.QMovie("GUIfiles//mic.gif")
        self.gui.Gif_3.setMovie(self.gui.label3)
        self.gui.label3.start()
        
        startExe.start()



GuiApp = QApplication(sys.argv)
friday_gui = Gui_Start()
friday_gui.show()
exit(GuiApp.exec_())



