from typing import TYPE_CHECKING
from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from variables import MEDIUM_FONT_SIZE, isEmpty, isNumOrDot, isValidNumber
from styles import qss
if TYPE_CHECKING:

    from display import Display
    from info import Info

class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()


    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)

    
        
class ButtonGrid(QGridLayout):
    def __init__(self, display: "Display",info: "Info", *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self._grid_mask = [
             ['C', '◀', '^', '/'],
             ['7', '8', '9', '*'],
             ['4', '5', '6', '-'],
             ['1', '2', '3', '+'],
             ['',  '0', '.', '='],
         ]
        self.display = display
        self.info = info
        self._equation = ""
        self._makeGrid()
        
    @property
    def equation(self):
        return self._equation
    
    @equation.setter
    def equation(self,value):
        self._equation = value
        self.info.setText(value)     

    def _makeGrid(self):
        for i, row in enumerate(self._grid_mask):
            for j, button_text in enumerate(row):
                button = Button(button_text)
                if not isNumOrDot(button_text) and not isEmpty(button_text):
                    button.setProperty("cssClass", "specialButton")
                    self._configSpecialButton(button)
                
                
                self.addWidget(button, i , j)


                slot = self._makeSlot(self._insertButtonTextToDisplay,button)
                self._connectButtonCliked(button, slot)
 



    def _connectButtonCliked(self, button, slot):
        button.clicked.connect(slot)
        


    def _configSpecialButton(self, button):
        text = button.text()

        if text == "C":
            slot = self._makeSlot(self._clearDisplay)
            self._connectButtonCliked(button, slot)



    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
             func(*args, **kwargs)
        return realSlot
 



    def _insertButtonTextToDisplay(self, button):
         button_text = button.text()
         new_display_value = self.display.text() + button_text # sabendo o que terá no meu display

         if not isValidNumber(new_display_value):
             return
         
         self.display.insert(button_text)


        
    def _clearDisplay(self):
        self.display.clear()



        