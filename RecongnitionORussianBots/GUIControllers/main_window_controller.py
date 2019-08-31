# from PyQt5 import QtCore, QtGui, QtWidgets
# from main_window_ui import Ui_MainWindow
# from results_window_ui import Ui_ResultsWindow
#
#
# class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
#     def __init__(self, parent=None):
#         super(MainWindow, self).__init__(parent)
#         self.setupUi(self)
#         self.showResultsButton.clicked.connect(self.openResultsWindow)
#         self.resultsWindow = None
#
#     @QtCore.pyqtSlot()
#     def openResultsWindow(self):
#         self.hide()
#         self.resultsWindow = ResultsWindow(self)
#         self.resultsWindow.show()