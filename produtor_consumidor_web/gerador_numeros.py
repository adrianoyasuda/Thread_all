from multiprocessing import Queue
from multiprocessing.managers import BaseManager

from produtor_numeros import Produtor
from consumidor_respostas import Consumidor


queueNumeros = Queue(100)
queueRespostas = Queue(100)
class QueueManager(BaseManager):pass


if __name__ == "__main__":
    
    produtor = Produtor(queueNumeros)
    produtor.start()
    
    consumidor = Consumidor(queueRespostas)
    consumidor.start()

    QueueManager.register('get_queue_numeros',callable=lambda: queueNumeros)
    QueueManager.register('get_queue_respostas',callable=lambda: queueRespostas)
    m = QueueManager(address=('',50000),authkey=b'abc')
    m.get_server().serve_forever()




