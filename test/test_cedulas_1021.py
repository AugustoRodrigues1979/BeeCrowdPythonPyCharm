import random

from cedulas_1021.cedulas import run_challenge, split_float_number_into_integer_parts
import unittest.mock
from unittest.mock import patch
import io
import tracemalloc
import time
import sys


def show_assert_failure_reason(expected_string, actual_string):
    print('\n')  # Skip one line
    print('Expected String:', '\n', expected_string)  # Print Expected String
    print('\n')  # Skip one line
    print('Actual String:', '\n', actual_string)  # Print Actual String


def decode_time(seconds):
    if seconds < 3600:  # Check if exist at last one hour in seconds variable
        hours = 0  # Initialize amount of hours to 0
        _, remainder = divmod(seconds, 3600)  # Get hours and rest time from division seconds for 3600 seconds
    else:
        hours, remainder = divmod(seconds, 3600)  # Set hours and rest time from division seconds for 3600 seconds
    minutes, seconds = divmod(remainder, 60)  # Set minutes and seconds from division rest time for 60 seconds
    hours, minutes, seconds = int(round(hours, 0)), int(round(minutes, 0)), int(round(seconds, 0))  # Round hours, minutes and seconds
    return f"Elapsed time: {hours:02d}:{minutes:02d}:{seconds:02d}"  # Return line contains elapsed time


def show_progress(amount_processed_numbers, amount_unprocessed_numbers, first_trace):
    if not hasattr(show_progress, "start_time"):  # Check if this function has an attribute called start_time
        show_progress.start_time = 0  # Initialize start_time attribute

    if first_trace:  # Check if its is a first trace
        show_progress.start_time = time.time()  # Initialize start_time attribute
        tracemalloc.start()  # Initialize tracemalloc

    current, peak = tracemalloc.get_traced_memory()  # Get the current size and peak size of memory blocks traced by tracemalloc
    elapsed_time = decode_time(time.time() - show_progress.start_time)  # Get the elapsed time since the first trace

    progress_in_percentage = (amount_processed_numbers / amount_unprocessed_numbers) * 10**2
    progress = ''  # Initialize the text progress
    progress = progress + f'Progress:{progress_in_percentage:.02f}% '  # Set progress in porcentage
    progress = progress + f'[Processed Numbers:{amount_processed_numbers}/{amount_unprocessed_numbers}] '  # Set Amount Numbers processed
    progress = progress + f'{elapsed_time} '  # Set elapsed time since the first trace
    progress = progress + f'Current memory:{current / 1024 / 1024:.2f}MB '  # Set the use current memory usage
    progress = progress + f'Peak memory:{peak / 1024 / 1024:.2f}MB '  # Set the peak memory usage
    print(progress, end='\r')  # Show text progress


def get_wallet_string(title_wallet, type_wallet, wallet_list):
    output_wallet_string = title_wallet + ':\n'
    for wallet_index in range(len(wallet_list)):
        my_dict = wallet_list[wallet_index]
        output_wallet_string = output_wallet_string + f"{my_dict['amount']} {type_wallet} de R$ {my_dict['value']:.02f}" + '\n'

    output_wallet_string = output_wallet_string[:len(output_wallet_string)]
    return output_wallet_string


def clean_wallet(wallet_type):
    if wallet_type == 'notes':  # Check if wallet contains only notes
        return [
            {'value': 100, 'amount': 0},
            {'value': 50, 'amount': 0},
            {'value': 20, 'amount': 0},
            {'value': 10, 'amount': 0},
            {'value': 5, 'amount': 0},
            {'value': 2, 'amount': 0},
        ]  # Return the wallet with only notes
    else:  # Wallet contains only coins
        return [
            {'value': 1, 'amount': 0},
            {'value': 0.50, 'amount': 0},
            {'value': 0.25, 'amount': 0},
            {'value': 0.10, 'amount': 0},
            {'value': 0.05, 'amount': 0},
            {'value': 0.01, 'amount': 0},
        ]  # Return the wallet with only coins


