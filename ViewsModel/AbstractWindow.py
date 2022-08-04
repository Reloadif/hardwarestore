from PyQt5 import QtCore, QtWidgets

class AbstractPage(QtWidgets.QMainWindow):
    transitionSignal = QtCore.pyqtSignal(str)
    closeSignal = QtCore.pyqtSignal()

    def transition(self, pageName):
        self.transitionSignal.emit(pageName)
    
    def close(self):
        self.closeSignal.emit()