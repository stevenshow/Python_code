from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QDialogButtonBox, QMainWindow
from PyQt5.uic import loadUi
import os
import sqlite3
#
# 
# TODO Figure out how to browse to a database file the user already has created
# Create a way to parse the data based on a time frame and give results
class MainWindow(QMainWindow):
    # Try to set default date to the current date for ease of entertaining
    # Find out easier way to keep name for multiple entries
    def __init__(self):
        super(MainWindow, self).__init__()
        self.path = os.path.dirname(__file__) + '/'
        loadUi(self.path + 'h_tracker.ui', self)
        self.health_dict = {}
        self.stats = {}
        self.weight = 0.0
        self.calories = 0.0
        self.name = ''
        self.date = ''
        center_align = QtCore.Qt.AlignCenter
        self.date_input.setAlignment(center_align)
        self.date_input.setDateTime(QtCore.QDateTime.currentDateTime())
        self.name_input.setAlignment(center_align)
        self.weight_input.setAlignment(center_align)
        self.calorie_intake.setAlignment(center_align)

class DataWindow(QDialog):
    def __init__(self):
        super(DataWindow, self).__init__()
        self.path = os.path.dirname(__file__) + '/'
        loadUi(self.path + "load_h_tracker.ui", self)
        self.init_buttons()
        

    def init_buttons(self):
        self.browse.clicked.connect(self.browsefiles)
        self.exit.clicked.connect(lambda: self.close())

    def browsefiles(self):
        # QFileDialog(self, Window Name, Default FN Opener, Accepted Files)
        fname = QFileDialog.getOpenFileName(self, 'Open File', self.path, 'sqlite3 files (*.sqlite3)')
        self.filename.setText(fname[0])

    def save_data(self):
        # Placeholder until I can figure out how to store data into database correctly
        self.date = self.date_input.text()
        self.weight = self.weight_input.text()
        self.calories = self.calorie_input.text()
        self.name = self.name_input.text()
        self.stats[self.date] = [self.weight, self.calories]
        self.health_dict[self.name] = self.stats
        self.db_path = os.path.join(self.path, f'{self.name.lower()}_trackerdb.sqlite3')
        
        self.connection = sqlite3.connect(self.db_path)
        print('h_trackerdb created successfully!')
        self.cursor = self.connection.cursor()
        
        # Checks to make sure the table does not already exist
        listOfTables = self.cursor.execute(
        """SELECT * FROM sqlite_master WHERE type='table'; """).fetchall()       
        if (listOfTables == []):        
            self.cursor.execute('''CREATE TABLE health_stats (
                    name TEXT,
                    weight REAL,
                    calories REAL,
                    date TEXT
                    )''')
        if self.name == '' or any(char.isdigit() for char in self.name):
            self.dlg = QtWidgets.QDialog(self.centralwidget)
            self.dlg.setWindowTitle('Please Enter a valid Name')
            self.dlg.resize(300,30)
            self.dlg.exec_()
        elif self.weight.isdigit() == False:
            self.dlg = QtWidgets.QDialog(self.centralwidget)
            self.dlg.setWindowTitle('Invalid weight entry!')
            self.dlg.resize(300,30)
            self.dlg.exec_()
        elif self.calories.isdigit() == False:
            self.dlg = QtWidgets.QDialog(self.centralwidget)
            self.dlg.setWindowTitle('Invalid calorie entry!')
            self.dlg.resize(300,30)
            self.dlg.exec_()
        else:
            print(self.health_dict)
            self.cursor.execute('''INSERT INTO health_stats VALUES (?,?,?,?)''', (self.name.lower(), self.weight, self.calories, self.date))
            self.instruction.setText(f'Successfully saved data for {self.name}!')
            print('Data has been saved!')
            print(self.name, self.weight, self.calories, self.date)
            self.connection.commit()
            self.connection.close()

    def open_file_window(self):
        print("Opened file!")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    DataWindow = DataWindow()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(MainWindow)
    widget.addWidget(DataWindow)
    widget.setFixedHeight(400)
    widget.setFixedWidth(450)
    widget.show()
    sys.exit(app.exec_())
