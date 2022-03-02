''' Course Class for Project 2 of cs2420 '''

class Course:
    ''' Course object '''
    def __init__(self, number=0, name="", credit=0.0, grade=0.0):
        ''' number is int. name is string. credit and grade are floats '''
        if not isinstance(number, int):
            raise ValueError('number must be an int')
        if number < 0:
            raise ValueError('number must not be a negative integer')
        if not isinstance(name, str):
            raise ValueError('name must be a string')
        if not isinstance(credit, float):
            raise ValueError('credit must be a float')
        if credit < 0.0:
            raise ValueError('credit must be a positive float')
        if not isinstance(grade, float):
            raise ValueError('grade must be a float')
        if grade < 0.0 or grade > 4.0:
            raise ValueError('grade must be a positive float from 0.0 to 4.0')
        self.__number = number
        self.__name = name
        self.__credit = credit
        self.__grade = grade
        self.next = None

    def number(self):   #pylint: disable=missing-function-docstring
        return self.__number
    def name(self):     #pylint: disable=missing-function-docstring
        return self.__name
    def credit_hr(self): #pylint: disable=missing-function-docstring
        return self.__credit
    def grade(self): #pylint: disable=missing-function-docstring
        return self.__grade
    def __str__(self): #pylint: disable=missing-function-docstring
        return f"cs{self.number()} {self.name()} Grade:{self.grade()} Credit Hours: {self.credit_hr()}"
