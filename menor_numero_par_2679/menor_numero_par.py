from sys import stdin, stdout

def run_challenge():
    number = int(input())
    if number % 2 == 0:
        number += 2
    else:
        number += 1

    print(str(number), end='\n')

if __name__ == '__main__':
    run_challenge()