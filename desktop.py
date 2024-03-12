from PyQt5.QtCore import *
#Подключение виджетов приложения,надписи,вертикальной линии,окна,кнопки
from PyQt5.QtWidgets import QApplication,QLabel,QVBoxLayout,QWidget,QPushButton
#Создание приложения
app = QApplication([])
#Создание окна
window = QWidget()
#Создание кнопки с надписью
button = QPushButton('Кнопка с секретом')
#Показ окна(По умолчанию окна скрыты)
window.show()
#Создание надписи с текстом
label = QLabel('Ты просто чудо')
label2 = QLabel('Ты просто чудо')
#Создание вертикальной линии
vlayout = QVBoxLayout()
#Добавление к ней виджета и положения относительно неё
vlayout.addWidget(label,0,alignment=Qt.AlignLeft)
vlayout.addWidget(label2,0,alignment=Qt.AlignLeft)
vlayout.addWidget(button,0,alignment=Qt.AlignHCenter)
#Добавление линии в окно
window.setLayout(vlayout)
#Функция для показа надписи
def show_label():
    label.show()
#Обработка функции по нажатию на кнопку
button.clicked.connect(show_label)
#Не закрывать приложение пока не нажата кнопка выйти
app.exec_()