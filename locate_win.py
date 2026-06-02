from PyQt5.QtCore import Qt,QTimer,QLocale, QRegularExpression
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton,QLabel,QVBoxLayout, QLineEdit
import random as ran
import time
import third_win
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QRegularExpressionValidator
import os
import locale
import socket
import platform


class Window5(QWidget):
    def __init__(self):
        super().__init__()
        self.show()
        self.setWindowTitle('Локация')
        self.resize(600, 400)
        

        location_qt = QLabel('Локация')
        user_location_txt = self.get_system_country()
        user_local_ip_txt = self.get_local_ip()
        user_get_processor_name_txt = self.get_processor_name()

        user_get_processor_name_qt = QLabel(user_get_processor_name_txt)
        user_location_qt = QLabel(user_location_txt)
        user_local_ip_qt = QLabel(user_local_ip_txt)


        #self.reg_button.clicked.connect(self.showthirdwin)

        self.setWindowFlags(Qt.WindowTitleHint) 


        v_line = QVBoxLayout()
        v_line.addWidget(location_qt, alignment = Qt.AlignCenter)
        v_line.addWidget(user_location_qt, alignment = Qt.AlignCenter)
        v_line.addWidget(user_local_ip_qt, alignment = Qt.AlignCenter)
        v_line.addWidget(user_get_processor_name_qt, alignment = Qt.AlignCenter)

        self.setLayout(v_line)
        self.show()


        # regex = QRegularExpression("^[a-zA-Zа-яА-ЯёЁ]+$")

        # validator = QRegularExpressionValidator(regex)

        # self.login_hint.setValidator(validator)


        # self.login_hint.setMaxLength(20)     
        # self.password_hint.setMaxLength(10)  

    
    def get_system_country(self):
        try:
            # Получаем настройки локали по умолчанию
            lang_code, _ = locale.getdefaultlocale()

            # Если значение не найдено, пробуем альтернативный метод для POSIX-систем
            if not lang_code:
                lang_code = (
                    os.environ.get("LANG")
                    or os.environ.get("LC_ALL")
                    or os.environ.get("LC_CTYPE")
                )

            if lang_code:
                # Локаль обычно имеет вид 'ru_RU' или 'en_US.UTF-8'
                # Разделяем строку, чтобы достать код страны после подчеркивания
                parts = lang_code.split(".")[0].split("_")
                if len(parts) > 1:
                    return parts[1].upper()  # Возвращает двухбуквенный код (RU, US)

        except Exception:
            pass

        return "UNKNOWN"
    def get_local_ip(self):
        try:
            # Создаем фиктивное подключение для определения активного сетевого интерфейса
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            local_ip = s.getsockname()[0]
            s.close()
            return local_ip
        except Exception:
            return "127.0.0.1"

    def get_processor_name(self):
        return platform.processor() or "UNKNOWN"