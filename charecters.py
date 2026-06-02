from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QVBoxLayout, QPushButton, QLabel)

from random import randint


armo = [0 , 0 , 0 , 0 , 0 , 0]

queue = randint(0 , 1)

num_bullet = 0
for i in range(6):
    armo[i] = randint(0, 100)

class MainCharecter():
    def __init__(self, alive):
        self.alive = alive
    
    def shoot_enemy(self, enemy): # по врагу
        global num_bullet
        global armo
        if armo[num_bullet] > 60:
             enemy.alive = False
        num_bullet += 1

    def reroll(self): # ролл барабана
        global num_bullet
        num_bullet = random.randint(0, 6)
        
    def shoot_self(self): #по себе
        global num_bullet
        global armo
        for i in armo:
            for a in range(6):
                if armo[num_bullet] > 60:
                    self.alive = False # класс себя - hp или смерт
                else:
                    pass # потеря ходя

    def ur_queue(self):
        global queue
        if queue == 0:
            pass # твоя очередь

class AnotherMainCharecter(MainCharecter):
     '''класс для онлайна'''

class MSG (MainCharecter):
    def random_doing(self):# выбор действия
        self.doing = random.randint(0, 100)
        if self.doing < 36:
            shoot_self()
        elif self.doing < 60:
            shoot_enemy()
        else:
            reroll()
            if random.randict(0,1) == 0:
                shoot_enemy()
            else:
                shoot_self()
       #         if alive == True
                 #   shoot_enemy
    def my_queue(self):
        global queue
        if queue == 1:
            pass # ход бота

            
