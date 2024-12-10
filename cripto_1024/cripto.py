from sys import stdin
from unittest.mock import patch

def run_challenge():
    first_digit_ASCII = ord('!')
    last_digit_ASCII = ord('~')

    def apply_first_step(digit_str):
        new_digit = ord(digit_str) + 3
        if new_digit > last_digit_ASCII:
            new_digit += first_digit_ASCII - last_digit_ASCII
        return chr(new_digit)

    def apply_third_step(digit_str):
        new_digit = ord(digit_str) - 1
        if new_digit < first_digit_ASCII:
            new_digit = last_digit_ASCII
        return chr(new_digit)

    amount_lines = input()
    if amount_lines == '':
        return

    amount_lines = int(amount_lines)
    if amount_lines <= 0:
        return

    for index_line in range(amount_lines):
        line_input_str = input()
        if line_input_str == '':
            print('')
            continue
        line_input_lst = list(line_input_str)
        for inverted_index, digit in enumerate(line_input_lst[::-1]):
            original_index = len(line_input_lst) - 1 - inverted_index

            line_input_lst[inverted_index] = apply_first_step(line_input_lst[inverted_index])
            line_input_lst[original_index] = apply_first_step(line_input_lst[original_index])

            line_input_lst[original_index], line_input_lst[inverted_index] = line_input_lst[inverted_index], line_input_lst[original_index]

            if inverted_index >= len(line_input_lst) // 2:
                line_input_lst[inverted_index] = apply_third_step(line_input_lst[inverted_index])





if __name__ == '__main__':
    input = stdin.readline
    run_challenge()