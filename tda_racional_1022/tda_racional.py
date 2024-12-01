# A tarefa aqui neste problema é ler uma expressão matemática na forma de dois números
# Racionais (numerador / denominador) e apresentar o resultado da operação.
#
# Cada operando ou operador é separado por um espaço em branco. A sequência de cada linha que
# contém a expressão a ser lida é: número, caractere, número, caractere, número, caractere, número.
# A resposta deverá ser apresentada e posteriormente simplificada.
#
# Deverá então ser apresentado o sinal de igualdade e em seguida a resposta simplificada.
# No caso de não ser possível uma simplificação, deve ser apresentada a mesma resposta após o sinal de igualdade.
#
# Considerando N1 e D1 como numerador e denominador da primeira fração, segue a orientação de como deverá ser realizada
# cada uma das operações:
# Soma: (N1*D2 + N2*D1) / (D1*D2)
# Subtração: (N1*D2 - N2*D1) / (D1*D2)
# Multiplicação: (N1*N2) / (D1*D2)
# Divisão: (N1/D1) / (N2/D2), ou seja (N1*D2)/(N2*D1)
#
# Entrada
# A entrada contem vários casos de teste. A primeira linha de cada caso de teste contem um inteiro N (1 ≤ N ≤ 1*104),
# indicando a quantidade de casos de teste que devem ser lidos logo a seguir.
# Cada caso de teste contém um valor racional X (1 ≤ X ≤ 1000), uma operação (-, +, * ou /) e
# outro valor racional Y (1 ≤ Y ≤ 1000).
#
# Saída
# A saída consiste em um valor racional, seguido de um sinal de igualdade e outro valor racional,
# que é a simplificação do primeiro valor. No caso do primeiro valor não poder ser simplificado, o mesmo deve ser
# repetido após o sinal de igualdade.
import math


def contains_only_integer_numbers(s):
    try:
        int(s)  # Try converting to integer number
        return True  # Return True if possible conversion string s in a number
    except ValueError:
        return False  # Return False if do not possible conversion string s in a number


def split_operation_in_token_dict(operation_str):
    n1, r1, d1, operation_type, n2, r2, d2 = operation_str.split()  # Split operation provided in tokens
    token_dict = dict()  # Create a dict will store all valid tokens
    token_dict['K_N1'] = n1  # Store first numerator
    token_dict['K_D1'] = d1  # Store first denominator
    token_dict['K_OPERATION'] = operation_type  # Store operation type
    token_dict['K_N2'] = n2  # Store second numerator
    token_dict['K_D2'] = d2  # Store second denominator

    if not contains_only_integer_numbers(n1) or not contains_only_integer_numbers(d1):  # Check if numerator and denominator are integer type
        raise ValueError('N1 and D1 should is integer type')  # Raise an exception

    if not contains_only_integer_numbers(n2) or not contains_only_integer_numbers(d2):  # Check if numerator and denominator are integer type
        raise ValueError('N2 and D2 should is integer type')  # Raise an exception

    if not operation_type in ['+', '-', '*', '/']:  # Check if operation type provided by user is a valid operation
        raise ValueError('User provided invalid operation')  # Raise an exception

    return token_dict  # Return token dict


def get_valid_operation():
    operation_str = input()  # Get a user operation

    if operation_str == '':  # Check if operation contain an empty string
        raise ValueError('User provided empty operation')  # Raise an exception

    return split_operation_in_token_dict(operation_str)  # Split the operation into valid tokens and store those tokens in a dict


def split_numbers_in_operation_dict(operation_dict):
    n1 = operation_dict['K_N1']
    d1 = operation_dict['K_D1']
    n2 = operation_dict['K_N2']
    d2 = operation_dict['K_D2']
    return int(n1), int(d1), int(n2), int(d2)


def run_operation(operation_dict):
    n1, d1, n2, d2 = split_numbers_in_operation_dict(operation_dict)  # Get all operands numbers from a dict
    racional_number = dict()
    if operation_dict['K_OPERATION'] == '+':  # Check if operation is a sum
        racional_number['K_R1'] = (n1 * d2 + n2 * d1)
        racional_number['K_R2'] = (d1 * d2)
        return racional_number  # Return result of sum

    if operation_dict['K_OPERATION'] == '-':  # Check if operation is a subtraction
        racional_number['K_R1'] = (n1 * d2 - n2 * d1)
        racional_number['K_R2'] = (d1 * d2)
        return racional_number  # Return result of subtraction

    if operation_dict['K_OPERATION'] == '*':  # Check if operation is a multiplication
        racional_number['K_R1'] = (n1 * n2)
        racional_number['K_R2'] = (d1 * d2)
        return racional_number  # Return result of multiplication

    if operation_dict['K_OPERATION'] == '/':  # Check if operation is a division
        racional_number['K_R1'] = (n1 * d2)
        racional_number['K_R2'] = (n2 * d1)
        return racional_number  # Return result of division

    raise ValueError('Do not possible run operation provided by user')  # Raise an exception because what operation provided is an invalid operation


def get_result_simple(result_dict):
    greatest_common_divisor = math.gcd(result_dict['K_R1'], result_dict['K_R2'])  # Get the greatest common divisor between result one and result two

    if greatest_common_divisor == 1:  # Check if greatest common divisor is equal to one
        return result_dict  # Return dict with R1 / R2 in the simple form

    result_dict['K_R1'] = result_dict['K_R1'] // greatest_common_divisor  # Return number in the simple form
    result_dict['K_R2'] = result_dict['K_R2'] // greatest_common_divisor  # Return number in the simple form
    return get_result_simple(result_dict)  # Return dict with R1 / R2 in the simple form representation


def get_line_result(result_dict):
    original_dict = dict()  # Create a dict for store original results for a specify operation
    original_dict['K_R1'], original_dict['K_R2'] = result_dict['K_R1'], result_dict['K_R2']  # Store original values in a dict
    simple_result_dict = get_result_simple(original_dict)  # Get a simple result from the original values
    return f"{result_dict['K_R1']}/{result_dict['K_R2']} = {simple_result_dict['K_R1']}/{simple_result_dict['K_R2']}"  # Create line result for show to user


def run_challenge():
    amount_use_case = int(input())  # Get amount of use case
    if amount_use_case <= 0:  # Check if amount is valid
        raise ValueError('Enter a valid number of use case')  # Raise exception

    result_list = []  # Create a list for store main results from each operation provided by user
    for index_use_case in range(amount_use_case):  # For each use case provided by user
        operation_dict = get_valid_operation()  # Store a dictionary which contains all valid tokens within the operation provided by user
        result_list.append(run_operation(operation_dict))  # Store result from each operation provided by user

    for index_use_case in range(amount_use_case):  # For each use case provided by user
        line_result = get_line_result(result_list[index_use_case])  # Store the result of operation to after show for user
        print(line_result)  # Show result for each operation provided by user


if __name__ == '__main__':
    run_challenge()
