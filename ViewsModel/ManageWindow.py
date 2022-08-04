from PyQt5 import uic
from PyQt5.QtWidgets import QInputDialog, QTableWidgetItem

from .AbstractWindow import AbstractPage
from .TapeWindow import TapeWindow
from .MatplotWindow import MatplotWindow

from UserInterface.ManageWindow import Ui_Manage

import Modules.DbController as DbController
from Modules.SharedFunction import ShowErorMassageBox

# Модель окна основной рабочей области со всеми запросами

class ManageWindow(AbstractPage):
    def __init__(self):
        super().__init__()

        self.userInterface = Ui_Manage()
        self.userInterface.setupUi(self)

        self.userInterface.ComposeBarGraphButton.hide()
        self.setHandlers()
    
    def setHandlers(self):
        self.userInterface.TableNameComboBox.currentTextChanged.connect(self.onChangedTableNameComboBox)

        self.userInterface.TapeFormButton.clicked.connect(self.onClickTapeFormButton)
        self.userInterface.AddRecordButton.clicked.connect(self.onClickAddRecordButton)
        self.userInterface.DeleteRecordButton.clicked.connect(self.onClickDeleteRecordButton)
        self.userInterface.SearchRecordButton.clicked.connect(self.onClickSearchRecordButton)
        self.userInterface.ComposeBarGraphButton.clicked.connect(self.onClickComposeBarGraphButton)
        self.userInterface.ComposeReportButton.clicked.connect(self.onClickComposeReportButton)
        self.userInterface.ReturnBackButton.clicked.connect(self.onClickReturnBackButton)

        self.userInterface.FirstCellButton.clicked.connect(self.onClickFirstCellButton)
        self.userInterface.LastCellButton.clicked.connect(self.onClickLastCellButton)
        self.userInterface.NextCellButton.clicked.connect(self.onClickNextCellButton)
        self.userInterface.PreviousCellButton.clicked.connect(self.onClickPreviousCellButton)
    
    def onChangedTableNameComboBox(self, text):
        if text == "Сотрудники":
            self.userInterface.ComposeBarGraphButton.show()
        else: self.userInterface.ComposeBarGraphButton.hide()

        DbController.ControllerDataBase.tableContext.setNewContext(text)
        self.SelectQuery()

    def onClickTapeFormButton(self):
        self.tapeWindow = TapeWindow(DbController.ControllerDataBase.tableContext.culumnHeader, DbController.ControllerDataBase.currentReply)
        self.tapeWindow.show()

    def onClickAddRecordButton(self):
        insertData, ok = QInputDialog.getText(self, 'Добавление записи',  DbController.ControllerDataBase.tableContext.addingTemplate)
        if ok:
            parameters = insertData.split(",")
            if len(parameters) == len(DbController.ControllerDataBase.tableContext.culumnHeader):
                DbController.ControllerDataBase.insert(parameters)
                self.SelectQuery()
            else: ShowErorMassageBox("Количетсво введенных данных не совпадает с шаблоном! Также обратите внимания что данные чередуются запятой!")
    
    def onClickDeleteRecordButton(self):
        currentRow = self.userInterface.TableOfRecordWidget.currentRow()
        if currentRow != -1:
            try:
                DbController.ControllerDataBase.delete(searchId(self.userInterface.TableOfRecordWidget.item(currentRow,0).text()))
                self.SelectQuery()
            except (Exception) as exception: 
                ShowErorMassageBox("Данное удаление невозможно!")
                print(exception)
        else: ShowErorMassageBox("Выберите строку для удаления!")
    
    def onClickSearchRecordButton(self):
        insertData, ok = QInputDialog.getText(self, 'Поиск записи',  DbController.ControllerDataBase.tableContext.addingTemplate)
        successfullSearch = []

        if ok: 
            parameters = insertData.split(",")
            if (len(parameters) != 0):
                for i in range(len(DbController.ControllerDataBase.currentReply)):
                    isFirst = True
                    for j in range(1, len(DbController.ControllerDataBase.currentReply[i])):
                        lower = str(DbController.ControllerDataBase.currentReply[i][j]).lower()
                        if(lower.find(parameters[0].lower()) != -1):
                            if isFirst:
                                successfullSearch.append(DbController.ControllerDataBase.currentReply[i])
                                isFirst = False

        if len(successfullSearch) != 0:
            self.userInterface.TableOfRecordWidget.setRowCount(len(successfullSearch))
            for i in range(self.userInterface.TableOfRecordWidget.rowCount()):
                for j in range(self.userInterface.TableOfRecordWidget.columnCount()):
                    self.userInterface.TableOfRecordWidget.setItem(i, j, QTableWidgetItem(str(successfullSearch[i][j+1])))

    def onClickComposeBarGraphButton(self):
        employeeRequestSelect = """SELECT idEmployee, fullname, telephone, post.salary FROM hardware_store.employee
                                    JOIN hardware_store.post ON post.idPost = fPost
                                    ORDER BY idEmployee"""
        DbController.ControllerDataBase.cursor.execute(employeeRequestSelect)
        
        self.barGraph = MatplotWindow(DbController.ControllerDataBase.cursor.fetchall())
        self.barGraph.draw()
        self.barGraph.show()

    def onClickComposeReportButton(self):
        self.transition("ReportWindow")

    def onClickReturnBackButton(self):
        self.transition("AboutWindow")

    def onClickFirstCellButton(self):
        self.userInterface.TableOfRecordWidget.setCurrentCell(0, 0)

    def onClickLastCellButton(self):
        self.userInterface.TableOfRecordWidget.setCurrentCell(self.userInterface.TableOfRecordWidget.rowCount() - 1, self.userInterface.TableOfRecordWidget.columnCount() - 1)

    def onClickNextCellButton(self):
        if (self.userInterface.TableOfRecordWidget.currentRow() == -1):
            self.onClickFirstCellButton()
            return
        
        row = self.userInterface.TableOfRecordWidget.rowCount() - 1
        column = self.userInterface.TableOfRecordWidget.columnCount() - 1
        currentRow = self.userInterface.TableOfRecordWidget.currentRow()
        currentColumn = self.userInterface.TableOfRecordWidget.currentColumn()
        if (currentRow < row):
            if(currentColumn < column):
                self.userInterface.TableOfRecordWidget.setCurrentCell(currentRow, currentColumn + 1)
                return
            else: self.userInterface.TableOfRecordWidget.setCurrentCell(currentRow + 1, 0)
        else:
            if(currentColumn < column):
                self.userInterface.TableOfRecordWidget.setCurrentCell(currentRow, currentColumn + 1)
                return

    def onClickPreviousCellButton(self):
        if self.userInterface.TableOfRecordWidget.currentRow() == -1:
            self.onClickFirstCellButton()
            return
        
        currentRow = self.userInterface.TableOfRecordWidget.currentRow()
        currentColumn = self.userInterface.TableOfRecordWidget.currentColumn()
        if (currentRow > 0):
            if(currentColumn >= 0):
                if(currentColumn == 0): self.userInterface.TableOfRecordWidget.setCurrentCell(currentRow - 1, self.userInterface.TableOfRecordWidget.columnCount() - 1)
                else: self.userInterface.TableOfRecordWidget.setCurrentCell(currentRow, currentColumn - 1)
                return
        else:
            if(currentColumn > 0): self.userInterface.TableOfRecordWidget.setCurrentCell(currentRow, currentColumn - 1)

    def SelectQuery(self):
        self.userInterface.TableOfRecordWidget.setSortingEnabled(False)

        DbController.ControllerDataBase.select()
        self.userInterface.TableOfRecordWidget.setColumnCount(len(DbController.ControllerDataBase.tableContext.culumnHeader))
        self.userInterface.TableOfRecordWidget.setHorizontalHeaderLabels(DbController.ControllerDataBase.tableContext.culumnHeader)

        self.userInterface.TableOfRecordWidget.setRowCount(len(DbController.ControllerDataBase.currentReply))
        for i in range(self.userInterface.TableOfRecordWidget.rowCount()):
            for j in range(self.userInterface.TableOfRecordWidget.columnCount()):
                self.userInterface.TableOfRecordWidget.setItem(i, j, QTableWidgetItem(str(DbController.ControllerDataBase.currentReply[i][j+1])))
        
        self.userInterface.TableOfRecordWidget.setSortingEnabled(True)

def searchId(name):
    data = DbController.ControllerDataBase.currentReply

    for record in data:
        if(str(record[1]).find(name) != -1):
            return record[0]