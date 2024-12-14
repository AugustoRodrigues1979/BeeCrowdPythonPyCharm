import unittest
from unittest.mock import patch

from tomada_1930.tomada import run_challenge


class MyTestCase(unittest.TestCase):
    def test_challenge_provided_valid_result_with_four_ruler_with_minimal_sockets_each(self):
        mock_inputs = iter(["2 2 2 2"])
        expected_output = '5'
        with patch('builtins.print') as mock_print:  # Mock print function
            with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
                run_challenge()  # Run Challenge
                actual_output = mock_print.call_args.args[0]

        self.assertEqual(expected_output, actual_output)

    def test_challenge_provided_valid_result_with_four_ruler_with_maximal_sockets_each(self):
        mock_inputs = iter(["6 6 6 6"])
        expected_output = '21'
        with patch('builtins.print') as mock_print:  # Mock print function
            with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
                run_challenge()  # Run Challenge
                actual_output = mock_print.call_args.args[0]

        self.assertEqual(expected_output, actual_output)

    def test_challenge_provided_valid_result_with_example_provided_by_beecrowde(self):
        mock_inputs = iter(["2 4 3 2"])
        expected_output = '8'
        with patch('builtins.print') as mock_print:  # Mock print function
            with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
                run_challenge()  # Run Challenge
                actual_output = mock_print.call_args.args[0]

        self.assertEqual(expected_output, actual_output)

if __name__ == '__main__':
    unittest.main()
