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

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # Inicializando a altura do nó

def height(node):
    if not node:
        return 0
    return node.height

def get_balance(node):
    if not node:
        return 0
    return height(node.left) - height(node.right)

def right_rotate(y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    y.height = max(height(y.left), height(y.right)) + 1
    x.height = max(height(x.left), height(x.right)) + 1
    return x

def left_rotate(x):
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    x.height = max(height(x.left), height(x.right)) + 1
    y.height = max(height(y.left), height(y.right)) + 1
    return y

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, node, key):
        if not node:
            return Node(key)
        if key < node.key:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)
        node.height = max(height(node.left), height(node.right)) + 1
        balance = get_balance(node)
        if balance > 1 and key < node.left.key:
            return right_rotate(node)
        if balance < -1 and key > node.right.key:
            return left_rotate(node)
        if balance > 1 and key > node.left.key:
            node.left = left_rotate(node.left)
            return right_rotate(node)
        if balance < -1 and key < node.right.key:
            node.right = right_rotate(node.right)
            return left_rotate(node)
        return node

    def insert_key(self, key):
        self.root = self.insert(self.root, key)

    def inorder(self, root, func_by_key):
        if not root:
            return
        self.inorder(root.left,func_by_key)
        func_by_key(root.key)
        self.inorder(root.right,func_by_key)

def round_down(number, decimal_places):
    factor = 10 ** decimal_places
    return math.floor(number * factor) / factor

def collect_info_house():
    amount_residents_and_consume_by_family = input()
    amount_tokens = amount_residents_and_consume_by_family.split()
    amount_residents, amount_consumed_family = list(map(int,amount_tokens))
    average_consume_by_person = amount_consumed_family // amount_residents
    return average_consume_by_person, amount_residents, amount_consumed_family

def mount_second_line(average_consume_avl):
    def func_by_key(consumption_value):
        average_consumption = consumption_value // 1000
        residents = consumption_value % 1000
        if func_by_key.previous_consumption == -1:
            func_by_key.previous_consumption = average_consumption
        if func_by_key.previous_consumption != average_consumption:
            func_by_key.output_str += f"{func_by_key.total_residents}-{func_by_key.previous_consumption} "
            func_by_key.total_residents = residents
            func_by_key.previous_consumption = average_consumption
        else:
            func_by_key.total_residents += residents
    func_by_key.output_str = ''
    func_by_key.total_residents = 0
    func_by_key.previous_consumption = -1
    average_consume_avl.inorder(average_consume_avl.root, func_by_key)
    func_by_key.output_str += f"{func_by_key.total_residents}-{func_by_key.previous_consumption}"
    return func_by_key.output_str

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
        avl = AVLTree()
        for home_index in range(amount_house):  # For each home
            average_consume_by_person, amount_residents, amount_consumed_family  = collect_info_house()
            avl.insert_key(average_consume_by_person * 1000 + amount_residents)
            total_persons += amount_residents
            total_amount_consume += amount_consumed_family
        output_second_line = mount_second_line(avl)
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
