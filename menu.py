# Импортируем необходимые модули
# sys нужен для корректного завершения приложения
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QMainWindow,
    QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QLabel
)
import sys

from main_win import Main_Win

# 1. Создаем объект приложения
app = QApplication(sys.argv)

# 2. Определяем главное окно, наследуясь от QMainWindow
class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Menu')
        self.resize(1440, 720) 
       # button_style =    не понял как кнопки настроить
     #       QPushButton {
   #             font-size: 12px;          /* Уменьшаем размер шрифта */
  #              padding: 4px 8px;         /* Уменьшаем внутренние отступы */
  #              min-width: 80px;          /* Минимальная ширина */
 #               max-width: 120px;         /* Максимальная ширина */
 #           }
       
        self.init_ui()
        self.connects()


    def init_ui(self):
        self.name = QLabel('Будующее название')
        self.play = QPushButton('Играть')
        self.settings = QPushButton('Настройки') # потом погут пригодиться
        self.exit = QPushButton('Выход') # просто выход с окна


        # --- Создание макетов ---
        # Горизонтальный макет для кнопок
        self.V_layout = QVBoxLayout()
        self.V_layout.addWidget(self.name, alignment = Qt.AlignCenter)
        self.V_layout.addWidget(self.play)
        self.V_layout.addWidget(self.settings)
        self.V_layout.addWidget(self.exit)

        # --- Сборка окна ---
        # Создаем центральный виджет, который будет содержать все наши элементы
        central_widget = QWidget()
        central_widget.setLayout(self.V_layout)

        # Устанавливаем этот виджет как центральный для главного окна
        self.setCentralWidget(central_widget)

    def next_click_game(self): # вызов нового окна
        self.tw = Main_Win()
        self.hide()

    def connects(self): # связь
        self.play.clicked.connect(self.next_click_game) # почему то сразу кидает на окно с игрой
        self.exit.clicked.connect(self.next_click_exit)

    def next_click_exit(self): # вход
        sys.exit(app.exec())

# 3. Создаем экземпляр нашего окна и показываем его
win = Menu()
win.show()

# 4. Запускаем основной цикл обработки событий приложения.
# sys.exit гарантирует корректное закрытие программы.
sys.exit(app.exec_())