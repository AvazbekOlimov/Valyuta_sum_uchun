from PyQt6.QtWidgets import *
from PyQt6 import QtCore, QtGui
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import sys
class Window(QMainWindow):
	def __init__(self):
		super().__init__()		
		self.setWindowTitle("Valyuta")
		self.setGeometry(100, 100, 500, 400)
		self.UiComponents()
		self.show()
		
	def UiComponents(self):
		line_edit = QLineEdit(self)
		line_edit.setGeometry(165, 150, 150, 40)
		dol = QPushButton(f"$ Dollar",self)
		dol.setGeometry(130,70,75,30)
		rubl = QPushButton(f"₽ Rubl",self)
		rubl.setGeometry(205,70,75,30)
		euro = QPushButton(f"€ Euro",self)
		euro.setGeometry(280,70,75,30)
		label = QLabel(self)
		label.setGeometry(180, 250, 120, 25)
		label.setWordWrap(True)
		
		self.setStyleSheet("""
            Window{
                background: rgb(34, 40, 49);
            }
            QPushButton{
                background: rgb(57, 62, 70);
                color: rgb(0, 173, 181);
                margin-right: 5px;
                border-radius: 20px;                
            }
            QLineEdit{
                background: rgb(238, 238, 238);
		        color: rgb(0, 173, 181);
                font-weight: 700;
            }
            QLabel{
                background: rgb(238, 238, 238);
                color: rgb(0, 173, 181);
                margin-right: 5px;
                font-weight: 700;
            }
        """)
		def turn_to_dollar():
			value = line_edit.text()
			value = int(value) * 11360
			label.setText(str(value)+'$')
		dol.clicked.connect(turn_to_dollar)
		def turn_to_rubl():
			value = line_edit.text()
			value = int(value) * 130
			label.setText(str(value)+'₽')
		rubl.clicked.connect(turn_to_rubl)	
		def turn_to_euro():
			value = line_edit.text()
			value = int(value) * 11600
			label.setText(str(value)+'€')		
		euro.clicked.connect(turn_to_euro)	
        
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
