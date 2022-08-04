# Клиенты
customerColumnHeader = ["ФИО", "Адрес", "Номер телефона"]
customerAddingTemplate = "Введите запись в формате: ФИО, Адрес, Номер телефона (+7(000)000-00-00)"

customerRequestSelect = """SELECT * FROM customer ORDER BY idCustomer"""

customerRequestDelete = """DELETE from customer where idCustomer = %s"""

customerRequestInsert = """INSERT into customer (fullname, address, telephone) VALUES (%s,%s,%s)"""

# Заказы
orderColumnHeader = ["Заказчик", "Сотрудник", "Товар", "Дата заказа", "Статус заказа"]
orderAddingTemplate = "Введите запись в формате: Заказчик, Сотрудник, Товар, Дата заказа, Статус заказа"

orderRequestSelect = """SELECT idOrder, customer.fullname, employee.fullname, product.name, orderDate, orderStatus FROM hardware_store.order
                        JOIN hardware_store.customer ON customer.idCustomer = fCustomer
                        JOIN hardware_store.employee ON employee.idEmployee = fEmployee
                        JOIN hardware_store.product ON product.idProduct = fProduct
                        ORDER BY idOrder"""

orderRequestDelete = """DELETE from hardware_store.order where idOrder = %s"""

orderRequestInsert = """INSERT into order (fCustomer, fEmployee, fProduct, orderDate, orderStatus) VALUES (%s,%s,%s,%s,%s)"""

# Товары
productColumnHeader = ["Наименование", "Цена", "Описание"]
productAddingTemplate = "Введите запись в формате: Наименование, Цена, Описание"

productRequestSelect = "SELECT * from product ORDER BY idProduct"

productRequestDelete = """DELETE from product where idProduct = %s"""

productRequestInsert = """INSERT into product (name, price, description) VALUES (%s,%s,%s)"""

# Сотрудники
employeeColumnHeader = ["ФИО", "Номер телефона", "Должность"]
employeeAddingTemplate = "Введите запись в формате: ФИО, Номер телефона, Должность"

employeeRequestSelect = """SELECT idEmployee, fullname, telephone, post.postName FROM hardware_store.employee
                            JOIN hardware_store.post ON post.idPost = fPost
                            ORDER BY idEmployee"""

employeeRequestDelete = """DELETE from employee where idEmployee = %s"""

employeeRequestInsert = """INSERT into employee (fullname, telephone, fPost) VALUES (%s,%s,%s)"""

# Должности
postColumnHeader = ["Наименование", "Зарплата", "Обязаности"]
postAddingTemplate = "Введите запись в формате: Наименование, Зарплата, Обязаности"

postRequestSelect = """SELECT * FROM post ORDER BY idPost"""

postRequestDelete = """DELETE from post where idPost = %s"""

postRequestInsert = """INSERT into post (postName, salary, responsibilities) VALUES (%s,%s,%s)"""

# Отчеты

hrDepartmentByPosition = """SELECT idEmployee, fullname, telephone, post.postName FROM hardware_store.employee
                            JOIN hardware_store.post ON post.idPost = fPost
                            WHERE post.postName = %s
                            ORDER BY idEmployee"""

workReportByEmployee = """SELECT idOrder, customer.fullname, employee.fullname, product.name, orderDate, orderStatus FROM hardware_store.order
                          JOIN hardware_store.customer ON customer.idCustomer = fCustomer
                          JOIN hardware_store.employee ON employee.idEmployee = fEmployee
                          JOIN hardware_store.product ON product.idProduct = fProduct
                          WHERE employee.fullname = %s
                          ORDER BY idOrder"""

purchaseHistoryByCustomer = """SELECT idOrder, customer.fullname, employee.fullname, product.name, orderDate, orderStatus FROM hardware_store.order
                               JOIN hardware_store.customer ON customer.idCustomer = fCustomer
                               JOIN hardware_store.employee ON employee.idEmployee = fEmployee
                               JOIN hardware_store.product ON product.idProduct = fProduct
                               WHERE customer.fullname = %s
                               ORDER BY idOrder"""

purchaseHistoryByProduct = """SELECT idOrder, customer.fullname, employee.fullname, product.name, orderDate, orderStatus FROM hardware_store.order
                               JOIN hardware_store.customer ON customer.idCustomer = fCustomer
                               JOIN hardware_store.employee ON employee.idEmployee = fEmployee
                               JOIN hardware_store.product ON product.idProduct = fProduct
                               WHERE product.name = %s
                               ORDER BY idOrder"""