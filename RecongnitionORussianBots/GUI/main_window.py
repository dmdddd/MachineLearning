# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\HiTorus\Desktop\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainApplicationWindow(object):
    def setupUi(self, MainApplicationWindow):
        MainApplicationWindow.setObjectName("MainApplicationWindow")
        MainApplicationWindow.resize(431, 480)
        self.centralwidget = QtWidgets.QWidget(MainApplicationWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.modelGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.modelGroupBox.setGeometry(QtCore.QRect(10, 10, 411, 61))
        self.modelGroupBox.setObjectName("modelGroupBox")
        self.loadModelButton = QtWidgets.QPushButton(self.modelGroupBox)
        self.loadModelButton.setGeometry(QtCore.QRect(100, 19, 75, 25))
        self.loadModelButton.setObjectName("loadModelButton")
        self.createModelButton = QtWidgets.QPushButton(self.modelGroupBox)
        self.createModelButton.setGeometry(QtCore.QRect(240, 19, 75, 25))
        self.createModelButton.setObjectName("createModelButton")
        self.datasetGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.datasetGroupBox.setGeometry(QtCore.QRect(10, 73, 411, 58))
        self.datasetGroupBox.setObjectName("datasetGroupBox")
        self.browseDatasetButton = QtWidgets.QPushButton(self.datasetGroupBox)
        self.browseDatasetButton.setGeometry(QtCore.QRect(310, 23, 61, 21))
        self.browseDatasetButton.setObjectName("browseDatasetButton")
        self.datasetLineEdit = QtWidgets.QLineEdit(self.datasetGroupBox)
        self.datasetLineEdit.setGeometry(QtCore.QRect(40, 23, 261, 20))
        self.datasetLineEdit.setText("")
        self.datasetLineEdit.setObjectName("datasetLineEdit")
        self.classificationSummaryGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.classificationSummaryGroupBox.setGeometry(QtCore.QRect(10, 273, 411, 171))
        self.classificationSummaryGroupBox.setObjectName("classificationSummaryGroupBox")
        self.classificationSummaryTextEdit = QtWidgets.QTextEdit(self.classificationSummaryGroupBox)
        self.classificationSummaryTextEdit.setGeometry(QtCore.QRect(20, 20, 371, 141))
        self.classificationSummaryTextEdit.setObjectName("classificationSummaryTextEdit")
        self.embeddingGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.embeddingGroupBox.setGeometry(QtCore.QRect(10, 134, 411, 98))
        self.embeddingGroupBox.setObjectName("embeddingGroupBox")
        self.embeddingModelLineEdit = QtWidgets.QLineEdit(self.embeddingGroupBox)
        self.embeddingModelLineEdit.setGeometry(QtCore.QRect(40, 19, 261, 20))
        self.embeddingModelLineEdit.setText("")
        self.embeddingModelLineEdit.setObjectName("embeddingModelLineEdit")
        self.embeddingModelBrowseButton = QtWidgets.QPushButton(self.embeddingGroupBox)
        self.embeddingModelBrowseButton.setGeometry(QtCore.QRect(310, 19, 61, 21))
        self.embeddingModelBrowseButton.setObjectName("embeddingModelBrowseButton")
        self.vectorSizeLabel = QtWidgets.QLabel(self.embeddingGroupBox)
        self.vectorSizeLabel.setGeometry(QtCore.QRect(41, 56, 71, 16))
        self.vectorSizeLabel.setObjectName("vectorSizeLabel")
        self.vectorSizeSpinBox = QtWidgets.QDoubleSpinBox(self.embeddingGroupBox)
        self.vectorSizeSpinBox.setGeometry(QtCore.QRect(111, 56, 62, 22))
        self.vectorSizeSpinBox.setDecimals(0)
        self.vectorSizeSpinBox.setMinimum(1.0)
        self.vectorSizeSpinBox.setMaximum(9999.0)
        self.vectorSizeSpinBox.setProperty("value", 300.0)
        self.vectorSizeSpinBox.setObjectName("vectorSizeSpinBox")
        self.showResultsButton = QtWidgets.QPushButton(self.centralwidget)
        self.showResultsButton.setEnabled(True)
        self.showResultsButton.setGeometry(QtCore.QRect(260, 239, 85, 31))
        self.showResultsButton.setObjectName("showResultsButton")
        self.classifyButton = QtWidgets.QPushButton(self.centralwidget)
        self.classifyButton.setGeometry(QtCore.QRect(100, 239, 91, 31))
        self.classifyButton.setObjectName("classifyButton")
        MainApplicationWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainApplicationWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 431, 21))
        self.menubar.setObjectName("menubar")
        MainApplicationWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainApplicationWindow)
        self.statusbar.setObjectName("statusbar")
        MainApplicationWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainApplicationWindow)
        QtCore.QMetaObject.connectSlotsByName(MainApplicationWindow)

    def retranslateUi(self, MainApplicationWindow):
        _translate = QtCore.QCoreApplication.translate
        MainApplicationWindow.setWindowTitle(_translate("MainApplicationWindow", "Bot Recognition"))
        self.modelGroupBox.setTitle(_translate("MainApplicationWindow", "Classification Model"))
        self.loadModelButton.setText(_translate("MainApplicationWindow", "Load model"))
        self.createModelButton.setText(_translate("MainApplicationWindow", "Create new"))
        self.datasetGroupBox.setTitle(_translate("MainApplicationWindow", "Dataset"))
        self.browseDatasetButton.setText(_translate("MainApplicationWindow", "Browse"))
        self.classificationSummaryGroupBox.setTitle(_translate("MainApplicationWindow", "Classification Summary"))
        self.embeddingGroupBox.setTitle(_translate("MainApplicationWindow", "Embedding Model"))
        self.embeddingModelBrowseButton.setText(_translate("MainApplicationWindow", "Browse"))
        self.vectorSizeLabel.setText(_translate("MainApplicationWindow", "Vector size"))
        self.showResultsButton.setText(_translate("MainApplicationWindow", "Show results"))
        self.classifyButton.setText(_translate("MainApplicationWindow", "Classify"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainApplicationWindow = QtWidgets.QMainWindow()
    ui = Ui_MainApplicationWindow()
    ui.setupUi(MainApplicationWindow)
    MainApplicationWindow.show()
    sys.exit(app.exec_())

