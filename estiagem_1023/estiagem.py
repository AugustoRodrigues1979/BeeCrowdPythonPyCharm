# Devido às constantes estiagens que aconteceram nos últimos tempos em algumas regiões do Brasil,
# o governo federal criou um órgão para a avaliação do consumo destas regiões com finalidade de
# verificar o comportamento da população na época de racionamento. Este órgão responsável irá pegar
# algumas cidades (por amostragem) e verificará como está sendo o consumo de cada uma das pessoas da
# cidade e o consumo médio de cada cidade por habitante.
#
# Entrada
# A entrada contém vários casos de teste. A primeira linha de cada caso de teste contém um
# inteiro N (1 ≤ N ≤ 1*106), indicando a quantidade de imóveis. As N linhas contém um par de
# valores X (1 ≤ X ≤ 10) e Y (1 ≤ Y ≤ 200), indicando a quantidade de moradores de cada imóvel
# e o respectivo consumo total de cada imóvel (em m3). Com certeza, nenhuma residência consome
# mais do que 200 m3 por mês. O final da entrada é representado pelo número zero.
#
# Saída
# Para cada entrada, deve-se apresentar a mensagem “Cidade# n:”, onde n é o número da cidade
# seguindo a sequência (1, 2, 3, ...) e em seguida deve-se listar, por ordem ascendente de consumo,
# a quantidade de pessoas seguido de um hífen e o consumo destas pessoas, arredondando o valor para baixo.
# Na terceira linha da saída deve-se mostrar o consumo médio por pessoa da cidade, com 2 casas
# decimais sem arredondamento, considerando o consumo real total.
#
# Imprimir uma linha em branco entre dois casos de teste consecutivos.
# No fim da saída não deve haver uma linha em branco.
#
import math

def round_down(number, decimal_places):
    factor = 10 ** decimal_places
    return math.floor(number * factor) / factor

def collect_info_house():
    amount_residents_and_consume_by_family = input()
    amount_tokens = amount_residents_and_consume_by_family.split()
    amount_residents, amount_consumed_family = list(map(int,amount_tokens))
    average_consume_by_person = amount_consumed_family // amount_residents
    return average_consume_by_person, amount_residents, amount_consumed_family

def mount_second_line(average_consume_lst):
    average_consume_lst.sort()
    output_str = ''
    total_residents = 0
    previous_consumption = -1
    for consumption_value in average_consume_lst:
        average_consumption = consumption_value // 1000
        residents = consumption_value % 1000
        if previous_consumption == -1:
            previous_consumption = average_consumption
        if previous_consumption != average_consumption:
            output_str += f"{total_residents}-{previous_consumption} "
            total_residents = residents
            previous_consumption = average_consumption
        else:
            total_residents += residents
    output_str += f"{total_residents}-{previous_consumption}"
    return output_str

def run_challenge():
    info_city_str = ''
    exist_at_least_one_city = False
    id_city = 0
    while True:
        amount_house = int(input())
        if amount_house == 0:
            break
        id_city += 1
        output_first_line = f'Cidade# {id_city}:'
        total_persons = 0
        total_amount_consume = 0
        consumption_list = []
        for home_index in range(amount_house):  # For each home
            average_consume_by_person, amount_residents, amount_consumed_family  = collect_info_house()
            consumption_list.append(average_consume_by_person * 1000 + amount_residents)
            total_persons += amount_residents
            total_amount_consume += amount_consumed_family
        output_second_line = mount_second_line(consumption_list)
        average_consume_by_city = total_amount_consume / total_persons
        average_consume_by_city = round_down(average_consume_by_city, 2)
        output_third_line = f'Consumo medio: {average_consume_by_city:.02f} m3.'
        info_city_str += output_first_line + '\n' + output_second_line + '\n' + output_third_line
        info_city_str += '\n'
        exist_at_least_one_city = True
    if exist_at_least_one_city:
        print(info_city_str[:-1], end='')

if __name__ == '__main__':
    run_challenge()
