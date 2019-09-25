# coding=utf-8
# import random
from random import randint

if __name__ == '__main__':

    lista = []
    print("20 número aleatórios entre 1 e 10")

    for x in range(1, 20):
        lista.append(randint(1, 10))

    print(lista)
