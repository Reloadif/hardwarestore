import matplotlib
matplotlib.use('Qt5Agg')

from PyQt5 import QtWidgets, QtGui

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import matplotlib.pyplot as pyplot
import numpy

class MatplotWindow(QtWidgets.QMainWindow):
    def __init__(self, data):
        super(MatplotWindow, self).__init__()

        self.data = data
        self.figure = pyplot.figure()
        self.canvas = FigureCanvas(self.figure)
        self.setCentralWidget(self.canvas)
        self.setWindowTitle("Отчет")
        self.setWindowIcon(QtGui.QIcon("./UserInterface/icons/reportGraph.png"))
    
    def draw(self):
        labels = []
        y = []
        for row in range(len(self.data)):
            labels.append(getFirstNumberOfFullname(str(self.data[row][1])))
            y.append(int(self.data[row][3]))
    
        x = numpy.arange(0, len(y))

        pyplot.bar(x, y, align='center')
        pyplot.xticks(x, labels)
        pyplot.ylabel("Заработная плата в р.")
        pyplot.xlabel("Инициалы сотрудника")
        pyplot.title("Отчет по заработной плате")

        self.canvas.draw()

def getFirstNumberOfFullname(fullname):
    result = ""
    arrayOfPart = fullname.split()
    for i in arrayOfPart:
        result += i[0] + "."

    return result