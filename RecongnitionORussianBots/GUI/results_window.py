# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\HiTorus\Desktop\results_window.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ResultsWindow(object):
    def setupUi(self, ResultsWindow):
        ResultsWindow.setObjectName("ResultsWindow")
        ResultsWindow.resize(574, 434)
        self.centralwidget = QtWidgets.QWidget(ResultsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.resultsGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.resultsGroupBox.setGeometry(QtCore.QRect(10, 10, 551, 381))
        self.resultsGroupBox.setObjectName("resultsGroupBox")
        self.loadResultsButton = QtWidgets.QPushButton(self.resultsGroupBox)
        self.loadResultsButton.setGeometry(QtCore.QRect(9, 330, 75, 23))
        self.loadResultsButton.setObjectName("loadResultsButton")
        self.saveResultsButton = QtWidgets.QPushButton(self.resultsGroupBox)
        self.saveResultsButton.setGeometry(QtCore.QRect(99, 330, 75, 23))
        self.saveResultsButton.setObjectName("saveResultsButton")
        self.backButton = QtWidgets.QPushButton(self.resultsGroupBox)
        self.backButton.setGeometry(QtCore.QRect(466, 330, 75, 23))
        self.backButton.setObjectName("backButton")
        self.groupOneBox = QtWidgets.QTextEdit(self.resultsGroupBox)
        self.groupOneBox.setGeometry(QtCore.QRect(10, 60, 531, 111))
        self.groupOneBox.setObjectName("groupOneBox")
        self.groupTwoBox = QtWidgets.QTextEdit(self.resultsGroupBox)
        self.groupTwoBox.setGeometry(QtCore.QRect(10, 200, 531, 111))
        self.groupTwoBox.setObjectName("groupTwoBox")
        self.groupOneLabel = QtWidgets.QLabel(self.resultsGroupBox)
        self.groupOneLabel.setGeometry(QtCore.QRect(10, 35, 111, 20))
        self.groupOneLabel.setObjectName("groupOneLabel")
        self.groupTwoLabel = QtWidgets.QLabel(self.resultsGroupBox)
        self.groupTwoLabel.setGeometry(QtCore.QRect(10, 175, 43, 20))
        self.groupTwoLabel.setObjectName("groupTwoLabel")
        self.messageLabel = QtWidgets.QLabel(self.resultsGroupBox)
        self.messageLabel.setGeometry(QtCore.QRect(10, 20, 531, 16))
        self.messageLabel.setObjectName("messageLabel")
        self.showGroupOneSal = QtWidgets.QPushButton(self.resultsGroupBox)
        self.showGroupOneSal.setGeometry(QtCore.QRect(421, 36, 121, 21))
        self.showGroupOneSal.setObjectName("showGroupOneSal")
        self.showGroupTwoSal = QtWidgets.QPushButton(self.resultsGroupBox)
        self.showGroupTwoSal.setGeometry(QtCore.QRect(421, 176, 121, 21))
        self.showGroupTwoSal.setObjectName("showGroupTwoSal")
        ResultsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ResultsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 574, 21))
        self.menubar.setObjectName("menubar")
        ResultsWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ResultsWindow)
        self.statusbar.setObjectName("statusbar")
        ResultsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ResultsWindow)
        QtCore.QMetaObject.connectSlotsByName(ResultsWindow)

    def retranslateUi(self, ResultsWindow):
        _translate = QtCore.QCoreApplication.translate
        ResultsWindow.setWindowTitle(_translate("ResultsWindow", "Bot Recognition"))
        self.resultsGroupBox.setTitle(_translate("ResultsWindow", "Results"))
        self.loadResultsButton.setText(_translate("ResultsWindow", "Load"))
        self.saveResultsButton.setText(_translate("ResultsWindow", "Save"))
        self.backButton.setText(_translate("ResultsWindow", "Back"))
        self.groupOneLabel.setText(_translate("ResultsWindow", "Group 1"))
        self.groupTwoLabel.setText(_translate("ResultsWindow", "Group 2"))
        self.messageLabel.setText(_translate("ResultsWindow", "Data Split"))
        self.showGroupOneSal.setText(_translate("ResultsWindow", "Show Saliency Mapping"))
        self.showGroupTwoSal.setText(_translate("ResultsWindow", "Show Saliency Mapping"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ResultsWindow = QtWidgets.QMainWindow()
    ui = Ui_ResultsWindow()
    ui.setupUi(ResultsWindow)
    ResultsWindow.show()
    sys.exit(app.exec_())

