def run_challenge():
    initial_data_lst = list(map(int, input().split()))

    if len(initial_data_lst) != 2:
        return

    amount_days, amount_balance = initial_data_lst[0], initial_data_lst[1]
    if amount_days <= 0 or amount_days >= 31:
        return

    smallest_balance = amount_balance
    last_balance = amount_balance
    for day in range(amount_days):
        amount_balance = int(input())
        last_balance += amount_balance
        if last_balance < smallest_balance:
            smallest_balance = last_balance

    print(f'{smallest_balance}')

if __name__ == '__main__':
    run_challenge()
