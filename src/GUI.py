from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *
from functools import partial
import sys
from Logic import *


buttons_ui = ["clear", "", "", "<<",
              "7", "8", "9", "/" , 
              "4", "5", "6", "x",
              "1", "2", "3", "-", 
              "0", "", "=" , "+"]

DEFAULT = ""


class Calculator(QWidget):
    
    def __init__(self):
        super(Calculator, self).__init__()
        self.calc = Logic()
        self.text = ""
        self.layout_main = QGridLayout()
        self.create_window()
        self.create_ui()
        self.reset()
        self.setLayout(self.layout_main)
        self.show()
        
    def reset(self):
        self.text = DEFAULT

    def create_window(self):
        self.setFixedSize(300, 200)
        self.setWindowTitle("PyCalculator")

    def create_lcd(self):
        # displays input
        self.label_in = QLabel(self)
        self.label_in.setAlignment(QtCore.Qt.AlignRight)
        self.label_in.adjustSize()
        self.label_in.setText(DEFAULT)
        self.label_in.setStyleSheet("background-color: white; border: 0px solid black; color: black; ")
        # displays output
        self.label_out = QLabel(self)
        self.label_out.setAlignment(QtCore.Qt.AlignRight)
        self.label_out.adjustSize()
        self.my_font = QtGui.QFont()
        self.my_font.setBold(True)
        self.my_font.setItalic(True)
        self.label_out.setFont(self.my_font)
        self.label_out.setStyleSheet("border: 0px; background-color:rgba(0,0,0,0%);")
        self.label_out.setText("")
        self.layout_main.addWidget(self.label_in, 0 , 0, 1, 4)
        self.layout_main.addWidget(self.label_out, 1, 0, 1, 4)


    def create_buttons(self): 
        count = 4
        for i, val in enumerate(buttons_ui):    
            a = QPushButton(val, self)
            if val in self.calc.get_mapping():
                a.setStyleSheet('QPushButton {background-color: gray; color: yellow}')
            else:
                a.setStyleSheet('QPushButton {background-color: gray; color: white}')
            a.setFont(self.my_font)
            a.clicked.connect(partial(self.add_to_screen, val))
            row = int(i / count)  + 2
            col = i % count 
            self.layout_main.addWidget(a, row, col, 1, 1)
    
    def create_ui(self):
        self.create_lcd()
        self.create_buttons()
    
    def add_to_screen(self, string):
        if string == "clear":
            self.reset()
        elif string == "<<":
            self.text = self.text[:-1]
        elif string == "=":
            pass
        else:
            self.text += string
        output = self.calc.execute(self.text)
        self.label_in.setText(self.text)
        self.label_out.setText(output)


def main():
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()       
