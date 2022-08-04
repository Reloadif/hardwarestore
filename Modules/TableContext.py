from .StaticResource import *

# Класс для удобного обращения к таблицам базы данных

class TableContext():
    def __init__(self):
            self.tableName = "None"
            self.culumnHeader = None
            self.addingTemplate = None
            self.requestSelect = None
            self.requestDelete = None
            self.requestInsert = None

    def setNewContext(self, rawTableName):
        if(rawTableName == "Клиенты"):
            self.tableName = "customer"
            self.culumnHeader = customerColumnHeader
            self.addingTemplate = customerAddingTemplate
            self.requestSelect = customerRequestSelect
            self.requestDelete = customerRequestDelete
            self.requestInsert = customerRequestInsert
            return

        if(rawTableName == "Заказы"):
            self.tableName = "order"
            self.culumnHeader = orderColumnHeader
            self.addingTemplate = orderAddingTemplate
            self.requestSelect = orderRequestSelect
            self.requestDelete = orderRequestDelete
            self.requestInsert = orderRequestInsert
            return

        if(rawTableName == "Товары"):
            self.tableName = "product"
            self.culumnHeader = productColumnHeader
            self.addingTemplate = productAddingTemplate
            self.requestSelect = productRequestSelect
            self.requestDelete = productRequestDelete
            self.requestInsert = productRequestInsert
            return

        if(rawTableName == "Сотрудники"):
            self.tableName = "employee"
            self.culumnHeader = employeeColumnHeader
            self.addingTemplate = employeeAddingTemplate
            self.requestSelect = employeeRequestSelect
            self.requestDelete = employeeRequestDelete
            self.requestInsert = employeeRequestInsert
            return

        if(rawTableName == "Должности"):
            self.tableName = "post"
            self.culumnHeader = postColumnHeader
            self.addingTemplate = postAddingTemplate
            self.requestSelect = postRequestSelect
            self.requestDelete = postRequestDelete
            self.requestInsert = postRequestInsert
        
        if(rawTableName == "Отдел кадров - по должности"):
            self.tableName = "employee"
            self.requestSelect = hrDepartmentByPosition
        
        if(rawTableName == "Отчет о работе - по сотруднику"):
            self.tableName = "order"
            self.requestSelect = workReportByEmployee
        
        if(rawTableName == "История покупок - по клиенту"):
            self.tableName = "order"
            self.requestSelect = purchaseHistoryByCustomer

        if(rawTableName == "История покупок - по товару"):
            self.tableName = "order"
            self.requestSelect = purchaseHistoryByProduct