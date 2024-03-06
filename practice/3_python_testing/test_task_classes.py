"""
Write tests for classes in 2_python_part_2/task_classes.py (Homework, Teacher, Student).
Check if all methods working correctly.
Also check corner-cases, for example if homework number of days is negative.
"""

import datetime
from unittest.mock import patch
from task_classes import Teacher, Student, Homework 

def test_teacher():
    teacher = Teacher('Dmitry', 'Orlyakov')
    homework = teacher.create_homework('Learn functions', 3)

    assert homework.text == 'Learn functions'
    assert homework.deadline == datetime.timedelta(days=3)
    assert teacher.first_name == 'Dmitry'
    assert teacher.last_name == 'Orlyakov'

def test_student():
    student = Student('Vladislav', 'Popov')
    teacher = Teacher('Dmitry', 'Orlyakov')
    homework = teacher.create_homework('Learn functions', 3)

    result = student.do_homework(homework) 
    assert result == homework

def is_active():
    return False

def test_student2():
    student = Student('Vladislav', 'Popov')
    teacher = Teacher('Dmitry', 'Orlyakov')
    homework = teacher.create_homework('Learn functions', 0)
    homework.is_active = is_active
    result = student.do_homework(homework) 
    assert result == None

def test_homework():
    homework = Homework('Learn functions', 2)
    assert homework.is_active() == True

def test_homework2():
    homework = Homework('Learn functions', 0)
    assert homework.is_active() == False
