import unittest
from unittest.mock import patch
from identificando_cha_2006.identificando_cha import run_challenge


def read_input_file(filename_str):
    with open(filename_str, 'r') as file:
        file_content = file.read()  # Read all contents, including '\n', and store them in a single string

    return file_content

def join_all_results(mock_print):
    result = ''
    for i in range(len(mock_print.call_args_list)):
        result += mock_print.call_args_list[i][0][0]
        if 'end' in mock_print.call_args_list[i].kwargs:
            result += mock_print.call_args_list[i].kwargs['end']
        else:
            if i != len(mock_print.call_args_list) - 1:
                result += '\n'

    return result


class MyTestCase(unittest.TestCase):
    def test_challenge_with_invalid_minimal_amount_tea(self):
        invalid_amount_tea_lst = ['0', '1 2 2 3 1']
        mock_inputs = iter(invalid_amount_tea_lst)
        expected_calls = 0
        with patch('builtins.print') as mock_print:  # Mock print function
            with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
                run_challenge()  # Run Challenge
                actual_calls = mock_print.call_count
        self.assertEqual(expected_calls, actual_calls)

    def test_challenge_with_invalid_maximal_amount_tea(self):
        invalid_amount_tea_lst = ['5', '1 2 2 3 1']
        mock_inputs = iter(invalid_amount_tea_lst)
        expected_calls = 0
        with patch('builtins.print') as mock_print:  # Mock print function
            with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
                run_challenge()  # Run Challenge
                actual_calls = mock_print.call_count
        self.assertEqual(expected_calls, actual_calls)

    def test_challenge_with_valid_input_from_beecrowd_1(self):
        input_beecrowd_lst = ['1', '1 2 3 2 1']
        mock_inputs = iter(input_beecrowd_lst)
        expected_calls = 1
        expected_output_str = '2'
        with patch('builtins.print') as mock_print:  # Mock print function
            with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
                run_challenge()  # Run Challenge
                actual_calls = mock_print.call_count
                actual_output_str = join_all_results(mock_print)
        self.assertEqual(expected_calls, actual_calls)
        self.assertEqual(expected_output_str, actual_output_str)

    def test_challenge_with_valid_input_from_diego_urban_UDEBUG(self):
        input_beecrowd_lst = ['2', '1 3 2 4 3']
        mock_inputs = iter(input_beecrowd_lst)
        expected_calls = 1
        expected_output_str = '1'
        with patch('builtins.print') as mock_print:  # Mock print function
            with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
                run_challenge()  # Run Challenge
                actual_calls = mock_print.call_count
                actual_output_str = join_all_results(mock_print)
        self.assertEqual(expected_calls, actual_calls)
        self.assertEqual(expected_output_str, actual_output_str)

if __name__ == '__main__':
    unittest.main()
