from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication

from ViewsModel.AbstractWindow import AbstractPage
from ViewsModel.LogInWindow import LogInWindow
from ViewsModel.AboutWindow import AboutWindow
from ViewsModel.ManageWindow import ManageWindow
from ViewsModel.ReportWindow import ReportWindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.stackedWidget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stackedWidget)

        self.listPages = {}
        self.isFirst = True

        self.register(LogInWindow(), "LogInWindow")
        self.register(AboutWindow(), "AboutWindow")
        self.register(ManageWindow(), "ManageWindow")
        self.register(ReportWindow(), "ReportWindow")
        self.transition("LogInWindow")

    def register(self, widget, name):
        self.listPages[name] = widget
        self.stackedWidget.addWidget(widget)
        if isinstance(widget, AbstractPage):
            widget.transitionSignal.connect(self.transition)
            widget.closeSignal.connect(self.onCloseHandler)

    @QtCore.pyqtSlot(str)
    def transition(self, name):
        if name in self.listPages:
            widget = self.listPages[name]
            if(name == "ManageWindow"):
                if self.isFirst:
                    widget.onChangedTableNameComboBox("Клиенты")
                    widget.SelectQuery()
                    self.isFirst = False
            self.stackedWidget.setCurrentWidget(widget)
            self.setWindowIcon(widget.windowIcon())
            self.setWindowTitle(widget.windowTitle())
            self.setMaximumWidth(widget.width())
            self.setMaximumHeight(widget.height())
    
    @QtCore.pyqtSlot()
    def onCloseHandler(self):
        self.close()

def main():
    app = QApplication([])
    w = MainWindow()
    w.show()
    app.exec()

if __name__ == '__main__':
    main()