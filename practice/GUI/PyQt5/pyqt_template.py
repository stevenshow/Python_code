import sys

from PyQt5 import QtCore as qtc  # Low level (signals, slots)
from PyQt5 import QtGui as qtg  # Relate to GUI fonts, colors, etc
from PyQt5 import QtWidgets as qtw  # Widgets and layouts

class MainWindow(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Your code will go here


        # Your code ends here
        self.show()

if __name__ == "__main__":  # Only run this code if you are running this script specifically and not importing
    app = qtw.QApplication(sys.argv) # Always the first thing run 
    w = MainWindow(windowTitle='Hello World')
    sys.exit(app.exec_())
