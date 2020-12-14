# Implementação básica de maior divisor comum

import sys


def findDivisors(n: int):
    divisors = []
    for cur in range(1, n+1):
        if (n / cur).is_integer():
            divisors.append(cur)

    return divisors


def GCD(n1: int, n2: int):
    n1_divisors = findDivisors(n1)
    n2_divisors = findDivisors(n2)

    res = []

    if(len(n1_divisors) == len(n2_divisors)):
        res = [n for n in n1_divisors if n in n2_divisors]
    else:
        biggest = n1_divisors if len(n1_divisors) > len(
            n2_divisors) else n2_divisors

        smallest = n1_divisors if len(n1_divisors) < len(
            n2_divisors) else n2_divisors

        res = [n for n in biggest if n in smallest]

    return max(res)


try:
    if(len(sys.argv) == 3):
        n1, n2 = int(sys.argv[1]), int(sys.argv[2])
        print(GCD(n1, n2))
    elif(len(sys.argv) > 3):
        print("Demasiadas opções, tem de inserir apenas dois números")
except:
    print("Tẽm de inserir dois números")
