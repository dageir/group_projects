from PyQt5.QtCore import Qt,QTimer
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton,QLabel,QVBoxLayout
from urllib.request import urlopen
import json
import random as ran
import time
import second_win
import os
import winsound


# Создание главного приложения PyQt, управляющего всеми окнами
app = QApplication([])

# Функция переключения окон: закрывает текущее окно, выдерживает паузу и открывает второе
SAVE_FILE = "username.txt"

def load_username():
    if not os.path.exists(SAVE_FILE):
        return None
    with open(SAVE_FILE, "r", encoding="utf-8") as file:
        return file.read().strip()
        
current_user = load_username()
def showsecondwin():
    win1.hide()
    time.sleep(0.8) # Пауза перед открытием (может заморозить интерфейс на 0.8 сек)
    second_win.win2 = second_win.Window2() # Создание объекта окна из соседнего файла second_win.py
    second_win.win2.show()

# Класс "глючного" или технического стартового окна с греческими символами в заголовке
class ZeroWin1(QWidget):
    def __init__(self):
        super().__init__()
        words = ["αβγδεζηθ", "ικλμνξοπρ", "σςτυ", "φχψω"]
        random_word = ran.choice(words) # Выбор случайного набора букв для заголовка
        self.setWindowTitle(random_word)
        self.resize(600, 200)
        self.setWindowFlags(Qt.WindowTitleHint) # Отображает только заголовок окна без кнопок свернуть/закрыть
        self.show()

# Главное приветственное окно приложения
class Window1(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(' ')
        self.resize(400, 200)

        # Создание текстовых надписей и кнопки
        start_txt = QLabel('Добро пожаловать в SPARK!')
        description_txt = QLabel('Карта свободных мест и очередей в реальном времени.\nТвой город без ожидания и толпы.')
        self.start_button = QPushButton('Начать')

        # Подключение события клика на кнопку к функции переключения окон
        self.start_button.clicked.connect(showsecondwin)

        self.setWindowFlags(Qt.WindowTitleHint) # Скрытие кнопок управления окном

        # Вертикальное позиционирование элементов строго по центру окна
        v_line = QVBoxLayout()
        v_line.addWidget(start_txt, alignment = Qt.AlignCenter)
        v_line.addWidget(description_txt, alignment = Qt.AlignCenter)
        v_line.addWidget(self.start_button, alignment = Qt.AlignCenter)
        self.setLayout(v_line)
        self.show()

# Скрипт случайного появления пугающих/глюкающих окон перед запуском основной программы
counter_first = 0 
if ran.randint(1,5) <=2: # С вероятностью 40% (если выпадет 1 или 2) запустится этот блок
    for i in range(3): # Цикл создаст и покажет 3 странных окна по очереди
        winzero = ZeroWin1()
        winzero.show()
        # Вычисление случайных координат на экране со смещением
        countx = (ran.randint(6,1000)) + counter_first
        county = (ran.randint(5,700)) + counter_first
        winzero.move(countx,county) # Перемещение окна в случайную точку экрана
        time.sleep(0.04) # Окно задерживается на экране всего на 40 миллисекунд
        winzero.hide() # Окно мгновенно скрывается
        counter_first+= ran.randint(10,200) # Наращивание смещения для следующего окна
    time.sleep(0.5) # Небольшая пауза после серии "глюков"
    winsound.MessageBeep(winsound.MB_ICONHAND) # Воспроизведение стандартного системного звука ошибки Windows

# Запуск основного приветственного окна приложения
win1 = Window1()

# Запуск главного цикла обработки событий PyQt (программа работает, пока не закроют окна)
app.exec_()