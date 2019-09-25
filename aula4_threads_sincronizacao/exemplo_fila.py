from threading import Thread
from queue import Queue
import random
import time

class Produtor(Thread):

    def __init__(self,fila):
        Thread.__init__(self)
        self.fila = fila
    
    def run(self):
        for x in range(5):
            i=random.randint(1, 50)
            print("Produzido {}".format(i))
            fila.put(i)
            time.sleep(2)

class Consumidor(Thread):

    def __init__(self,fila):
        Thread.__init__(self)
        self.fila = fila
        
    def run(self):
        for x in range(5):
            i=self.fila.get()
            self.fila.task_done()
            print("Consumindo {}".format(i))
            time.sleep(3)

if __name__ == "__main__":
    
    fila = Queue(5)

    produtor = Produtor(fila)
    consumidor = Consumidor(fila)

    produtor.start()
    consumidor.start()

    produtor.join()
    consumidor.join()
