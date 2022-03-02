''' CourseList class for Project 2 of cs2420 '''
from course import Course

class CourseList:
    ''' singly linked list of Course objects '''
    def __init__(self):
        ''' list is created empty '''
        self.head = None

    def insert(self, course):
        ''' course is a Course object. inserts course in assending order in the list '''
        if not isinstance(course, Course):
            raise ValueError(f'Inappropriate type: {type(course)}. A Course is required')

        self.head = self.insert_helper(self.head, course)

    def insert_helper(self, cursor, course):
        if cursor is None:
            return course
        if cursor.number() < course.number():
            cursor.next = self.insert_helper(cursor.next, course)
            return cursor

        course.next = cursor
        return course

    def remove(self, number):
        ''' removes one occurance of a course (by course's number) '''
        if not isinstance(number, int):
            raise ValueError(f'Inappropriate type: {type(number)}. An int is required')
        self.head = self.remove_helper(self.head, number)


    def remove_helper(self, cursor, number):
        ''' recursrion helper. DO NOT CALL DIRECTLY '''

        if cursor is None:
            return None
        if cursor.number() == number:
            return cursor.next

        cursor.next = self.remove_helper(cursor.next, number)
        return cursor

    def remove_all(self, number):
        ''' removes ALL occurances of a course (by course's number) '''
        if not isinstance(number, int):
            raise ValueError(f'Inappropriate type: {type(number)}. An int is required')
        self.head = self.remove_all_helper(self.head, number)

    def remove_all_helper(self, cursor, number):
        if cursor is None:
            return None

        cursor.next = self.remove_all_helper(cursor.next, number)
        if cursor.number() == number:
            # delete thias one
            return cursor.next
        else:
            return cursor


    def find(self, number):
        if not isinstance(number, int):
            raise ValueError(f'Inappropriate type: {type(number)}. An int is required')
        return self.find_helper(self.head, number)

    def find_helper(self, cursor, number):
        if cursor is None:
            return -1
        if cursor.number() == number:
            return cursor
        return self.find_helper(cursor.next, number)

    def size(self):
        return self.size_helper(self.head)

    def size_helper(self, cursor):
        if cursor is None:
            return 0
        return 1 + self.size_helper(cursor.next)

    def is_sorted(self):
        return self.is_sorted_helper(self.head)

    def is_sorted_helper(self, cursor):
        if cursor is None:
            return True
        if cursor.next is None:
            return True
        if cursor.number() > cursor.next.number():
            return False
        return self.is_sorted_helper(cursor.next)

    def calculate_gpa(self):
        grade_points = self.calculate_grade_points(self.head)
        if grade_points == 0.0:
            return 0.0
        total_credits = self.calculate_total_credits(self.head)
        if total_credits == 0.0:
            return 0.0
        return grade_points / total_credits

    def calculate_grade_points(self, cursor):
        if cursor is None:
            return 0.0
        return (cursor.credit_hr() * cursor.grade()) + self.calculate_grade_points(cursor.next)

    def calculate_total_credits(self, cursor):
        if cursor is None:
            return 0.0
        return cursor.credit_hr() + self.calculate_total_credits(cursor.next)

    def __str__(self):  #pylint: disable=missing-function-docstring
        return self.__str__helper(self.head)

    def __str__helper(self, cursor):
        if cursor is None:
            return '\n'
        return str(cursor) + '\n' + self.__str__helper(cursor.next)

    def __iter__(self):
        self.cursor = self.head
        return self

    def __next__(self):
        ''' move iterator to next Course in the linked list '''
        if self.cursor is None:
            raise StopIteration
        else:
            course = self.cursor
            self.cursor = self.cursor.next
            return course
