from PyQt5.QtCore import *
#Подключение виджетов приложения,надписи,вертикальной линии,окна,кнопки
from PyQt5.QtWidgets import QApplication,QLabel,QVBoxLayout,QWidget,QPushButton
import instr
class ThirdWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.appear()
        self.initUi()
        self.show()
    def appear(self):
        self.setWindowTitle(instr.txt_title)
        self.resize(800,600)
    def initUi(self):
        self.label = QLabel(instr.txt_index)
        self.label2 = QLabel(instr.txt_workheart)
        self.vlayout2 = QVBoxLayout()
        self.vlayout2.addWidget(self.label)
        self.vlayout2.addWidget(self.label2)
        self.setLayout(self.vlayout2)
    

