from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sqlite3
#
# 
# TODO Figure out how to save the database file in a user specified location
# and figure out how to browse to a database file the user already has created

class Ui_SecondWindow(object):
    def __init__(self):
        self.path = os.path.dirname(__file__) + '/'

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")

        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.instruction = QtWidgets.QLabel(self.centralwidget)
        self.instruction.setGeometry(QtCore.QRect(200, 60, 300, 20))
        self.instruction.setObjectName("instruction")
        self.instruction.setText('Enter in your stats below then press save')

        self.name_input = QtWidgets.QLineEdit(self.centralwidget)
        self.name_input.setGeometry(QtCore.QRect(290, 120, 131, 28))
        self.name_input.setObjectName("name_input")
        self.name_label = QtWidgets.QLabel(self.centralwidget)
        self.name_label.setGeometry(QtCore.QRect(220, 124, 58, 16))
        self.name_label.setObjectName("name_label")

        self.weight_input = QtWidgets.QLineEdit(self.centralwidget)
        self.weight_input.setGeometry(QtCore.QRect(290, 162, 131, 28))
        self.weight_input.setObjectName("weight_input")
        self.weight_label = QtWidgets.QLabel(self.centralwidget)
        self.weight_label.setGeometry(QtCore.QRect(220, 160, 51, 31))
        self.weight_label.setObjectName("weight_label")

        self.calorie_input = QtWidgets.QLineEdit(self.centralwidget)
        self.calorie_input.setGeometry(QtCore.QRect(290, 202, 131, 28))
        self.calorie_input.setObjectName("calorie_input")
        self.calorie_label = QtWidgets.QLabel(self.centralwidget)
        self.calorie_label.setGeometry(QtCore.QRect(219, 202, 61, 27))
        self.calorie_label.setObjectName("calorie_label")

        self.date_input = QtWidgets.QDateEdit(self.centralwidget)
        self.date_input.setGeometry(QtCore.QRect(290, 242, 131, 24))
        self.date_input.setObjectName("date_input")
        self.date_label = QtWidgets.QLabel(self.centralwidget)
        self.date_label.setGeometry(QtCore.QRect(220, 247, 48, 16))
        self.date_label.setObjectName("date_label")

        self.Save_button = QtWidgets.QPushButton(self.centralwidget)
        self.Save_button.setGeometry(QtCore.QRect(530, 400, 85, 28))
        self.Save_button.setObjectName("Save_button")
        self.Save_button.clicked.connect(lambda: MainWindow.close())
        self.Exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.Exit_button.setGeometry(QtCore.QRect(440, 400, 85, 28))
        self.Exit_button.setObjectName("Exit_button")
        self.Exit_button.clicked.connect(lambda:MainWindow.close())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Health Tracker"))
        self.Save_button.setText(_translate("MainWindow", "Load"))
        self.Exit_button.setText(_translate("MainWindow", "Exit"))
        self.date_label.setText(_translate("MainWindow", "Date"))
        self.calorie_label.setText(_translate("MainWindow", "Calories"))
        self.weight_label.setText(_translate("MainWindow", "Weight"))
        self.name_label.setText(_translate("MainWindow", "Name"))
    

        