def get_output_expected_string(target_value):
    wallet_list = [
        {'wallet': clean_wallet('notes'), 'title': 'NOTAS', 'type_wallet': 'nota(s)'},
        {'wallet': clean_wallet('coins'), 'title': 'MOEDAS', 'type_wallet': 'moeda(s)'},
    ]  # Initialize wallet list with all values amount to zero

    output_wallet_string = ''  # Initialize output string
    for wallet_item in wallet_list:  # For each item wallet in wallet list
        while True:  # Initialize infinite loop
            index_found = False  # Initialize that nout founded first position with minor amount value founded in the wallet list
            index_value = -1  # Initialize index which contain the first position with minor amount value founded in the wallet list
            for i in range(len(wallet_item['wallet'])):  # For each dict in wallet_item
                my_dict = wallet_item['wallet'][i]  # Store wallet_item in dict
                if target_value >= my_dict['value']:  # Check if target value is greater than or equal to value in actual dict
                    index_found, index_value = True, i  # Set what the minor amount value was localized
                    break  # Stop loop iteraction

            if not index_found:  # Check if amount minor value index was not localized
                break  # Stop search for amount minor value

            my_dict = wallet_item['wallet'][index_value]  # Store wallet with amount minor value in a dict
            my_dict['amount'] = my_dict['amount'] + 1  # Update the amount property
            target_value = round(target_value - my_dict['value'], 2)  # Update the amount property

        title_wallet = wallet_item['title']  # Get title from wallet item
        type_wallet = wallet_item['type_wallet']  # Get type from wallet item
        data_wallet = wallet_item['wallet']  # Get data dict from wallet item
        output_wallet_string = output_wallet_string + get_wallet_string(title_wallet, type_wallet, data_wallet)

    return output_wallet_string


