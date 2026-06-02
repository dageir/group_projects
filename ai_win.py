import json
from urllib.request import urlopen, Request  
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit, QHBoxLayout
import random as ran
import time
import second_win
import subprocess
import winsound
import os
import third_win
import requests
from urllib.parse import quote
from PyQt5.QtCore import QThread, pyqtSignal
import cv2


class AIWorker(QThread):
    finished = pyqtSignal(str)

    def __init__(self, user_text):
        super().__init__()
        self.user_text = user_text

    def run(self):
        try:
            # Обновленный промпт согласно легенде SPARK
            prompt = (
                f"Ты ассистент компании SPARK (Карта свободных мест и очередей в реальном времени. "
                f"Твой город без ожидания и толпы)."
                f"Ответь юзеру: {self.user_text}. Будь краток (до 15 слов)."
            )
            encoded_prompt = quote(prompt)
            url = f"https://text.pollinations.ai/{encoded_prompt}?model=openai"
            
            response = requests.get(url, timeout=10)
            text = response.text.strip() if response.status_code == 200 else "..."
        except:
            text = "..."
        
        self.finished.emit(text)
class Window4(QWidget):
    def __init__(self, name):
        super().__init__()
        self.setWindowTitle(' ')
        self.move(300, 300)
        self.resize(300, 100)
        
        self.username = os.getlogin()
        self.name = name
        self.msg_count = 0 
        
        glitch = 'SPARK_BOT: Привет,' + self.make_zalgo(self.username) +"!" + "Чем я могу сегодня помочь " +  self.make_zalgo("тебе") + '?'

        self.first_message_fromai = QLabel(glitch)
        self.user_message = QLabel('')
        self.text_to_ai = QLineEdit("")
        self.send_button = QPushButton('Отправить')
        

        self.photo_label = QLabel('') 

        self.text_to_ai.setMaxLength(25)
        self.send_button.clicked.connect(self.sendfunction)
        
        self.setWindowFlags(Qt.WindowTitleHint) 
        
        v_line = QVBoxLayout() 
        h_line = QHBoxLayout()
        v_line.addLayout(h_line)
        v_line.addWidget(self.first_message_fromai, alignment = Qt.AlignCenter)
        v_line.addWidget(self.user_message, alignment = Qt.AlignLeft)

        v_line.addWidget(self.photo_label, alignment = Qt.AlignCenter) 
        
        v_line.addWidget(self.text_to_ai, alignment = Qt.AlignLeft)
        v_line.addWidget(self.send_button, alignment = Qt.AlignRight)

        self.setLayout(v_line)
        self.show()
        self.shake_window() 
        self.resize(400, 100)
        self.move(900, 70)
        self.setWindowTitle('SPARK_BOT')
        self.ai_thread = None

    # Метод закрытия текущего окна
    def exitbuttonfunc(self):
        self.close()

    # Функция наложения комбинируемых диакритических знаков для создания эффекта "глючного" текста
    def make_zalgo(self, text): # из интернета взял
        diacritics = [chr(i) for i in range(0x0300, 0x036F)]
        glitched_text = []
        for char in text:
            glitched_text.append(char)
            # Добавление от 3 до 8 случайных знаков поверх каждой буквы
            for _ in range(ran.randint(3, 8)):  
                glitched_text.append(ran.choice(diacritics))  
        return "".join(glitched_text)


    # Функция получения названия текущей Wi-Fi сети через системную команду Windows 'netsh'
    def get_wifi_name(self): #Эту функцию тоже из интернета взял. Нужна чтобы определить wifi юзера
        import subprocess
        try:
            # Вызов консольной команды и декодирование результата в кодировку cp866 (кириллица Windows)
            meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'interfaces']).decode('cp866', errors='ignore')
            for line in meta_data.split('\n'):
                if "SSID" in line and "BSSID" not in line:
                    parts = line.split(":")
                    if len(parts) > 1:
                        wifi_name = parts[1].strip()
                        if wifi_name:  
                            return wifi_name
        except Exception:
            pass
        
        return "???"
        
    # Эффект "хакерской" атаки: заголовок меняется на имя Wi-Fi, окно дёргается, издаёт писк и исчезает на 2 секунды
    def shake_window(self):
        qustionmark ='??'
        multiplymark = 1
        for i in range(5):
            self.setWindowTitle((self.get_wifi_name() + (qustionmark)*multiplymark))
            multiplymark+=1
            self.move(300 + ran.randint(-70, 70), 70 + ran.randint(-40, 40))
            time.sleep(0.005)
        winsound.Beep(1500, 700) # Пронзительный писк частотой 1500 Гц длительностью 0.7 секунды
        winsound.MessageBeep(winsound.MB_ICONHAND) # Системный звук критической ошибки Windows
        self.hide() 
        time.sleep(2) 
        self.show() 
        
    def sendfunction(self):
        self.msg_count += 1
        user_raw_text = self.text_to_ai.text().strip()
        
        if self.msg_count == 3:
            self.user_message.setText("ПОСМОТРИ НА МЕНЯ")
            self.text_to_ai.clear()
            self.first_message_fromai.setText(self.make_zalgo("O_o_O_X_X_X"))
            QApplication.processEvents() 
            time.sleep(1)
            self.scary_event()
            return

  
        if user_raw_text:
            self.user_message.setText(f"{self.name} : {user_raw_text}")
            self.text_to_ai.clear()
            self.first_message_fromai.setText("SPARK_BOT: Думает...")
            self.ai_thread = AIWorker(user_raw_text)
            self.ai_thread.finished.connect(self.update_bot_response)
            self.ai_thread.start()

    def sendfunction(self):
        self.msg_count += 1
        user_raw_text = self.text_to_ai.text().strip()
        

        if self.msg_count == 3:
            self.user_message.setText(f"{self.name} : ПОСМОТРИ НА МЕНЯ")
            self.text_to_ai.clear()
            
            
            self.first_message_fromai.setText(self.make_zalgo("я: ERROR"))
            QApplication.processEvents() #
            time.sleep(5) 
            
            self.scary_event()
            return

        # Обычная работа
        if user_raw_text:
            self.user_message.setText(f"{self.name} : {user_raw_text}")
            self.text_to_ai.clear()
            self.first_message_fromai.setText("SPARK_BOT: Думает...")
            self.ai_thread = AIWorker(user_raw_text)
            self.ai_thread.finished.connect(self.update_bot_response)
            self.ai_thread.start()
    def scary_event(self):
        winsound.MessageBeep(winsound.MB_ICONHAND)
        self.hide() 
        time.sleep(2)
        
        time.sleep(1.5)

        self.setWindowTitle(self.make_zalgo(self.username))
        self.move(500,300) 
        self.show()

        phrases = ["SPARK_BOT: ", "SPARK_BOT: ΓΔΕΖΗ"]
        for i, phrase in enumerate(phrases):
            self.first_message_fromai.setText(phrase)
            

            for _ in range(60):
                intensity = 10 if i == 0 else 55 
                self.move(self.x() + ran.randint(-intensity, intensity), 
                          self.y() + ran.randint(-intensity, intensity))
                winsound.Beep(500, 5)
                time.sleep(0.01)
                QApplication.processEvents()
        time.sleep(0.1)
        winsound.Beep(200, 4000)
        self.close() 
    def update_bot_response(self, ai_text):
        
        glitched_response = "SPARK_BOT: " + ai_text
        
        
        self.first_message_fromai.setText(glitched_response)
        
        
        self.send_button.setEnabled(True)