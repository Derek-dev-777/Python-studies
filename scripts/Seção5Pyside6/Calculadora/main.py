import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication,  QLabel
from main_window import MainWindow
from display import Display
from info import Info
from buttons import Button, ButtonGrid
from variables import LOGO_PATH
from styles import setupTheme

if __name__ == "__main__":

    # Cria a aplicação
    app = QApplication(sys.argv) # Cria o aplicativo
    setupTheme(app)
    window = MainWindow() # janela principal

    # theme

    

    #Info
    info = Info("2.0 ^ 10.0 = 1024")
    window.addWidgetToVLayout(info)

    # Display
    display = Display() # display seria o input
    display.setPlaceholderText("Digite um numero") # se n tiver nada digitado, mostra essa string
    window.addWidgetToVLayout(display) # adiciona meu display na janela usando a função criada

    #Grid , criando o layout dos botões

    buttonsGrid = ButtonGrid(display, info)
    window.vLayout.addLayout(buttonsGrid)

    #Button, criando os botões, adicionando eles na minha layout de botões ( ButtonGrid )
    # assim podemos manipulalos ( button, 0, 0) " botão na linha 0 e coluna zero"



    # Define o icone do programa
    icon = QIcon(str(LOGO_PATH))
    app.setWindowIcon(icon)
    window.setWindowIcon(icon)

    # Mantem rodando o programa
    
    window.show()
    app.exec()