class TestCedulas:

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    def test_amount_equal_to_zero(self):
        with patch('builtins.input', return_value='0'):
            with patch('builtins.print') as mock_print:
                run_challenge()
                mock_print.assert_any_call('NOTAS:')
                mock_print.assert_any_call("0 nota(s) de R$ 100.00")
                mock_print.assert_any_call('0 nota(s) de R$ 50.00')
                mock_print.assert_any_call('0 nota(s) de R$ 20.00')
                mock_print.assert_any_call('0 nota(s) de R$ 10.00')
                mock_print.assert_any_call('0 nota(s) de R$ 5.00')
                mock_print.assert_any_call('0 nota(s) de R$ 2.00')

                mock_print.assert_any_call('MOEDAS:')
                mock_print.assert_any_call('0 moeda(s) de R$ 1.00')
                mock_print.assert_any_call('0 moeda(s) de R$ 0.50')
                mock_print.assert_any_call('0 moeda(s) de R$ 0.25')
                mock_print.assert_any_call('0 moeda(s) de R$ 0.10')
                mock_print.assert_any_call('0 moeda(s) de R$ 0.05')
                mock_print.assert_any_call('0 moeda(s) de R$ 0.01')

    def test_amount_equal_to_0_01(self):
        with patch('builtins.input', return_value='0.01'):
            with patch('builtins.print') as mock_print:
                run_challenge()
                mock_print.assert_any_call('NOTAS:')
                mock_print.assert_any_call("0 nota(s) de R$ 100.00")
                mock_print.assert_any_call('0 nota(s) de R$ 50.00')
                mock_print.assert_any_call('0 nota(s) de R$ 20.00')
                mock_print.assert_any_call('0 nota(s) de R$ 10.00')
                mock_print.assert_any_call('0 nota(s) de R$ 5.00')
                mock_print.assert_any_call('0 nota(s) de R$ 2.00')

                mock_print.assert_any_call('MOEDAS:')
                mock_print.assert_any_call('0 moeda(s) de R$ 1.00')
                mock_print.assert_any_call('0 moeda(s) de R$ 0.50')
                mock_print.assert_any_call('0 moeda(s) de R$ 0.25')
                mock_print.assert_any_call('0 moeda(s) de R$ 0.10')
                mock_print.assert_any_call('0 moeda(s) de R$ 0.05')
                mock_print.assert_any_call('1 moeda(s) de R$ 0.01')

    def test_amount_equal_to_0_02(self):
        with patch('builtins.input', return_value='0.02'):
            with patch('builtins.print') as mock_print:
                run_challenge()
                mock_print.assert_any_call('NOTAS:')
                mock_print.assert_any_call("0 nota(s) de R$ 100.00")
                mock_print.assert_any_call('0 nota(s) de R$ 50.00')
                mock_print.assert_any_call('0 nota(s) de R$ 20.00')
                mock_print.assert_any_call('0 nota(s) de R$ 10.00')
                mock_print.assert_any_call('0 nota(s) de R$ 5.00')
                mock_print.assert_any_call('0 nota(s) de R$ 2.00')

                mock_print.assert_any_call('MOEDAS:')
                mock_print.assert_any_call('0 moeda(s) de R$ 1.00')
                mock_print.assert_any_call('0 moeda(s) de R$ 0.50')
                mock_print.assert_any_call('0 moeda(s) de R$ 0.25')
                mock_print.assert_any_call('0 moeda(s) de R$ 0.10')
                mock_print.assert_any_call('0 moeda(s) de R$ 0.05')
                mock_print.assert_any_call('2 moeda(s) de R$ 0.01')

    def test_amount_equal_to_0_03(self):
        with patch('builtins.input', return_value='0.03'):
            with patch('builtins.print') as mock_print:
                run_challenge()
                mock_print.assert_any_call('NOTAS:')
                mock_print.assert_any_call("0 nota(s) de R$ 100.00")
                mock_print.assert_any_call('0 nota(s) de R$ 50.00')
                mock_print.assert_any_call('0 nota(s) de R$ 20.00')
                mock_print.assert_any_call('0 nota(s) de R$ 10.00')
                mock_print.assert_any_call('0 nota(s) de R$ 5.00')
                mock_print.assert_any_call('0 nota(s) de R$ 2.00')

                mock_print.assert_any_call('MOEDAS:')
                mock_print.assert_any_call('0 moeda(s) de R$ 1.00')
                mock_print.assert_any_call('0 moeda(s) de R$ 0.50')
                mock_print.assert_any_call('0 moeda(s) de R$ 0.25')
                mock_print.assert_any_call('0 moeda(s) de R$ 0.10')
                mock_print.assert_any_call('0 moeda(s) de R$ 0.05')
                mock_print.assert_any_call('3 moeda(s) de R$ 0.01')

    def test_amount_equal_to_0_04(self):
        with patch('builtins.input', return_value='0.04'):
            with patch('builtins.print') as mock_print:
                run_challenge()
                mock_print.assert_any_call('NOTAS:')
                mock_print.assert_any_call("0 nota(s) de R$ 100.00")
                mock_print.assert_any_call('0 nota(s) de R$ 50.00')
                mock_print.assert_any_call('0 nota(s) de R$ 20.00')
                mock_print.assert_any_call('0 nota(s) de R$ 10.00')
                mock_print.assert_any_call('0 nota(s) de R$ 5.00')
                mock_print.assert_any_call('0 nota(s) de R$ 2.00')

                mock_print.assert_any_call('MOEDAS:')
                mock_print.assert_any_call('0 moeda(s) de R$ 1.00')
                mock_print.assert_any_call('0 moeda(s) de R$ 0.50')
                mock_print.assert_any_call('0 moeda(s) de R$ 0.25')
                mock_print.assert_any_call('0 moeda(s) de R$ 0.10')
                mock_print.assert_any_call('0 moeda(s) de R$ 0.05')
                mock_print.assert_any_call('4 moeda(s) de R$ 0.01')

    def test_amount_equal_to_0_05(self):
        with patch('builtins.input', return_value='0.05'):
            with patch('builtins.print') as mock_print:
                run_challenge()
                mock_print.assert_any_call('NOTAS:')
                mock_print.assert_any_call("0 nota(s) de R$ 100.00")
                mock_print.assert_any_call('0 nota(s) de R$ 50.00')
                mock_print.assert_any_call('0 nota(s) de R$ 20.00')
                mock_print.assert_any_call('0 nota(s) de R$ 10.00')
                mock_print.assert_any_call('0 nota(s) de R$ 5.00')
                mock_print.assert_any_call('0 nota(s) de R$ 2.00')

                mock_print.assert_any_call('MOEDAS:')
                mock_print.assert_any_call('0 moeda(s) de R$ 1.00')
                mock_print.assert_any_call('0 moeda(s) de R$ 0.50')
                mock_print.assert_any_call('0 moeda(s) de R$ 0.25')
                mock_print.assert_any_call('0 moeda(s) de R$ 0.10')
                mock_print.assert_any_call('1 moeda(s) de R$ 0.05')
                mock_print.assert_any_call('0 moeda(s) de R$ 0.01')

    def test_amount_equal_to_0_06(self):
        with patch('builtins.input', return_value='0.06'):
            with patch('builtins.print') as mock_print:
                run_challenge()
                mock_print.assert_any_call('NOTAS:')
                mock_print.assert_any_call("0 nota(s) de R$ 100.00")
                mock_print.assert_any_call('0 nota(s) de R$ 50.00')
                mock_print.assert_any_call('0 nota(s) de R$ 20.00')
                mock_print.assert_any_call('0 nota(s) de R$ 10.00')
                mock_print.assert_any_call('0 nota(s) de R$ 5.00')
                mock_print.assert_any_call('0 nota(s) de R$ 2.00')

                mock_print.assert_any_call('MOEDAS:')
                mock_print.assert_any_call('0 moeda(s) de R$ 1.00')
                mock_print.assert_any_call('0 moeda(s) de R$ 0.50')
                mock_print.assert_any_call('0 moeda(s) de R$ 0.25')
                mock_print.assert_any_call('0 moeda(s) de R$ 0.10')
                mock_print.assert_any_call('1 moeda(s) de R$ 0.05')
                mock_print.assert_any_call('1 moeda(s) de R$ 0.01')

    def test_amount_between_0_00_to_1_00(self):
        target_value = 100.00  # Initialize target_value to maximum amount of money
        actual_value = 0  # Initialize actual_value to first amount of money
        step_value = 0.01
        amount_values_unprocessed = int(((target_value - actual_value) / step_value) + 1)
        amount_values_processed = 0
        while actual_value <= target_value:  # Run until the all amounts is processed
            actual_value_string = str(round(float(actual_value), 2))  # Initialize actual_value_string from actual amount value
            title_amount_string = actual_value_string + '\n'  # Initialize the main value amount expected in output
            output_expected_string = title_amount_string + get_output_expected_string(actual_value)  # Initialize detail of amount in expected output

            with patch('builtins.input', return_value=actual_value_string):  # Set mock for input function
                with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:  # Set mock for print function
                    run_challenge()  # Run challenge
                    output_challenge_string = title_amount_string + mock_stdout.getvalue()  # Get detail of amount created by run_challenge function

            if output_expected_string != output_challenge_string:  # Check if result expected is not equal to result gived from run_challenge function
                show_assert_failure_reason(output_expected_string, output_challenge_string)  # Show failure text from assert

            assert output_expected_string == output_challenge_string  # Run assert

            amount_values_processed += 1  # Increment amount values processed

            if actual_value == 0:  # Check if its is first iteration
                print()  # Skip one line
                show_progress(amount_values_processed, amount_values_unprocessed, True)  # Show line progress
            else:  # Run for other iteractions
                show_progress(amount_values_processed, amount_values_unprocessed, False)  # Show line progress


            actual_value = round(actual_value + 0.01, 2)  # Set next value amount
        print('')

    def test_split_float_number_into_integer_parts(self):
        begin_interval = 0
        end_interval = 1000000
        expected_integer_part_number = random.randrange(begin_interval, end_interval)
        expected_decimal_part_number = random.randrange(0, 99)
        float_number = float(f'{expected_integer_part_number}.{expected_decimal_part_number}')
        obtained_integer_part_number, obtained_decimal_part_number = split_float_number_into_integer_parts(float_number)
        assert expected_integer_part_number == obtained_integer_part_number
        assert expected_decimal_part_number == obtained_decimal_part_number
        assert type(expected_decimal_part_number) == type(obtained_decimal_part_number)
        assert type(expected_decimal_part_number) == type(obtained_decimal_part_number)
        assert float_number == float(f'{obtained_integer_part_number}.{obtained_decimal_part_number}')
