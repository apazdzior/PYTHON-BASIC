"""
Write tests for division() function in 2_python_part_2/task_exceptions.py
In case (1,1) it should check if exception were raised
In case (1,0) it should check if return value is None and "Division by 0" printed
If other cases it should check if division is correct

TIP: to test output of print() function use capfd fixture
https://stackoverflow.com/a/20507769
"""

from task_exceptions import division

def test_division_ok(capfd):
    result = division(6, 2)
    captured, err = capfd.readouterr()
    assert result == 3
    assert captured == "Division finished\n"


def test_division_by_zero(capfd):
    result = division(6, 0)
    captured, err = capfd.readouterr()
    assert result == None
    assert captured == "Division by 0\nDivision finished\n"


def test_division_by_one(capfd):
    result = division(6, 1)
    captured, err = capfd.readouterr()
    assert captured == "Deletion on 1 get the same result\nDivision finished\n"
