from multiprocessing import Process
from threading import Thread

lista_das_listas=[]

class MeuProcesso(Process):

    def __init__(self,lista):
        Process.__init__(self)
        self.lista = lista
    
    def run(self):
        
        print("Processo...{}".format(self.lista))
        for a in range(5,10,1):
            self.lista.append(a)

        lista_das_listas.append(self.lista)
        print("Fim - Processo...{}".format(self.lista))
        #ver porque esta imprimindo igual....
        print(hex(id(lista_das_listas)))

class MinhaThread(Thread):

    def __init__(self,lista):
        Thread.__init__(self)
        self.lista = lista
    
    def run(self):
        
        print("Thread...{}".format(self.lista))
        for a in range(5,10,1):
            self.lista.append(a)

        lista_das_listas.append(self.lista)
        print("Fim - Thread...{}".format(self.lista))
    

if __name__ == "__main__":
    lista=[1,2,3,4]
    processo = MeuProcesso(lista)
    processo.start()
    processo.join()
    print("Pai...{}".format(lista))
    print(lista_das_listas)

    ###Agora com thread####
    lista=[1,2,3,4]
    thread = MinhaThread(lista)
    thread.start()
    thread.join()
    print("Pai...{}".format(lista))
    print(lista_das_listas)