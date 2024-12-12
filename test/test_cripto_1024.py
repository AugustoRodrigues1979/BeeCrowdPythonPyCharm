import random
import unittest
from cripto_1024.cripto import run_challenge_simple, run_challenge, apply_first_step, apply_third_step
from unittest.mock import patch


def join_all_results(mock_print):
    result = ''
    for i in range(len(mock_print.call_args_list)):
        result += mock_print.call_args_list[i][0][0]
    return result


def replace_char_at_position(input_string, position, new_char):
    if position < 0 or position >= len(input_string):
        return
    string_list = list(input_string)  # Convert the string to a list
    for index in range(position, len(input_string)):
        string_list[index] = new_char  # Replace the character at the given position
    return ''.join(string_list)  # Join the list back into a string


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.mock_challenge = run_challenge_simple # Should change between run_challenge_simple and run_challenge

    def test_challenge_with_empty_string(self):
        mock_inputs = iter([""])
        with patch('builtins.print') as mock_print:  # Mock print function
            with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
                self.mock_challenge()
                self.assertEqual(mock_print.call_count, 0)

    def test_challenge_with_zero_lines(self):
        mock_inputs = iter([""])
        with patch('builtins.print') as mock_print:  # Mock print function
            with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
                self.mock_challenge()
                self.assertEqual(mock_print.call_count, 0)

    def test_challenge_with_one_case_with_empty_line(self):
        mock_inputs = iter(["1", ""])
        with patch('builtins.print') as mock_print:  # Mock print function
            with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
                self.mock_challenge()
                self.assertEqual(mock_print.call_count, 1)
                self.assertEqual('', mock_print.call_args[0][0])

    def test_apply_first_step_generate_valid_same_result_provided_by_beecrowd(self):
        expected_output = 'Wh{wr #3'
        entry_input = 'Texto #3'
        actual_ouput = ''
        for i in range(len(entry_input)):
            digit = entry_input[i]
            actual_ouput += apply_first_step(digit)
        self.assertEqual(expected_output, actual_ouput)

    def test_apply_third_step_generate_valid_same_result_provided_by_beecrowd(self):
        expected_output = '3# rvzgV'
        entry_input = '3# rw{hW'
        actual_ouput = ''
        for i in range(len(entry_input)):
            digit = entry_input[i]
            if i >= len(entry_input) // 2:
                actual_ouput += apply_third_step(digit)
            else:
                actual_ouput += digit
        self.assertEqual(expected_output, actual_ouput)

    def test_mock_run_challenge_generate_same_result_provided_by_beecrowd_line_1(self):
        mock_inputs = iter(["1", "Texto #3"])
        with patch('builtins.print') as mock_print:  # Mock print function
            with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
                self.mock_challenge()
                self.assertEqual(mock_print.call_count, 1)
                self.assertEqual('3# rvzgV', mock_print.call_args[0][0])

    def test_mock_run_challenge_generate_result_with_simple_string_with_three_a(self):
        mock_inputs = iter(["1", "aaa"])
        with patch('builtins.print') as mock_print:  # Mock print function
            with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
                self.mock_challenge()
                self.assertEqual(mock_print.call_count, 1)
                self.assertEqual('dcc', mock_print.call_args[0][0])

    def test_mock_run_challenge_generate_same_result_provided_by_beecrowd_line_2(self):
        mock_inputs = iter(["1", "abcABC1"])
        with patch('builtins.print') as mock_print:  # Mock print function
            with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
                self.mock_challenge()
                self.assertEqual(mock_print.call_count, 1)
                self.assertEqual('1FECedc', mock_print.call_args[0][0])

    def test_mock_run_challenge_generate_same_result_provided_by_beecrowd_line_3(self):
        mock_inputs = iter(["1", "vxpdylY .ph"])
        with patch('builtins.print') as mock_print:  # Mock print function
            with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
                self.mock_challenge()
                self.assertEqual(mock_print.call_count, 1)
                self.assertEqual('ks. \\n{frzx', mock_print.call_args[0][0])

    def test_mock_run_challenge_generate_same_result_provided_by_beecrowd_line_4(self):
        mock_inputs = iter(["1", "vv.xwfxo.fd"])
        with patch('builtins.print') as mock_print:  # Mock print function
            with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
                self.mock_challenge()
                self.assertEqual(mock_print.call_count, 1)
                self.assertEqual('gi.r{hyz-xx', mock_print.call_args[0][0])

    def test_mock_run_challenge_generate_same_result_provided_by_beecrowd_all_line_4(self):
        expected_output = '3# rvzgV' + '1FECedc' + 'ks. \\n{frzx' + 'gi.r{hyz-xx'
        mock_inputs = iter(["4", "Texto #3", "abcABC1", "vxpdylY .ph", "vv.xwfxo.fd"])
        with patch('builtins.print') as mock_print:  # Mock print function
            with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
                self.mock_challenge()
                self.assertEqual(mock_print.call_count, 4)
                actual_output = join_all_results(mock_print)
                self.assertEqual(expected_output, actual_output)

    def test_mock_run_challenge_generate_same_result_provided_by_beecrowd_long_line_with_odd_items(self):
        long_line_input = ['a'] * random.randrange(1, 10, 2)
        expected_output = ['d'] * len(long_line_input)
        expected_output = replace_char_at_position(''.join(expected_output), (len(long_line_input) // 2), 'c')
        msg_err = 'Input Line:' + ''.join(long_line_input)
        iter_lst = ['1', long_line_input]
        mock_inputs = iter(iter_lst)
        with patch('builtins.print') as mock_print:  # Mock print function
            with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
                self.mock_challenge()
                self.assertEqual(1, mock_print.call_count)
                actual_output = join_all_results(mock_print)
                self.assertEqual(expected_output, actual_output, msg_err)

    def test_mock_run_challenge_generate_same_result_provided_by_beecrowd_long_line_with_even_items(self):
        long_line_input = ['a'] * random.randrange(2, 10, 2)
        expected_output = ['d'] * len(long_line_input)
        expected_output = replace_char_at_position(''.join(expected_output), (len(long_line_input) // 2), 'c')
        msg_err = 'Input Line:' + ''.join(long_line_input)
        iter_lst = ['1', long_line_input]
        mock_inputs = iter(iter_lst)
        with patch('builtins.print') as mock_print:  # Mock print function
            with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
                self.mock_challenge()
                self.assertEqual(1, mock_print.call_count)
                actual_output = join_all_results(mock_print)
                self.assertEqual(expected_output, actual_output, msg_err)

    def test_mock_run_challenge_show_valid_result_when_run_same_random_test_with_long_line_with_random_amount_chars(self):
        end_range = random.randrange(10, 100, 20)
        for i in range(end_range):
            self.test_mock_run_challenge_generate_same_result_provided_by_beecrowd_long_line_with_odd_items()
            self.test_mock_run_challenge_generate_same_result_provided_by_beecrowd_long_line_with_even_items()


if __name__ == '__main__':
    unittest.main()
