# Leia um valor de ponto flutuante com duas casas decimais.
# Este valor representa um valor monetário.
#
# A seguir, calcule o menor número de notas e moedas possíveis
# no qual o valor pode ser decomposto. As notas consideradas
# são de 100, 50, 20, 10, 5, 2.
#
# As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01.
# A seguir mostre a relação de notas necessárias.
def run_challenge():
    amount_input = float(input())

    banknotes = [100, 50, 20, 10, 5, 2]
    bankcoins = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

    print('NOTAS:')
    for i in range(len(banknotes)):
        amount_notes = amount_input // banknotes[i]
        amount_input = amount_input % banknotes[i]
        print(f"{amount_notes:.0f} nota(s) de R$ {banknotes[i]:.2f}")

    print('MOEDAS:')
    for i in range(len(bankcoins)):
        if bankcoins[i] != 1:
            amount_coins = (amount_input*100) // (bankcoins[i]*100)
        else:
            amount_coins = amount_input // bankcoins[i]
        amount_input = round(amount_input % bankcoins[i],2)
        print(f"{amount_coins:.0f} moeda(s) de R$ {bankcoins[i]:.2f}")


if __name__ == '__main__':
    run_challenge()