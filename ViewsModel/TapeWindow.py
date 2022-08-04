from PyQt5 import uic
from PyQt5.QtWidgets import QLabel, QLineEdit

from .AbstractWindow import AbstractPage

from UserInterface.TapeWindow import Ui_Tape

from Modules.SharedFunction import ShowErorMassageBox

# Модель окна ленточной формы

class TapeWindow(AbstractPage):
    def __init__(self, tapeTemplate, dataContext):
        super().__init__()

        self.tapeTemplate = tapeTemplate
        self.dataContext = dataContext
        self.currentRow = 0
        self.maxRow = len(self.dataContext)

        self.userInterface = Ui_Tape()
        self.userInterface.setupUi(self)

        self.lineEdits = []

        self.setWidgetsOnLayout()
        self.setHandlers()
    
    def setWidgetsOnLayout(self):
        for i in range(len(self.tapeTemplate)):
            label = QLabel(str(self.tapeTemplate[i]))
            label.setStyleSheet("color: white;")
            self.userInterface.MainTapeLayout.addWidget(label)

            lineEdit = QLineEdit()
            lineEdit.setText(str(self.dataContext[self.currentRow][i+1]))
            lineEdit.setReadOnly(True)
            lineEdit.setStyleSheet("color: white;")
            self.userInterface.MainTapeLayout.addWidget(lineEdit)

            self.lineEdits.append(lineEdit)

    def setHandlers(self):
        self.userInterface.PreviousRecordButton.clicked.connect(self.onClickPreviousRecordButton)
        self.userInterface.NextRecordButton.clicked.connect(self.onClickNextRecordButton)

    def onClickPreviousRecordButton(self):
        if(self.currentRow == 0):
            ShowErorMassageBox("Назад больше перемещаться нельзя!")
            return

        self.currentRow -= 1
        for i in range(len(self.lineEdits)):
            self.lineEdits[i].setText(str(self.dataContext[self.currentRow][i+1]))

    def onClickNextRecordButton(self):
        if(self.currentRow == self.maxRow - 1):
            ShowErorMassageBox("Вперед больше перемещаться нельзя!")
            return

        self.currentRow += 1
        for i in range(len(self.lineEdits)):
            self.lineEdits[i].setText(str(self.dataContext[self.currentRow][i+1]))