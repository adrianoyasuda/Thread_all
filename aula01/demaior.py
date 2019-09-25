

idade=int(input("Digite sua idade:"))
print(idade)
if not idade < 18 and idade < 1:
    print("De menor e bebe")
elif idade >= 60:
    print("De maior e idoso")
else:
    print("Só de maior...")


#if __name__ == '__main__':
