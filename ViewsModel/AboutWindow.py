from PyQt5 import uic

from .AbstractWindow import AbstractPage

from UserInterface.AboutWindow import Ui_About
 
class AboutWindow(AbstractPage):
    def __init__(self):
        super().__init__()

        self.userInterface = Ui_About()
        self.userInterface.setupUi(self)

        self.userInterface.AboutApplicationText.hide()
        self.hide = True

        self.setHandlers()
    
    def setHandlers(self):
        self.userInterface.OpenManageWindowButton.clicked.connect(self.onClickOpenManageWindowButton)
        self.userInterface.ReturnBackButton.clicked.connect(self.onClickReturnBackButton)
        self.userInterface.OpenAboutApplication.clicked.connect(self.onClickOpenAboutApplication)
        self.userInterface.CloseMainWindowButton.clicked.connect(self.onClickCloseMainWindowButton)
    
    def onClickOpenManageWindowButton(self):
        self.transition("ManageWindow")

    def onClickReturnBackButton(self):
        self.transition("LogInWindow")

    def onClickOpenAboutApplication(self):            
        if self.hide: self.userInterface.AboutApplicationText.show()
        else: self.userInterface.AboutApplicationText.hide()

        if self.hide == True: self.hide = False
        else: self.hide = True
    
    def onClickCloseMainWindowButton(self):
        self.close()