from sys import stdin, stdout


def print_with_flush(output_str):
    stdout.write(output_str)
    stdout.flush()


def run_challenge():
    result_dict = dict()
    id_serie_use_case = 0
    while True:
        amount_list = list(map(int, (input()).split()))
        amount_marble, amount_queries = amount_list[0], amount_list[1]

        if amount_marble == 0 and amount_queries == 0:
            break

        list_numbers = [-1]
        for i in range(amount_marble):
            list_numbers.append(int(input()))

        list_numbers.sort()

        marble_dict = dict()
        for i in range(len(list_numbers)):
            marble_key = str(list_numbers[i])
            if not marble_key in marble_dict.keys():
                marble_dict[marble_key] = i

        query_result_dict = dict()
        request_query_list = []
        for i in range(amount_queries):
            query_number = str(int(input()))
            if query_number in marble_dict:
                query_result_dict[query_number] = f'{int(query_number)} found at {marble_dict[query_number]}'
            else:
                query_result_dict[query_number] = f'{int(query_number)} not found'
            request_query_list.append(query_number)

        id_serie_use_case += 1
        result_dict[str(id_serie_use_case)] = dict()
        result_dict[str(id_serie_use_case)]["data"] = query_result_dict
        result_dict[str(id_serie_use_case)]["queries_id"] = request_query_list


    id_serie_use_case = 1
    for key_result in result_dict.keys():
        print(f'CASE# {id_serie_use_case}:\n')
        id_serie_use_case += 1
        query_result_dict = result_dict[key_result]
        request_query_list = query_result_dict['queries_id']
        for i in range(len(request_query_list)):
            query_key = str(request_query_list[i])
            result_str = query_result_dict['data'][query_key]
            print(f'{result_str}\n')


if __name__ == '__main__':
    input = stdin.readline
    print = stdout.write
    run_challenge()
