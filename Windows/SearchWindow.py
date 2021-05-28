# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SearchWindow123(2).ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QMainWindow, QTableWidget, QMessageBox
from PyQt5.QtCore import QDir, QSize
from Functions.FMImplementation import *
from Functions.SearchnAnalyze import *

class Ui_SearchWindow(object):

    def openMainWindow(self):
        from MainWindow import Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, SearchWindow):
        self.w = 545
        self.h = 520
        SearchWindow.setObjectName("SearchWindow")
        SearchWindow.resize(self.w, self.h)
        SearchWindow.setFixedSize(self.w, self.h)
        #SearchWindow.setFixedSize(SearchWindow.layout.sizeHint())

        SearchWindow.setStyleSheet("background: black;")
        self.centralwidget = QtWidgets.QWidget(SearchWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(150, 340, 241, 71))
        self.textEdit.setStyleSheet("color: white;")
        self.textEdit.setObjectName("textEdit")
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(self.w//2 - 150//2 - 241//2 - 150//2 + 6, 300, 150, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft Uighur")
        font.setPointSize(14)
        self.label3.setFont(font)
        self.label3.setStyleSheet("color: white;")
        self.label3.setObjectName("label3")
        self.SearchButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.SearchButton1.setGeometry(QtCore.QRect(self.w//2 - 121//2 + 241//2 + 121//2 + 10, 300, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft Uighur")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.SearchButton1.setFont(font)
        self.SearchButton1.setStyleSheet("background:blue;\n"
"border-color: rgb(4, 111, 2);\n"
"border-radius:10px;\n"
"font: bold 18px;\n"
"padding: 6px;\n"
"border-style: outset;\n"
"border-width: 0.3px;\n"
"border-color: rgb(0, 0, 127);\n"
"color: white;\n"
"\n"
"")
        self.SearchButton1.setObjectName("SearchButton1")
        self.textEdit1 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit1.setGeometry(QtCore.QRect(self.w//2 - 241//2, 300, 241, 21))
        self.textEdit1.setStyleSheet("color: white;")
        self.textEdit1.setObjectName("textEdit1")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(0, 40, self.w, 50))
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Gill Sans Ultra Bold")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label1.setFont(font)
        self.label1.setStyleSheet("color: white;")
        self.label1.setObjectName("label1")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(self.w//2 - 331//2, 100, 331, 121))
        font = QtGui.QFont()
        font.setFamily("Microsoft Uighur")
        font.setPointSize(16)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("color: white;")
        self.groupBox.setObjectName("groupBox")
        self.radioButton1 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton1.setGeometry(QtCore.QRect(10, 30, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Microsoft Uighur")
        font.setPointSize(14)
        self.radioButton1.setFont(font)
        self.radioButton1.setObjectName("radioButton1")
        self.radioButton3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton3.setGeometry(QtCore.QRect(10, 70, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft Uighur")
        font.setPointSize(14)
        self.radioButton3.setFont(font)
        self.radioButton3.setObjectName("radioButton3")
        self.radioButton2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton2.setGeometry(QtCore.QRect(10, 50, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft Uighur")
        font.setPointSize(14)
        self.radioButton2.setFont(font)
        self.radioButton2.setObjectName("radioButton2")
        self.radioButton4 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton4.setGeometry(QtCore.QRect(10, 90, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Microsoft Uighur")
        font.setPointSize(14)
        self.radioButton4.setFont(font)
        self.radioButton4.setObjectName("radioButton4")
        self.GoBack = QtWidgets.QPushButton(self.centralwidget)
        self.GoBack.setGeometry(QtCore.QRect(30, 430, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Microsoft Uighur")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.GoBack.setFont(font)
        self.GoBack.setStyleSheet("background:blue;\n"
"border-color: rgb(4, 111, 2);\n"
"border-radius:10px;\n"
"font: bold 18px;\n"
"padding: 6px;\n"
"border-style: outset;\n"
"border-width: 0.3px;\n"
"border-color: rgb(0, 0, 127);\n"
"color: white;\n"
"\n"
"")
        self.GoBack.setObjectName("GoBack")
        self.DataSetButton = QtWidgets.QPushButton(self.centralwidget)
        self.DataSetButton.setGeometry(QtCore.QRect(self.w//2 - 101//2 - 241//2 - 101//2 - 10, 260, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft Uighur")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.DataSetButton.setFont(font)
        self.DataSetButton.setStyleSheet("background:blue;\n"
"border-color: rgb(4, 111, 2);\n"
"border-radius:10px;\n"
"font: bold 18px;\n"
"padding: 6px;\n"
"border-style: outset;\n"
"border-width: 0.3px;\n"
"border-color: rgb(0, 0, 127);\n"
"color: white;\n"
"\n"
"")
        self.DataSetButton.setObjectName("DataSetButton")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(self.w//2 - 241//2, 260, 241, 21))
        self.textEdit_2.setStyleSheet("color: white;")
        self.textEdit_2.setObjectName("textEdit_2")
        SearchWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SearchWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, self.w, 21))
        self.menubar.setObjectName("menubar")
        SearchWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SearchWindow)
        self.statusbar.setObjectName("statusbar")
        SearchWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SearchWindow)
        QtCore.QMetaObject.connectSlotsByName(SearchWindow)

        #linking buttons
        #searchButton
        self.SearchButton1.clicked.connect(lambda: self.Search(self.textEdit1.toPlainText()))
        #Go back button
        self.GoBack.clicked.connect(self.openMainWindow)
        self.GoBack.clicked.connect(SearchWindow.close)
        #Choose dir button
        self.DataSetButton.clicked.connect(self.openDialogBox)
        #preventing text in choose data textedit
        self.textEdit_2.setDisabled(True)
        #clicking different radio buttons will reset the result box
        self.radioButton1.clicked.connect(self.clear_radiobuttons)
        self.radioButton2.clicked.connect(self.clear_radiobuttons)
        self.radioButton3.clicked.connect(self.clear_radiobuttons)
        self.radioButton4.clicked.connect(self.clear_radiobuttons)

    def retranslateUi(self, SearchWindow):
        _translate = QtCore.QCoreApplication.translate
        SearchWindow.setWindowTitle(_translate("SearchWindow", "SearchWindow"))
        self.textEdit.setHtml(_translate("SearchWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Results</p></body></html>"))
        self.label3.setText(_translate("SearchWindow", "Enter bases sequence:"))
        self.SearchButton1.setText(_translate("SearchWindow", "Search for location"))
        self.label1.setText(_translate("SearchWindow", "Search Engine"))
        self.groupBox.setTitle(_translate("SearchWindow", "Use a Search operation from:"))
        self.radioButton1.setText(_translate("SearchWindow", "FM Index"))
        self.radioButton3.setText(_translate("SearchWindow", "Linear Search"))
        self.radioButton2.setText(_translate("SearchWindow", "Suffix Tree"))
        self.radioButton4.setText(_translate("SearchWindow", "Hash Table"))
        self.GoBack.setText(_translate("SearchWindow", "Go back"))
        self.DataSetButton.setText(_translate("SearchWindow", "Choose a dataset"))

    def openDialogBox(self):
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        self.textEdit_2.setText(str(path))
        self.textEdit.clear()

    def clear_radiobuttons(self):
            self.textEdit.clear()


    def Search(self, query):
        if self.textEdit_2.toPlainText()=="":
                self.MessageBoxDirectoryError()
        elif self.textEdit1.toPlainText()=="":
                self.MessageBoxGeneError()
        elif self.radioButton1.isChecked()==False and self.radioButton2.isChecked()==False and self.radioButton3.isChecked()==False and self.radioButton4.isChecked()==False:
                self.MessageBoxDSError()
        else:
                if self.radioButton1.isChecked(): #Fm Index search
                        self.textEdit.setText(str(fm_index_find(self.textEdit_2.toPlainText(), query)))

                elif self.radioButton2.isChecked(): #Suffix Tree search
                        self.textEdit.setText(str(suffix_tree_find(self.textEdit_2.toPlainText(), query)))

                elif self.radioButton3.isChecked(): #Linear Search
                        self.textEdit.setText(str(linear_find(self.textEdit_2.toPlainText(), query)))

                elif self.radioButton4.isChecked(): #Hash Table
                        self.textEdit.setText(str(rabin_karp_find(self.textEdit_2.toPlainText(), query)))


    def MessageBoxDirectoryError(self):
        msg = QMessageBox()
        msg.setText("Please choose a data set!")
        msg.setWindowTitle("Error!")
        msg.setIcon(QMessageBox.Critical)
        msg.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(255, 255, 255)")
        msg.exec_()

    def MessageBoxGeneError(self):
        msg = QMessageBox()
        msg.setText("Cannot proceed until DNA sequence given!")
        msg.setWindowTitle("Error!")
        msg.setIcon(QMessageBox.Critical)
        msg.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(255, 255, 255)")
        msg.exec_()

    def MessageBoxDSError(self):
        msg = QMessageBox()
        msg.setText("Looks like you have forgotten to select which Searching operation to use!")
        msg.setWindowTitle("Error!")
        msg.setIcon(QMessageBox.Critical)
        msg.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(255, 255, 255)")
        msg.exec_()



if __name__ == "__main__":
    import sys
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QtWidgets.QApplication(sys.argv)
    app.setAttribute(QtCore.Qt.AA_DisableHighDpiScaling)
    SearchWindow = QtWidgets.QMainWindow()
    ui = Ui_SearchWindow()
    ui.setupUi(SearchWindow)
    SearchWindow.show()
    sys.exit(app.exec_())