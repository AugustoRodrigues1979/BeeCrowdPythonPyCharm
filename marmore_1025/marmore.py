from sys import stdin


def run_challenge():
    result_dict = dict()
    id_serie_use_case = 0
    while True:
        amount_list = list(map(int, (input()).split()))
        amount_marble, amount_queries = amount_list[0], amount_list[1]

        if amount_marble == 0 and amount_queries == 0:
            break

        marble_dict = dict()

        marble_pos = 2
        for i in range(amount_marble):
            marble_key = input()
            if not marble_key in marble_dict.keys():
                marble_dict[marble_key] = marble_pos
            marble_pos += 1

        query_result_dict = dict()
        for i in range(amount_queries):
            query_number = input()
            if query_number in marble_dict:
                query_result_dict[query_number] = f'{int(query_number)} found at {marble_dict[query_number]}'
            else:
                query_result_dict[query_number] = f'{int(query_number)} not found'

        id_serie_use_case += 1
        result_dict[str(id_serie_use_case)] = query_result_dict

    id_serie_use_case = 1
    for key_result in result_dict.keys():
        print(f'CASE# {id_serie_use_case}:', end='\n')
        id_serie_use_case += 1
        query_result_dict = result_dict[key_result]
        for query_key in query_result_dict:
            result_str = query_result_dict[query_key]
            print(f'{result_str}', end='\n')


if __name__ == '__main__':
    input = stdin.readline
    run_challenge()
