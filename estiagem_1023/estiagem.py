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

IDX_ID_CITY = 0
IDX_AVERAGE_CONSUMPTION_BY_PERSON = 1
IDX_AVERAGE_CONSUMPTION_HOUSE = 2
IDX_AMOUNT_RESIDENTS = 3


def round_down(number, decimal_places):
    factor = 10 ** decimal_places
    return math.floor(number * factor) / factor


def collect_info_house():
    amount_residents, amount_consumed_family = list(map(int, input().split()))
    average_consume_by_person = amount_consumed_family // amount_residents
    return average_consume_by_person, amount_residents, amount_consumed_family


def split_info_city(data_number_city):
    data_city_lst = []
    expoent_number = 9
    while expoent_number >= 0:
        data_city_lst.append(data_number_city // (10 ** expoent_number))
        data_number_city = data_number_city % (10 ** expoent_number)
        expoent_number -= 3
    return data_city_lst


def collect_data_city():
    amount_cities = 0
    cities_list = []
    while True:
        amount_house = int(input())
        if amount_house == 0:
            break
        amount_cities += 1
        for home_index in range(amount_house):  # For each home
            average_consume_by_person, amount_residents, amount_consumed_family = collect_info_house()
            all_info_in_only_number = amount_cities * (10 ** 9)
            all_info_in_only_number += average_consume_by_person * (10 ** 6)
            all_info_in_only_number += amount_consumed_family * (10 ** 3)
            all_info_in_only_number += amount_residents * (10 ** 0)
            cities_list.append(all_info_in_only_number)
    return amount_cities, cities_list


def mount_output_by_city(output_second_line, average_consumption_by_city, id_city):
    output_first_line = f'Cidade# {id_city}:'
    output_third_line = f'Consumo medio: {average_consumption_by_city:.02f} m3.'
    return output_first_line + '\n' + output_second_line + '\n' + output_third_line


def mount_output_str(cities_list):
    last_id_city = -1
    last_average_consumption_by_house = -1
    total_residents_by_city = 0
    total_consumption_by_city = 0
    output_second_line = ''
    final_output_str = ''
    total_residents_with_same_average_consumption = 0
    amount_cities_processed = 1
    for info_number_city in cities_list:
        info_city_list = split_info_city(info_number_city)
        id_city = info_city_list[IDX_ID_CITY]
        average_consumption_person = info_city_list[IDX_AVERAGE_CONSUMPTION_BY_PERSON]
        amount_consumption_family = info_city_list[IDX_AVERAGE_CONSUMPTION_HOUSE]
        amount_residents = info_city_list[IDX_AMOUNT_RESIDENTS]

        if last_id_city == -1:
            last_id_city = id_city
            last_average_consumption_by_house = average_consumption_person

        change_city = (last_id_city != id_city)
        change_consumption_by_house = (last_average_consumption_by_house != average_consumption_person)

        if change_city:
            amount_cities_processed += 1

            output_second_line += f"{total_residents_with_same_average_consumption}-{last_average_consumption_by_house}"
            average_consumption_by_city = round_down(total_consumption_by_city / total_residents_by_city, 2)
            final_output_str += mount_output_by_city(output_second_line, average_consumption_by_city, last_id_city)
            if amount_cities_processed < len(cities_list):
                final_output_str += '\n'

            last_average_consumption_by_house = average_consumption_person
            total_residents_with_same_average_consumption = amount_residents

            last_id_city = id_city
            total_residents_by_city = amount_residents
            total_consumption_by_city = amount_consumption_family

            output_second_line = ''
        else:
            total_residents_by_city += amount_residents
            total_consumption_by_city += amount_consumption_family

            if change_consumption_by_house:
                output_second_line += f"{total_residents_with_same_average_consumption}-{last_average_consumption_by_house} "
                last_average_consumption_by_house = average_consumption_person
                total_residents_with_same_average_consumption = amount_residents
            else:
                total_residents_with_same_average_consumption += amount_residents

    output_second_line += f"{total_residents_with_same_average_consumption}-{last_average_consumption_by_house}"
    average_consumption_by_city = round_down(total_consumption_by_city / total_residents_by_city, 2)
    final_output_str += mount_output_by_city(output_second_line, average_consumption_by_city, last_id_city)
    return final_output_str


def run_challenge():
    amount_cities, cities_list = collect_data_city()
    if amount_cities == 0:
        return
    cities_list.sort()
    output = mount_output_str(cities_list)
    print(output, end='')


if __name__ == '__main__':
    run_challenge()
