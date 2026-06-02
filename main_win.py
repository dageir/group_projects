from random import randint

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QMainWindow,
    QVBoxLayout, QHBoxLayout, QPushButton, QWidget
)
import sys

from charecters import (MainCharecter, AnotherMainCharecter, MSG)
# 1. Создаем объект приложения
app = QApplication(sys.argv)

armo = [0 , 0 , 0 , 0 , 0 , 0]

queue = randint(0 , 1)

num_bullet = 0
for i in range(6):
    armo[i] = randint(0, 100)

# 2. Определяем главное окно, наследуясь от QMainWindow
class Main_Win(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('idk1')
        self.resize(1440, 720) 
       # button_style =    не понял как кнопки настроить
     #       QPushButton {
   #             font-size: 12px;          /* Уменьшаем размер шрифта */
  #              padding: 4px 8px;         /* Уменьшаем внутренние отступы */
  #              min-width: 80px;          /* Минимальная ширина */
 #               max-width: 120px;         /* Максимальная ширина */
 #           }
       
        self.init_ui()                      
        
        self.show()
    def init_ui(self):
        # --- Создание виджетов (кнопок) ---
        self.shoot = QPushButton('shot')
        self.shoot_to_me = QPushButton('shoot_to_me')
        self.reroll = QPushButton('reroll')



        # --- Создание макетов ---
        # Горизонтальный макет для кнопок
        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.shoot)
        self.h_layout.addWidget(self.shoot_to_me)
        self.h_layout.addWidget(self.reroll)

        # Вертикальный макет (основной), в который вложим горизонтальный
        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.h_layout)

        # --- Сборка окна ---
        # Создаем центральный виджет, который будет содержать все наши элементы
        central_widget = QWidget()
        central_widget.setLayout(self.main_layout)

        # Устанавливаем этот виджет как центральный для главного окна
        self.setCentralWidget(central_widget)

        def connects(self): # связь с кнопкой shot_to_me
            self.shoot_to_me.clicked.connect(self.do_shot_to_me)
            self.shoot.clicked.connect(self.do_shoot)
            self.reroll.clicked.connect(self.do_reroll)
            
        def do_shoot_to_me(self): # вызов shoot_to_me
            MainCharecter.shoot_to_me()

        def do_shoot(self): # вызов shoot
            MainCharecter.shoot()

        def do_reroll(self): # вызов reroll
            MainCharecter.reroll()

if __name__ == '__main__':
    game = Main_Win()
    game.show()
