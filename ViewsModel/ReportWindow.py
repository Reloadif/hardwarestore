from PyQt5 import uic, QtCore

from .AbstractWindow import AbstractPage

from UserInterface.ReportWindow import Ui_Report

import Modules.DbController as DbController
from Modules.SharedFunction import ShowInformationMassageBox

# Модель окна отчетов

class ReportWindow(AbstractPage):
    def __init__(self):
        super().__init__()

        self.userInterface = Ui_Report()
        self.userInterface.setupUi(self)

        self.userInterface.FilterNameComboBox.hide()
        self.setHandlers()
    
    def setHandlers(self):
        self.userInterface.AddNewReportButton.clicked.connect(self.onClickAddNewReportButton)
        self.userInterface.SpecialReportsCheckBox.stateChanged.connect(self.onStateChangedSpecialReportsCheckBox)
        self.userInterface.TableNameComboBox.currentTextChanged.connect(self.onTextChangedTableNameComboBox)
        self.userInterface.ReturnBackButton.clicked.connect(self.onClickReturnBackButton)

    def onClickAddNewReportButton(self):
        DbController.ControllerDataBase.tableContext.setNewContext(self.userInterface.TableNameComboBox.currentText())
        self.userInterface.ListOfReportWidget.clear()

        if(self.userInterface.SpecialReportsCheckBox.checkState() == QtCore.Qt.Checked):
            DbController.ControllerDataBase.customSelectWithParameter(self.userInterface.FilterNameComboBox.currentText())
        else: DbController.ControllerDataBase.select()

        if(len(DbController.ControllerDataBase.currentReply) != 0):
            for record in DbController.ControllerDataBase.currentReply:
                preparedItem = ""
                for i in range(1, len(record)):
                    if (i == len(record) - 1):
                        preparedItem += str(record[i])
                    else: preparedItem += (str(record[i]) + ", ")

                self.userInterface.ListOfReportWidget.addItem(preparedItem + '\n')

        else: ShowInformationMassageBox("По этому запросу отчет пуст!")

    def onStateChangedSpecialReportsCheckBox(self, state):
        if(state == QtCore.Qt.Checked):
            self.userInterface.TableNameComboBox.clear()
            self.userInterface.FilterNameComboBox.show()
            self.userInterface.TableNameComboBox.addItem("Отдел кадров - по должности")
            self.userInterface.TableNameComboBox.addItem("Отчет о работе - по сотруднику")
            self.userInterface.TableNameComboBox.addItem("История покупок - по товару")
            self.userInterface.TableNameComboBox.addItem("История покупок - по клиенту")
        else:
            self.userInterface.TableNameComboBox.clear()
            self.userInterface.FilterNameComboBox.hide()
            self.userInterface.TableNameComboBox.addItem("Клиенты")
            self.userInterface.TableNameComboBox.addItem("Заказы")
            self.userInterface.TableNameComboBox.addItem("Товары")
            self.userInterface.TableNameComboBox.addItem("Сотрудники")
            self.userInterface.TableNameComboBox.addItem("Должности")

    def onTextChangedTableNameComboBox(self, text):
        if(self.userInterface.SpecialReportsCheckBox.checkState() == QtCore.Qt.Checked):
            if(text == "Отдел кадров - по должности"):
                selectRequest = """SELECT postName FROM hardware_store.post
                                   ORDER BY idPost"""
                DbController.ControllerDataBase.cursor.execute(selectRequest)
                self.fillComboBox(DbController.ControllerDataBase.cursor.fetchall())
            elif(text == "Отчет о работе - по сотруднику"):
                selectRequest = """SELECT fullname FROM hardware_store.employee
                                   ORDER BY idEmployee"""
                DbController.ControllerDataBase.cursor.execute(selectRequest)
                self.fillComboBox(DbController.ControllerDataBase.cursor.fetchall())
            elif(text == "История покупок - по товару"):
                selectRequest = """SELECT name FROM hardware_store.product
                                   ORDER BY idProduct"""
                DbController.ControllerDataBase.cursor.execute(selectRequest)
                self.fillComboBox(DbController.ControllerDataBase.cursor.fetchall())
            elif(text == "История покупок - по клиенту"):
                selectRequest = """SELECT fullname FROM hardware_store.customer
                                   ORDER BY idCustomer"""
                DbController.ControllerDataBase.cursor.execute(selectRequest)
                self.fillComboBox(DbController.ControllerDataBase.cursor.fetchall())

    def onClickReturnBackButton(self):
        self.transition("ManageWindow")
    
    def fillComboBox(self, fillText):
        self.userInterface.FilterNameComboBox.clear()
        for item in fillText:
            self.userInterface.FilterNameComboBox.addItem(str(item[0]))