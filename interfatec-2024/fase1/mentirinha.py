import math


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def is_primo_de_mentirinha(N):
    raiz = int(math.sqrt(N))

    if raiz * raiz == N and is_prime(raiz):
        return "sim"

    return "nao"


n = int(input())

print(is_primo_de_mentirinha(n))
