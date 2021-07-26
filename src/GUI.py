from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *
from functools import partial
import sys
from LOGIC import evaluate, ops


# This is the list of buttons in calulator 
# it will come below the display
# the string value is both the value that will be shown and the value that will be passed on click
# if "" is seen then no button is created
buttons_ui: list = [
    ["(",  ")",  "DEL", "AC"],
    ["7",  "8",  "9",   "/" ], 
    ["4",  "5",  "6",   "*" ],
    ["1",  "2",  "3",   "-" ],
    [".",  "0",  "^" ,   "+"],
]

DEFAULT: str = ""



def get_style(bg_color, color, border=2, font_size=24) -> str: 
    """The [return] value can be set for QElement: e,  by passing argument in e.setsetStyleSheet()"""
    return f"""
            background-color : {bg_color}; 
            color            : {color}; 
            border           : {border}px solid black; 
            font-size        : {font_size}px;
            alignment: AlignRight;
            font             :   'Times New Roman';
        """


class Calculator(QWidget):
    
    def __init__(self):
        super(Calculator, self).__init__()
        # setting window configuration
        self.setFixedSize(400, 300)
        self.setWindowTitle("PyCalculator") 
        # text that will be displayed in input label
        self.text = DEFAULT
        # creating layout
        self.layout_main = QGridLayout()
        # adding elements to layout
        self.create_lcd()
        self.create_buttons()
        # adding layout to window            
        self.setLayout(self.layout_main)
        
    def reset(self):
        # resettinfg the input label to show ""
        self.text = DEFAULT


    def create_lcd(self):
        # displays input
        self.label_in = QLabel(self)
        self.label_in.setAlignment(QtCore.Qt.AlignRight)
        self.label_in.setStyleSheet(get_style("white", "black"))
        # displays output
        self.label_out = QLabel(self)
        self.label_out.setAlignment(QtCore.Qt.AlignRight)
        self.label_out.setStyleSheet(get_style("rgba(0,0,0,0%)", "black", border=0, font_size=36))
        self.layout_main.addWidget(self.label_in, 0 , 0, 1, 4)
        self.layout_main.addWidget(self.label_out, 1, 0, 1, 4)


    def create_buttons(self):   
        for row, values in enumerate(buttons_ui):
            for col, val in enumerate(values):
                # if buttons have "" then don't add it to ui
                if val != "": 
                    # setting stylesheet for 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, .
                    if val.isdigit() or val == ".":  spreadsheet= get_style("lightgray", "black")
                    # setting stylesheet for AC, DEL
                    elif val.isalpha(): spreadsheet= get_style("yellow", "black") 
                    # setting stylesheet for AC, DEL
                    else: spreadsheet= get_style("darkgray", "yellow")
                    
                    # creating button and adding it to main menu
                    btn = QPushButton(val, self)
                    btn.setStyleSheet(spreadsheet)
                    btn.clicked.connect(partial(self.add_to_screen, val)) 
                    self.layout_main.addWidget(btn, row + 3, col, 1, 1)
    
  
    
    def add_to_screen(self, string):
        # When a button is clicked it will send the value for based on button_ui
        # That value is set such as: 
        # if input is  AC, it will clear the self.text
        # if input is  DEL will remove the last element from text
        # otherwise the value is added to seld.text
        if   string == "AC" :  self.reset()
        elif string == "DEL":  self.text = self.text[:-1]
        else: self.text += string
        # after every input the value is automatically  displayed in out label
        output = evaluate(self.text)[:20]
        self.label_in.setText(self.text)
        self.label_out.setText(output)


def main():
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()       
