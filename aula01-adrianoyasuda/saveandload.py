import json


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return "Nome: {}  Idade: {}".format(self.nome, self.idade)


if __name__ == '__main__':

    lpessoas = []

    for x in range(3):
        pessoa = Pessoa(input("Digite seu nome: "), int(input("Digite sua Idade: ")))
        lpessoas.append(pessoa)

    for p in lpessoas:
        json_string = json.dumps([p.__dict__ for p in lpessoas])

        arq = open("pessoas.json", "w")
        arq.write(json_string)
        arq.close()

    arq = open("pessoas.json", "r")
    jpessoas = arq.read()
    json_string = json.loads(jpessoas)

    lpessoas.clear()

    for s in json_string:
        pessoa = Pessoa(**s)
        lpessoas.append(pessoa)

    print("----------Json Carregado------------")
    for p in lpessoas:
        print(p)
