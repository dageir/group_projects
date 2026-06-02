# напиши здесь код третьего экрана приложения
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QFileDialog, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class ImageLoader(QWidget):

def main():
    # Создаем объект приложения
    app = QApplication(sys.argv)

    # Создаем главное окно
    window = QWidget()
    window.setWindowTitle()
    window.resize(600, 400)

    # Создаем виджеты
    image_label = QLabel()
    image_label.setAlignment(Qt.AlignCenter)
    image_label.setStyleSheet("border: 1px solid gray;")

    load_button = QPushButton()

    # Размещаем виджеты в окне
    layout = QVBoxLayout(window)
    layout.addWidget(image_label)
    layout.addWidget(load_button)

    # Определяем действие для кнопки (вложенная функция для наглядности)
    def on_load_click():
        file_name, _ = QFileDialog.getOpenFileName(
            window, "67.jpg", "", ""
        )
        if file_name:
            pixmap = QPixmap(file_name)
            if not pixmap.isNull():
                # Масштабируем изображение под размер лейбла с сохранением пропорций
                scaled_pixmap = pixmap.scaled(
                    image_label.size(),
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation
                )
                image_label.setPixmap(scaled_pixmap)
                image_label.setText("")
            else:
                image_label.setText("Не удалось загрузить изображение.")

    # Связываем сигнал нажатия кнопки с нашей функцией
    load_button.clicked.connect(on_load_click)

    # Отображаем окно и запускаем цикл обработки событий
    window.show()
    sys.exit(app.exec_())