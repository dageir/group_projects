import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QApplication, 
                             QVBoxLayout, QPushButton, QLabel, QLineEdit)

txt_hello = "конвертор"
txt_instruction = "Введите значения для конвертирования"

win_title = "конвертор^^"
win_width = 500
win_height = 500
win_x = 600
win_y = 100

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()

    def set_appear(self):
        self.setWindowTitle(win_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.hello_txt = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction) 
        
        self.input1 = QLineEdit()
        self.input2 = QLineEdit()
        self.input3 = QLineEdit()
        self.input4 = QLineEdit()

        self.input1.setPlaceholderText("")
        self.input2.setPlaceholderText("")
        self.input3.setPlaceholderText("")
        self.input4.setPlaceholderText("")
        
        input_width = 150
        self.input1.setFixedWidth(input_width)
        self.input2.setFixedWidth(input_width)
        self.input3.setFixedWidth(input_width)
        self.input4.setFixedWidth(input_width)
        
        
        self.main_layout = QVBoxLayout()
        
        
        self.main_layout.addWidget(self.hello_txt, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.instruction, alignment=Qt.AlignCenter)
        
        
        self.columns_layout = QHBoxLayout()
        
      
        self.left_layout = QVBoxLayout()
        self.left_layout.addWidget(self.input1, alignment=Qt.AlignCenter)
        self.left_layout.addWidget(self.input2, alignment=Qt.AlignCenter)
        
        
        self.right_layout = QVBoxLayout()
        self.right_layout.addWidget(self.input3, alignment=Qt.AlignCenter)
        self.right_layout.addWidget(self.input4, alignment=Qt.AlignCenter)
        
        
        self.columns_layout.addLayout(self.left_layout)
        self.columns_layout.addLayout(self.right_layout)
        
        
        self.main_layout.addLayout(self.columns_layout)
        
        self.setLayout(self.main_layout)

app = QApplication(sys.argv)
main_win = MainWin()
sys.exit(app.exec_())
