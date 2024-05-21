import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

def recuadro(datos):
    recuadros=[]
    for i in range(len(datos)):
        #aux=instancia()
        #aux.nombre=datos[i][0]
        #aux.escuela=datos[i][1]
        #aux.id=datos[i][2]
        recuadros.append()
    return recuadros

def g_barras(lista,name_x,name_y):
    x_labels,y=[],[]
    for i in range(len(lista)):
        x_labels.append(lista[i][1])
        y.append(lista[i][0])
    x = range(len(x_labels))
    
    fig, ax = plt.subplots()
    ax.bar(x,y)
    ax.set_xlabel(name_x)
    ax.set_ylabel(name_y)
    ax.set_xticks(x)
    ax.set_xticklabels(x_labels)
    return fig

def g_lineas(lista,name_x,name_y):
    x_labels,y=[],[]
    for i in range(len(lista)):
        x_labels.append(lista[i][1])
        y.append(lista[i][0])
    x = range(len(x_labels))
    
    fig, ax = plt.subplots()
    ax.plot(x,y,marker='o')
    ax.set_xlabel(name_x)
    ax.set_ylabel(name_y)
    ax.set_xticks(x)
    ax.set_xticklabels(x_labels)
    return fig

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Ejemplo de lista
        lista_ejemplo = [(1, "A"), (2, "B"), (3, "C")]

        # Llamar a la función para generar el gráfico de líneas
        fig = g_lineas(lista_ejemplo, "Letras", "Números")

        canvas = FigureCanvas(fig)
        layout.addWidget(canvas)

        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle('Gráfico de Líneas en QWidget')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
