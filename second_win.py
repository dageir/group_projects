from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QVBoxLayout, QLabel, QHBoxLayout, QMessageBox, QRadioButton)

import instr as ins

class Opros1(QWidget):
    
    
    def __init__(self):
        ''' окно, в котором располагается приветствие '''
        super().__init__()

        # создаём и настраиваем графические элементы:
        self.initUI()

        # устанавливает связи между элементами
        self.connects()

        # устанавливает, как будет выглядеть окно (надпись, размер, место)
        self.set_appear()

        # старт:
        self.show()
    def show_win(self):
        vic_win = QMessageBox()
        vic_win.setText('ТЫ ОТВЕТИЛ ВЕРНО!!!!!! проект на стадии разработки будут добавлены вопросы и шутки и ранг.')
        vic_win.exec_()
    def show_lose(self):
        vic_lo = QMessageBox()
        vic_lo.setText('ТЫ ОТВЕТИЛ НЕ ВЕРНО!!!!!! проект на стадии разработки будут добавлены вопросы и шутки и ранг.')
        vic_lo.exec_()
    def six_seven(self):
        win_sixSeven = QMessageBox()
        next_click67
    def initUI(self):
        ''' создаёт графические элементы '''
        self.btn_next1 = QRadioButton(ins.txt_I_1vopros, self)
        self.btn_next2 = QRadioButton(ins.txt_I_2vopros, self)
        self.btn_next3 = QRadioButton(ins.txt_I_3vopros, self)
        self.btn_next4 = QRadioButton(ins.txt_I_4vopros, self)
        self.vopros_text = QLabel(ins.txt_I_vopros)

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.vopros_text, alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.btn_next1, alignment=Qt.AlignCenter)
        self.layout_line.addWidget(self.btn_next2, alignment=Qt.AlignCenter)
        self.layout_line.addWidget(self.btn_next3, alignment=Qt.AlignCenter)
        self.layout_line.addWidget(self.btn_next4, alignment=Qt.AlignCenter)
        self.setLayout(self.layout_line)

    

    def connects(self):
        self.btn_next1.clicked.connect(self.next_click)
        self.btn_next3.clicked.connect(self.show_win)
        self.btn_next1.clicked.connect(self.show_lose)
        self.btn_next2.clicked.connect(self.show_lose)
        self.btn_next4.clicked.connect(self.show_lose)

    ''' устанавливает, как будет выглядеть окно (надпись, размер, место) '''
    def set_appear(self):
        self.setWindowTitle(ins.txt_title)
        self.resize(ins.win_width, ins.win_height)
        self.move(ins.win_x, ins.win_y)

    def next_click(self):
        self.tw = ImageLoader()
        self.hide()

    


 