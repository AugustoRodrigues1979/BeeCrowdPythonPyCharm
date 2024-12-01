# Leia um valor de ponto flutuante com duas casas decimais.
# Este valor representa um valor monetário.
#
# A seguir, calcule o menor número de notas e moedas possíveis
# no qual o valor pode ser decomposto. As notas consideradas
# são de 100, 50, 20, 10, 5, 2.
#
# As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01.
# A seguir mostre a relação de notas necessárias.
def split_float_number_into_integer_parts(float_number):
    float_number_str = f'{float_number:.02f}'
    integer_part_str, decimal_part_str = float_number_str.split('.')
    integer_part = int(integer_part_str)  # Get integer part
    decimal_part = int(decimal_part_str)  # Get decimal part
    return integer_part, decimal_part  # Returning the integer part and decimal part of the original number


def run_challenge():
    float_amount_input = float(input())
    banknotes = [100, 50, 20, 10, 5, 2]
    bankcoins = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

    integer_part_amount, decimal_part_amount = split_float_number_into_integer_parts(float_amount_input)  # Split number in integer and decimal part

    print('NOTAS:')
    for i in range(len(banknotes)):
        amount_notes = integer_part_amount // banknotes[i]
        integer_part_amount = integer_part_amount % banknotes[i]
        print(f"{amount_notes:.0f} nota(s) de R$ {banknotes[i]:.2f}")

    print('MOEDAS:')
    if integer_part_amount >= 0:
        amount_coins = integer_part_amount // bankcoins[0]
        print(f"{amount_coins:.0f} moeda(s) de R$ {bankcoins[0]:.2f}")

    for i in range(1, len(bankcoins)):
        integer_part_coins = int(bankcoins[i] * 100)
        amount_coins = decimal_part_amount // integer_part_coins
        decimal_part_amount = decimal_part_amount % integer_part_coins
        print(f"{amount_coins:.0f} moeda(s) de R$ {bankcoins[i]:.2f}")


if __name__ == '__main__':
    run_challenge()
