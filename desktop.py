from PyQt5.QtCore import *
#Подключение виджетов приложения,надписи,вертикальной линии,окна,кнопки
from PyQt5.QtWidgets import QApplication,QLabel,QVBoxLayout,QWidget,QPushButton
import instr
from secondwindow import *
#Создание приложения
current = 0
app = QApplication([])
#Создание окна
class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.appear()
        self.initUi()
        self.connects()
        self.show()
    def appear(self):
        self.setWindowTitle(instr.txt_title)
        self.resize(800,600)
    def initUi(self):
        self.label = QLabel(instr.txt_hello)
        self.label2 = QLabel(instr.txt_instruction)
        self.button = QPushButton(instr.txt_next)
        #Создание вертикальной линии
        self.vlayout = QVBoxLayout()
        #Добавление к ней виджета и положения относительно неё
        self.vlayout.addWidget(self.label,0,alignment=Qt.AlignLeft)
        self.vlayout.addWidget(self.label2,0,alignment=Qt.AlignLeft)
        self.vlayout.addWidget(self.button,0,alignment=Qt.AlignHCenter)
        self.setLayout(self.vlayout)
    def connects(self):
        self.button.clicked.connect(self.changewindow)
    def changewindow(self):
        self.hide()
        self.sw = SecondWindow()
        
window = MainWindow()
#Не закрывать приложение пока не нажата кнопка выйти
app.exec_()