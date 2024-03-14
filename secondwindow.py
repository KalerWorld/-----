from PyQt5.QtCore import *
#Подключение виджетов приложения,надписи,вертикальной линии,окна,кнопки
from PyQt5.QtWidgets import QApplication,QLabel,QVBoxLayout,QWidget,QPushButton,QLineEdit,QHBoxLayout
import instr
from thirdwindow import *
class SecondWindow(QWidget):
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
        #Имя
        self.name = QLabel(instr.txt_name)
        self.nameEdit = QLineEdit()
        #Возраст
        self.age = QLabel(instr.txt_age)
        self.ageEdit = QLineEdit()
        #1 Тест
        self.test1 = QLabel(instr.txt_test1)
        self.test1edit = QLineEdit(instr.txt_hinttest1)
        self.test1btn = QPushButton(instr.txt_starttest1)
        #2 Тест
        self.test2 = QLabel(instr.txt_test2)
        self.test2edit = QLineEdit(instr.txt_hinttest2)
        self.test2btn = QPushButton(instr.txt_starttest2)
        #3 Тест
        self.test3 = QLabel(instr.txt_test3)
        self.test3edit = QLineEdit(instr.txt_hinttest3)
        self.test3btn = QPushButton(instr.txt_starttest3)
        #Кнопка для перехода к 3 экрану
        self.button = QPushButton(instr.txt_sendresults)
        self.timer = QLabel('0')
        self.vlayout = QVBoxLayout()
        self.vlayout2 = QVBoxLayout()
        self.hlayout = QHBoxLayout()
        self.vlayout.addWidget(self.name,0,Qt.AlignLeft)
        self.vlayout.addWidget(self.nameEdit,0,Qt.AlignLeft)
        self.vlayout.addWidget(self.age,0,Qt.AlignLeft)
        self.vlayout.addWidget(self.ageEdit,0,Qt.AlignLeft)
        self.vlayout.addWidget(self.test1,0,Qt.AlignLeft)
        self.vlayout.addWidget(self.test1btn,0,Qt.AlignLeft)
        self.vlayout.addWidget(self.test1edit,0,Qt.AlignLeft)
        self.vlayout.addWidget(self.test2,0,Qt.AlignLeft)
        self.vlayout.addWidget(self.test2btn,0,Qt.AlignLeft)
        self.vlayout.addWidget(self.test2edit,0,Qt.AlignLeft)
        self.vlayout.addWidget(self.test3,0,Qt.AlignLeft)
        self.vlayout.addWidget(self.test3btn,0,Qt.AlignLeft)
        self.vlayout.addWidget(self.test3edit,0,Qt.AlignLeft)
        self.vlayout.addWidget(self.button,0,Qt.AlignRight)
        self.vlayout2.addWidget(self.timer,0,Qt.AlignRight)
        self.hlayout.addLayout(self.vlayout)
        self.hlayout.addLayout(self.vlayout2)
        self.setLayout(self.hlayout)
    def connects(self):
        self.button.clicked.connect(self.changewindow)
    def changewindow(self):
        self.hide()
        self.tw = ThirdWindow()


