from threading import Thread
import sys
import math
import time

MAXLINHAS=10
MAXTHREADS=5

class Buscador(Thread):


    def __init__(self, linhas, inicio, fim, palavra):
        Thread.__init__(self)
        self.linhas = linhas
        self.inicio = inicio
        self.fim = fim
        self.palavra=palavra

    def run(self):
        encontrei=[]
        #inclui o nome da thread para verificar
        encontrei.append(self.name)
        for i,l in enumerate(self.linhas):
            if self.palavra in l:
                encontrei.append(i+self.inicio+1)

        #mostra os resultados
        print(encontrei)


if __name__ == "__main__":

    narq = sys.argv[1]
    palavra = input("Digite uma palavra a ser buscada:")
    arq = open(narq, "r")

    linhas = arq.readlines()

    inicio=0
    fim=0
    count=0

    while count < len(linhas):
        threads = []
        for i in range(MAXTHREADS):
            inicio=count
            fim=inicio+MAXLINHAS
            selecionadas = linhas[inicio:fim]
            if(len(selecionadas)>0):
                t = Buscador(selecionadas, inicio, fim, palavra)
                t.start()
                threads.append(t)
                count+=len(selecionadas)

        for t in threads:
            t.join()