class Ui_MainWindow(object):
    def __init__(self):
        self.health_dict = {}
        self.stats = {}
        self.weight = 0.0
        self.calories = 0.0
        self.name = ''
        self.date = ''
        self.path = os.path.dirname(__file__) + '/'

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")

        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.instruction = QtWidgets.QLabel(self.centralwidget)
        self.instruction.setGeometry(QtCore.QRect(200, 60, 300, 20))
        self.instruction.setObjectName("instruction")
        self.instruction.setText('Enter in your stats below then press save')

        self.name_input = QtWidgets.QLineEdit(self.centralwidget)
        self.name_input.setGeometry(QtCore.QRect(290, 120, 131, 28))
        self.name_input.setObjectName("name_input")
        self.name_label = QtWidgets.QLabel(self.centralwidget)
        self.name_label.setGeometry(QtCore.QRect(220, 124, 58, 16))
        self.name_label.setObjectName("name_label")

        self.weight_input = QtWidgets.QLineEdit(self.centralwidget)
        self.weight_input.setGeometry(QtCore.QRect(290, 162, 131, 28))
        self.weight_input.setObjectName("weight_input")
        self.weight_label = QtWidgets.QLabel(self.centralwidget)
        self.weight_label.setGeometry(QtCore.QRect(220, 160, 51, 31))
        self.weight_label.setObjectName("weight_label")

        self.calorie_label = QtWidgets.QLabel(self.centralwidget)
        self.calorie_label.setGeometry(QtCore.QRect(219, 202, 61, 27))
        self.calorie_label.setObjectName("calorie_label")
        self.calorie_input = QtWidgets.QLineEdit(self.centralwidget)
        self.calorie_input.setGeometry(QtCore.QRect(290, 202, 131, 28))
        self.calorie_input.setObjectName("calorie_input")

        self.date_input = QtWidgets.QDateEdit(self.centralwidget)
        self.date_input.setGeometry(QtCore.QRect(290, 242, 131, 24))
        self.date_input.setObjectName("date_input")
        self.date_label = QtWidgets.QLabel(self.centralwidget)
        self.date_label.setGeometry(QtCore.QRect(220, 247, 48, 16))
        self.date_label.setObjectName("date_label")

        self.Save_button = QtWidgets.QPushButton(self.centralwidget)
        self.Save_button.setGeometry(QtCore.QRect(530, 400, 85, 28))
        self.Save_button.setObjectName("Save_button")
        self.Save_button.clicked.connect(self.save_data)
        self.Exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.Exit_button.setGeometry(QtCore.QRect(350, 400, 85, 28))
        self.Exit_button.setObjectName("Exit_button")
        self.Exit_button.clicked.connect(lambda:MainWindow.close())
        self.Load_button = QtWidgets.QPushButton(self.centralwidget)
        self.Load_button.setGeometry(QtCore.QRect(440, 400, 85, 28))
        self.Load_button.setObjectName("Load_button")
        self.Load_button.clicked.connect(self.open_file_window)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Health Tracker"))
        self.Load_button.setText(_translate("Load_button", "Load"))
        self.Save_button.setText(_translate("MainWindow", "Save"))
        self.Exit_button.setText(_translate("MainWindow", "Exit"))
        self.date_label.setText(_translate("MainWindow", "Date"))
        self.calorie_label.setText(_translate("MainWindow", "Calories"))
        self.weight_label.setText(_translate("MainWindow", "Weight"))
        self.name_label.setText(_translate("MainWindow", "Name"))

    # def setupUi2(self, MainWindow):
    #     MainWindow.setObjectName("MainWindow")

    #     MainWindow.resize(640, 480)
    #     self.centralwidget = QtWidgets.QWidget(MainWindow)
    #     self.centralwidget.setObjectName("centralwidget")
    #     MainWindow.setCentralWidget(self.centralwidget)
    #     self.menubar = QtWidgets.QMenuBar(MainWindow)
    #     self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
    #     self.menubar.setObjectName("menubar")
    #     MainWindow.setMenuBar(self.menubar)
    #     self.statusbar = QtWidgets.QStatusBar(MainWindow)
    #     self.statusbar.setObjectName("statusbar")
    #     MainWindow.setStatusBar(self.statusbar)

    #     self.instruction = QtWidgets.QLabel(self.centralwidget)
    #     self.instruction.setGeometry(QtCore.QRect(200, 60, 300, 20))
    #     self.instruction.setObjectName("instruction")
    #     self.instruction.setText('Enter in your stats below then press save')

    #     self.name_input = QtWidgets.QLineEdit(self.centralwidget)
    #     self.name_input.setGeometry(QtCore.QRect(290, 120, 85, 25))
    #     self.name_input.setObjectName("file_input")
    #     self.name_label = QtWidgets.QLabel(self.centralwidget)
    #     self.name_label.setGeometry(QtCore.QRect(220, 124, 58, 16))
    #     self.name_label.setObjectName("file_label")

    #     self.Load_button = QtWidgets.QPushButton(self.centralwidget)
    #     self.Load_button.setGeometry(QtCore.QRect(530, 400, 85, 28))
    #     self.Load_button.setObjectName("Load_button")
    #     self.Load_button.clicked.connect(lambda: MainWindow.close())
    #     self.Exit_button = QtWidgets.QPushButton(self.centralwidget)
    #     self.Exit_button.setGeometry(QtCore.QRect(440, 400, 85, 28))
    #     self.Exit_button.setObjectName("Exit_button")
    #     self.Exit_button.clicked.connect(lambda:MainWindow.close())
    #     self.retranslateUi2(MainWindow)
    #     QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # def retranslateUi2(self, MainWindow):
    #     _translate = QtCore.QCoreApplication.translate
    #     MainWindow.setWindowTitle(_translate("MainWindow", "Health Tracker"))
    #     self.Load_button.setText(_translate("MainWindow", "Load"))
    #     self.Exit_button.setText(_translate("MainWindow", "Exit"))
    #     self.date_label.setText(_translate("MainWindow", "Date"))
    #     self.calorie_label.setText(_translate("MainWindow", "Calories"))
    #     self.weight_label.setText(_translate("MainWindow", "Weight"))
    #     self.name_label.setText(_translate("MainWindow", "Name"))

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
        ui.setupUi2(MainWindow)
        MainWindow.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
