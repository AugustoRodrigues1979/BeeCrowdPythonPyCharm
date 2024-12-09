import random

import pytest
from estiagem_1023.estiagem import run_challenge, radix_sort
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


@pytest.fixture
def mock_input_with_negative_amount_use_case():
    with patch('builtins.input', return_value='-1'):
        yield


def check_ordered_list(arr_list):
    if len(arr_list) == 0:
        return True
    for k in range(0, len(arr_list) - 1):
        previous_value = arr_list[k]
        for i in range(k + 1, len(arr_list)):
            last_value = arr_list[i]
            if previous_value > last_value:
                print('previous_value:', k, " == ", previous_value)
                print('last_value:', i, " == ", last_value)
                return False
    return True


def test_run_challenge_dont_show_output_when_provided_zero_use_case(mock_input_with_zero_use_case):
    with patch('builtins.print') as mock_print:  # Mock print function
        run_challenge()  # Run Challenge
        assert mock_print.call_count == 0


def test_run_challenge_show_correct_output_when_provided_info_consumption_for_one_group_of_persons():
    mock_inputs = iter([
        "1", "9 90",  # Use case with valid amount of residents by house with consumption less than zero
        "0"
    ])
    expected_output = 'Cidade# 1:\n9-10\nConsumo medio: 10.00 m3.'
    actual_output = ''
    with patch('builtins.print') as mock_print:  # Mock print function
        with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
            run_challenge()  # Run Challenge
            actual_output += mock_print.call_args.args[0]

    assert actual_output == expected_output


def test_run_challenge_show_correct_output_when_provided_info_consumption_for_third_group_of_persons():
    mock_inputs = iter([
        "3", "3 22", "2 11", "3 39",  # Use case with 3 use case when each contain valid amount of person and valid consumption
        "0"
    ])
    expected_output = 'Cidade# 1:\n2-5 3-7 3-13\nConsumo medio: 9.00 m3.'
    actual_output = ''
    with patch('builtins.print') as mock_print:  # Mock print function
        with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
            run_challenge()  # Run Challenge
            actual_output += mock_print.call_args.args[0]

    assert actual_output == expected_output


def test_run_challenge_show_correct_output_when_provided_common_consumption_between_groups_of_person():
    mock_inputs = iter([
        "5", "1 25", "2 20", "3 31", "2 40", "6 70",  # Use case with 3 use case when each contain valid amount of person and valid consumption
        "0"
    ])

    expected_output = 'Cidade# 1:\n5-10 6-11 2-20 1-25\nConsumo medio: 13.28 m3.'
    actual_output = ''
    with patch('builtins.print') as mock_print:  # Mock print function
        with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
            run_challenge()  # Run Challenge
            actual_output += mock_print.call_args.args[0]

    assert actual_output == expected_output


def test_run_challenge_show_correct_output_when_provided_example_from_judge_beecrowd():
    mock_inputs = iter([
        "3", "3 22", "2 11", "3 39",
        "5", "1 25", "2 20", "3 31", "2 40", "6 70",
        "2", "1 1", "3 2",
        "0"
    ])

    expected_output = ''
    expected_output += "Cidade# 1:\n2-5 3-7 3-13\nConsumo medio: 9.00 m3.\n\n"
    expected_output += "Cidade# 2:\n5-10 6-11 2-20 1-25\nConsumo medio: 13.28 m3.\n\n"
    expected_output += "Cidade# 3:\n3-0 1-1\nConsumo medio: 0.75 m3."

    actual_output = ''
    with patch('builtins.print') as mock_print:  # Mock print function
        with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
            run_challenge()  # Run Challenge
            actual_output += mock_print.call_args.args[0]

    assert actual_output == expected_output

def test_radix_sort_with_large_info_city_list_provided_by_collect_data_city():
    info_city_lst = [random.randint(0, 10 ** 12 - 1) for _ in range(10 ** 3)]
    max_value = max(info_city_lst)
    radix_sort(info_city_lst, max_value)
    is_list_ordered = check_ordered_list(info_city_lst)
    assert is_list_ordered

