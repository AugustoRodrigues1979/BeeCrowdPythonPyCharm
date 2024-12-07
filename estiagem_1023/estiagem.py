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

def callback_for_item_default(result, value):
    result.append(value)

def create_node(value):
    return {'value': value, 'left': None, 'right': None}

def insert(root, value):
    new_node = create_node(value)
    if root is None:
        return new_node
    current = root
    while True:
        if value < current['value']:
            if current['left'] is None:
                current['left'] = new_node
                return root
            current = current['left']
        else:
            if current['right'] is None:
                current['right'] = new_node
                return root
            current = current['right']

def balance_tree(root):
    callback = callback_for_item_default
    inorder_values = inorder(root,callback)
    return sorted_array_to_bst(inorder_values)

def inorder(root, callback_for_item):
    stack = []
    result = []
    current = root
    while current is not None or stack:
        while current is not None:
            stack.append(current)
            current = current['left']
        current = stack.pop()
        callback_for_item(result, current['value'])
        current = current['right']
    return result

def sorted_array_to_bst(arr):
    if not arr:
        return None
    def insert_level_order(arr, root, i, n):
        if i < n:
            node = create_node(arr[i])
            root = node
            root['left'] = insert_level_order(arr, root['left'], 2 * i + 1, n)
            root['right'] = insert_level_order(arr, root['right'], 2 * i + 2, n)
        return root
    return insert_level_order(arr, None, 0, len(arr))

def get_list_inorder(root, callback_for_item=callback_for_item_default):
    return inorder(root, callback_for_item)

def round_down(number, decimal_places):
    factor = 10 ** decimal_places
    return math.floor(number * factor) / factor

def collect_info_house():
    amount_residents_and_consume_by_family = input()
    amount_tokens = amount_residents_and_consume_by_family.split()
    amount_residents, amount_consumed_family = list(map(int,amount_tokens))
    average_consume_by_person = amount_consumed_family // amount_residents
    return average_consume_by_person, amount_residents, amount_consumed_family

def mount_second_line(root, average_consumption_city):
    def treatment_by_consumption(consumption_array, key_consumption):
        key_consumption = key_consumption // 1000
        key_consumption_str = str(key_consumption)
        if key_consumption_str in average_consumption_city:
            amount_residents = average_consumption_city.pop(key_consumption_str)
            treatment_by_consumption.output_str += f"{amount_residents}-{key_consumption_str}"
            if len(average_consumption_city) > 0:
                treatment_by_consumption.output_str += " "

    treatment_by_consumption.output_str = ''
    get_list_inorder(root, treatment_by_consumption)
    list_a = [4,5,6,7,22,1,-3,4]
    list_a.sort()
    return treatment_by_consumption.output_str

def collect_data_city():
    amount_cities = 0
    cities_dict = dict()
    while True:
        amount_house = int(input())
        if amount_house == 0:
            break
        amount_cities += 1
        total_persons = 0
        total_amount_consume = 0
        root = None
        average_consumption_by_house = dict()
        for home_index in range(amount_house):  # For each home
            average_consume_by_person, amount_residents, amount_consumed_family  = collect_info_house()
            root = insert(root, average_consume_by_person * 1000 + amount_residents)
            total_persons += amount_residents
            total_amount_consume += amount_consumed_family
            key_average_consumption = str(average_consume_by_person)
            if key_average_consumption in average_consumption_by_house:
                average_consumption_by_house[key_average_consumption] += amount_residents
            else:
                average_consumption_by_house[key_average_consumption] = amount_residents

        cities_dict[f'K_CITY_'+str(amount_cities)] = [root, total_persons, total_amount_consume, average_consumption_by_house]
    return amount_cities, cities_dict

def run_challenge():
    info_city_str = ''
    amount_cities, cities_dict = collect_data_city()
    if amount_cities == 0:
        return
    id_city = 0
    for key_city in cities_dict:
        info_city_lst = cities_dict[key_city]
        output_first_line = f'Cidade# {id_city+1}:'
        output_second_line = mount_second_line(info_city_lst[0], info_city_lst[3])
        average_consume_by_city = info_city_lst[2] / info_city_lst[1]
        average_consume_by_city = round_down(average_consume_by_city, 2)
        output_third_line = f'Consumo medio: {average_consume_by_city:.02f} m3.'
        info_city_str += output_first_line + '\n' + output_second_line + '\n' + output_third_line
        if id_city < amount_cities - 1:
            info_city_str += '\n'
        id_city += 1

    print(info_city_str, end='')

if __name__ == '__main__':
    run_challenge()
