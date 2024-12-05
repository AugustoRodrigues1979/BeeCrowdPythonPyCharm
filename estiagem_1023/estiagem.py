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

    amount_residents_and_consume_by_family = input()  # Get amount of residents within the family
    if amount_residents_and_consume_by_family == '':  # Check if amount is equal an empty string
        raise ValueError('Provide a valid amount residents and amount of consume')  # Raise an exception

    amount_tokens = amount_residents_and_consume_by_family.split()  # Get amount residents and amount consume by house
    if len(amount_tokens) != 2:  # Check if amount of tokens is equal to 2
        raise ValueError('Provide ONE valid amount residents AND ONE amount of consume')  # Raise an exception

    amount_residents, amount_consumed_family = list(map(int,amount_tokens))

    if amount_residents <= 0:  # Check if amount of residents is less than or equal to zero
        raise ValueError('Number of residents cannot be equal to or less than zero')  # Raise an exception

    if amount_consumed_family <= 0:  # Check if amount consumed by family is less than or equal to zero
        raise ValueError('Amount consumed by family cannot be equal to or less than zero')  # Raise an exception

    average_consume_by_person = amount_consumed_family // amount_residents  # Get average consume by person
    return average_consume_by_person, amount_residents, amount_consumed_family

def mount_second_line(keys_list,city_dict):
    keys_list.sort()
    previous_key = -1
    output_str = ''
    for key in keys_list:
        if previous_key != key:
            key_str = str(key)
            info_house_dict = city_dict[key_str]
            output_str += f"{info_house_dict['K_AMOUNT_RESIDENTS']}-{key_str} "  # Build string
        previous_key = key

    output_str = output_str[:-1]
    return output_str

def run_challenge():
    info_city_str = ''
    exist_at_least_one_city = False
    id_city = 0 # Initialize id city
    while True:  # Setting an endless loop
        amount_house = int(input())  # Get amount of use case
        if amount_house < 0:  # Check if amount of use case is less then zero
            raise ValueError('Use case quantity cannot be is less then zero')  # Raise an exception

        if amount_house == 0:  # Check if amount of use case is equal to zero
            break  # Stop the collect use case

        id_city += 1
        output_first_line = f'Cidade# {id_city}:'  # Build first line info about the specify city

        total_persons = 0
        total_amount_consume = 0

        keys_list = [0] * amount_house
        kex_list_index = 0
        city_dict = dict()  # Create city dict
        for home_index in range(amount_house):  # For each home
            average_consume_by_person, amount_residents, amount_consumed_family  = collect_info_house()  # Collect info associate by house
            city_key = f'{average_consume_by_person}'  # Build the key for each city based on average consumption per person
            if city_key in city_dict:  # Check if exist a consume_key in average_consume_dict dict
                consumption_dict = city_dict[city_key]
                consumption_dict['K_AMOUNT_RESIDENTS'] = consumption_dict["K_AMOUNT_RESIDENTS"] + amount_residents  # Store info about house in common consume key
            else:  # Don't exist consume key in average consume dict
                city_dict[city_key] = {
                    'K_AMOUNT_RESIDENTS': amount_residents
                }

            keys_list[kex_list_index] = average_consume_by_person
            kex_list_index += 1

            total_persons += amount_residents
            total_amount_consume += amount_consumed_family

        output_second_line = mount_second_line(keys_list,city_dict)
        average_consume_by_city = total_amount_consume / total_persons  # Get average consume by city
        average_consume_by_city = round_down(average_consume_by_city, 2)
        output_third_line = f'Consumo medio: {average_consume_by_city:.02f} m3.'  # Build third line for show for user

        info_city_str += output_first_line + '\n' + output_second_line + '\n' + output_third_line  # Return all info about specify city
        info_city_str += '\n'
        exist_at_least_one_city = True

    if exist_at_least_one_city:  # Check if exist at least one city
        print(info_city_str[:-1], end='')  # Show the output for user


if __name__ == '__main__':
    run_challenge()
