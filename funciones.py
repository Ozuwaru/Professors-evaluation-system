import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtChart import QChart, QChartView,QBarCategoryAxis, QBarSeries, QBarSet, QCategoryAxis, QLineSeries
from PyQt5.QtGui import QPainter
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from PyQt5.QtCore import Qt

class Busqueda:
    #aqui se lee la info desde la BDD buscando coincidencias
    def lectura(self):
        self.lista=[]
    
    def recuadro(self):
        recuadros=[]
        for i in range(len(self.lista)):
            #aux=instancia()
            #aux.nombre=self.lista[i][0]
            #aux.escuela=self.lista[i][1]
            #aux.id=self.lista[i][2]
            recuadros.append()
        return recuadros

class Graficas:
    def ejes(self,lista):
        self.x_labels,self.y=[],[]
        
        for i in range(len(lista)):
            self.x_labels.append(lista[i][0])
            self.y.append(lista[i][1])
        self.x = range(len(self.x_labels))
        

    def g_barras(self,lista,name_x,name_y):
        self.ejes(lista)
        
        bar_set = QBarSet(name_y)
        for i in self.y:
            bar_set<<i 
            
        series=QBarSeries()
        series.append(bar_set)
        
        chart=QChart()
        chart.addSeries(series)
        chart.setTitle(f"Gráfico de barras: {name_x} vs {name_y}")
        
        axisX=QCategoryAxis()
        for i, label in enumerate(self.x_labels):
            axisX.append(label, i)
        
        axisX.setTitleText(name_x)
        
        chart.createDefaultAxes()
        chart.setAxisX(axisX, series)
        chart.axisY(series).setTitleText(name_y)
        
        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)
        return chart_view
        
        # self.ejes(lista)
        
        # bar_set = QBarSet(name_y)
        # for i in self.y:
        #     bar_set << i
            
        # series = QBarSeries()
        # series.append(bar_set)
        
        # chart = QChart()
        # chart.addSeries(series)
        # chart.setTitle(f"Gráfico de barras: {name_x} vs {name_y}")
        
        # axisX = QBarCategoryAxis()
        # axisX.append(self.x_labels)
        # axisX.setTitleText(name_x)
        
        # chart.addAxis(axisX, Qt.AlignBottom)
        # series.attachAxis(axisX)
        
        # chart.createDefaultAxes()
        # chart.axisY(series).setTitleText(name_y)
        
        # chart_view = QChartView(chart)
        # chart_view.setRenderHint(QPainter.Antialiasing)
        # return chart_view
        
        
        
        # self.x_labels,self.y=[],[]
        # for i in range(len(lista)):
        #     self.x_labels.append(lista[i][1])
        #     self.y.append(lista[i][0])
        # self.x = range(len(self.x_labels))
        
        #fig, ax = plt.subplots()
        #ax.bar(self.x,self.y)
        #ax.set_xlabel(name_x)
        #ax.set_ylabel(name_y)
        #ax.set_xticks(self.x)
        #ax.set_xticklabels(self.x_labels)
        #return fig

    def g_lineas(self,lista,name_x,name_y):
        self.ejes(lista)
        
        series=QLineSeries()
        for i in range(len(self.x)):
            series.append(i, self.y[i])
        
        chart=QChart()
        chart.addSeries(series)
        chart.setTitle(f"Gráfico de líneas: {name_x} vs {name_y}")
        
        axisX=QCategoryAxis()
        for i, label in enumerate(self.x_labels):
            axisX.append(label, i)
        axisX.setTitleText(name_x)
        
        chart.createDefaultAxes()
        chart.setAxisX(axisX, series)
        chart.axisY(series).setTitleText(name_y)
        
        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)
        return chart_view
        
        # fig, ax = plt.subplots()
        # ax.plot(self.x,self.y,marker='o')
        # ax.set_xlabel(name_x)
        # ax.set_ylabel(name_y)
        # ax.set_xticks(self.x)
        # ax.set_xticklabels(self.x_labels)
        # return fig

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        graficas = Graficas()
        
        lista_ejemplo = [("A",1), ("B", 2), ("C",3)]

        chart_view_barras = graficas.g_barras(lista_ejemplo, "Letras", "Números")
        chart_view_lineas = graficas.g_lineas(lista_ejemplo, "Letras", "Números")

        container = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(chart_view_barras)
        # layout.addWidget(chart_view_lineas)
        container.setLayout(layout)
        
        self.setCentralWidget(container)
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Gráficos con QChart')
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#         self.graf=Graficas()

#     def initUI(self):
#         layout = QVBoxLayout()
#         self.setLayout(layout)

#         lista_ejemplo = [(1, "A"), (2, "B"), (3, "C")]

#         fig = self.graf.g_lineas(lista_ejemplo, "Letras", "Números")

#         canvas = FigureCanvas(fig)
#         layout.addWidget(canvas)

#         self.setGeometry(100, 100, 600, 400)
#         self.setWindowTitle('Gráfico de Líneas en QWidget')
#         self.show()
