from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMessageBox, QLineEdit, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from random import choice
from txt import txt_error1

app = QApplication([])

class Window(QWidget): 
    def __init__(self):
        super().__init__()
        self.symbols = '-=_+!@#$%^&*()"№;:?.,<>`~1234567890qwruisdfgjlzvnQWRUISDFGJLZVNйцгшщзъфыплджэячиьбюЙЦГШЩЗЪФЫПЛДЖЭЯЧИЬ'
        self.initUI()
        
    def password_generation(self):
        p = []
        count = int(self.count_symbols.text())
        if count > 50 or count < 5:
            self.error_show()
        else:
            for i in range(count):
                p.append(choice(self.symbols))
            str_password = ''.join(p)
            self.password.setText(str_password)
            return str_password
    
    def error_show(self):
        self.error.show()
    
    def initUI(self):
        '''создание виджетов'''
        self.error = QMessageBox()
        self.count_symbols = QLineEdit('20')
        self.question = QLabel('В поле введите кол-во символов, которое вам нужно:')
        self.text = QLabel('Привет! Я тебе сгенерирую пароль, который не сможет отгадать даже Кевин Митник.')
        self.text2 = QLabel('Ваш пароль:')
        self.password = QLabel('*Пусто*')
        self.button = QPushButton('Сгенерировать')

        '''настройка виджетов'''
        self.error.setWindowTitle('Ошибка №1325: Недоступный диапозон')
        self.error.setText(txt_error1)
        self.setWindowTitle('Генератор надёжного пароля')
        self.resize(640, 360)
        self.password.setTextInteractionFlags(Qt.TextSelectableByMouse)
        
        '''создание линий'''
        g1_line = QHBoxLayout()
        g2_line = QHBoxLayout()
        g3_line = QHBoxLayout()
        g4_line = QHBoxLayout()
        g1_line.addWidget(self.text, alignment = Qt.AlignCenter)
        g2_line.addWidget(self.text2, alignment = Qt.AlignCenter)
        g2_line.addWidget(self.password, alignment = Qt.AlignCenter)
        g3_line.addWidget(self.question, alignment = Qt.AlignCenter)
        g3_line.addWidget(self.count_symbols, alignment = Qt.AlignCenter)
        g4_line.addWidget(self.button, alignment = Qt.AlignCenter)
        v_line = QVBoxLayout()
        v_line.addLayout(g1_line)
        v_line.addLayout(g2_line)
        v_line.addLayout(g3_line)
        v_line.addLayout(g4_line)
        self.setLayout(v_line)

        '''соединения при нажатии определённого виджета'''
        self.button.clicked.connect(self.password_generation)
main_win = Window()
main_win.show()

app.exec_()

#Задание: сделать кол-во сгенерированных паролей