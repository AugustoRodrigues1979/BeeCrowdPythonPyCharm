import unittest
from unittest.mock import patch
from saldo_vovo_2434.saldo_vovo import run_challenge


class MyTestCase(unittest.TestCase):
    def test_challenge_with_empty_input(self):
        mock_inputs = iter([''])
        expected_print_calls = 0
        with patch('builtins.print') as mock_print:  # Mock print function
            with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
                run_challenge()  # Run Challenge
                actual_print_calls = mock_print.call_count
        self.assertEqual(expected_print_calls, actual_print_calls)

    def test_challenge_with_invalid_input_with_one_string(self):
        mock_inputs = iter(['5'])
        expected_print_calls = 0
        with patch('builtins.print') as mock_print:  # Mock print function
            with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
                run_challenge()  # Run Challenge
                actual_print_calls = mock_print.call_count
        self.assertEqual(expected_print_calls, actual_print_calls)

    def test_challenge_with_invalid_input_with_negative_amount_days(self):
        mock_inputs = iter(['-10 0', '0', '0'])
        expected_print_calls = 0
        with patch('builtins.print') as mock_print:  # Mock print function
            with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
                run_challenge()  # Run Challenge
                actual_print_calls = mock_print.call_count
        self.assertEqual(expected_print_calls, actual_print_calls)

    def test_challenge_with_invalid_input_with_amount_days_less_then_zero(self):
        mock_inputs = iter(['0 20', '-30', '198'])
        expected_print_calls = 0
        with patch('builtins.print') as mock_print:  # Mock print function
            with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
                run_challenge()  # Run Challenge
                actual_print_calls = mock_print.call_count
        self.assertEqual(expected_print_calls, actual_print_calls)

    def test_challenge_with_invalid_input_with_amount_days_greather_thirty_days(self):
        mock_inputs = iter(['31 501', '-30', '198'])
        expected_print_calls = 0
        with patch('builtins.print') as mock_print:  # Mock print function
            with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
                run_challenge()  # Run Challenge
                actual_print_calls = mock_print.call_count
        self.assertEqual(expected_print_calls, actual_print_calls)

    def test_challenge_with_one_day_of_movement_with_positive_balance(self):
        mock_inputs = iter(['1 1000', '100', '2800', '50'])
        expected_output = '1000'
        with patch('builtins.print') as mock_print:  # Mock print function
            with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
                run_challenge()  # Run Challenge
                actual_output = mock_print.call_args.args[0]
        self.assertEqual(expected_output, actual_output)

    def test_challenge_with_one_day_of_movement_with_negative_balance(self):
        mock_inputs = iter(['1 -870', '100', '-800', '50'])
        expected_output = '-870'
        with patch('builtins.print') as mock_print:  # Mock print function
            with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
                run_challenge()  # Run Challenge
                actual_output = mock_print.call_args.args[0]
        self.assertEqual(expected_output, actual_output)

    def test_challenge_with_one_day_of_movement_with_zero_balance(self):
        mock_inputs = iter(['1 0', '100', '-800', '50'])
        expected_output = '0'
        with patch('builtins.print') as mock_print:  # Mock print function
            with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
                run_challenge()  # Run Challenge
                actual_output = mock_print.call_args.args[0]
        self.assertEqual(expected_output, actual_output)

    def test_challenge_with_valid_input_beewcrod(self):
        mock_inputs = iter(['3 1000', '100', '-800', '50'])
        expected_output = '300'
        with patch('builtins.print') as mock_print:  # Mock print function
            with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
                run_challenge()  # Run Challenge
                actual_output = mock_print.call_args.args[0]
        self.assertEqual(expected_output, actual_output)

    def test_challenge_with_valid_input_beewcrod_2(self):
        mock_inputs = iter(['6 -200', '-100', '1000', '-2000', '100', '-50', '2000'])
        expected_output = '-1300'
        with patch('builtins.print') as mock_print:  # Mock print function
            with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
                run_challenge()  # Run Challenge
                actual_output = mock_print.call_args.args[0]
        self.assertEqual(expected_output, actual_output)

    def test_challenge_with_valid_input_buixzy_1(self):
        mock_inputs = iter(['9 2558', '-9363', '-4040', '7444', '4275', '5365', '7169', '-4675', '-7083', '-1134'])
        expected_output = '-10845'
        with patch('builtins.print') as mock_print:  # Mock print function
            with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
                run_challenge()  # Run Challenge
                actual_output = mock_print.call_args.args[0]
        self.assertEqual(expected_output, actual_output)

    def test_challenge_with_valid_input_buixzy_2(self):
        mock_inputs = iter(['11 -729', '4425', '-6348', '8425', '-206', '6922', '9715', '6024', '6052', '-6906', '2315', '-2666'])
        expected_output = '-2652'
        with patch('builtins.print') as mock_print:  # Mock print function
            with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
                run_challenge()  # Run Challenge
                actual_output = mock_print.call_args.args[0]
        self.assertEqual(expected_output, actual_output)

    def test_challenge_with_valid_input_denoyr_3(self):
        mock_inputs = iter(['21 875', '-806', '183', '471', '-1', '86', '-313', '99', '-104', '953', '861', '-33', '9', '94', '103', '-105', '999', '-991', '135', '-1000', '13', '0'])
        expected_output = '69'
        with patch('builtins.print') as mock_print:  # Mock print function
            with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
                run_challenge()  # Run Challenge
                actual_output = mock_print.call_args.args[0]
        self.assertEqual(expected_output, actual_output)


if __name__ == '__main__':
    unittest.main()
