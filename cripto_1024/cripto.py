from sys import stdin


def apply_first_step(digit_str):
    if not digit_str.isalpha():
        return digit_str
    new_digit = ord(digit_str) + 3
    return chr(new_digit)


def apply_third_step(digit_str):
    new_digit = ord(digit_str) - 1
    return chr(new_digit)


def run_challenge_simple():
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
        for index_char in range(len(line_input_str)):
            line_input_lst[index_char] = apply_first_step(line_input_lst[index_char])

        line_input_lst.reverse()

        for index_char in range(len(line_input_str) // 2, len(line_input_str)):
            line_input_lst[index_char] = chr(ord(line_input_lst[index_char]) - 1)

        print(''.join(line_input_lst))


def run_challenge():
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
        for original_index in range(0, len(line_input_lst) // 2):
            inverted_index = len(line_input_lst) - original_index - 1

            line_input_lst[inverted_index] = apply_first_step(line_input_lst[inverted_index])
            line_input_lst[original_index] = apply_first_step(line_input_lst[original_index])

            line_input_lst[original_index], line_input_lst[inverted_index] = line_input_lst[inverted_index], line_input_lst[original_index]

            if inverted_index >= len(line_input_lst) // 2:
                line_input_lst[inverted_index] = apply_third_step(line_input_lst[inverted_index])

        if (len(line_input_lst)) % 2 != 0:
            original_index = (len(line_input_lst)) // 2 + (len(line_input_lst)) % 2
            original_index -= 1
            line_input_lst[original_index] = apply_first_step(line_input_lst[original_index])
            line_input_lst[original_index] = apply_third_step(line_input_lst[original_index])

        print(''.join(line_input_lst))


if __name__ == '__main__':
    input = stdin.readline
    run_challenge()
