# display é como se fosse um input, é onde você podera digitar ( uma barra de pesquisa etc)

from variables import BIG_FONT_SIZE, TEXT_MARGIN, MINIMUN_WIDTH
from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt


class Display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    # basicamente o CSS do meu input
    def configStyle(self):
        margins = [TEXT_MARGIN for i in range(4)]
        self.setStyleSheet(f"font-size: {BIG_FONT_SIZE}px") # determinando o size da minha fonte
        self.setMinimumHeight(BIG_FONT_SIZE * 2) # tamanho da altura do input
        self.setMinimumWidth(MINIMUN_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight) # alinhando meu input para a extrema direita
        self.setTextMargins(*margins)