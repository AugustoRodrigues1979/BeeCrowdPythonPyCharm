from sys import stdin


def run_challenge():
    amount_rulers_list = list(map(int,input().split()))
    amount_rulers_list[0] -= 1
    amount_rulers_list[1] -= 1
    amount_rulers_list[2] -= 1

    total_sockets = amount_rulers_list[0] + amount_rulers_list[1] + amount_rulers_list[2] + amount_rulers_list[3]

    print(str(total_sockets), end='\n')


if __name__ == '__main__':
    input = stdin.readline
    run_challenge()
