import pytest
from tda_racional_1022.tda_racional import run_challenge
from unittest.mock import patch

input_invalid_expression_math = ['1 / 2 * 3 - 4', ' abcd ']
@pytest.fixture
def mock_empty_input():
    with patch('builtins.input', return_value=''):
        yield

@pytest.fixture
def mock_input_with_zero_use_case():
    with patch('builtins.input', return_value='0'):
        yield

def test_run_challenge_raise_exception_when_enter_empty_entry(mock_empty_input):
    with pytest.raises(Exception): # Set a way to capture exception in this test
        run_challenge() # Run Challenge

def test_run_challenge_raise_exception_when_enter_with_zero_use_case(mock_input_with_zero_use_case):
    with pytest.raises(Exception): # Set a way to capture exception in this test
        run_challenge() # Run Challenge

def test_run_challenge_raise_exception_when_provided_use_case_without_operation():
    mock_inputs = iter(["1", ""]) # Set reply strings for mock function
    with pytest.raises(ValueError): # Set a way to capture exception in this test
        with patch('builtins.input', lambda: next(mock_inputs)): # Mock input function
            run_challenge() # Run Challenge

def test_run_challenge_raise_exception_when_provided_invalid_operation():
    mock_inputs = iter(['1','1/2 * 3/4']) # Mock output without space in racional number
    with pytest.raises(ValueError): # Set a way to capture exception in this test
        with patch('builtins.input', lambda: next(mock_inputs)): # Mock input function
            run_challenge() # Run Challenge

    mock_inputs = iter(['1', '1 / 2 // 3 / 4']) # Mock output with invalid operator - //
    with pytest.raises(ValueError): # Set a way to capture exception in this test
        with patch('builtins.input', lambda: next(mock_inputs)): # Mock input function
            run_challenge() # Run Challenge

    mock_inputs = iter(['1', 'invalid expression']) # Mock output with invalid expression math
    with pytest.raises(ValueError): # Set a way to capture exception in this test
        with patch('builtins.input', lambda: next(mock_inputs)): # Mock input function
            run_challenge() # Run Challenge

def test_run_challenge_with_valid_expressions_math():
    mock_inputs = iter(['4','1 / 2 + 3 / 4','1 / 2 - 3 / 4','2 / 3 * 6 / 6','1 / 2 / 3 / 4']) # Mock output without space in racional number
    with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
        with patch('builtins.print') as mock_print: # Mock print function
            run_challenge() # Run Challenge
            mock_print.assert_any_call('10/8 = 5/4') # Check if first result provided by run_challenge is correct answer
            mock_print.assert_any_call('-2/8 = -1/4') # Check if second result provided by run_challenge is correct answer
            mock_print.assert_any_call('12/18 = 2/3') # Check if third result provided by run_challenge is correct answer
            mock_print.assert_any_call('4/6 = 2/3') # Check if fourth result provided by run_challenge is correct answer

