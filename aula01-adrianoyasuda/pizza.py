# coding=utf-8
import os


class Pizza:
    def __init__(self, sabor, preco):
        self.sabor = sabor
        self.preco = preco

    def __str__(self):
        return "{}        R${}".format(self.sabor, self.preco)


if __name__ == '__main__':
    lpizzas = []
    lpedidos = []
    op = 0

    while op != 4:
        os.system('clear')
        print ("1 - Cadastrar Pizza")
        print ("2 - Fazer Pedido")
        print ("3 - Ver Carrinho")
        print ("4 - Sair")
        op = int(input())

        if op == 1:
            os.system('clear')
            pizza = Pizza(input("Sabor: "), float(input("Preço: ")))
            lpizzas.append(pizza)

        if op == 2:
            os.system('clear')
            n = 0
            print ("-------------Cardápio Pizzas 🍕---------------")
            for p in lpizzas:
                print("{} - {}".format(n, p))
                n = n + 1

            lpedidos.append(int(input()))

        if op == 3:
            os.system('clear')
            total = 0.0
            print ("------------- Carrinho --------------------")
            for c in lpedidos:
                print (lpizzas[c])
                total = total + lpizzas[c].preco
            print ("Total: R${}".format(total))
            input()
