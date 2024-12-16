import unittest
from unittest.mock import patch
from menor_numero_par_2679.menor_numero_par import run_challenge

class MyTestCase(unittest.TestCase):
    def test_challenge_with_valid_input_beewcrod(self):
        mock_inputs = iter(['1'])
        expected_output = '2'
        with patch('builtins.print') as mock_print:  # Mock print function
            with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
                run_challenge()  # Run Challenge
                actual_output = mock_print.call_args.args[0]
        self.assertEqual(expected_output, actual_output)


if __name__ == '__main__':
    unittest.main()
