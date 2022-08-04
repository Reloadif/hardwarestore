from PyQt5 import uic

from .AbstractWindow import AbstractPage

from UserInterface.LogInWindow import Ui_LogIn

import Modules.DbController as DbController
from Modules.SharedFunction import ShowErorMassageBox
 
class LogInWindow(AbstractPage):
    def __init__(self):
        super().__init__()

        self.userInterface = Ui_LogIn()
        self.userInterface.setupUi(self)

        self.setHandlers()
    
    def setHandlers(self):
        self.userInterface.LogInButton.clicked.connect(self.onClickLogInButton)
    
    def onClickLogInButton(self):
        username = self.userInterface.UsernameLineEdit.text()
        password = self.userInterface.PasswordLineEdit.text()

        try: DbController.ControllerDataBase = DbController.DbController(username, password)
        except(Exception): 
            ShowErorMassageBox("Данные для входа введены не верно!")
            return

        self.transition("AboutWindow")