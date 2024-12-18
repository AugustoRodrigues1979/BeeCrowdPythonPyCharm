import random
import unittest
from cripto_1024.cripto import run_challenge_simple, run_challenge, apply_first_step, apply_third_step
from unittest.mock import patch

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
        expected_output = '3# rvzgV' + '\n'
        expected_output += '1FECedc' + '\n'
        expected_output += 'ks. \\n{frzx' + '\n'
        expected_output += 'gi.r{hyz-xx'

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

    def test_challenge_show_valid_result_with_monir004_input_data_01(self):
        input_str = read_input_file('cripto_monir004_input_01.txt')
        input_lst = input_str.split('\n')
        mock_inputs = iter(input_lst)

        expected_output = read_input_file('cripto_monir004_output_01.txt')
        expected_calls = int(input_lst[0])

        with patch('builtins.print') as mock_print:  # Mock print function
            with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
                mock_print.reset_mock()
                run_challenge()  # Run Challenge
                actual_calls = mock_print.call_count
                actual_output = join_all_results(mock_print)
        self.assertEqual(expected_calls, actual_calls)
        self.assertEqual(expected_output, actual_output)

    def test_challenge_show_valid_result_for_each_line_monir004_input_data_01(self):
        input_str = read_input_file('cripto_monir004_input_01.txt')
        output_str = read_input_file('cripto_monir004_output_01.txt')

        input_lst = input_str.split('\n')
        output_lst = output_str.split('\n')

        amount_item = int(input_lst[0])
        for index in range(1,amount_item):
            line_str = input_lst[index]
            mock_inputs = iter(['1', line_str])

            expected_output = output_lst[index-1]
            expected_calls = 1

            with patch('builtins.print') as mock_print:  # Mock print function
                with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
                    mock_print.reset_mock()
                    run_challenge()  # Run Challenge
                    actual_calls = mock_print.call_count
                    actual_output = join_all_results(mock_print)

            self.assertEqual(expected_calls, actual_calls)
            self.assertEqual(expected_output, actual_output)



if __name__ == '__main__':
    unittest.main()
