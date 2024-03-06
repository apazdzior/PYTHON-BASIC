"""
Write tests for a read_numbers function.
It should check successful and failed cases
for example:
Test if user inputs: 1, 2, 3, 4
Test if user inputs: 1, 2, Text

Tip: for passing custom values to the input() function
Use unittest.mock patch function
https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch

TIP: for testing builtin input() function create another function which return input() and mock returned value
"""
from task_input_output import read_numbers
from unittest.mock import patch

def mock_input(mock_values):
    return lambda _: mock_values.pop(0)

@patch('builtins.input', side_effect=mock_input(["10", "20", "30", ""]))
def test_read_numbers_with_valid_inputs(mock_input):
    result = read_numbers(3)
    assert result == "Avg: 20.00"

@patch('builtins.input', side_effect=mock_input([""] * 3))
def test_read_numbers_with_no_inputs(mock_input):
    result = read_numbers(3)
    assert result == "No numbers entered"

@patch('builtins.input', side_effect=mock_input(["abc", "20", "30", ""]))
def test_read_numbers_with_invalid_inputs(mock_input):
    result = read_numbers(3)
    assert result == "Avg: 25.00"

@patch('builtins.input', side_effect=mock_input(["abc", "20", "def", ""]))
def test_read_numbers_with_mixed_inputs(mock_input):
    result = read_numbers(3)
    assert result == "Avg: 20.00"

@patch('builtins.input', side_effect=mock_input(["0", "0", "0", ""]))
def test_read_numbers_with_zero_inputs(mock_input):
    result = read_numbers(3)
    assert result == "Avg: 0.00"

@patch('builtins.input', side_effect=mock_input(["-10", "-20", "-30", ""]))
def test_read_numbers_with_negative_inputs(mock_input):
    result = read_numbers(3)
    assert result == "Avg: -20.00"