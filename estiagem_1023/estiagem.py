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
from sys import stdin


def get_info_each_house(house_dict):
    return f"{house_dict['K_AMOUNT_RESIDENTS']}-{house_dict['K_AMOUNT_CONSUME_PERSON']}"  # Build string


def get_all_amount_person(house_dict):
    return int(house_dict['K_AMOUNT_RESIDENTS'])


def get_all_amount_consume(house_dict):
    return int(house_dict['K_AMOUNT_CONSUME_FAMILY'])


def round_down(number, decimal_places):
    factor = 10 ** decimal_places
    return math.floor(number * factor) / factor


def show_info_city(id_city, output_second_line, amount_person_by_city, amount_consume_by_city):
    output_first_line = f'Cidade# {id_city}:'  # Build first line info about the specify city
    output_second_line = output_second_line.rstrip(' ')
    average_consume_by_city = amount_consume_by_city / amount_person_by_city  # Get average consume by city
    average_consume_by_city = round_down(average_consume_by_city, 2)
    output_third_line = f'Consumo medio: {average_consume_by_city:.02f} m3.'  # Build third line for show for user
    return output_first_line + '\n' + output_second_line + '\n' + output_third_line  # Return all info about specify city


def collect_info_house():
    amount_residents_and_consume_by_family = input()  # Get amount of residents within the family
    amount_tokens = amount_residents_and_consume_by_family.split()  # Get amount residents and amount consume by house
    amount_residents, amount_consumed_family = [int(amount) for amount in amount_tokens]  # Convert each amount string in integer amount
    average_consume_by_person = amount_consumed_family // amount_residents  # Get average consume by person
    info_house_dict = {
        'K_AMOUNT_RESIDENTS': amount_residents,
        'K_AMOUNT_CONSUME_FAMILY': amount_consumed_family,
        'K_AMOUNT_CONSUME_PERSON': average_consume_by_person
    }  # Create a dict with info about all residents in specify house
    return average_consume_by_person, info_house_dict  # Return average consume by person and info about a house


def mount_second_line(consumption_dict):
    output_second_line = ''  # Set a second line with empty string
    processed_keys = 0
    amount_keys = len(consumption_dict)
    for key in sorted(map(int, consumption_dict.keys())):  # For each key in sorted keys list
        key_str = str(key)  # Create a key string from the integer key
        output_second_line += get_info_each_house(consumption_dict[key_str][0])
        if processed_keys != amount_keys - 1:
            output_second_line += ' '
        processed_keys += 1

    return output_second_line  # Returns ordered city dict


def update_total_amount_person(consumption_dict, house_consumption_dict):
    actual_amount_persons = int(consumption_dict["K_AMOUNT_RESIDENTS"])
    amount_person_in_house = int(house_consumption_dict["K_AMOUNT_RESIDENTS"])
    return actual_amount_persons + amount_person_in_house


def update_real_consumption(average_consumption_dict, house_consumption_dict):
    actual_consumption = int(average_consumption_dict["K_AMOUNT_CONSUME_FAMILY"])
    house_consumption = int(house_consumption_dict["K_AMOUNT_CONSUME_FAMILY"])
    return actual_consumption + house_consumption


def run_challenge():
    number_city = 0  # Initialize id city
    while True:  # Setting an endless loop
        amount_house = int(input())  # Get amount of use case
        if amount_house == 0:  # Check if amount of use case is equal to zero
            break  # Stop the collect use case

        amount_person_by_city = 0  # Initialize amount of person for zero
        amount_consume_by_city = 0  # Initialize amount of person for zero
        city_dict = dict()  # Create city dict
        for home_index in range(amount_house):  # For each home
            average_consume_by_person, info_house_dict = collect_info_house()  # Collect info associate by house
            amount_person_by_city += get_all_amount_person(info_house_dict)
            amount_consume_by_city += get_all_amount_consume(info_house_dict)
            city_key = f'{average_consume_by_person}'  # Build the key for each city based on average consumption per person
            if city_key in city_dict.keys():  # Check if exist a consume_key in average_consume_dict dict
                consumption_dict = city_dict[city_key][0]
                consumption_dict['K_AMOUNT_RESIDENTS'] = update_total_amount_person(consumption_dict, info_house_dict)  # Store info about house in common consume key
                consumption_dict['K_AMOUNT_CONSUME_FAMILY'] = update_real_consumption(consumption_dict, info_house_dict)  # Store info about house in common consume key
            else:  # Don't exist consume key in average consume dict
                city_dict[city_key] = []
                city_dict[city_key].append(info_house_dict)  # Store info about house in new consume key

        output_second_line = mount_second_line(city_dict)
        number_city += 1  # Update id city
        info_city_str = show_info_city(number_city, output_second_line, amount_person_by_city, amount_consume_by_city)  # Builds output string based in all average consume provided by user
        if number_city > 1:
            info_city_str = '\n\n' + info_city_str
        print(info_city_str, end='')  # Show the output for user


if __name__ == '__main__':
    input = stdin.readline
    run_challenge()
