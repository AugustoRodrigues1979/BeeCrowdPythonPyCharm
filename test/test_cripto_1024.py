import unittest
from cripto_1024.cripto import run_challenge
from unittest.mock import patch

class MyTestCase(unittest.TestCase):
    def test_challenge_with_empty_string(self):
        mock_inputs = iter([""])
        with patch('builtins.print') as mock_print:  # Mock print function
            with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
                run_challenge()
                self.assertEqual(mock_print.call_count,0)

    def test_challenge_with_zero_lines(self):
        mock_inputs = iter([""])
        with patch('builtins.print') as mock_print:  # Mock print function
            with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
                run_challenge()
                self.assertEqual(mock_print.call_count,0)

    def test_challenge_with_one_case_with_empty_line(self):
        mock_inputs = iter(["1", ""])
        with patch('builtins.print') as mock_print:  # Mock print function
            with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
                run_challenge()
                self.assertEqual(mock_print.call_count,1)
                self.assertEqual(mock_print.call_args[0][0], '')


if __name__ == '__main__':
    unittest.main()
