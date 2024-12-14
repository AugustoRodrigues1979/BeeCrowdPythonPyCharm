import random
import unittest
from unittest.mock import patch

from marmore_1025.marmore import run_challenge


def ensure_first_occurrence_of_number(number, numbers_list):
    index_number = 0
    for i in range(len(numbers_list)):
        if numbers_list[i] == number:
            index_number = i
            break
    return index_number


def number_with_in_lst(start_range, end_range, amount_numbers, properties):
    _, _, numbers_list = number_dont_with_in_lst(start_range, end_range, amount_numbers, properties)
    index_number_in_list = random.randrange(0, len(numbers_list))
    number_in_the_list = numbers_list[index_number_in_list]
    index_number_in_list = ensure_first_occurrence_of_number(number_in_the_list, numbers_list)

    use_case_lst = [f'{len(numbers_list)} 1']
    use_case_lst.extend(map(str, numbers_list))
    use_case_lst.append(f'{number_in_the_list}')
    use_case_lst.append('0 0')

    return index_number_in_list, number_in_the_list, use_case_lst


def remove_duplicate_numbers(numbers_list):
    return list(set(numbers_list))


def number_dont_with_in_lst(start_range, end_range, amount_numbers, properties):
    step_number = random.randrange(1, 30)
    number_list = [random.randrange(start_range, end_range + 1, step_number) for _ in range(amount_numbers)]

    if properties['unique_numbers']:
        number_list = remove_duplicate_numbers(number_list)

    if properties['type_order'] == 1:
        number_list.reverse()
    else:
        if properties['type_order'] == 2:
            number_list.sort()

    number_not_in_list = generate_number_not_in_list(start_range, end_range, number_list)

    use_case_lst = [f'{len(number_list)} 1']
    use_case_lst.extend(map(str, number_list))
    use_case_lst.append(f'{number_not_in_list}')
    use_case_lst.append('0 0')

    return number_not_in_list, use_case_lst, number_list


def generate_number_not_in_list(start_range, end_range, numbers_list):
    new_number = random.randint(start_range, end_range)
    while new_number in numbers_list:
        new_number = random.randint(start_range, end_range)
    return new_number


def join_all_results(mock_print):
    result = ''
    for i in range(len(mock_print.call_args_list)):
        result += mock_print.call_args_list[i][0][0]
        if 'end' in mock_print.call_args_list[i].kwargs.keys():
            result += mock_print.call_args_list[i].kwargs['end']
    return result


class MyTestCase(unittest.TestCase):
    def test_challenge_returns_empty_output_when_provided_zero_cases(self):
        mock_inputs = iter(['0 0'])
        expected_calls = 0
        with patch('builtins.print') as mock_print:  # Mock print function
            with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
                run_challenge()  # Run Challenge
                actual_calls = mock_print.call_count
        self.assertEqual(expected_calls, actual_calls)

    def test_challenge_return_result_provided_by_beecrowde(self):
        mock_inputs = iter(['4 1', '2', '3', '5', '1', '5', '0 0'])
        expected_output = 'CASE# 1:\n5 found at 4\n'
        expected_calls = 2
        with patch('builtins.print') as mock_print:  # Mock print function
            with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
                run_challenge()  # Run Challenge
                actual_calls = mock_print.call_count
                actual_output = join_all_results(mock_print)
        self.assertEqual(expected_calls, actual_calls)
        self.assertEqual(expected_output, actual_output)

    def test_challenge_return_result_provided_by_beecrowde_2(self):
        mock_inputs = iter(['4 1', '2', '3', '5', '1', '5', '5 2', '1', '3', '3', '3', '1', '2', '3', '0 0'])
        expected_output = 'CASE# 1:\n5 found at 4\nCASE# 2:\n2 not found\n3 found at 3\n'
        expected_calls = 5
        with patch('builtins.print') as mock_print:  # Mock print function
            with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
                run_challenge()  # Run Challenge
                actual_calls = mock_print.call_count
                actual_output = join_all_results(mock_print)
        self.assertEqual(expected_calls, actual_calls)
        self.assertEqual(expected_output, actual_output)

    def test_challenge_when_provided_random_list_numbers_without_specify_number_in_list(self):
        properties = {
            'type_order': random.randrange(1, 4),
            'unique_numbers': random.choice([True, False])
        }
        start_range, end_range, amount_numbers = 1, 10 ** 4, 64
        number_not_in_list, use_case_lst, _ = number_dont_with_in_lst(start_range, end_range, amount_numbers, properties)
        mock_inputs = iter(use_case_lst)
        expected_output = f'CASE# 1:\n{number_not_in_list} not found\n'
        expected_calls = 2
        with patch('builtins.print') as mock_print:  # Mock print function
            with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
                run_challenge()  # Run Challenge
                actual_calls = mock_print.call_count
                actual_output = join_all_results(mock_print)
        self.assertEqual(expected_calls, actual_calls)
        self.assertEqual(expected_output, actual_output)

    def test_challenge_when_provided_random_list_numbers_with_specify_number_in_list(self):
        properties = {
            'type_order': random.randrange(1, 4),
            'unique_numbers': random.choice([True, False])
        }
        start_range, end_range, amount_numbers = 1, 10 ** 4, 64
        index_number, number_in_list, use_case_lst = number_with_in_lst(
            start_range,
            end_range,
            amount_numbers,
            properties
        )
        mock_inputs = iter(use_case_lst)
        expected_output = f'CASE# 1:\n{number_in_list} found at {index_number + 2}\n'
        expected_calls = 2
        with patch('builtins.print') as mock_print:  # Mock print function
            with patch('builtins.input', lambda: next(mock_inputs)):  # Mock input function
                run_challenge()  # Run Challenge
                actual_calls = mock_print.call_count
                actual_output = join_all_results(mock_print)
        self.assertEqual(expected_calls, actual_calls)
        self.assertEqual(expected_output, actual_output)

    def test_stress_challenge_with_random_numbers_list(self):
        amount_test = random.randrange(10**2, 10**3)
        for i in range(amount_test):
            self.test_challenge_when_provided_random_list_numbers_without_specify_number_in_list()
            self.test_challenge_when_provided_random_list_numbers_with_specify_number_in_list()


if __name__ == '__main__':
    unittest.main()
