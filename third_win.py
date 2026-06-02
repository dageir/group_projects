from PyQt5.QtCore import Qt,QTimer
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton,QLabel,QVBoxLayout, QLineEdit,QHBoxLayout
import random as ran
import time
import second_win
import os
import ai_win
import locate_win

# Класс третьего (главного меню) окна приложения, принимающий данные пользователя
class Window3(QWidget):
    def __init__(self,name,password):
        super().__init__()
        # Сохранение переданных из окна регистрации имени и пароля в свойства объекта
        self.name = name
        self.password = password
        self.show()
        
        # Получение имени пользователя текущей учетной записи операционной системы Windows/Linux
        username_win = os.getlogin()
        #self.setWindowTitle(username_win + '?')
        #time.sleep(2)
        
        self.setWindowTitle('SPARIK')
        self.resize(400, 200)
        
        # Создание элементов интерфейса: текстовых меток и кнопок навигации
        nameofcompany = QLabel('SPARIK')
        usersuper = 'Привет,' + self.name # Приветственная строка с именем зарегистрированного юзера
        labeluser = QLabel(usersuper)
        version = QLabel('v0.4.0-beta.7+build.892')
        self.tellaismthbutton = QPushButton('Поговорить с ИИ агентом')
        self.locationbutton = QPushButton('Локация')
        self.exitbutton = QPushButton('Выйти')

        # Привязка событий нажатия на кнопки к соответствующим методам класса
        self.exitbutton.clicked.connect(self.exitbuttonfunc)
        self.tellaismthbutton.clicked.connect(self.showaiwin)
        self.locationbutton.clicked.connect(self.showlocatewin)
        
        self.setWindowFlags(Qt.WindowTitleHint) # Скрытие стандартных кнопок управления окном
        
        # Настройка сетки слоев для размещения элементов
        v_line = QVBoxLayout() # Главный вертикальный контейнер
        h_line = QHBoxLayout() # Вспомогательный горизонтальный контейнер для верхней строки
        v_line.addLayout(h_line)
        
        # Позиционирование элементов в окне с выравниванием по разным краям
        v_line.addWidget(labeluser, alignment = Qt.AlignLeft)
        h_line.addWidget(version, alignment = Qt.AlignRight) # Версия улетает в правый верхний угол
        v_line.addWidget(nameofcompany, alignment = Qt.AlignCenter)
        v_line.addWidget(self.tellaismthbutton, alignment = Qt.AlignLeft)
        v_line.addWidget(self.locationbutton, alignment = Qt.AlignLeft)
        v_line.addWidget(self.exitbutton, alignment = Qt.AlignLeft)
        
        self.setLayout(v_line)
        self.show()
        
    # Функция закрытия приложения при нажатии кнопки Выйти
    # Внимание: здесь пропущен аргумент self, метод может упасть при вызове
    def exitbuttonfunc():
        self.close()

    # Метод для скрытия текущего меню и открытия четвертого окна (чат-бота с ИИ)
    def showaiwin(self):
        self.hide()
        time.sleep(0.8) # Искусственная задержка (замораживает интерфейс)
        # Создание объекта четвертого окна из файла ai_win.py и передача туда имени пользователя
        ai_win.win4 = ai_win.Window4(self.name) 
        ai_win.win4.show()
    def showlocatewin(self):
        self.hide()
        time.sleep(0.8) # Искусственная задержка (замораживает интерфейс)
        # Создание объекта четвертого окна из файла ai_win.py и передача туда имени пользователя
        locate_win.win5 = locate_win.Window5() 
        locate_win.win5.show()