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
import bisect


def get_info_each_house(house_list):
    output_str = ''
    for house_index in range(len(house_list)):
        house_dict = house_list[house_index]
        output_str += f"{house_dict['K_AMOUNT_RESIDENTS']}-{house_dict['K_AMOUNT_CONSUME_PERSON']} "  # Build string

    return output_str


def get_all_amount_person(house_list):
    total_persons = 0
    for house_index in range(len(house_list)):
        house_dict = house_list[house_index]
        total_persons += int(house_dict['K_AMOUNT_RESIDENTS'])

    return total_persons


def get_all_amount_consume(house_list):
    total_amount_consume = 0
    for house_index in range(len(house_list)):
        house_dict = house_list[house_index]
        total_amount_consume += int(house_dict['K_AMOUNT_CONSUME_FAMILY'])

    return total_amount_consume


def round_down(number, decimal_places):
    factor = 10 ** decimal_places
    return math.floor(number * factor) / factor


def show_info_city(id_city, city_dict, sorted_integer_key_list):
    output_first_line = f'Cidade# {id_city}:'  # Build first line info about the specify city
    amount_person_by_city = 0  # Initialize amount of person for zero
    amount_consume_by_city = 0  # Initialize amount of person for zero

    output_second_line = ''  # Initialize second line info about the specify city
    for consume_key in sorted_integer_key_list:  # For each consume key in sorted_key_list
        house_list = city_dict[str(consume_key)]
        output_second_line += get_info_each_house(house_list)
        amount_person_by_city += get_all_amount_person(house_list)
        amount_consume_by_city += get_all_amount_consume(house_list)

    output_second_line = output_second_line.rstrip(' ')
    average_consume_by_city = amount_consume_by_city / amount_person_by_city  # Get average consume by city
    average_consume_by_city = round_down(average_consume_by_city, 2)
    output_third_line = f'Consumo medio: {average_consume_by_city:.02f} m3.'  # Build third line for show for user
    return output_first_line + '\n' + output_second_line + '\n' + output_third_line  # Return all info about specify city


def collect_info_house():
    amount_residents_and_consume_by_family = input()  # Get amount of residents within the family
    if amount_residents_and_consume_by_family == '':  # Check if amount is equal a empty string
        raise ValueError('Provide a valid amount residents and amount of consume')  # Raise an exception

    amount_tokens = amount_residents_and_consume_by_family.split()  # Get amount residents and amount consume by house
    if len(amount_tokens) != 2:  # Check if amount of tokens is equal to 2
        raise ValueError('Provide ONE valid amount residents AND ONE amount of consume')  # Raise an exception

    amount_residents, amount_consumed_family = [int(amount) for amount in amount_tokens]  # Convert each amount string in integer amount
    if amount_residents <= 0:  # Check if amount of residents is less than or equal to zero
        raise ValueError('Number of residents cannot be equal to or less than zero')  # Raise an exception

    if amount_consumed_family <= 0:  # Check if amount consumed by family is less than or equal to zero
        raise ValueError('Amount consumed by family cannot be equal to or less than zero')  # Raise an exception

    average_consume_by_person = amount_consumed_family // amount_residents  # Get average consume by person
    info_house_dict = {
        'K_AMOUNT_RESIDENTS': amount_residents,
        'K_AMOUNT_CONSUME_FAMILY': amount_consumed_family,
        'K_AMOUNT_CONSUME_PERSON': average_consume_by_person
    }  # Create a dict with info about all residents in specify house
    return average_consume_by_person, info_house_dict  # Return average consume by person and info about a house


def sort_average_consume(list_keys, original_average_consume_dict):
    sorted_dict = dict()  # Create new dict what will contain sorted average consume dict
    for consume_key in list_keys:
        consume_key_str = str(consume_key)  # Create a key string from the integer key
        sorted_dict[consume_key_str] = original_average_consume_dict[consume_key_str]
    return sorted_dict  # Returns ordered city dict


def update_total_amount_person(consumption_dict, house_consumption_dict):
    actual_amount_persons = int(consumption_dict["K_AMOUNT_RESIDENTS"])
    amount_person_in_house = int(house_consumption_dict["K_AMOUNT_RESIDENTS"])
    return actual_amount_persons + amount_person_in_house


def update_real_consumption(average_consumption_dict, house_consumption_dict):
    actual_consumption = int(average_consumption_dict["K_AMOUNT_CONSUME_FAMILY"])
    house_consumption = int(house_consumption_dict["K_AMOUNT_CONSUME_FAMILY"])
    return actual_consumption + house_consumption

def insert_new_key(list_keys, key):
    position = bisect.bisect_left(list_keys, key) # Encontrar a posição onde o elemento deve ser inserido
    list_keys.insert(position, key) # Inserir o elemento na posição correta
    return list_keys

def run_challenge():
    number_city = 0  # Initialize id city
    state_city_lst = []  # Initialize state city list
    while True:  # Setting an endless loop
        amount_house = int(input())  # Get amount of use case
        if amount_house < 0:  # Check if amount of use case is less then zero
            raise ValueError('Use case quantity cannot be is less then zero')  # Raise an exception

        if amount_house == 0:  # Check if amount of use case is equal to zero
            break  # Stop the collect use case

        integer_keys_list = []
        city_dict = dict()  # Create city dict
        for home_index in range(amount_house):  # For each home
            average_consume_by_person, info_house_dict = collect_info_house()  # Collect info associate by house
            city_key = f'{average_consume_by_person}'  # Build the key for each city based on average consumption per person
            if city_key in city_dict.keys():  # Check if exist a consume_key in average_consume_dict dict
                consumption_dict = city_dict[city_key][0]
                consumption_dict['K_AMOUNT_RESIDENTS'] = update_total_amount_person(consumption_dict, info_house_dict)  # Store info about house in common consume key
                consumption_dict['K_AMOUNT_CONSUME_FAMILY'] = update_real_consumption(consumption_dict, info_house_dict)  # Store info about house in common consume key
            else:  # Don't exist consume key in average consume dict
                city_dict[city_key] = []
                city_dict[city_key].append(info_house_dict)  # Store info about house in new consume key
                integer_keys_list = insert_new_key(integer_keys_list,average_consume_by_person)

        #sorted_city_dict = sort_average_consume(integer_keys_list, city_dict)
        number_city += 1  # Update id city
        info_city_str = show_info_city(number_city, city_dict, integer_keys_list)  # Builds output string based in all average consume provided by user
        state_city_lst.append(info_city_str)  # Store output string in state city list

    if len(state_city_lst) > 0:  # Check if exist at least one city
        output_str = '\n'.join(state_city_lst)  # Insert '\n' between two cities
        print(output_str, end='')  # Show the output for user


if __name__ == '__main__':
    run_challenge()
