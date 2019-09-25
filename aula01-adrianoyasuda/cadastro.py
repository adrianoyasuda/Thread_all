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
		print(p)
