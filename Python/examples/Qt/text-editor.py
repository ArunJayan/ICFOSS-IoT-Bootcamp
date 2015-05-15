from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

app_obj = QApplication(sys.argv)

window = QMainWindow()
window.resize(800,600)

text = QTextEdit(window)
text.resize(600,500)

#now we have to define the action
open = QAction(QIcon('exit.png'), '&Exit', window)
open.setShortcut('Ctrl+Q')
open.setStatusTip('Exit application')
open.triggered.connect(qApp.quit)
window.statusBar()
menubar = window.menuBar()
fileMenu = menubar.addMenu('&File')
fileMenu.addAction(open)
window.show()
sys.exit(app_obj.exec_())