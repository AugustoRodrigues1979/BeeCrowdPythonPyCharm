import unittest
from unittest.mock import patch

from roteadores_1774.roteadores_kruskal import run_challenge

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
    def test_challenge_when_invalid_routers_amount(self):
        invalid_amount_routers_lst = ['0 0', '1 1', '2 3', '61 100']
        for i in range(len(invalid_amount_routers_lst)):
            mock_inputs = iter([invalid_amount_routers_lst[i]])
            expected_calls = 0
            with patch('builtins.print') as mock_print:  # Mock print function
                with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
                    run_challenge()  # Run Challenge
                    actual_calls = mock_print.call_count
            self.assertEqual(expected_calls, actual_calls)

    def test_challenge_when_invalid_cable_amount(self):
        invalid_amount_cable_lst = ['3 0', '3 1', '3 2', '10 9', '60 59', '60 201']
        for i in range(len(invalid_amount_cable_lst)):
            mock_inputs = iter([invalid_amount_cable_lst[i]])
            expected_calls = 0
            with patch('builtins.print') as mock_print:  # Mock print function
                with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
                    run_challenge()  # Run Challenge
                    actual_calls = mock_print.call_count
            self.assertEqual(expected_calls, actual_calls)

    def test_challenge_when_provided_example_from_beecrowd(self):
        input_str = ['7 12','1 3 6','1 4 9','2 3 17','2 5 32','2 7 27','3 4 11','3 5 4','4 5 3','4 6 19','5 6 13','5 7 15','6 7 5']
        mock_inputs = iter(input_str)

        expected_calls = 1
        expected_output_str = '48'

        with patch('builtins.print') as mock_print:  # Mock print function
            with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
                run_challenge()  # Run Challenge
                actual_calls = mock_print.call_count
                actual_output_str = join_all_results(mock_print)

        self.assertEqual(expected_calls, actual_calls)
        self.assertEqual(expected_output_str, actual_output_str)

    def test_challenge_when_provided_example_from_feodorv_input_01(self):
        input_lst = read_input_file('roteadores_feodorv_input_01.txt')
        mock_inputs = iter(input_lst.split('\n'))

        expected_output = read_input_file('roteadores_feodorv_output_01.txt')
        expected_calls = expected_output.count('\n') + 1

        with patch('builtins.print') as mock_print:  # Mock print function
            with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
                run_challenge()  # Run Challenge
                actual_calls = mock_print.call_count
                actual_output = join_all_results(mock_print)
        self.assertEqual(expected_calls, actual_calls)
        self.assertEqual(expected_output, actual_output)

    def test_challenge_when_provided_small_path_between_routers_1(self):
        input_str = ['3 3','1 3 6','1 2 1','3 2 1']
        mock_inputs = iter(input_str)

        expected_calls = 1
        expected_output_str = '2'

        with patch('builtins.print') as mock_print:  # Mock print function
            with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
                mock_print.reset_mock()
                run_challenge()  # Run Challenge
                actual_calls = mock_print.call_count
                actual_output_str = join_all_results(mock_print)

        self.assertEqual(expected_calls, actual_calls)
        self.assertEqual(expected_output_str, actual_output_str)

if __name__ == '__main__':
    unittest.main()
