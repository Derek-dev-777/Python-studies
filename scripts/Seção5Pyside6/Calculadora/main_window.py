
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QGridLayout

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent,*args,**kwargs)

        # Configurando o layout BASICO:

        self.cw = QWidget() #n sei a definiçao ainda
        self.vLayout = QVBoxLayout() # o tipo de layout
        self.gridLayout = QGridLayout()
        self.cw.setLayout(self.vLayout)
        self.setCentralWidget(self.cw)

        # COnfigurando o titulo do app
        self.setWindowTitle("calculadora") 

    # Ajustando o tamanho da tela ( POR ULTIMO )
    def adjustFixedSize(self):
        self.adjustSize() # ajusta o tamanho da tela de acordo com as letras etc 
        self.setFixedSize(self.width(), self.height()) # e apos ajustar, deixamos o tamanho fixo do adjust

    #Função para adicionar um widget no layout (label, button etc)
    def addWidgetToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)
        # # sempre que for adicionado um widget, ele ajusta o tamanho da janela

    def addWidgetToGridLayout( self, widget: QWidget):
        self.vLayout.addLayout(widget)