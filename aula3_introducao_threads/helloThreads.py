from threading import Thread

from time import sleep
from random import randint

class Trabalhador(Thread):

    def __init__(self,id):
        Thread.__init__(self)
        self.mensagem = "Eu sou um trabalhador..."
        self.id=id

    def print_mensagem(self):
        print("{} {}".format(self.id,self.mensagem))
    
    def run(self):
        print("Iniciando thread...")
        x=0
        while(x<10):
            self.print_mensagem()
            sleep(randint(1,3))
            x+=1
        print("Finalizando thread.")

if __name__=='__main__':
    print("Processo iniciado...")
    for a in range(5):
        t = Trabalhador(a)
        t.start()
    print("Processo finalizado.")