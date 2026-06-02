from PyQt5.QtCore import Qt,QTimer,QLocale, QRegularExpression
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton,QLabel,QVBoxLayout, QLineEdit
import random as ran
import time
import third_win
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QRegularExpressionValidator
import os

# Класс окна регистрации (второй шаг приложения)
class Window2(QWidget):
    def __init__(self):
        super().__init__()
        self.show()
        self.setWindowTitle(' ')
        self.resize(600, 400)
        
        # Создание текстовых меток интерфейса
        reg_txt = QLabel('Регистрация')
        login = QLabel('Имя:')
        password = QLabel('Пароль:')
        
        # Создание полей ввода для логина и пароля
        self.login_hint = QLineEdit('')
        self.password_hint = QLineEdit('')
        self.reg_button = QPushButton('Зарегистрироваться')

        # Подключение кнопки к функции проверки данных и открытия третьего окна
        self.reg_button.clicked.connect(self.showthirdwin)

        self.setWindowFlags(Qt.WindowTitleHint) # Скрытие кнопок управления окном (свернуть/закрыть)

        # Вертикальная компоновка всех элементов интерфейса
        v_line = QVBoxLayout()
        v_line.addWidget(reg_txt, alignment = Qt.AlignCenter)
        v_line.addWidget(login, alignment = Qt.AlignLeft)
        v_line.addWidget(self.login_hint, alignment = Qt.AlignLeft)
        v_line.addWidget(password, alignment = Qt.AlignLeft)
        v_line.addWidget(self.password_hint, alignment = Qt.AlignLeft)
        v_line.addWidget(self.reg_button, alignment = Qt.AlignCenter)

        self.setLayout(v_line)
        self.show()

        # Регулярное выражение: разрешает вводить в логин ТОЛЬКО буквы (русские и английские)
        regex = QRegularExpression("^[a-zA-Zа-яА-ЯёЁ]+$")
        # Создание валидатора на основе регулярного выражения
        validator = QRegularExpressionValidator(regex)
        # Применение валидатора к полю ввода имени (цифры и пробелы ввести не получится)
        self.login_hint.setValidator(validator)

        # Ограничение на максимальное количество символов в полях ввода
        self.login_hint.setMaxLength(20)     # Логин: не длиннее 20 символов
        self.password_hint.setMaxLength(10)  # Пароль: не длиннее 10 символов

    # Метод проверки условий регистрации и переключения на третье окно
    def showthirdwin(self):
        # Проверка: длина имени должна быть от 3 символов, а пароля — от 5 символов
        if len(self.login_hint.text())>= 3 and len(self.password_hint.text())>=5:
            self.hide() # Скрытие текущего окна регистрации
            time.sleep(0.8) # Искусственная задержка (замораживает интерфейс)
            
            # Считывание финального текста из полей ввода
            username = self.login_hint.text()
            userpassword = self.password_hint.text()
            
            # Передача введенных данных (имени и пароля) при создании третьего окна
            third_win.win3 = third_win.Window3(username,userpassword) 
            third_win.win3.show() # Отображение третьего окна
            