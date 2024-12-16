from sys import stdin, stdout

def run_challenge():
    number = int(input())
    if number % 2 == 0:
        number *= 2
    else:
        number += 1

    print(str(number))

if __name__ == '__main__':
    input = stdin.readline
    print = stdout.write
    run_challenge()